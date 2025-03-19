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

mse_with_id = [
    76.78, 77.31, 69.12, 70.54,  # TabNet
    76.56, 73.61, 68.31, 63.73,  # Optimized TabNet
    1639.26, 1627.85, 1693.12, 1699.67,  # FastAI
    83.74, 76.22, 77.11, 77.74   # Optimized FastAI
]

rmse_with_id = [
    8.76, 8.79, 8.31, 8.40,  # TabNet
    8.75, 8.58, 8.27, 7.98,  # Optimized TabNet
    40.49, 40.35, 41.15, 41.23,  # FastAI
    9.15, 8.73, 8.78, 8.82   # Optimized FastAI
]

mae_with_id = [
    6.97, 7.29, 6.43, 6.76,  # TabNet
    7.20, 6.91, 6.90, 6.36,  # Optimized TabNet
    39.18, 39.05, 39.42, 39.64,  # FastAI
    7.36, 6.91, 6.88, 6.78   # Optimized FastAI
]

r2_with_id = [
    0.50, 0.49, 0.65, 0.64,  # TabNet
    0.50, 0.52, 0.65, 0.68,  # Optimized TabNet
    -9.77, -9.69, -7.58, -7.61,  # FastAI
    0.45, 0.50, 0.61, 0.61   # Optimized FastAI
]

mse_without_id = [
    81.74, 74.65, 77.84, 75.41,  # TabNet
    70.73, 69.81, 64.70, 67.14,  # Optimized TabNet
    1649.62, 1651.25, 1721.72, 1713.95,  # FastAI
    81.71, 76.30, 87.26, 71.06   # Optimized FastAI
]

rmse_without_id = [
    9.04, 8.64, 8.82, 8.68,  # TabNet
    8.41, 8.36, 8.04, 8.19,  # Optimized TabNet
    40.62, 40.64, 41.49, 41.40,  # FastAI
    9.04, 8.73, 9.34, 8.43   # Optimized FastAI
]

mae_without_id = [
    7.49, 7.02, 7.37, 7.05,  # TabNet
    6.56, 6.85, 6.77, 6.50,  # Optimized TabNet
    39.36, 39.39, 39.72, 39.84,  # FastAI
    7.22, 7.02, 6.95, 6.39   # Optimized FastAI
]

r2_without_id = [
    0.46, 0.51, 0.61, 0.62,  # TabNet
    0.54, 0.54, 0.67, 0.66,  # Optimized TabNet
    -9.83, -9.84, -7.72, -7.68,  # FastAI
    0.46, 0.50, 0.56, 0.64   # Optimized FastAI
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
plt.savefig("dnn_regression_metrics.png", bbox_inches="tight")
plt.show()