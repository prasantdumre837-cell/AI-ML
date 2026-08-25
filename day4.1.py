import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "StudyHours": [
        2.5, 3.0, 4.5, 5.0, 6.0, 1.5, 2.0, 3.5, 4.0, 5.5,
        6.5, 7.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.5, 1.0, 2.0
    ],
    "Attendance": [
        75, 80, 85, 90, 88, 70, 72, 78, 82, 90,
        95, 92, 68, 76, 84, 86, 93, 96, 65, 70
    ],
    "Score": [
        45, 50, 65, 72, 75, 38, 42, 55, 60, 78,
        85, 88, 40, 48, 62, 70, 82, 92, 30, 40
    ]
}

df = pd.DataFrame(data)

df.to_csv("student_scores_clean.csv", index=False)

print(df.head()) 

#step1 
df=pd.read_csv("student_scores_clean.csv")
print(df.head())

# Step 2: Select the input features and target value.
X = df[["StudyHours", "Attendance"]]
y = df["Score"]

# Step 3: Split the data, then train the regression model.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Import the evaluation metrics.
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Step 5
predictions=model.predict(X_test)
print(predictions)

#step 6

mae= mean_absolute_error(y_test, predictions)
mse= mean_squared_error(y_test, predictions)
print("MAE:",mae)
print("MSE:",mse)

#step7
new_student = [(6,90)] #6 study hours, 90% attendance
predicted_score= model.predict(new_student)
print("Predicted Score:", predicted_score)
