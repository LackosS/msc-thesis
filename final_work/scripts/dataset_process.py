import pandas as pd
import os

# Directories containing the .xlsx files
#progalap_directory = r'D:\Szakdolgozat\Final_Work\dataset\progalap_without_groups_and_time'
progalap_directory = r'D:\Szakdolgozat\Final_Work\dataset\progalap_with_groups_and_time'
#improg_directory = r'D:\Szakdolgozat\Final_Work\dataset\improg_without_groups_and_time'
improg_directory = r'D:\Szakdolgozat\Final_Work\dataset\improg_with_groups_and_time'
final_directory = r'D:\Szakdolgozat\Final_Work\dataset'

def process_timeslot(timeslot):
    day_mapping = {"Hétfo": 1, "Kedd": 2, "Szerda": 3, "Csütörtök": 4, "Péntek": 5}
    
    parts = timeslot.split(" ")
    day = day_mapping.get(parts[0], 0)
    start_hour = int(parts[1].split(":")[0])
    
    return day, start_hour

# Merge all .xlsx files in progalap
progalap_data = []
for filename in os.listdir(progalap_directory):
    if filename.endswith('.xlsx') and not filename.startswith("~$"):
        file_path = os.path.join(progalap_directory, filename)
        df = pd.read_excel(file_path, sheet_name=None)
        first_sheet_name = list(df.keys())[0]
        df = df[first_sheet_name]

        if 'Időpont' in df.columns:
            df[['Nap', 'Óra']] = df['Időpont'].apply(lambda x: pd.Series(process_timeslot(x)))
            df.drop(columns=['Időpont'], inplace=True)

        progalap_data.append(df)

merged_progalap = pd.concat(progalap_data, ignore_index=True)

# Finding the maximum values for normalization
max_beadando = 100
max_zh = 100

# Normalize scores
merged_progalap['Beadandó'] = ((merged_progalap['Beadandó'] / max_beadando) * 30).round(1) // 0.5 * 0.5
merged_progalap['ZH'] = ((merged_progalap['ZH'] / max_zh) * 50).round(1) // 0.5 * 0.5

# Merge all .xlsx files in improg
improg_data = []
for filename in os.listdir(improg_directory):
    if filename.endswith('.xlsx') and not filename.startswith("~$"):
        file_path = os.path.join(improg_directory, filename)
        df = pd.read_excel(file_path, sheet_name=None)
        first_sheet_name = list(df.keys())[0]
        df = df[first_sheet_name]

        if 'Időpont' in df.columns:
            df[['Nap', 'Óra']] = df['Időpont'].apply(lambda x: pd.Series(process_timeslot(x)))
            df.drop(columns=['Időpont'], inplace=True)

        improg_data.append(df)

merged_improg = pd.concat(improg_data, ignore_index=True)

# Merge progalap with improg
final_merged_df = pd.concat([merged_progalap, merged_improg], ignore_index=True)

# Step 2: Add a new column 'Id' before 'AnonymId' and assign unique IDs
id_map = {}
current_id = 1

def get_id(anonym_id):
    global current_id
    if anonym_id not in id_map:
        id_map[anonym_id] = current_id
        current_id += 1
    return id_map[anonym_id]

final_merged_df.insert(0, 'Id', final_merged_df['AnonymId'].map(get_id))

# Step 3: Fill empty fields (NaN) with zero
final_merged_df_filled = final_merged_df.fillna(0)

# Step 4: Filter rows based on the criteria
ropzh_columns = [col for col in final_merged_df_filled.columns if 'röpZH' in col]
final_merged_df_filled['röpZH_sum'] = final_merged_df_filled[ropzh_columns].sum(axis=1)

filtered_df = final_merged_df_filled[~((final_merged_df_filled['röpZH_sum'] > 6) & (final_merged_df_filled['ZH'] <= 20))]
filtered_df = filtered_df[~((filtered_df['röpZH_sum'] <= 5) & (filtered_df['ZH'] >= 40))]

filtered_df = filtered_df.drop(columns=['röpZH_sum'])

# Step 5: Round numerical values except specific columns
exclude_columns = ['Id', 'AnonymId']
numerical_columns = [col for col in filtered_df.select_dtypes(include='number').columns if col not in exclude_columns]
filtered_df[numerical_columns] = filtered_df[numerical_columns].round(2)

# Base renaming dictionary
column_renames = {
    'Csoport': 'Group',
    'ZH': 'Final_Exam',
    'Beadandó': 'Assignment',
    'AnonymId': 'AnonymId',
}

# Only add 'Nap' and 'Óra' if they exist
if 'Nap' in filtered_df.columns:
    column_renames['Nap'] = 'Day'
if 'Óra' in filtered_df.columns:
    column_renames['Óra'] = 'Start_Hour'

# Handle röpZH columns
for col in filtered_df.columns:
    if 'röpZH' in col:
        parts = col.split('röpZH')
        prefix = parts[0].strip()

        if prefix == '':
            new_name = 'Weekly_Exam'
        elif prefix == '+1':
            new_name = 'Bonus_Weekly_Exam'
        elif prefix == '+1 (javító)':
            new_name = 'Bonus_Weekly_Exam_Retake'
        elif prefix.endswith('.'):
            try:
                num = int(prefix[:-1])
                ordinal = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth',
                           'Seventh', 'Eighth', 'Ninth', 'Tenth']
                if 1 <= num <= len(ordinal):
                    new_name = f"{ordinal[num-1]}_Weekly_Exam"
                else:
                    new_name = f"Week{num}_Weekly_Exam"
            except ValueError:
                new_name = f"{prefix}_Weekly_Exam"
        else:
            new_name = f"{prefix}_Weekly_Exam"

        column_renames[col] = new_name

# Apply renaming
filtered_df = filtered_df.rename(columns=column_renames)

# Step 6: Save the final processed data to one Excel file
#output_file = os.path.join(final_directory, 'dataset_without_groups_and_time.xlsx')
output_file = os.path.join(final_directory, 'dataset_with_groups_and_time.xlsx')
filtered_df.to_excel(output_file, index=False)
print(f'Final processed data saved to: {output_file}')
