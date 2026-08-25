import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)
n_rows = 1000

# Generate dirty department entries
departments = np.random.choice(
    ['Sales', 'sales', 'MARKETING', 'Marketing', ' IT ', 'IT', 'HR', np.nan],
    size=n_rows,
    p=[0.2, 0.1, 0.15, 0.15, 0.1, 0.15, 0.1, 0.05]
)

# Create initial raw data dictionary
data = {
    'Employee_ID': [f'EMP_{i:04d}' for i in range(1, n_rows + 1)],
    'Age': np.random.choice([22, 28, 35, 42, 50, -5, 150, np.nan], size=n_rows, p=[0.2, 0.25, 0.2, 0.15, 0.1, 0.04, 0.03, 0.03]),
    'Department': departments,
    'Salary': np.random.choice([45000, 60000, 75000, 90000, 120000, 500000, np.nan], size=n_rows, p=[0.2, 0.25, 0.2, 0.15, 0.1, 0.02, 0.08]),
    'Join_Date': np.random.choice(['2020-01-15', '2021/05/20', '12-10-2019', '2022-08-01', 'InvalidDate', np.nan], size=n_rows, p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.05]),
    'Performance_Score': np.random.choice([1.0, 2.0, 3.0, 4.0, 5.0, np.nan], size=n_rows, p=[0.1, 0.2, 0.4, 0.2, 0.05, 0.05]),
    'Remote_Ratio': np.random.choice(['0%', '50%', '100%', '50', np.nan], size=n_rows, p=[0.3, 0.3, 0.3, 0.05, 0.05])
}

df_dirty = pd.DataFrame(data)
print("Dirty Dataset Created Successfully!")
print(df_dirty.head(10))

df_clean= df_dirty.copy()

df_clean = df_dirty.copy()
# task 1
df_clean['Department'] = df_clean['Department'].astype(str).str.strip().str.title()
df_clean['Department'] = df_clean['Department'].replace('Nan', 'Unknown')

print(df_clean)

# task2
df_clean.loc[(df_clean['Age'] < 18) | (df_clean['Age'] > 70), 'Age'] = np.nan
df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median()).astype(int)
print(df_clean)

# Task 3
df_clean['Join_Date'] = pd.to_datetime(
    df_clean['Join_Date'], errors='coerce', format='mixed'
)
date_mode = df_clean['Join_Date'].mode().iloc[0]
df_clean['Join_Date'] = df_clean['Join_Date'].fillna(date_mode)
print(df_clean)

# Task 4
df_clean['Remote_Ratio'] = df_clean['Remote_Ratio'].astype(str).str.replace('%', '').str.strip()
df_clean['Remote_Ratio'] = pd.to_numeric(df_clean['Remote_Ratio'], errors='coerce')
df_clean['Remote_Ratio'] = df_clean['Remote_Ratio'].fillna(df_clean['Remote_Ratio'].median())
print(df_clean)

# Task 5
df_clean.loc[df_clean['Salary'] > 200000, 'Salary'] = np.nan
df_clean['Salary'] = df_clean.groupby('Department')['Salary'].transform(lambda x: x.fillna(x.median()))

df_clean.info()
print(df_clean)

# # Exercise 1
# avg_salary = df_clean.groupby('Department')['Salary'].mean().sort_values()
# plt.figure(figsize=(8, 4))
# plt.barh(avg_salary.index, avg_salary.values, color='skyblue', edgecolor='black')
# plt.title('Average Salary by Department')
# plt.xlabel('Salary ($)')
# plt.ylabel('Department')
# plt.grid(axis='x', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()


# avg_salary = df_clean.groupby('Department')['Salary'].mean().sort_values()
# plt.figure(figsize=(8, 4))
# plt.barh(avg_salary.index, avg_salary.values, color='skyblue', edgecolor='black')
# plt.title('Average Salary by Department')
# plt.xlabel('Salary ($)')
# plt.ylabel('Department')
# plt.grid(axis='x', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# avg_salary = df_clean.groupby('Age')['Salary'].mean().sort_values()
# plt.figure(figsize=(8, 4))
# plt.barh(avg_salary.index, avg_salary.values, color='skyblue', edgecolor='black')
# plt.title('Average Salary by Age')
# plt.xlabel('Salary ($)')
# plt.ylabel('Age')
# plt.grid(axis='x', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# # Exercise 2
# plt.figure(figsize=(8, 4))
# plt.hist(df_clean['Salary'], bins=15, color='teal', edgecolor='black', alpha=0.7)
# plt.axvline(df_clean['Salary'].mean(), color='red', linestyle='dashed', linewidth=1.5, label=f'Mean Salary ({df_clean["Salary"].mean():.1f})')
# plt.title('Distribution of Employee Salary')
# plt.xlabel('Salary')
# plt.ylabel('Frequency')
# plt.legend()
# plt.tight_layout()
# plt.show()

# Exercise 3 scatter plot.
# plt.figure(figsize=(8, 5))
# scatter = plt.scatter(df_clean['Age'], df_clean['Salary'], c=df_clean['Performance_Score'], cmap='viridis', alpha=0.6, edgecolors='w')
# plt.colorbar(scatter, label='Performance Score')
# plt.title('Employee Age vs. Salary')
# plt.xlabel('Age')
# plt.ylabel('Salary ($)')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()


# Exercise 4
# Exercise 4
df_clean['Join_Year'] = df_clean['Join_Date'].dt.year
yearly_joins = df_clean.groupby('Join_Year').size().sort_index()

plt.figure(figsize=(8, 4))
plt.plot(yearly_joins.index, yearly_joins.values, marker='o', color='darkorange', linewidth=2)
plt.title('New Hires Count by Year')
plt.xlabel('Year')
plt.ylabel('Number of Hires')
plt.xticks(yearly_joins.index)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
