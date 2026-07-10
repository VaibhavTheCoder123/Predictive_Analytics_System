import pandas as pd
import os

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("="*60)
print("Original Dataset")
print("="*60)

print(f"Shape : {df.shape}")
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ----------------------------
# Check Blank Values
# ----------------------------

print("\nBlank values in TotalCharges:")

blank_values = (df["TotalCharges"] == " ").sum()
print(blank_values)

# ----------------------------
# Convert TotalCharges to Numeric
# ----------------------------

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# ----------------------------
# Missing Values Again
# ----------------------------

print("\nMissing Values After Conversion:")

print(df.isnull().sum())

# ----------------------------
# Fill Missing Values
# ----------------------------

median_value = df["TotalCharges"].median()

df["TotalCharges"] = df["TotalCharges"].fillna(median_value)

# ----------------------------
# Remove Duplicates
# ----------------------------

df = df.drop_duplicates()

# ----------------------------
# Verify
# ----------------------------

print("\nAfter Cleaning")

print("Shape:", df.shape)

print("\nMissing Values:")

print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ----------------------------
# Create Folder
# ----------------------------

os.makedirs("cleaned_data", exist_ok=True)

# ----------------------------
# Save Cleaned Dataset
# ----------------------------

df.to_csv("cleaned_data/cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")

# below code was used to check the dataset before cleaning, but it is commented out now. so no need to run it again.

# import pandas as pd

# # Load dataset
# df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# print("=" * 50)
# print("Dataset Loaded Successfully")
# print("=" * 50)

# print("\nFirst 5 Rows:")
# print(df.head())

# print("\nDataset Shape:")
# print(df.shape)

# print("\nColumn Names:")
# print(df.columns.tolist())

# print("\nDataset Information:")
# print(df.info())

# print("\nMissing Values:")
# print(df.isnull().sum())

# print("\nDuplicate Rows:")
# print(df.duplicated().sum())