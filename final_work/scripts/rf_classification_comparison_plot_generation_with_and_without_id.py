import matplotlib.pyplot as plt
import numpy as np

# Models
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

# Accuracy Data (With and Without ID)
performance_tiered_with_id = [
    82.31, 83.39, 88.43, 88.43,
    82.31, 83.39, 88.43, 88.43,
    81.59, 81.95, 88.02, 88.43,
    81.95, 82.67, 88.84, 88.43,
    81.23, 83.03, 88.43, 89.26
]

subject_based_with_id = [
    42.60, 44.40, 51.65, 51.65,
    42.96, 44.04, 52.07, 52.07,
    46.93, 45.49, 52.07, 52.48,
    44.40, 45.49, 55.37, 53.31,
    46.57, 44.40, 50.00, 54.55
]

buffer_zone_with_id = [
    49.46, 51.26, 54.13, 55.79,
    57.40, 57.04, 55.79, 56.20,
    57.76, 60.29, 56.20, 57.44,
    58.48, 61.37, 59.50, 58.26,
    60.29, 59.21, 57.02, 57.44
]

performance_tiered_without_id = [
    81.59, 82.67, 88.84, 88.02,
    81.59, 82.67, 88.84, 88.02,
    81.95, 82.31, 88.02, 88.43,
    82.31, 83.03, 89.26, 88.84,
    81.23, 83.03, 88.84, 88.84
]

subject_based_without_id = [
    44.96, 46.57, 51.24, 53.31,
    42.96, 46.93, 52.07, 52.89,
    44.04, 45.85, 52.48, 50.83,
    44.77, 44.77, 53.72, 53.31,
    45.13, 39.71, 54.55, 50.83
]

buffer_zone_without_id = [
    46.93, 50.90, 53.72, 54.13,
    46.93, 51.26, 54.55, 53.72,
    49.46, 50.18, 54.96, 53.72,
    45.85, 48.01, 56.61, 56.20,
    51.26, 45.85, 60.33, 57.44
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
plt.savefig("rf_classification_accuracy.png", bbox_inches="tight")
plt.show()
