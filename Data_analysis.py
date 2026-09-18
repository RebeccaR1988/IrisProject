import pandas as pd

from Iris_data_main import load_dataset as datacleaning
from Iris_data_main import check_dimensions as variablescheck
from Iris_data_main import inspect_missing_values as checknulls
from statistics import calculate_summary_statistics as stats
from visualization import plot_histograms as histogram
from visualization import plot_boxplots as boxplots

# Download raw CSV directly from GitHub
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Save directly to Excel (.xlsx)
df.to_excel("iris.xlsx", index=False)
print("Saved iris.xlsx successfully!")

datacleaning()
variablescheck()
checknulls()
stats()
histogram()
boxplots()
