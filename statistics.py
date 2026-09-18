import pandas as pd
import seaborn as sns

# 1. Load the Iris dataset
df = sns.load_dataset("iris")

# 2. Extract numeric columns (excluding the categorical 'species' column)
numeric_df = df.drop(columns=["species"])

# 3. Calculate Summary Statistics
means = numeric_df.mean()
std_devs = numeric_df.std()
correlation_matrix = numeric_df.corr()

# 4. Display Results
print("=== MEANS ===")
print(means)
print("\n=== STANDARD DEVIATIONS ===")
print(std_devs)
print("\n=== CORRELATION MATRIX ===")
print(correlation_matrix)