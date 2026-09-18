import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_histograms(df: pd.DataFrame) -> None:
    """Plots a 2x2 grid of histograms for the four Iris features."""
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # Match column names regardless of dot notation (R) or snake_case (Python)
    cols = {
        "sepal_length": df.columns[0],
        "sepal_width": df.columns[1],
        "petal_length": df.columns[2],
        "petal_width": df.columns[3],
    }

    axes[0, 0].hist(df[cols["sepal_length"]], color="lightblue", edgecolor="black")
    axes[0, 0].set_title("Sepal Length")

    axes[0, 1].hist(df[cols["sepal_width"]], color="lightgreen", edgecolor="black")
    axes[0, 1].set_title("Sepal Width")

    axes[1, 0].hist(df[cols["petal_length"]], color="lightpink", edgecolor="black")
    axes[1, 0].set_title("Petal Length")

    axes[1, 1].hist(
        df[cols["petal_width"]], color="lightyellow", edgecolor="black"
    )
    axes[1, 1].set_title("Petal Width")

    plt.tight_layout()
    plt.show()


def plot_boxplots(df: pd.DataFrame) -> None:
    """Plots a boxplot of Sepal Length grouped by Species."""
    species_col = [c for c in df.columns if "spec" in c.lower()][0]
    sepal_len_col = df.columns[0]

    plt.figure(figsize=(7, 5))
    sns.boxplot(x=species_col, y=sepal_len_col, data=df, palette="Set2")
    plt.title("Sepal Length por especie")
    plt.xlabel("Species")
    plt.ylabel("Sepal Length")
    plt.show()


def plot_scatter(df: pd.DataFrame) -> None:
    """Plots a scatter plot of Petal Length vs Petal Width colored by Species."""
    species_col = [c for c in df.columns if "spec" in c.lower()][0]
    petal_len_col = df.columns[2]
    petal_wid_col = df.columns[3]

    plt.figure(figsize=(7, 5))
    sns.scatterplot(
        x=petal_len_col,
        y=petal_wid_col,
        hue=species_col,
        style=species_col,
        s=70,
        data=df,
    )
    plt.title("Petal Length vs Petal Width")
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")
    plt.show()


# Load Iris and run functions
iris = sns.load_dataset("iris")

plot_histograms(iris)
plot_boxplots(iris)
plot_scatter(iris)
