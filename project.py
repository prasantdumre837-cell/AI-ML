import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Create the DataFrame
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 23, 28, 33, 38, 42, 48, 52, 27, 31, 36, 41, 46, 55],
    "Income": [25000, 30000, 35000, 45000, 50000, 60000, 70000, 28000, 32000, 40000, 48000, 55000, 65000, 75000, 33000, 38000, 47000, 58000, 68000, 80000],
    "SpendingScore": [75, 80, 65, 60, 55, 50, 40, 85, 70, 65, 55, 50, 45, 35, 75, 70, 60, 50, 45, 30],
    "Purchased": [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

# 2. Explore dataset
print("--- First 5 Rows ---")
print(df.head())
print("\n--- Shape ---")
print(df.shape)
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 3. Visualize Income vs Spending Score
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(
    data=df, 
    x="Income", 
    y="SpendingScore", 
    hue="Purchased", 
    style="Purchased", 
    palette={0: "red", 1: "green"}, 
    s=100
)
plt.title("Income vs Spending Score")
plt.xlabel("Income ($)")
plt.ylabel("Spending Score (1-100)")

# 4. Select Features
X = df[["Age", "Income", "SpendingScore"]]

# 5. Select Target
y = df["Purchased"]

# 6. Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Train Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 8. Make Predictions
y_pred = model.predict(X_test)

# 9. Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# 10. Visualize Actual vs Predicted Values
plt.subplot(1, 2, 2)
results_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred}).reset_index(drop=True)
sns.scatterplot(data=results_df, x=results_df.index, y="Actual", color="blue", label="Actual", s=120, marker="o")
sns.scatterplot(data=results_df, x=results_df.index, y="Predicted", color="orange", label="Predicted", s=60, marker="X")
plt.title("Actual vs Predicted Values")
plt.xlabel("Test Sample Index")
plt.ylabel("Purchased (0 or 1)")
plt.legend()

plt.tight_layout()
plot_path = "model_results.png"
plt.savefig(plot_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"\nVisualization saved to: {plot_path}")

# 11. Predict for a New Customer (e.g., Age=30, Income=40000, SpendingScore=70)
new_customer = pd.DataFrame([[30, 40000, 70]], columns=["Age", "Income", "SpendingScore"])
new_prediction = model.predict(new_customer)
prediction_label = "Will Purchase (1)" if new_prediction[0] == 1 else "Will Not Purchase (0)"

print(f"\nNew Customer Prediction (Age=30, Income=$40k, Score=70): {prediction_label}")
