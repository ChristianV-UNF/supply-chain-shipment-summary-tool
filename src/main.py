import os

from load_data import load_dataset
from visualizations import plot_top_countries, plot_shipment_mode_distribution


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "supply_delivery_history.csv")

    df = load_dataset(file_path)

    if df is not None:
        print("\nDataset Preview:")
        print(df.head())

        print("\nDataset Shape:")
        print(df.shape)
        fig1 = plot_top_countries(df)
        fig2 = plot_shipment_mode_distribution(df)

        print("\nVisualization functions executed successfully.")
    else:
        print("\nNo data available to display. Check whether the dataset path is correct and whether the file contains data.")


if __name__ == "__main__":
    main()