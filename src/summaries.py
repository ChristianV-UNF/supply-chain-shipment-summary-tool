import pandas as pd

def generate_shipment_summary(df: pd.DataFrame) -> dict:
    """
    Generate shipment summary metrics.

    Args:
        df (pd.DataFrame): Cleaned shipment dataset.

    Returns:
        dict: Shipment summary metrics.
    """

    required_columns = [
    "Line Item Quantity",
    "Line Item Value",
    "Freight Cost (USD)",
    "Line Item Insurance (USD)"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    summary = {
        "total_shipments": len(df),
        "total_quantity": df["Line Item Quantity"].sum(),
        "total_item_value": df["Line Item Value"].sum(),
        "total_freight_cost": df["Freight Cost (USD)"].sum(),
        "total_insurance_cost": df["Line Item Insurance (USD)"].sum(),
        "average_item_value": df["Line Item Value"].mean()
    }

    return summary


def summarize_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate shipment summaries grouped by destination country.
    """

    country_summary = (
        df.groupby("Country")
        .agg(
            shipment_count=("Country", "count"),
            total_item_value=("Line Item Value", "sum")
        )
        .reset_index()
        .sort_values(by="shipment_count", ascending=False)
    )

    return country_summary


def summarize_by_vendor(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate shipment summaries grouped by vendor.
    """

    vendor_summary = (
        df.groupby("Vendor")
        .agg(
            shipment_count=("Vendor", "count"),
            total_item_value=("Line Item Value", "sum")
        )
        .reset_index()
        .sort_values(by="shipment_count", ascending=False)
    )

    return vendor_summary


def top_countries_by_value(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Return the top countries ranked by total shipment value.
    """

    top_countries = (
        df.groupby("Country")
        .agg(total_item_value=("Line Item Value", "sum"))
        .reset_index()
        .sort_values(by="total_item_value", ascending=False)
        .head(top_n)
    )

    return top_countries