import pandas as pd
import os

# File directories
progalap_directory = r'D:\Szakdolgozat\Final_Work\dataset\progalap_with_groups_and_time'
improg_directory = r'D:\Szakdolgozat\Final_Work\dataset\improg_with_groups_and_time'
final_directory = r'D:\Szakdolgozat\Final_Work\dataset'

def process_timeslot(timeslot):
    day_mapping = {"Hétfo": 1, "Kedd": 2, "Szerda": 3, "Csütörtök": 4, "Péntek": 5}
    parts = timeslot.split(" ")
    day = day_mapping.get(parts[0], 0)
    start_hour = int(parts[1].split(":")[0])
    return day, start_hour

def load_and_prepare_data(directory, rescale=True):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.xlsx') and not filename.startswith("~$"):
            file_path = os.path.join(directory, filename)
            df = pd.read_excel(file_path, sheet_name=None)
            first_sheet_name = list(df.keys())[0]
            df = df[first_sheet_name]
            if 'Időpont' in df.columns:
                df[['Nap', 'Óra']] = df['Időpont'].apply(lambda x: pd.Series(process_timeslot(x)))
                df.drop(columns=['Időpont'], inplace=True)
            if rescale:
                df['Beadandó'] = ((df['Beadandó'] / 100) * 30).round(1) // 0.5 * 0.5
                df['ZH'] = ((df['ZH'] / 100) * 50).round(1) // 0.5 * 0.5
            data.append(df)
    merged = pd.concat(data, ignore_index=True)
    return merged.fillna(0)

def rename_columns(df, prefix):
    column_renames = {}
    for col in df.columns:
        if col == 'AnonymId':
            continue
        short_col = col.replace(f'{prefix}_', '')

        if short_col == 'Csoport':
            new_col = f'{prefix}_Group'
        elif short_col == 'ZH':
            new_col = f'{prefix}_Final_Exam'
        elif short_col == 'Beadandó':
            new_col = f'{prefix}_Assignment'
        elif short_col == 'Nap':
            new_col = f'{prefix}_Day'
        elif short_col == 'Óra':
            new_col = f'{prefix}_Start_Hour'
        elif 'röpZH' in short_col:
            parts = short_col.split('röpZH')
            pre = parts[0].strip()
            if pre == '':
                new_col = f'{prefix}_Weekly_Exam'
            elif pre == '+1':
                new_col = f'{prefix}_Bonus_Weekly_Exam'
            elif pre == '+1 (javító)':
                new_col = f'{prefix}_Bonus_Weekly_Exam_Retake'
            elif pre.endswith('.'):
                try:
                    num = int(pre[:-1])
                    ordinal = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth',
                               'Seventh', 'Eighth', 'Ninth', 'Tenth']
                    if 1 <= num <= len(ordinal):
                        new_col = f'{prefix}_{ordinal[num-1]}_Weekly_Exam'
                    else:
                        new_col = f'{prefix}_Week{num}_Weekly_Exam'
                except:
                    new_col = f'{prefix}_{pre}_Weekly_Exam'
            else:
                new_col = f'{prefix}_{pre}_Weekly_Exam'
        else:
            new_col = f'{prefix}_{short_col}'

        column_renames[col] = new_col
    return df.rename(columns=column_renames)

# Load and preprocess both datasets
merged_progalap = load_and_prepare_data(progalap_directory)
merged_improg = load_and_prepare_data(improg_directory, False)

# Prefix columns to distinguish between subjects
progalap_prefixed = merged_progalap.add_prefix('Prog_')
improg_prefixed = merged_improg.add_prefix('Improg_')

# Restore AnonymId for merging
progalap_prefixed = progalap_prefixed.rename(columns={'Prog_AnonymId': 'AnonymId'})
improg_prefixed = improg_prefixed.rename(columns={'Improg_AnonymId': 'AnonymId'})

progalap_prefixed = rename_columns(progalap_prefixed, 'Prog')
improg_prefixed = rename_columns(improg_prefixed, 'Improg')

# Merge only students present in both datasets
combined_df = pd.merge(progalap_prefixed, improg_prefixed, on='AnonymId', how='inner')

ropzh_cols_prog = [col for col in combined_df.columns if 'Prog_' in col and 'Weekly_Exam' in col]
ropzh_cols_improg = [col for col in combined_df.columns if 'Improg_' in col and 'Weekly_Exam' in col]

combined_df['Prog_röpZH_sum'] = combined_df[ropzh_cols_prog].sum(axis=1)
combined_df['Improg_röpZH_sum'] = combined_df[ropzh_cols_improg].sum(axis=1)

# Define suspicious patterns
prog_filter = ((combined_df['Prog_röpZH_sum'] > 6) & (combined_df['Prog_Final_Exam'] <= 20)) | \
              ((combined_df['Prog_röpZH_sum'] <= 5) & (combined_df['Prog_Final_Exam'] >= 40))

improg_filter = ((combined_df['Improg_röpZH_sum'] > 6) & (combined_df['Improg_Final_Exam'] <= 20)) | \
                ((combined_df['Improg_röpZH_sum'] <= 5) & (combined_df['Improg_Final_Exam'] >= 40))

# Remove suspicious entries
combined_df = combined_df[~(prog_filter | improg_filter)]

# Drop helper columns
combined_df = combined_df.drop(columns=['Prog_röpZH_sum', 'Improg_röpZH_sum'])

# Round numeric columns (except AnonymId)
numerical_columns = [col for col in combined_df.select_dtypes(include='number').columns if col != 'AnonymId']
combined_df[numerical_columns] = combined_df[numerical_columns].round(2)

# Save to Excel
output_file = os.path.join(final_directory, 'combined_dataset_with_groups_and_time.xlsx')
combined_df.to_excel(output_file, index=False)
print(f'Combined dataset saved to: {output_file}')