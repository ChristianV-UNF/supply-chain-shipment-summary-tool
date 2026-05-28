import os

from load_data import load_dataset
from cleaning import clean_shipment_data
from summaries import generate_shipment_summary

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "supply_delivery_history.csv")

    df = load_dataset(file_path)

    if df is not None:
        print("\nOriginal Dataset Shape:")
        print(df.shape)

        print("\nOriginal Column Types:")
        print(df.dtypes)

        print("\nOriginal Missing Values:")
        print(df.isnull().sum())

        print("\nCleaning dataset...")
        cleaned_df = clean_shipment_data(df)

        print("\nCleaned Dataset Preview:")
        print(cleaned_df.head())

        print("\nCleaned Dataset Shape:")
        print(cleaned_df.shape)

        print("\nCleaned Column Types:")
        print(cleaned_df.dtypes)

        print("\nCleaned Missing Values:")
        print(cleaned_df.isnull().sum())

        print("\nDuplicate Rows After Cleaning:")
        print(cleaned_df.duplicated().sum())

        shipment_summary = generate_shipment_summary(cleaned_df)
        print("\nShipment Summary Metrics")
        print(shipment_summary)


if __name__ == "__main__":
    main()
