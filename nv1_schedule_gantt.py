import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import defaultdict

# ---- Timeline axis (months) ----
MONTHS = [
    "Aug-25", "Sep-25", "Oct-25", "Nov-25", "Dec-25",
    "Jan-26", "Feb-26", "Mar-26", "Apr-26", "May-26", "Jun-26",
    "Jul-26", "Aug-26", "Sep-26", "Oct-26", "Nov-26", "Dec-26",
    "Jan-27", "Feb-27", "Mar-27", "Apr-27", "May-27"
]
def m(label: str) -> int:
    """Return 0-based index for a month label in MONTHS."""
    return MONTHS.index(label)

# ---- Activities ----
TASKS = [
    ("Testing / Demos",                    "Aug-25", "Oct-25", "alpha"),
    ("Improved Hydrodynamic Design",       "Aug-25", "Sep-25", "alpha_plus"),
    ("Improved Hydrodynamic Design",       "Nov-25", "Dec-25", "alpha_plus"),
    ("Improved Hydrodynamic Mechanism Sourcing", "Oct-25", "Oct-25", "alpha_plus"),
    ("Testing / Demos",                    "Nov-25", "Nov-25", "alpha_plus"),
    ("Boat Shows",                         "Dec-25", "Feb-26", "alpha_plus"),
    ("Testing / Demos",                    "Mar-26", "Apr-27", "alpha_plus"),
    ("Hull Design",                        "Aug-25", "Dec-25", "beta"),
    ("Hull Build",                         "Jan-26", "Jul-26", "beta"),
    ("Interior Design / Sourcing",         "Sep-25", "Jul-26", "beta"),
    ("Mech / Elec Design",                 "Aug-25", "Jul-26", "beta"),
    ("Mech / Elec Supplier Selection",     "Aug-25", "Jun-26", "beta"),
    ("Mech / Elec Sourcing",               "Mar-26", "Jun-26", "beta"),
    ("Mechanical / Electrical Build",      "Jul-26", "Oct-26", "beta"),
    ("Testing / Fixing Issues",            "Nov-26", "Apr-27", "beta"),
]

# ---- Milestones ----
# Fields: (label, month, phase, description)
#MILESTONES = None
MILESTONES = [
    ("Testing / Fixing Issues", "May-27", "beta", "Delivery")
]

# ---- Convert month strings to indices ----
tasks_idx = [(label, m(start), m(end), phase) for (label, start, end, phase) in TASKS]
if MILESTONES is not None:
    milestones_idx = [(label, m(month), phase, desc) for (label, month, phase, desc) in MILESTONES]

# ---- Colors ----
COLORS = {
    "alpha":      "#1f77b4",
    "alpha_plus": "#4fa3d1",
    "beta":       "#0d3b66",
}

# ---- Group by (label, phase) ----
groups = defaultdict(list)
for label, start_i, end_i, phase in tasks_idx:
    groups[(label, phase)].append((start_i, end_i))

PHASE_PRETTY = {"alpha": "Alpha", "alpha_plus": "Alpha+", "beta": "Pre-Production"}

# ---- Plot ----
fig, ax = plt.subplots(figsize=(12, 6))
rows = list(groups.keys())  # (label, phase) pairs

# Draw bars
for y, (label, phase) in enumerate(rows):
    for start_i, end_i in groups[(label, phase)]:
        ax.barh(
            y=y,
            width=(end_i - start_i + 1),
            left=start_i,
            height=0.5,
            align="center",
            color=COLORS[phase],
            edgecolor="none"
        )

# Draw milestones
if MILESTONES is not None:
    for label, month_i, phase, desc in milestones_idx:
        if (label, phase) in rows:
            y = rows.index((label, phase))
            ax.scatter(
                month_i,  # center of month
                y,
                marker='D',
                s=100,
                color='orange',
                edgecolor='black',
                zorder=3
            )
            ax.text(
                month_i,
                y+.7,
                desc,
                ha='center',
                va='bottom',
                fontsize=10,
                rotation=0
            )

# Labels & axes
ylabels = [label for (label, _) in rows]

ax.set_yticks(range(len(rows)))
ax.set_yticklabels(ylabels)
ax.set_xticks(range(len(MONTHS)))
ax.set_xticklabels(MONTHS, rotation=45, ha="right")
ax.invert_yaxis()
ax.set_title("High-Level NV1 Schedule", fontsize=16, fontweight="bold", pad=12)
ax.set_xlabel("Timeline (Months)")
ax.set_ylabel("Activities")

# Vertical gridlines at month markers
ax.grid(axis='x', linestyle='--', color='gray', alpha=0.7)

legend_elements = [
    Patch(facecolor=COLORS["alpha"],      label="Alpha Activities"),
    Patch(facecolor=COLORS["alpha_plus"], label="Alpha+ Activities"),
    Patch(facecolor=COLORS["beta"],       label="Pre-Production Activities")
]
ax.legend(handles=legend_elements, loc="upper right")

plt.tight_layout()
plt.savefig("high_level_nv1_alpha_beta_engineering_schedule.png", dpi=300)
print("Saved: high_level_nv1_alpha_beta_engineering_schedule.png")

# Show the chart
plt.show()