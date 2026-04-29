import pandas as pd

# Load the dataset
df = pd.read_csv("patients.csv")

# Clean the dataset
df["name"] = df["name"].str.strip().str.title()
df["email"] = df["email"].str.strip().str.lower()
df["condition"] = df["condition"].str.strip().str.title()
df["gender"] = df["gender"].str.strip().str.title()

print("Cleaned Patient Data:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nNumber of columns:", len(df.columns))


# Basic analysis
total_patients = len(df)
average_age = df["age"].mean()
condition_counts = df["condition"].value_counts()

print("\nEMR Analysis Summary:")
print("Total Patients:", total_patients)
print("Average Age:", round(average_age, 2))

print("\nCondition Counts:")
print(condition_counts)


# Risk classification function
def classify_risk(row):
    if row["age"] > 50 or row["blood_pressure"] > 140 or row["glucose_level"] > 180:
        return "High Risk"
    elif row["age"] >= 30:
        return "Medium Risk"
    else:
        return "Low Risk"

# Apply risk classification
df["risk_level"] = df.apply(classify_risk, axis=1)

print("\nPatient Risk Levels:")
print(df[["name", "age", "blood_pressure", "glucose_level", "risk_level"]])


import matplotlib.pyplot as plt

# 1. Condition Distribution
plt.figure()
df["condition"].value_counts().plot(kind="bar")
plt.title("Condition Distribution")
plt.xlabel("Condition")
plt.ylabel("Number of Patients")
plt.savefig("condition_distribution.png")

# 2. Risk Level Distribution
plt.figure()
df["risk_level"].value_counts().plot(kind="bar")
plt.title("Risk Level Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Number of Patients")
plt.savefig("risk_distribution.png")

# 3. Age Distribution
plt.figure()
df["age"].plot(kind="hist", bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.savefig("age_distribution.png")

print("\nCharts saved successfully.")


# Save analysis to a text file
with open("analysis_report.txt", "w") as file:
    file.write("EMR ANALYSIS REPORT\n")
    file.write("====================\n\n")
    
    file.write(f"Total Patients: {total_patients}\n")
    file.write(f"Average Age: {round(average_age, 2)}\n\n")
    
    file.write("Condition Counts:\n")
    for condition, count in condition_counts.items():
        file.write(f"- {condition}: {count}\n")
    
    file.write("\nRisk Level Distribution:\n")
    risk_counts = df["risk_level"].value_counts()
    for risk, count in risk_counts.items():
        file.write(f"- {risk}: {count}\n")

print("\nReport saved as analysis_report.txt")