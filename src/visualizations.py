import matplotlib.pyplot as plt


def plot_top_countries(country_summary, top_n=10):
    """
    Create a bar chart showing the top countries by shipment count.

    Parameters:
        country_summary (DataFrame): Country summary DataFrame.
        top_n (int): Number of top countries to display.

    Returns:
        matplotlib.figure.Figure: Bar chart figure object.
    """

    top_data = country_summary.head(top_n)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(top_data["Country"], top_data["shipment_count"])

    ax.set_title("Top Countries by Shipment Count")
    ax.set_xlabel("Country")
    ax.set_ylabel("Shipment Count")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    return fig


def plot_shipment_mode_distribution(df):
    """
    Create a bar chart showing shipment mode distribution.

    Parameters:
        df (DataFrame): Cleaned shipment dataset.

    Returns:
        matplotlib.figure.Figure: Bar chart figure object.
    """

    shipment_mode_counts = df["Shipment Mode"].value_counts().reset_index()
    shipment_mode_counts.columns = ["Shipment Mode", "shipment_count"]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(
        shipment_mode_counts["Shipment Mode"],
        shipment_mode_counts["shipment_count"]
    )

    ax.set_title("Shipment Mode Distribution")
    ax.set_xlabel("Shipment Mode")
    ax.set_ylabel("Shipment Count")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    return fig