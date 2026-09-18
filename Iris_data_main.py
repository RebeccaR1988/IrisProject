import os
import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """Loads a CSV dataset from a specified path into a pandas DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at path: {file_path}")

    df = pd.read_csv(file_path)
    print(f"Successfully loaded '{file_path}' with {len(df)} records.")
    return df


def check_dimensions(df: pd.DataFrame) -> tuple[int, int]:
    """Displays and returns the row and column counts of the dataset."""
    rows, columns = df.shape
    print(f"Dataset Dimensions: {rows} rows, {columns} columns")
    return rows, columns


def inspect_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates missing counts and percentages per column, returning a summary DataFrame."""
    missing_count = df.isna().sum()
    missing_pct = (missing_count / len(df)) * 100

    summary = pd.DataFrame(
        {
            "Missing Values": missing_count,
            "Percentage (%)": missing_pct.round(2),
        }
    )

    columns_with_nulls = summary[summary["Missing Values"] > 0]

    if columns_with_nulls.empty:
        print("Data Quality: No missing values detected across any column.")
    else:
        print(f"Warning: {len(columns_with_nulls)} column(s) contain missing values:")
        print(columns_with_nulls)

    return summary