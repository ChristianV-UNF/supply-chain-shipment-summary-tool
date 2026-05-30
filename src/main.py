import os
import pandas as pd

from load_data import load_dataset
from cleaning import clean_shipment_data
from summaries import (
    generate_shipment_summary,
    summarize_by_country,
    summarize_by_vendor,
    top_countries_by_value,
    get_product_group_summary,
    get_shipment_mode_summary
)
from visualizations import (
    plot_top_countries,
    plot_shipment_mode_distribution
)

pd.set_option("display.float_format", "{:,.2f}".format)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "supply_delivery_history.csv")

    df = load_dataset(file_path)

    if df is None:
        print("\nNo data available to display. Check whether the dataset path is correct and whether the file contains data.")
        return

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

    # US-05: Country and Vendor Summaries
    country_summary = summarize_by_country(cleaned_df)
    vendor_summary = summarize_by_vendor(cleaned_df)
    top_countries = top_countries_by_value(cleaned_df)

    print("\nCountry Shipment Summary")
    print(country_summary.head(10))

    print("\nVendor Shipment Summary")
    print(vendor_summary.head(10))

    print("\nTop Countries by Item Value")
    print(top_countries)

    # US-06: Product Group and Shipment Mode Summaries
    product_group_summary = get_product_group_summary(cleaned_df)
    shipment_mode_summary = get_shipment_mode_summary(cleaned_df)

    print("\nProduct Group Summary:")
    print(product_group_summary.head(10))

    print("\nShipment Mode Summary:")
    print(shipment_mode_summary.head(10))

    # US-07: Visualization Functions
    country_chart = plot_top_countries(country_summary)
    shipment_mode_chart = plot_shipment_mode_distribution(cleaned_df)

    output_dir = os.path.join(script_dir, "..", "outputs")
    os.makedirs(output_dir, exist_ok=True)

    country_chart_path = os.path.join(output_dir, "top_countries_chart.png")
    shipment_mode_chart_path = os.path.join(output_dir, "shipment_mode_chart.png")

    country_chart.savefig(country_chart_path)
    shipment_mode_chart.savefig(shipment_mode_chart_path)

    print("\nVisualization functions executed successfully.")
    print(f"Top countries chart saved to: {country_chart_path}")
    print(f"Shipment mode chart saved to: {shipment_mode_chart_path}")


if __name__ == "__main__":
    main()