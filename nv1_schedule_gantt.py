# nv1_schedule_gantt.py
# Requires: matplotlib (pip install matplotlib)

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ---- Timeline axis (months) ----
MONTHS = [
    "Aug-25", "Sep-25", "Oct-25", "Nov-25", "Dec-25",
    "Jan-26", "Feb-26", "Mar-26", "Apr-26", "May-26", "Jun-26",
    "Jul-26", "Aug-26", "Sep-26", "Oct-26", "Nov-26", "Dec-26"
]
def m(label: str) -> int:
    """Return 0-based index for a month label in MONTHS."""
    return MONTHS.index(label)

# ---- Activities (final state) ----
# One row per bar. If an activity spans multiple disjoint periods (e.g., Alpha+ Testing / Demos),
# list them as separate rows.
# Fields: (label, start_month, end_month, phase)
TASKS = [
    # ALPHA
    ("Testing / Demos",                    "Aug-25", "Oct-25", "alpha"),

    # ALPHA+
    ("Improved Hydrodynamic Design",       "Aug-25", "Sep-25", "alpha_plus"),
    ("Improved Hydrodynamic Mechanism Sourcing", "Oct-25", "Oct-25", "alpha_plus"),
    ("Testing / Demos",                    "Nov-25", "Nov-25", "alpha_plus"),
    ("Boat Shows",                         "Dec-25", "Feb-26", "alpha_plus"),
    ("Testing / Demos",                    "Mar-26", "Aug-26", "alpha_plus"),

    # BETA
    ("Hull Design",                        "Aug-25", "Sep-25", "beta"),
    ("Hull Build",                         "Sep-25", "Mar-26", "beta"),
    ("Interior Design",                    "Sep-25", "Apr-26", "beta"),
    ("Mechanical / Electrical Design",     "Aug-25", "Apr-26", "beta"),
    ("Battery Sourcing",                   "Nov-25", "Feb-26", "beta"),
    ("Mechanical / Electrical Build",      "Mar-26", "Jul-26", "beta"),
    ("Testing / Demos",                    "Jun-26", "Dec-26", "beta"),
]

# Convert month strings to indices
tasks_idx = [(label, m(start), m(end), phase) for (label, start, end, phase) in TASKS]

# ---- Styling (blue theme) ----
COLORS = {
    "alpha":      "#1f77b4",  # medium blue
    "alpha_plus": "#4fa3d1",  # lighter blue
    "beta":       "#0d3b66",  # dark blue
}

# ---- Plot ----
fig, ax = plt.subplots(figsize=(12, 6))

for i, (label, start_i, end_i, phase) in enumerate(tasks_idx):
    ax.barh(
        y=i,
        width=(end_i - start_i + 1),       # inclusive months
        left=start_i,
        height=0.5,
        align="center",
        color=COLORS[phase],
        edgecolor="none"
    )

ax.set_yticks(range(len(tasks_idx)))
ax.set_yticklabels([t[0] for t in tasks_idx])

ax.set_xticks(range(len(MONTHS)))
ax.set_xticklabels(MONTHS, rotation=45, ha="right")

ax.invert_yaxis()  # top to bottom
ax.set_title("High-Level NV1 Alpha and Beta Engineering Schedule", fontsize=16, fontweight="bold", pad=12)
ax.set_xlabel("Timeline (Months)")
ax.set_ylabel("Activities")

legend_elements = [
    Patch(facecolor=COLORS["alpha"],      label="Alpha Activities"),
    Patch(facecolor=COLORS["alpha_plus"], label="Alpha+ Activities"),
    Patch(facecolor=COLORS["beta"],       label="Beta Activities"),
]
ax.legend(handles=legend_elements, loc="upper right")

plt.tight_layout()
plt.savefig("high_level_nv1_alpha_beta_engineering_schedule.png", dpi=300)
print("Saved: high_level_nv1_alpha_beta_engineering_schedule.png")