import matplotlib.pyplot as plt
import numpy as np

# Data from the table
models = [
    "Simple SVM (5 Exams, No Groups/Time)",
    "Simple SVM (6 Exams, No Groups/Time)",
    "Simple SVM (5 Exams, With Groups/Time)",
    "Simple SVM (6 Exams, With Groups/Time)",
    "Weighted SVM (5 Exams, No Groups/Time)",
    "Weighted SVM (6 Exams, No Groups/Time)",
    "Weighted SVM (5 Exams, With Groups/Time)",
    "Weighted SVM (6 Exams, With Groups/Time)",
    "Optimized SVM (5 Exams, No Groups/Time)",
    "Optimized SVM (6 Exams, No Groups/Time)",
    "Optimized SVM (5 Exams, With Groups/Time)",
    "Optimized SVM (6 Exams, With Groups/Time)",
    "Bagged SVM (5 Exams, No Groups/Time)",
    "Bagged SVM (6 Exams, No Groups/Time)",
    "Bagged SVM (5 Exams, With Groups/Time)",
    "Bagged SVM (6 Exams, With Groups/Time)",
    "Stacked SVM (5 Exams, No Groups/Time)",
    "Stacked SVM (6 Exams, No Groups/Time)",
    "Stacked SVM (5 Exams, With Groups/Time)",
    "Stacked SVM (6 Exams, With Groups/Time)"
]

mse = [
    95.53, 93.40, 165.25, 164.34,  # Simple SVM
    87.35, 155.46, 2578.02, 14798.54,  # Weighted SVM
    93.56, 91.96, 86.88, 87.12,  # Optimized SVM
    168.31, 168.39, 227.68, 227.72,  # Bagged SVM
    77.77, 75.89, 71.49, 66.35  # Stacked SVM
]

rmse = [
    9.77, 9.66, 12.86, 12.82,
    9.35, 12.47, 50.77, 121.65,
    9.67, 9.59, 9.32, 9.33,
    12.97, 12.98, 15.09, 15.09,
    8.82, 8.71, 8.46, 8.15
]

mae = [
    7.46, 7.42, 8.59, 8.50,
    7.20, 9.65, 39.28, 84.34,
    7.17, 7.13, 7.14, 7.08,
    9.04, 9.04, 9.52, 9.52,
    6.89, 6.84, 6.58, 6.09
]

r2 = [
    0.37, 0.39, 0.16, 0.17,
    0.43, -0.02, -12.06, -73.98,
    0.39, 0.40, 0.56, 0.56,
    -0.11, -0.11, -0.15, -0.15,
    0.49, 0.50, 0.64, 0.66
]
# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios': [3, 2]})

x = np.arange(len(models))
ax1.plot(x, mse, label="MSE", marker="o", linestyle="-", color="tab:red")
ax2.plot(x, rmse, label="RMSE", marker="s", linestyle="--", color="tab:blue")
ax2.plot(x, mae, label="MAE", marker="^", linestyle=":", color="tab:green")
ax2.plot(x, r2, label="R²", marker="d", linestyle="-.", color="tab:purple")

# Add value labels to each point slightly above the points
for i, txt in enumerate(mse):
    ax1.text(x[i], mse[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(rmse):
    ax2.text(x[i], rmse[i] + 0.3, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(mae):
    ax2.text(x[i], mae[i] + 0.3, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(r2):
    ax2.text(x[i], r2[i] + 0.3, f"{txt:.2f}", fontsize=8, ha='center')

ax2.set_xlabel("Model and Dataset", fontsize=14)
fig.text(0.1, 0.6, "Regression metrics", fontsize=16, ha='center', va='center', rotation=90)
ax2.set_ylabel("")
ax2.set_xticks(x)
ax2.set_xticklabels(models, rotation=45, fontsize=10, ha="right")

# Restore legend to upper right corner
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc="upper right", fontsize=12)

# Set limits for better visualization
ax1.set_ylim(min(mse) * 0.9, max(mse) * 1.1)
ax2.set_ylim(0, 14)
ax2.set_yticks(np.arange(0, 14, 1))  # More refined tick marks

# Hide x-axis on the first plot
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()

plt.title("", fontsize=16)
plt.tight_layout()

# Save and display the plot
plt.savefig("svm_regression_metrics_with_id.png")
plt.show()

mse = [
    93.29, 89.60, 162.75, 161.22,
    108.49, 447.18, 19671.66, 135473.64,
    94.54, 91.57, 85.61, 79.90,
    108.57, 107.59, 117.31, 116.95,
    76.75, 75.05, 73.50, 69.38
]

rmse = [
    9.66, 9.47, 12.76, 12.70,
    10.42, 21.15, 140.26, 368.07,
    9.72, 9.57, 9.25, 8.94,
    10.42, 10.37, 10.83, 10.81,
    8.76, 8.66, 8.57, 8.33
]

mae = [
    7.33, 7.24, 8.58, 8.46,
    8.27, 16.14, 70.77, 198.06,
    7.18, 7.14, 6.98, 6.53,
    7.82, 7.78, 7.87, 7.85,
    6.96, 6.84, 6.85, 6.36
]

r2 = [
    0.39, 0.41, 0.18, 0.18,
    0.29, -1.94, -98.66, -685.31,
    0.38, 0.40, 0.57, 0.60,
    0.29, 0.29, 0.41, 0.41,
    0.50, 0.51, 0.63, 0.65
]
# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios': [3, 2]})

x = np.arange(len(models))
ax1.plot(x, mse, label="MSE", marker="o", linestyle="-", color="tab:red")
ax2.plot(x, rmse, label="RMSE", marker="s", linestyle="--", color="tab:blue")
ax2.plot(x, mae, label="MAE", marker="^", linestyle=":", color="tab:green")
ax2.plot(x, r2, label="R²", marker="d", linestyle="-.", color="tab:purple")

# Add value labels to each point slightly above the points
for i, txt in enumerate(mse):
    ax1.text(x[i], mse[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(rmse):
    ax2.text(x[i], rmse[i] + 0.3, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(mae):
    ax2.text(x[i], mae[i] + 0.3, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(r2):
    ax2.text(x[i], r2[i] + 0.3, f"{txt:.2f}", fontsize=8, ha='center')

ax2.set_xlabel("Model and Dataset", fontsize=14)
fig.text(0.1, 0.6, "Regression metrics", fontsize=16, ha='center', va='center', rotation=90)
ax2.set_ylabel("")
ax2.set_xticks(x)
ax2.set_xticklabels(models, rotation=45, fontsize=10, ha="right")

# Restore legend to upper right corner
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc="upper right", fontsize=12)

# Set limits for better visualization
ax1.set_ylim(min(mse) * 0.9, max(mse) * 1.1)
ax2.set_ylim(0, 14)
ax2.set_yticks(np.arange(0, 14, 1))  # More refined tick marks

# Hide x-axis on the first plot
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()

plt.title("", fontsize=16)
plt.tight_layout()

# Save and display the plot
plt.savefig("svm_regression_metrics_without_id.png")
plt.show()