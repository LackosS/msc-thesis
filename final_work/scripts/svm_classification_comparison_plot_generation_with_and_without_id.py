import matplotlib.pyplot as plt
import numpy as np

# Data from the classification accuracy table
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

performance_tiered_with_id = [
    81.23, 81.95, 81.82, 81.82,  # Simple SVM
    80.51, 74.73, 66.12, 56.20,  # Weighted SVM
    80.87, 80.14, 85.95, 86.36,  # Optimized SVM
    79.42, 79.42, 81.82, 81.82,  # Bagged SVM
    81.59, 82.31, 88.02, 88.84   # Stacked SVM
]

subject_based_with_id = [
    49.10, 49.10, 49.59, 49.17,
    49.46, 41.52, 44.63, 35.95,
    52.71, 49.82, 54.96, 56.61,
    42.96, 42.96, 58.26, 58.26,
    45.49, 46.21, 54.96, 53.31
]

buffer_zone_with_id = [
    54.87, 54.87, 53.72, 53.72,
    50.54, 43.68, 48.35, 38.84,
    57.04, 53.79, 58.68, 60.74,
    45.85, 45.85, 61.16, 61.16,
    53.43, 53.43, 58.68, 57.85
]

performance_tiered_without_id = [
    81.59, 81.95, 81.82, 81.82,
    81.59, 57.40, 56.20, 49.17,
    80.51, 80.87, 86.78, 88.02,
    80.87, 80.87, 81.40, 81.40,
    81.95, 81.95, 88.43, 88.84
]

subject_based_without_id = [
    49.10, 49.10, 47.93, 49.59,
    33.21, 27.44, 41.74, 33.06,
    52.35, 49.10, 55.37, 57.85,
    51.99, 52.35, 53.31, 53.31,
    46.57, 46.21, 54.13, 52.89
]

buffer_zone_without_id = [
    55.23, 54.51, 54.13, 54.96,
    40.43, 27.08, 42.15, 35.95,
    56.68, 53.07, 61.57, 62.81,
    57.40, 57.76, 56.20, 56.20,
    49.46, 51.26, 57.02, 55.79
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
plt.savefig("svm_classification_accuracy.png", bbox_inches="tight")
plt.show()