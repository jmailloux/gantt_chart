# nv1_schedule_plot.py
# Plot logic that imports data from nv1_schedule_data.py
# Requires: matplotlib (pip install matplotlib)

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import defaultdict

from nv1_gantt_data import MONTHS, TASKS, MILESTONES

# ---- Helpers ----
def m(label: str) -> int:
    """Return 0-based index for a month label in MONTHS."""
    return MONTHS.index(label)

# ---- Colors & labels (kept in code) ----
COLORS = {
    "alpha":      "#1f77b4",
    "alpha_plus": "#4fa3d1",
    "beta":       "#0d3b66",
}

# Map for pretty-printing (not used in y-axis labels here, but kept for future use)
PHASE_PRETTY = {"alpha": "Alpha", "alpha_plus": "Alpha+", "beta": "Pre-Production"}

def build_chart(
    outfile: str = "high_level_nv1_alpha_beta_engineering_schedule.png",
    show: bool = True
):
    # ---- Convert month strings to indices ----
    tasks_idx = [(label, m(start), m(end), phase) for (label, start, end, phase) in TASKS]
    milestones_idx = None
    if MILESTONES is not None:
        milestones_idx = [(label, m(month), phase, desc) for (label, month, phase, desc) in MILESTONES]

    # ---- Group by (label, phase) ----
    groups = defaultdict(list)
    for label, start_i, end_i, phase in tasks_idx:
        groups[(label, phase)].append((start_i, end_i))

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
    if milestones_idx is not None:
        for label, month_i, phase, desc in milestones_idx:
            if (label, phase) in rows:
                y = rows.index((label, phase))
                ax.scatter(
                    month_i,  # positioning consistent with your latest code
                    y,
                    marker='D',
                    s=100,
                    color='orange',
                    edgecolor='black',
                    zorder=3
                )
                ax.text(
                    month_i,
                    y + 0.7,
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
    plt.savefig(outfile, dpi=300)
    print(f"Saved: {outfile}")

    if show:
        plt.show()

if __name__ == "__main__":
    build_chart()
