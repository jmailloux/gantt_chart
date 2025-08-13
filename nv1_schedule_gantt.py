# nv1_schedule_gantt.py
# Requires: matplotlib (pip install matplotlib)

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import defaultdict

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
    ("Hull Design",                        "Aug-25", "Dec-25", "beta"),
    ("Hull Build",                         "Jan-26", "Jul-26", "beta"),
    ("Interior Design",                    "Sep-25", "Sep-26", "beta"),
    ("Mech / Elec Design",                 "Aug-25", "Sep-26", "beta"),
    ("Mech / Elec Supplier Selection",     "Aug-25", "Sep-26", "beta"),
    ("Mech / Elec Sourcing",               "Mar-26", "Jun-26", "beta"),
    ("Mechanical / Electrical Build",      "Jul-26", "Oct-26", "beta"),
    ("Testing / Demos",                    "Nov-26", "Dec-26", "beta"),
]

# Convert month strings to indices
tasks_idx = [(label, m(start), m(end), phase) for (label, start, end, phase) in TASKS]

# ---- Styling (blue theme) ----
COLORS = {
    "alpha":      "#1f77b4",  # medium blue
    "alpha_plus": "#4fa3d1",  # lighter blue
    "beta":       "#0d3b66",  # dark blue
}

# ---- Group by (label, phase) so only same label+activity share a row ----
groups = defaultdict(list)  # key: (label, phase) -> list of (start_i, end_i)
for label, start_i, end_i, phase in tasks_idx:
    groups[(label, phase)].append((start_i, end_i))

PHASE_PRETTY = {"alpha": "Alpha", "alpha_plus": "Alpha+", "beta": "Beta"}

# ---- Plot ----
fig, ax = plt.subplots(figsize=(12, 6))

rows = list(groups.keys())  # list of (label, phase) pairs in insertion order
for y, (label, phase) in enumerate(rows):
    for start_i, end_i in groups[(label, phase)]:
        ax.barh(
            y=y,
            width=(end_i - start_i + 1),       # inclusive months
            left=start_i,
            height=0.5,
            align="center",
            color=COLORS[phase],
            edgecolor="none"
        )

# Build y tick labels
ylabels = [label for (label, _) in rows]

ax.set_yticks(range(len(rows)))
ax.set_yticklabels(ylabels)

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

# Show the chart immediately (blocks until the window is closed)
plt.show()