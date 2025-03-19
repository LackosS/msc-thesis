import matplotlib.pyplot as plt
import numpy as np

# Data from the classification accuracy table
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

performance_tiered = [
    82.31, 83.39, 88.43, 88.43,
    82.31, 83.39, 88.43, 88.43,
    81.59, 81.95, 88.02, 88.43,
    81.95, 82.67, 88.84, 88.43,
    81.23, 83.03, 88.43, 89.26
    ]
subject_based = [
    42.60, 44.40, 51.65, 51.65,
    42.96, 44.04, 52.07, 52.07,
    46.93, 45.49, 52.07, 52.48,
    44.40, 45.49, 55.37, 53.31,
    46.57, 44.40, 50.00, 54.55
    ]
buffer_zone = [
    49.46, 51.26, 54.13, 55.79,
    57.40, 57.04, 55.79, 56.20,
    57.76, 60.29, 56.20, 57.44,
    58.48, 61.37, 59.50, 58.26,
    60.29, 59.21, 57.02, 57.44
    ]

# Plotting classification accuracies
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(models))
ax.plot(x, performance_tiered, label="Performance-Tiered", marker="o", linestyle="-", color="tab:blue")
ax.plot(x, subject_based, label="Subject-Based", marker="s", linestyle="--", color="tab:orange")
ax.plot(x, buffer_zone, label="Buffer-Zone", marker="^", linestyle=":", color="tab:green")

# Add value labels to each point slightly above the points
for i, txt in enumerate(performance_tiered):
    ax.text(x[i], performance_tiered[i] + 1.5, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(subject_based):
    ax.text(x[i], subject_based[i] + 1.5, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(buffer_zone):
    ax.text(x[i], buffer_zone[i] + 1.5, f"{txt:.2f}", fontsize=8, ha='center')

ax.set_xlabel("Model and Dataset", fontsize=14)
ax.set_ylabel("Classification Accuracy (%)", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, fontsize=10, ha="right")
ax.set_ylim(0, max(max(performance_tiered), max(subject_based), max(buffer_zone)) * 1.2)

ax.legend(loc="lower right", fontsize=12)
plt.title("", fontsize=16)
plt.tight_layout()

# Save and display the plot
plt.savefig("rf_classification_accuracy_with_id.png")
plt.show()

performance_tiered = [
    81.59, 82.67, 88.84, 88.02,
    81.59, 82.67, 88.84, 88.02,
    81.95, 82.31, 88.02, 88.43,
    82.31, 83.03, 89.26, 88.84,
    81.23, 83.03, 88.84, 88.84
    ]
subject_based = [
    44.96, 46.57, 51.24, 53.31,
    42.96, 46.93, 52.07, 52.89,
    44.04, 45.85, 52.48, 50.83,
    44.77, 44.77, 53.72, 53.31,
    45.13, 39.71, 54.55, 50.83
    ]
buffer_zone = [
    46.93, 50.90, 53.72, 54.13,
    46.93, 51.26, 54.55, 53.72,
    49.46, 50.18, 54.96, 53.72,
    45.85, 48.01, 56.61, 56.20,
    51.26, 45.85, 60.33, 57.44
    ]

# Plotting classification accuracies
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(models))
ax.plot(x, performance_tiered, label="Performance-Tiered", marker="o", linestyle="-", color="tab:blue")
ax.plot(x, subject_based, label="Subject-Based", marker="s", linestyle="--", color="tab:orange")
ax.plot(x, buffer_zone, label="Buffer-Zone", marker="^", linestyle=":", color="tab:green")

# Add value labels to each point slightly above the points
for i, txt in enumerate(performance_tiered):
    ax.text(x[i], performance_tiered[i] + 1.5, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(subject_based):
    ax.text(x[i], subject_based[i] + 1.5, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(buffer_zone):
    ax.text(x[i], buffer_zone[i] + 1.5, f"{txt:.2f}", fontsize=8, ha='center')

ax.set_xlabel("Model and Dataset", fontsize=14)
ax.set_ylabel("Classification Accuracy (%)", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, fontsize=10, ha="right")
ax.set_ylim(0, max(max(performance_tiered), max(subject_based), max(buffer_zone)) * 1.2)

ax.legend(loc="lower right", fontsize=12)
plt.title("", fontsize=16)
plt.tight_layout()

# Save and display the plot
plt.savefig("rf_classification_accuracy_without_id.png")
plt.show()