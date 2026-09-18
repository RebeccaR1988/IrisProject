def calculate_summary_statistics(
    df: pd.DataFrame | None = None,
) -> dict[str, pd.Series | pd.DataFrame]:
    """Loads Iris dataset (if none provided), calculates means, standard deviations,

    and correlation matrix for numeric columns, prints and returns them.
    """
    # 1. Load default dataset if none provided
    if df is None:
        df = sns.load_dataset("iris")

    # 2. Select numeric columns (handles any non-numeric columns automatically)
    numeric_df = df.select_dtypes(include="number")

    # 3. Compute statistics
    means = numeric_df.mean()
    std_devs = numeric_df.std()
    correlation_matrix = numeric_df.corr()

    # 4. Display Results
    print("=== MEANS ===")
    print(means.round(3))
    print("\n=== STANDARD DEVIATIONS ===")
    print(std_devs.round(3))
    print("\n=== CORRELATION MATRIX ===")
    print(correlation_matrix.round(3))

    # 5. Return results in a structured dictionary
    return {
        "means": means,
        "std_devs": std_devs,
        "correlation_matrix": correlation_matrix,
    }
