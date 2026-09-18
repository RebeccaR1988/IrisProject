import pandas as pd

# Download raw CSV directly from GitHub
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Save directly to Excel (.xlsx)
df.to_excel("iris.xlsx", index=False)
print("Saved iris.xlsx successfully!")
