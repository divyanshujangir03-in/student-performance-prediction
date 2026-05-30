import pandas as pd

df = pd.read_csv("dataset/student-mat.csv", sep=';')

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x="studytime", y="G3", data=df)

plt.title("Study Time vs Final Grade")
plt.show()

numeric_df = df.select_dtypes(include=['int64'])

print(numeric_df.corr()["G3"].sort_values(ascending=False))


features = ["G1", "G2", "failures", "studytime", "Medu", "Fedu"]

X = df[features]
y = df["G3"]

print("X Shape:", X.shape)
print("y Shape:", y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Trained Successfully")

from sklearn.metrics import r2_score, mean_absolute_error

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

comparison = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred.round(2)
})

print(comparison.head(10))

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("Random Forest R2:",
      r2_score(y_test, rf_pred))

print("Random Forest MAE:",
      mean_absolute_error(y_test, rf_pred))

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.show()

import pickle

with open("models/model.pkl", "wb") as file:
    pickle.dump(rf, file)

print("Model Saved Successfully")