import pandas as pd

def generate_shipment_summary(df: pd.DataFrame) -> dict:
    """
    Generate shipment summary metrics.

    Args:
        df (pd.DataFrame): Cleaned shipment dataset.

    Returns:
        dict: Shipment summary metrics.
    """

    summary = {
        "total_shipments": len(df),
        "total_quantity": df["Line Item Quantity"].sum(),
        "total_item_value": df["Line Item Value"].sum(),
        "total_freight_cost": df["Freight Cost (USD)"].sum(),
        "total_insurance_cost": df["Line Item Insurance (USD)"].sum(),
        "average_item_value": df["Line Item Value"].mean()
    }

    return summary