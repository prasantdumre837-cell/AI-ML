import pandas as pd

data={"Name":["Hari","sita","gita","Ram","shyam","jack","john","kyle","wood","prashant"],
       "Age":[24,25,26,27,34,32,12,14,56,89],
       "Marks": [None, 85, 67, 92, 74, 81, 69, 15, 34, 95],
       "Address":["Butwal", "Kathmandu", "Pokhara", "Chitwan", "Syangja", "Butwal", "Lalitpur", "Bhaktapur", "Pokhara", "Kathmandu"]}
       
df=pd.DataFrame(data);
print(df)

print(df[["Name", "Age"]])
print("mean",df["Marks"].mean())
df["Result"]=df["Marks"]>=40
print(df)
df["Percentage"]=df["Marks"]/100*100
print(df)
print(df.describe())
print(df.isna().sum().sum())

mean_age=df["Age"].mean()
df["Age"].fillna(mean_age, inplace=True)
print(df)
print(df.duplicated())
