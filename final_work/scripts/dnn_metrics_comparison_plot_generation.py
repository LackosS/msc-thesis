import matplotlib.pyplot as plt
import numpy as np

# Data from the table
models = [
    "Tabnet Model (5 Exams, No Groups/Time)",
    "Tabnet Model (6 Exams, No Groups/Time)",
    "Tabnet Model (5 Exams, With Groups/Time)",
    "Tabnet Model (6 Exams, With Groups/Time)",
    "Optimized Tabnet Model (5 Exams, No Groups/Time)",
    "Optimized Tabnet Model (6 Exams, No Groups/Time)",
    "Optimized Tabnet Model (5 Exams, With Groups/Time)",
    "Optimized Tabnet Model (6 Exams, With Groups/Time)",
    "FastAI Model (5 Exams, No Groups/Time)",
    "FastAI Model (6 Exams, No Groups/Time)",
    "FastAI Model (5 Exams, With Groups/Time)",
    "FastAI Model (6 Exams, With Groups/Time)",
    "Optimized FastAI Model (5 Exams, No Groups/Time)",
    "Optimized FastAI Model (6 Exams, No Groups/Time)",
    "Optimized FastAI Model (5 Exams, With Groups/Time)",
    "Optimized FastAI Model (6 Exams, With Groups/Time)"
]

mse = [
    76.78, 77.31, 69.12, 70.54,  # TabNet
    76.56, 73.61, 68.31, 63.73,  # Optimized TabNet
    1639.26, 1627.85, 1693.12, 1699.67,  # FastAI
    83.74, 76.22, 77.11, 77.74   # Optimized FastAI
]

rmse = [
    8.76, 8.79, 8.31, 8.40,  # TabNet
    8.75, 8.58, 8.27, 7.98,  # Optimized TabNet
    40.49, 40.35, 41.15, 41.23,  # FastAI
    9.15, 8.73, 8.78, 8.82   # Optimized FastAI
]

mae = [
    6.97, 7.29, 6.43, 6.76,  # TabNet
    7.20, 6.91, 6.90, 6.36,  # Optimized TabNet
    39.18, 39.05, 39.42, 39.64,  # FastAI
    7.36, 6.91, 6.88, 6.78   # Optimized FastAI
]

r2 = [
    0.50, 0.49, 0.65, 0.64,  # TabNet
    0.50, 0.52, 0.65, 0.68,  # Optimized TabNet
    -9.77, -9.69, -7.58, -7.61,  # FastAI
    0.45, 0.50, 0.61, 0.61   # Optimized FastAI
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
ax2.set_ylim(0, 43)
ax2.set_yticks(np.arange(0, 43, 10))  # More refined tick marks

# Hide x-axis on the first plot
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()

plt.title("", fontsize=16)
plt.tight_layout()

# Save and display the plot
plt.savefig("dnn_regression_metrics_with_id.png")
plt.show()

mse = [
    81.74, 74.65, 77.84, 75.41,  # TabNet
    70.73, 69.81, 64.70, 67.14,  # Optimized TabNet
    1649.62, 1651.25, 1721.72, 1713.95,  # FastAI
    81.71, 76.30, 87.26, 71.06   # Optimized FastAI
]

rmse = [
    9.04, 8.64, 8.82, 8.68,  # TabNet
    8.41, 8.36, 8.04, 8.19,  # Optimized TabNet
    40.62, 40.64, 41.49, 41.40,  # FastAI
    9.04, 8.73, 9.34, 8.43   # Optimized FastAI
]

mae = [
    7.49, 7.02, 7.37, 7.05,  # TabNet
    6.56, 6.85, 6.77, 6.50,  # Optimized TabNet
    39.36, 39.39, 39.72, 39.84,  # FastAI
    7.22, 7.02, 6.95, 6.39   # Optimized FastAI
]

r2= [
    0.46, 0.51, 0.61, 0.62,  # TabNet
    0.54, 0.54, 0.67, 0.66,  # Optimized TabNet
    -9.83, -9.84, -7.72, -7.68,  # FastAI
    0.46, 0.50, 0.56, 0.64   # Optimized FastAI
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
ax2.set_ylim(0, 43)
ax2.set_yticks(np.arange(0, 43, 10))  # More refined tick marks

# Hide x-axis on the first plot
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()

plt.title("", fontsize=16)
plt.tight_layout()

# Save and display the plot
plt.savefig("dnn_regression_metrics_without_id.png")
plt.show()