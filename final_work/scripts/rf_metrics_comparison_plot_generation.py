import matplotlib.pyplot as plt
import numpy as np

# Data from the table
models = [
    "Simple RF (5 Exams, No Groups/Time)",
    "Simple RF (6 Exams, No Groups/Time)",
    "Simple RF (5 Exams, With Groups/Time)",
    "Simple RF (6 Exams, With Groups/Time)",
    "Weighted RF (5 Exams, No Groups/Time)",
    "Weighted RF (6 Exams, No Groups/Time)",
    "Weighted RF (5 Exams, With Groups/Time)",
    "Weighted RF (6 Exams, With Groups/Time)",
    "Optimized RF (5 Exams, No Groups/Time)",
    "Optimized RF (6 Exams, No Groups/Time)",
    "Optimized RF (5 Exams, With Groups/Time)",
    "Optimized RF (6 Exams, With Groups/Time)",
    "Bagged RF (5 Exams, No Groups/Time)",
    "Bagged RF (6 Exams, No Groups/Time)",
    "Bagged RF (5 Exams, With Groups/Time)",
    "Bagged RF (6 Exams, With Groups/Time)",
    "Stacked RF (5 Exams, No Groups/Time)",
    "Stacked RF (6 Exams, No Groups/Time)",
    "Stacked RF (5 Exams, With Groups/Time)",
    "Stacked RF (6 Exams, With Groups/Time)"
]

mse = [
    82.49, 78.42, 74.47, 72.80,
    83.02, 79.20, 74.81, 72.91,
    81.33, 76.88, 73.62, 71.75,
    79.40, 75.96, 70.63, 69.09,
    87.89, 85.02, 73.89, 73.39
    ]
rmse = [
    9.08, 8.86, 8.63, 8.53,
    9.11, 8.90, 8.65, 8.54,
    9.02, 8.77, 8.58, 8.47,
    8.91, 8.72, 8.40, 8.31,
    9.38, 9.22, 8.60, 8.57
    ]
mae = [
    7.09, 6.89, 6.57, 6.24,
    7.13, 6.94, 6.57, 6.25,
    7.01, 6.83, 6.60, 6.21,
    6.98, 6.87, 6.53, 6.22,
    7.17, 7.17, 6.67, 6.16
    ]
r2 = [
    0.46, 0.48, 0.62, 0.63,
    0.45, 0.48, 0.62, 0.63,
    0.47, 0.50, 0.63, 0.64,
    0.48, 0.50, 0.64, 0.65,
    0.42, 0.44, 0.63, 0.63
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
ax2.set_ylim(0, 10)
ax2.set_yticks(np.linspace(0, 10, 11))  # More refined tick marks

# Hide x-axis on the first plot
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()

plt.title("", fontsize=0)
plt.tight_layout()

# Save and display the plot
plt.savefig("rf_regression_metrics_with_id.png")
plt.show()

mse = [
    88.07, 77.95, 73.98, 75.86,
    88.03, 78.04, 74.43, 75.55,
    80.76, 75.71, 72.85, 70.52,
    82.08, 75.83, 69.40, 68.77,
    84.96, 78.51, 73.31, 73.01
    ]
rmse = [
    9.38, 8.83, 8.63, 8.69,
    9.11, 8.90, 8.65, 8.54,
    8.99, 8.70, 8.54, 8.40,
    9.06, 8.71, 8.33, 8.29,
    9.22, 8.86, 8.56, 8.54
    ]
mae = [
    7.29, 6.87, 6.60, 6.43,
    7.13, 6.94, 6.57, 6.25,
    7.02, 6.80, 6.56, 6.29,
    7.07, 6.87, 6.52, 6.28,
    7.05, 7.08, 6.61, 6.32
    ]
r2 = [
    0.42, 0.49, 0.63, 0.62,
    0.42, 0.49, 0.62, 0.62,
    0.47, 0.50, 0.63, 0.64,
    0.46, 0.50, 0.65, 0.65,
    0.44, 0.48, 0.63, 0.63
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
ax2.set_ylim(0, 10)
ax2.set_yticks(np.linspace(0, 10, 11))  # More refined tick marks

# Hide x-axis on the first plot
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()

plt.title("", fontsize=0)
plt.tight_layout()

# Save and display the plot
plt.savefig("rf_regression_metrics_without_id.png")
plt.show()