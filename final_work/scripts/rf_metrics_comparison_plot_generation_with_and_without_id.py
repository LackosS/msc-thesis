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

mse_with_id = [
    82.49, 78.42, 74.47, 72.80,
    83.02, 79.20, 74.81, 72.91,
    81.33, 76.88, 73.62, 71.75,
    79.40, 75.96, 70.63, 69.09,
    87.89, 85.02, 73.89, 73.39
    ]
rmse_with_id = [
    9.08, 8.86, 8.63, 8.53,
    9.11, 8.90, 8.65, 8.54,
    9.02, 8.77, 8.58, 8.47,
    8.91, 8.72, 8.40, 8.31,
    9.38, 9.22, 8.60, 8.57
    ]
mae_with_id = [
    7.09, 6.89, 6.57, 6.24,
    7.13, 6.94, 6.57, 6.25,
    7.01, 6.83, 6.60, 6.21,
    6.98, 6.87, 6.53, 6.22,
    7.17, 7.17, 6.67, 6.16
    ]
r2_with_id = [
    0.46, 0.48, 0.62, 0.63,
    0.45, 0.48, 0.62, 0.63,
    0.47, 0.50, 0.63, 0.64,
    0.48, 0.50, 0.64, 0.65,
    0.42, 0.44, 0.63, 0.63
    ]

mse_without_id = [
    88.07, 77.95, 73.98, 75.86,
    88.03, 78.04, 74.43, 75.55,
    80.76, 75.71, 72.85, 70.52,
    82.08, 75.83, 69.40, 68.77,
    84.96, 78.51, 73.31, 73.01
    ]
rmse_without_id = [
    9.38, 8.83, 8.63, 8.69,
    9.11, 8.90, 8.65, 8.54,
    8.99, 8.70, 8.54, 8.40,
    9.06, 8.71, 8.33, 8.29,
    9.22, 8.86, 8.56, 8.54
    ]
mae_without_id = [
    7.29, 6.87, 6.60, 6.43,
    7.13, 6.94, 6.57, 6.25,
    7.02, 6.80, 6.56, 6.29,
    7.07, 6.87, 6.52, 6.28,
    7.05, 7.08, 6.61, 6.32
    ]
r2_without_id = [
    0.42, 0.49, 0.63, 0.62,
    0.42, 0.49, 0.62, 0.62,
    0.47, 0.50, 0.63, 0.64,
    0.46, 0.50, 0.65, 0.65,
    0.44, 0.48, 0.63, 0.63
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
plt.savefig("rf_regression_metrics.png", bbox_inches="tight")
plt.show()