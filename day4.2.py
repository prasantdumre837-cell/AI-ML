import pandas as pd
from sklearn.cluster import KMeans
data = {
    "CustomerID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30
    ],

    "AnnualIncome": [
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
        45, 48, 50, 52, 55, 58, 60, 62, 65, 68,
        85, 88, 90, 92, 95, 98, 100, 105, 110, 115
    ],

    "SpendingScore": [
        39, 42, 38, 45, 40, 43, 37, 46, 41, 44,
        50, 55, 52, 58, 54, 60, 57, 62, 59, 65,
        75, 80, 78, 82, 77, 85, 81, 88, 84, 90
    ]
}

df = pd.DataFrame(data)

df.to_csv("mall_customers.csv", index=False)

print("Dataset created successfully!")
print(df.head())

#step1:Load the dataset
df=pd.read_csv("mall_customers.csv")

#step2:select the features to cluster on
X= df[["AnnualIncome", "SpendingScore"]]

#step3: Create and train the K-Means model(3 clusters)
model=KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)

#step4: Label each customer with their assigned cluster
df["Cluster"]=model.labels_

print(df.head())
print("Cluster centers:")
print(model.cluster_centers_)

import matplotlib.pyplot as plt
#step5:Visualize the customer segments
plt.scatter(df["AnnualIncome"],df["SpendingScore"], c=df["Cluster"], cmap="viridis")
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], c="red", marker="X", s=200)
plt.title("Customer Segments"); plt.xlabel("Annual Income"); plt.ylabel("Spending Score")
plt.show()

#step6 :Bonus-a simple classification demo(handwritten digits)
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

digits= load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)
clf=LogisticRegression(max_iter=2000)
clf.fit(X_train, y_train)
print("Demo classifier accuracy:", clf.score(X_test, y_test))

