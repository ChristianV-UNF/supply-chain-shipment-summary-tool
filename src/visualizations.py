import matplotlib.pyplot as plt
import pandas as pd
def plot_top_countries(df, top_n=10):
    """
    Create a bar chart of the top countries by shipment count.

    Parameters:
        df (pd.DataFrame): Shipment dataset
        top_n (int): Number of top countries to display

    Returns:
        matplotlib.figure.Figure
    """

    country_counts = df["Country"].value_counts().head(top_n)

    fig, ax = plt.subplots(figsize=(10, 6))
    country_counts.plot(kind="bar", ax=ax)

    ax.set_title("Top Countries by Shipment Count")
    ax.set_xlabel("Country")
    ax.set_ylabel("Number of Shipments")

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig
def plot_shipment_mode_distribution(df):
    """
    Create a bar chart showing shipment mode distribution.

    Parameters:
        df (pd.DataFrame): Shipment dataset

    Returns:
        matplotlib.figure.Figure
    """

    shipment_mode_counts = df["Shipment Mode"].fillna("Unknown").value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))
    shipment_mode_counts.plot(kind="bar", ax=ax)

    ax.set_title("Shipment Mode Distribution")
    ax.set_xlabel("Shipment Mode")
    ax.set_ylabel("Number of Shipments")

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig