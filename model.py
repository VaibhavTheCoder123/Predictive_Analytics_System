import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    PrecisionRecallDisplay
)

os.makedirs("models", exist_ok=True)
os.makedirs("model_images", exist_ok=True)

df = pd.read_csv("cleaned_data/cleaned_dataset.csv")

df.drop("customerID", axis=1, inplace=True)

df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

X = df.drop("Churn", axis=1)

X = pd.get_dummies(X, drop_first=True)

y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(max_iter=5000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
}

results = []

best_model = None
best_name = ""
best_accuracy = 0

for name, model in models.items():

    if name == "Logistic Regression":

        model.fit(X_train_scaled, y_train)

        prediction = model.predict(X_test_scaled)

    else:

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    results.append((name, accuracy))

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print(f"Accuracy : {accuracy:.4f}")

    print("\nClassification Report\n")

    print(classification_report(y_test, prediction))

    print("Confusion Matrix\n")

    print(confusion_matrix(y_test, prediction))

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model

        best_name = name

joblib.dump(best_model, "models/logistic_regression_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(X.columns.tolist(), "models/columns.pkl")

print("\nBest Model :", best_name)

print("Accuracy :", round(best_accuracy, 4))

names = [i[0] for i in results]

scores = [i[1] for i in results]

plt.figure(figsize=(7,5))

bars = plt.bar(names, scores)

plt.ylim(0.6,1)

plt.title("Model Accuracy Comparison")

plt.ylabel("Accuracy")

for bar in bars:

    yval = bar.get_height()

    plt.text(
        bar.get_x()+bar.get_width()/2,
        yval+0.01,
        round(yval,3),
        ha="center"
    )

plt.tight_layout()

plt.savefig("model_images/model_accuracy.png")

plt.close()

if best_name == "Logistic Regression":

    ConfusionMatrixDisplay.from_estimator(
        best_model,
        X_test_scaled,
        y_test
    )

else:

    ConfusionMatrixDisplay.from_estimator(
        best_model,
        X_test,
        y_test
    )

plt.title(f"Confusion Matrix ({best_name})")

plt.tight_layout()

plt.savefig("model_images/confusion_matrix.png")

plt.close()

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
)

importance = importance.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(8,6))

importance.sort_values().plot(kind="barh")

plt.title("Top 10 Important Features")

plt.tight_layout()

plt.savefig("model_images/feature_importance.png")

plt.close()

if best_name == "Logistic Regression":

    RocCurveDisplay.from_estimator(
        best_model,
        X_test_scaled,
        y_test
    )

else:

    RocCurveDisplay.from_estimator(
        best_model,
        X_test,
        y_test
    )

plt.title("ROC Curve")

plt.tight_layout()

plt.savefig("model_images/roc_curve.png")

plt.close()

if best_name == "Logistic Regression":

    PrecisionRecallDisplay.from_estimator(
        best_model,
        X_test_scaled,
        y_test
    )

else:

    PrecisionRecallDisplay.from_estimator(
        best_model,
        X_test,
        y_test
    )

plt.title("Precision Recall Curve")

plt.tight_layout()

plt.savefig("model_images/precision_recall_curve.png")

plt.close()

print("\nImages saved in model_images/")
print("Model saved in models/")
print("Scaler saved successfully.")
print("Training columns saved successfully.")