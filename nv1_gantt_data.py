# nv1_schedule_data.py
# Data-only module: months, tasks, milestones.

# ---- Timeline axis (months) ----
MONTHS = [
    "Aug-25", "Sep-25", "Oct-25", "Nov-25", "Dec-25",
    "Jan-26", "Feb-26", "Mar-26", "Apr-26", "May-26", "Jun-26",
    "Jul-26", "Aug-26", "Sep-26", "Oct-26", "Nov-26", "Dec-26",
    "Jan-27", "Feb-27", "Mar-27", "Apr-27", "May-27"
]

# ---- Activities ----
# Fields: (label, start_month, end_month, phase)
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
# Set to None if no milestones.
MILESTONES = [
    ("Testing / Fixing Issues", "May-27", "beta", "Delivery")
]
