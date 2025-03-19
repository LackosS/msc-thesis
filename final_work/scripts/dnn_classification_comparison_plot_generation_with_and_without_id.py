import matplotlib.pyplot as plt
import numpy as np

# Data from the classification accuracy table
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

performance_tiered_with_id = [
    84.48, 84.48, 89.26, 88.43,  # TabNet
    81.95, 83.75, 89.67, 88.02,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    82.67, 81.59, 87.18, 88.02   # Optimized FastAI
]


subject_based_with_id = [
    50.54, 39.35, 42.96, 44.77,  # TabNet
    42.24, 46.93, 44.21, 50.00,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    38.99, 49.82, 54.96, 52.48   # Optimized FastAI
]

buffer_zone_with_id = [
    54.87, 43.32, 65.70, 52.48,  # TabNet
    50.90, 50.18, 55.79, 58.68,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    55.23, 48.01, 60.74, 61.98   # Optimized FastAI
]


performance_tiered_without_id = [
    82.67, 83.03, 88.02, 88.02,  # TabNet
    81.95, 83.75, 89.26, 88.84,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    81.23, 80.87, 86.36, 86.78   # Optimized FastAI
]

subject_based_without_id = [
    42.96, 44.77, 43.39, 55.37,  # TabNet
    50.90, 43.32, 50.00, 53.31,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    48.38, 45.13, 52.89, 58.68   # Optimized FastAI
]


buffer_zone_without_id = [
    47.65, 47.29, 50.00, 58.68,  # TabNet
    56.68, 50.18, 52.48, 55.37,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    52.35, 50.18, 57.85, 62.40   # Optimized FastAI
]

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_ylim([0, 100]) 

x = np.arange(len(models))

for y_values, label, color in zip([
    performance_tiered_with_id, subject_based_with_id, buffer_zone_with_id,
    performance_tiered_without_id, subject_based_without_id, buffer_zone_without_id
], [
    "Performance-Tiered (With ID)", "Subject-Based (With ID)", "Buffer-Zone (With ID)",
    "Performance-Tiered (Without ID)", "Subject-Based (Without ID)", "Buffer-Zone (Without ID)"
], ["tab:blue", "tab:orange", "tab:green", "tab:blue", "tab:orange", "tab:green"]):
    alpha = 1.0 if "With ID" in label else 0.5
    linestyle = "-" if "Performance-Tiered" in label else "--" if "Subject-Based" in label else ":"
    marker = "o" if "Performance-Tiered" in label else "s" if "Subject-Based" in label else "^"
    ax.plot(x, y_values, label=label, marker=marker, linestyle=linestyle, color=color, alpha=alpha)
    for i, val in enumerate(y_values):
        ax.text(x[i], val + 1, f"{val:.2f}", fontsize=8, ha='center', color=color, alpha=alpha)

# Labels
ax.set_xlabel("Model and Dataset", fontsize=14)
ax.set_ylabel("Classification Accuracy (%)", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, fontsize=10, ha="right")
ax.grid(True, linestyle="--", alpha=0.7)
#ax.legend(loc="upper left", bbox_to_anchor=(0.8, 0.75), ncol=1, fontsize=8)
ax.legend(loc="lower center", bbox_to_anchor=(0.9, 0.0), ncol=1, fontsize=8)
plt.tight_layout()
plt.savefig("dnn_classification_accuracy.png", bbox_inches="tight")
plt.show()