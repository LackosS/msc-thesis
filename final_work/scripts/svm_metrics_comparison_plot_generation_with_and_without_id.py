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

mse_with_id = [
    95.53, 93.40, 165.25, 164.34,  # Simple SVM
    87.35, 155.46, 2578.02, 14798.54,  # Weighted SVM
    93.56, 91.96, 86.88, 87.12,  # Optimized SVM
    168.31, 168.39, 227.68, 227.72,  # Bagged SVM
    77.77, 75.89, 71.49, 66.35  # Stacked SVM
]

rmse_with_id = [
    9.77, 9.66, 12.86, 12.82,
    9.35, 12.47, 50.77, 121.65,
    9.67, 9.59, 9.32, 9.33,
    12.97, 12.98, 15.09, 15.09,
    8.82, 8.71, 8.46, 8.15
]

mae_with_id = [
    7.46, 7.42, 8.59, 8.50,
    7.20, 9.65, 39.28, 84.34,
    7.17, 7.13, 7.14, 7.08,
    9.04, 9.04, 9.52, 9.52,
    6.89, 6.84, 6.58, 6.09
]

r2_with_id = [
    0.37, 0.39, 0.16, 0.17,
    0.43, -0.02, -12.06, -73.98,
    0.39, 0.40, 0.56, 0.56,
    -0.11, -0.11, -0.15, -0.15,
    0.49, 0.50, 0.64, 0.66
]

mse_without_id = [
    93.29, 89.60, 162.75, 161.22,
    108.49, 447.18, 19671.66, 135473.64,
    94.54, 91.57, 85.61, 79.90,
    108.57, 107.59, 117.31, 116.95,
    76.75, 75.05, 73.50, 69.38
]

rmse_without_id = [
    9.66, 9.47, 12.76, 12.70,
    10.42, 21.15, 140.26, 368.07,
    9.72, 9.57, 9.25, 8.94,
    10.42, 10.37, 10.83, 10.81,
    8.76, 8.66, 8.57, 8.33
]

mae_without_id = [
    7.33, 7.24, 8.58, 8.46,
    8.27, 16.14, 70.77, 198.06,
    7.18, 7.14, 6.98, 6.53,
    7.82, 7.78, 7.87, 7.85,
    6.96, 6.84, 6.85, 6.36
]

r2_without_id = [
    0.39, 0.41, 0.18, 0.18,
    0.29, -1.94, -98.66, -685.31,
    0.38, 0.40, 0.57, 0.60,
    0.29, 0.29, 0.41, 0.41,
    0.50, 0.51, 0.63, 0.65
]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))

x = np.arange(len(models))

# With ID
ax.plot(x, mse_with_id, label="MSE (With ID)", marker="o", linestyle="-", color="tab:red")
ax.plot(x, rmse_with_id, label="RMSE (With ID)", marker="s", linestyle="--", color="tab:blue")
ax.plot(x, mae_with_id, label="MAE (With ID)", marker="^", linestyle=":", color="tab:green")
ax.plot(x, r2_with_id, label="R² (With ID)", marker="d", linestyle="-.", color="tab:purple")

# Without ID (faded colors)
ax.plot(x, mse_without_id, label="MSE (Without ID)", marker="o", linestyle="-", color="tab:red", alpha=0.5)
ax.plot(x, rmse_without_id, label="RMSE (Without ID)", marker="s", linestyle="--", color="tab:blue", alpha=0.5)
ax.plot(x, mae_without_id, label="MAE (Without ID)", marker="^", linestyle=":", color="tab:green", alpha=0.5)
ax.plot(x, r2_without_id, label="R² (Without ID)", marker="d", linestyle="-.", color="tab:purple", alpha=0.5)

# Labels
ax.set_xlabel("Model and Dataset", fontsize=14)
ax.set_ylabel("Regression Metrics", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, fontsize=10, ha="right")

# Add value labels above points
for i, (mse_w, mse_wo) in enumerate(zip(mse_with_id, mse_without_id)):
    ax.text(x[i], mse_w + 1, f"{mse_w:.2f}", fontsize=8, ha='center', color="tab:red")
    ax.text(x[i], mse_wo + 1, f"{mse_wo:.2f}", fontsize=8, ha='center', color="tab:red", alpha=0.5)

# Grid
ax.grid(True, linestyle="--", alpha=0.7)

ax.legend(loc="lower center", bbox_to_anchor=(0.92, 0.3), ncol=1, fontsize=8)

# Layout
plt.tight_layout()

# Save and display the plot
plt.savefig("svm_regression_metrics.png", bbox_inches="tight")
plt.show()