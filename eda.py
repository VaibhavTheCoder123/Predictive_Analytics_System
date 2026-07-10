import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("images", exist_ok=True)

df = pd.read_csv("cleaned_data/cleaned_dataset.csv")

sns.set_style("whitegrid")

plots = [
    ("gender", "Gender"),
    ("Partner", "Partner"),
    ("Dependents", "Dependents"),
    ("PhoneService", "Phone Service"),
    ("MultipleLines", "Multiple Lines"),
    ("InternetService", "Internet Service"),
    ("OnlineSecurity", "Online Security"),
    ("OnlineBackup", "Online Backup"),
    ("DeviceProtection", "Device Protection"),
    ("TechSupport", "Tech Support"),
    ("StreamingTV", "Streaming TV"),
    ("StreamingMovies", "Streaming Movies"),
    ("Contract", "Contract Type"),
    ("PaperlessBilling", "Paperless Billing"),
    ("PaymentMethod", "Payment Method")
]

for col, title in plots:
    plt.figure(figsize=(7,4))
    sns.countplot(data=df, x=col, hue="Churn")
    plt.xticks(rotation=20)
    plt.title(f"{title} vs Churn")
    plt.tight_layout()
    plt.savefig(f"images/{col}_vs_churn.png")
    plt.close()

numeric = ["tenure", "MonthlyCharges", "TotalCharges"]

for col in numeric:
    plt.figure(figsize=(7,4))
    sns.boxplot(data=df, x="Churn", y=col)
    plt.tight_layout()
    plt.savefig(f"images/{col}_boxplot.png")
    plt.close()

plt.figure(figsize=(8,5))
corr = df.copy()

corr["Churn"] = corr["Churn"].map({"No":0,"Yes":1})

corr["gender"] = corr["gender"].map({"Female":0,"Male":1})

sns.heatmap(corr[["tenure","MonthlyCharges","TotalCharges","SeniorCitizen","Churn"]].corr(),
            annot=True,
            cmap="coolwarm")

plt.tight_layout()
plt.savefig("images/correlation_heatmap.png")
plt.close()

print("EDA Completed")


# just upgrading the code to include more visualizations and save them as images for better analysis.


# import pandas as pd
# import matplotlib.pyplot as plt
# import os

# df = pd.read_csv("cleaned_data/cleaned_dataset.csv")

# os.makedirs("images", exist_ok=True)


# def save_plot(filename):
#     plt.tight_layout()
#     plt.savefig(f"images/{filename}")
#     plt.close()

# plt.figure(figsize=(6,4))
# df["Churn"].value_counts().plot(kind="bar")
# plt.title("Customer Churn Distribution")
# plt.xlabel("Churn")
# plt.ylabel("Customers")
# save_plot("01_churn_distribution.png")


# plt.figure(figsize=(6,4))
# df["gender"].value_counts().plot(kind="bar")
# plt.title("Gender Distribution")
# save_plot("02_gender_distribution.png")


# plt.figure(figsize=(7,4))
# df["Contract"].value_counts().plot(kind="bar")
# plt.title("Contract Type")
# save_plot("03_contract_type.png")


# plt.figure(figsize=(7,4))
# df["InternetService"].value_counts().plot(kind="bar")
# plt.title("Internet Service")
# save_plot("04_internet_service.png")



# plt.figure(figsize=(10,5))
# df["PaymentMethod"].value_counts().plot(kind="bar")
# plt.title("Payment Method")
# save_plot("05_payment_method.png")


# plt.figure(figsize=(8,4))
# plt.hist(df["tenure"], bins=20)
# plt.title("Tenure Distribution")
# plt.xlabel("Months")
# plt.ylabel("Customers")
# save_plot("06_tenure_distribution.png")


# plt.figure(figsize=(8,4))
# plt.hist(df["MonthlyCharges"], bins=20)
# plt.title("Monthly Charges")
# save_plot("07_monthly_charges.png")


# plt.figure(figsize=(8,4))
# plt.hist(df["TotalCharges"], bins=20)
# plt.title("Total Charges")
# save_plot("08_total_charges.png")


# plt.figure(figsize=(5,4))
# df["SeniorCitizen"].value_counts().plot(kind="bar")
# plt.title("Senior Citizen")
# save_plot("09_senior_citizen.png")


# plt.figure(figsize=(5,4))
# df["Dependents"].value_counts().plot(kind="bar")
# plt.title("Dependents")
# save_plot("10_dependents.png")

# print("EDA Completed Successfully")