import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

print("=" * 70)
print(" PLACEMENT MANAGEMENT SYSTEM")
print("=" * 70)

# --------------------------------------------------
# 1. PLACEMENT DATA USING PANDAS
# --------------------------------------------------
placement_data = {
    "Student_ID": [
        "S101", "S102", "S103", "S104", "S105",
        "S106", "S107", "S108", "S109", "S110"
    ],

    "Student_Name": [
        "Aarav", "Diya", "Rohan", "Priya", "Krish",
        "Ananya", "Rahul", "Meera", "Arjun", "Neha"
    ],

    "Branch": [
        "Computer", "IT", "Computer", "Electronics", "IT",
        "Computer", "Mechanical", "IT", "Computer", "Electronics"
    ],

    "CGPA": [
        8.7, 9.1, 8.2, 7.8, 8.9,
        9.3, 7.5, 8.6, 9.0, 8.0
    ],

    "Company": [
        "TCS", "Infosys", "Google", "Wipro", "Microsoft",
        "Amazon", "L&T", "Infosys", "TCS", "Wipro"
    ],

    "Package_LPA": [
        6.0, 7.0, 18.0, 5.5, 15.0,
        14.0, 5.0, 7.5, 6.5, 5.0
    ],

    "Status": [
        "Placed", "Placed", "Placed", "Placed", "Placed",
        "Placed", "Not Placed", "Placed", "Placed", "Not Placed"
    ]
}

placements = pd.DataFrame(placement_data)

print("\nPLACEMENT DETAILS")
print("-" * 70)
print(placements.to_string(index=False))

# --------------------------------------------------
# 2. NUMPY ANALYSIS
# --------------------------------------------------
cgpa = np.array(placements["CGPA"])
package = np.array(placements["Package_LPA"])

print("\nNUMPY STATISTICS")
print("-" * 70)
print("Total Students:", len(placements))
print("Average CGPA:", round(np.mean(cgpa), 2))
print("Highest CGPA:", np.max(cgpa))
print("Lowest CGPA:", np.min(cgpa))
print("Average Package:", round(np.mean(package), 2), "LPA")
print("Highest Package:", np.max(package), "LPA")
print("Lowest Package:", np.min(package), "LPA")

# --------------------------------------------------
# 3. PANDAS PLACEMENT ANALYSIS
# --------------------------------------------------
print("\nPANDAS ANALYSIS")
print("-" * 70)

placed = placements[
    placements["Status"] == "Placed"
]

not_placed = placements[
    placements["Status"] == "Not Placed"
]

print("\nPlaced Students:")
print(
    placed[
        ["Student_Name", "Company", "Package_LPA"]
    ].to_string(index=False)
)

print("\nNot Placed Students:")
print(
    not_placed[
        ["Student_Name", "Branch", "CGPA"]
    ].to_string(index=False)
)

# --------------------------------------------------
# 4. BRANCH-WISE PLACEMENT ANALYSIS
# --------------------------------------------------
branch_summary = placements.groupby("Branch").agg(
    Students=("Student_ID", "count"),
    Average_CGPA=("CGPA", "mean"),
    Average_Package=("Package_LPA", "mean")
)

print("\nBRANCH-WISE PLACEMENT ANALYSIS")
print("-" * 70)
print(branch_summary.round(2).to_string())

# --------------------------------------------------
# 5. COMPANY-WISE ANALYSIS
# --------------------------------------------------
company_summary = placements.groupby("Company").agg(
    Students=("Student_ID", "count"),
    Average_Package=("Package_LPA", "mean")
)

print("\nCOMPANY-WISE PLACEMENT ANALYSIS")
print("-" * 70)
print(company_summary.round(2).to_string())

# --------------------------------------------------
# 6. PLACEMENT PERCENTAGE
# --------------------------------------------------
placement_percentage = (
    len(placed) / len(placements)
) * 100

print("\nPLACEMENT RATE")
print("-" * 70)
print("Placed Students:", len(placed))
print("Not Placed Students:", len(not_placed))
print("Placement Percentage:",
      round(placement_percentage, 2), "%")

# --------------------------------------------------
# 7. SCIPY T-TEST
# --------------------------------------------------
print("\nSCIPY STATISTICAL ANALYSIS")
print("-" * 70)

# Test whether average CGPA is significantly different from 8
t_statistic, p_value = stats.ttest_1samp(
    cgpa,
    8
)

print("T-Statistic:", round(t_statistic, 4))
print("P-Value:", round(p_value, 4))

if p_value < 0.05:
    print("Result: Average CGPA is significantly different from 8.")
else:
    print("Result: No significant difference from 8.")

# --------------------------------------------------
# 8. SCIPY CORRELATION
# --------------------------------------------------
correlation, correlation_p = stats.pearsonr(
    cgpa,
    package
)

print("\nCorrelation between CGPA and Package:")
print("Correlation:", round(correlation, 4))
print("P-Value:", round(correlation_p, 4))

# --------------------------------------------------
# 9. MATPLOTLIB BAR GRAPH
# --------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(
    placements["Student_Name"],
    placements["Package_LPA"]
)

plt.title("Student Placement Package")
plt.xlabel("Students")
plt.ylabel("Package (LPA)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 10. MATPLOTLIB LINE GRAPH
# --------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(
    placements["Student_Name"],
    placements["CGPA"],
    marker="o"
)

plt.title("Student CGPA")
plt.xlabel("Students")
plt.ylabel("CGPA")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 11. BOKEH INTERACTIVE GRAPH
# --------------------------------------------------
source = ColumnDataSource(placements)

bokeh_plot = figure(
    x_range=placements["Student_Name"].tolist(),
    title="Placement Package - Interactive Bokeh Graph",
    x_axis_label="Students",
    y_axis_label="Package (LPA)",
    width=900,
    height=500
)

bokeh_plot.vbar(
    x="Student_Name",
    top="Package_LPA",
    width=0.6,
    source=source
)

bokeh_plot.xaxis.major_label_orientation = 0.8
show(bokeh_plot)

# --------------------------------------------------
# 12. FINAL SUMMARY
# --------------------------------------------------
print("\n" + "=" * 70)
print(" PLACEMENT SUMMARY")
print("=" * 70)

print("Total Students:", len(placements))
print("Placed Students:", len(placed))
print("Not Placed Students:", len(not_placed))
print("Placement Percentage:",
      round(placement_percentage, 2), "%")
print("Average CGPA:",
      round(np.mean(cgpa), 2))
print("Average Package:",
      round(np.mean(package), 2), "LPA")
print("Highest Package:",
      np.max(package), "LPA")

print("Student with Highest Package:",
      placements.loc[
          placements["Package_LPA"].idxmax(),
          "Student_Name"
      ])

print("Company Offering Highest Package:",
      placements.loc[
          placements["Package_LPA"].idxmax(),
          "Company"
      ])

print("\nPlacement Management System Completed Successfully!")
print("=" * 70)
