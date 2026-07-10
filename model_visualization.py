# this was create because i want to try some new things in the model.py file and i want to keep the original file as it is. so i created this file to try some new things.
# now I will try to visualize the model performance and save the images in a folder called model_images. I will also save the best model in a folder called models.
# this code is clashing with the original model.py file, so im going to comment out the code in the original model.py file and run this file instead. after running this file, i will uncomment the code in the original model.py file and delete this file.


# so dont consider this for final submission. this is just for testing purpose.


# import os
# import joblib
# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier

# from sklearn.metrics import (
#     accuracy_score,
#     ConfusionMatrixDisplay,
#     RocCurveDisplay,
#     PrecisionRecallDisplay
# )

# os.makedirs("model_images", exist_ok=True)

# df = pd.read_csv("cleaned_data/cleaned_dataset.csv")

# df.drop("customerID", axis=1, inplace=True)

# df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# X = df.drop("Churn", axis=1)
# X = pd.get_dummies(X, drop_first=True)

# y = df["Churn"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.20,
#     random_state=42,
#     stratify=y
# )

# scaler = StandardScaler()

# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# models = {
#     "Logistic Regression": LogisticRegression(max_iter=3000),
#     "Decision Tree": DecisionTreeClassifier(random_state=42),
#     "Random Forest": RandomForestClassifier(
#         n_estimators=200,
#         random_state=42
#     )
# }

# accuracy = {}

# best_model = None
# best_name = ""

# for name, model in models.items():

#     if name == "Logistic Regression":
#         model.fit(X_train_scaled, y_train)
#         pred = model.predict(X_test_scaled)

#     else:
#         model.fit(X_train, y_train)
#         pred = model.predict(X_test)

#     acc = accuracy_score(y_test, pred)

#     accuracy[name] = acc

#     if acc > max(accuracy.values()):
#         best_model = model
#         best_name = name

# plt.figure(figsize=(7,5))

# plt.bar(accuracy.keys(), accuracy.values())

# plt.title("Model Accuracy Comparison")

# plt.ylabel("Accuracy")

# for i, v in enumerate(accuracy.values()):
#     plt.text(i, v + 0.003, f"{v:.3f}", ha="center")

# plt.tight_layout()

# plt.savefig("model_images/model_accuracy.png")

# plt.close()

# if best_name == "Logistic Regression":

#     ConfusionMatrixDisplay.from_estimator(
#         best_model,
#         X_test_scaled,
#         y_test
#     )

# else:

#     ConfusionMatrixDisplay.from_estimator(
#         best_model,
#         X_test,
#         y_test
#     )

# plt.title("Confusion Matrix")

# plt.tight_layout()

# plt.savefig("model_images/confusion_matrix.png")

# plt.close()

# rf = RandomForestClassifier(
#     n_estimators=200,
#     random_state=42
# )

# rf.fit(X_train, y_train)

# importance = pd.Series(
#     rf.feature_importances_,
#     index=X.columns
# )

# importance = importance.sort_values(ascending=False).head(10)

# plt.figure(figsize=(8,6))

# importance.sort_values().plot(kind="barh")

# plt.title("Top 10 Feature Importance")

# plt.tight_layout()

# plt.savefig("model_images/feature_importance.png")

# plt.close()

# if best_name == "Logistic Regression":

#     RocCurveDisplay.from_estimator(
#         best_model,
#         X_test_scaled,
#         y_test
#     )

# else:

#     RocCurveDisplay.from_estimator(
#         best_model,
#         X_test,
#         y_test
#     )

# plt.tight_layout()

# plt.savefig("model_images/roc_curve.png")

# plt.close()

# if best_name == "Logistic Regression":

#     PrecisionRecallDisplay.from_estimator(
#         best_model,
#         X_test_scaled,
#         y_test
#     )

# else:

#     PrecisionRecallDisplay.from_estimator(
#         best_model,
#         X_test,
#         y_test
#     )

# plt.tight_layout()

# plt.savefig("model_images/precision_recall_curve.png")

# plt.close()

# joblib.dump(best_model, "models/final_model.pkl")

# print("\nVisualization files created successfully.")
# print("\nSaved in model_images/")