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

performance_tiered = [
    84.48, 84.48, 89.26, 88.43,  # TabNet
    81.95, 83.75, 89.67, 88.02,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    82.67, 81.59, 87.18, 88.02   # Optimized FastAI
]


subject_based = [
    50.54, 39.35, 42.96, 44.77,  # TabNet
    42.24, 46.93, 44.21, 50.00,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    38.99, 49.82, 54.96, 52.48   # Optimized FastAI
]

buffer_zone= [
    54.87, 43.32, 65.70, 52.48,  # TabNet
    50.90, 50.18, 55.79, 58.68,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    55.23, 48.01, 60.74, 61.98   # Optimized FastAI
]

# Plotting classification accuracies
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(models))
ax.plot(x, performance_tiered, label="Performance-Tiered", marker="o", linestyle="-", color="tab:blue")
ax.plot(x, subject_based, label="Subject-Based", marker="s", linestyle="--", color="tab:orange")
ax.plot(x, buffer_zone, label="Buffer-Zone", marker="^", linestyle=":", color="tab:green")

# Add value labels to each point slightly above the points
for i, txt in enumerate(performance_tiered):
    ax.text(x[i], performance_tiered[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(subject_based):
    ax.text(x[i], subject_based[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(buffer_zone):
    ax.text(x[i], buffer_zone[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')

ax.set_xlabel("Model and Dataset", fontsize=14)
ax.set_ylabel("Classification Accuracy (%)", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, fontsize=10, ha="right")
ax.legend(loc="lower right", fontsize=12)

plt.title("", fontsize=16)
ax.set_ylim(0, 100)
plt.tight_layout()

# Save and display the plot
plt.savefig("dnn_classification_accuracy_with_id.png")
plt.show()

performance_tiered = [
    82.67, 83.03, 88.02, 88.02,  # TabNet
    81.95, 83.75, 89.26, 88.84,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    81.23, 80.87, 86.36, 86.78   # Optimized FastAI
]

subject_based = [
    42.96, 44.77, 43.39, 55.37,  # TabNet
    50.90, 43.32, 50.00, 53.31,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    48.38, 45.13, 52.89, 58.68   # Optimized FastAI
]


buffer_zone = [
    47.65, 47.29, 50.00, 58.68,  # TabNet
    56.68, 50.18, 52.48, 55.37,  # Optimized TabNet
    4.69, 4.69, 7.85, 7.85,      # FastAI
    52.35, 50.18, 57.85, 62.40   # Optimized FastAI
]

# Plotting classification accuracies
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(models))
ax.plot(x, performance_tiered, label="Performance-Tiered", marker="o", linestyle="-", color="tab:blue")
ax.plot(x, subject_based, label="Subject-Based", marker="s", linestyle="--", color="tab:orange")
ax.plot(x, buffer_zone, label="Buffer-Zone", marker="^", linestyle=":", color="tab:green")

# Add value labels to each point slightly above the points
for i, txt in enumerate(performance_tiered):
    ax.text(x[i], performance_tiered[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(subject_based):
    ax.text(x[i], subject_based[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')
for i, txt in enumerate(buffer_zone):
    ax.text(x[i], buffer_zone[i] + 1, f"{txt:.2f}", fontsize=8, ha='center')

ax.set_xlabel("Model and Dataset", fontsize=14)
ax.set_ylabel("Classification Accuracy (%)", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, fontsize=10, ha="right")
ax.legend(loc="lower right", fontsize=12)

plt.title("", fontsize=16)
ax.set_ylim(0, 100)
plt.tight_layout()

# Save and display the plot
plt.savefig("dnn_classification_accuracy_without_id.png")
plt.show()