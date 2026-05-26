import pandas as pd


def clean_numeric_column(df, column_name):
    """
    Convert a numeric column stored as text into a proper numeric format.
    """

    df[column_name] = (
        df[column_name]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(" ", "", regex=False)
    )

    df[column_name] = pd.to_numeric(df[column_name], errors="coerce")

    return df


def clean_date_column(df, column_name):
    """
    Convert a date column into datetime format.
    """

    df[column_name] = pd.to_datetime(df[column_name], errors="coerce")

    return df


def clean_shipment_data(df):
    """
    Clean the shipment dataset by converting date and numeric columns.
    """

    cleaned_df = df.copy()

    date_columns = [
        "Scheduled Delivery Date",
        "Delivered to Client Date",
        "Delivery Recorded Date"
    ]

    numeric_columns = [
        "Line Item Quantity",
        "Line Item Value",
        "Pack Price",
        "Unit Price",
        "Weight (Kilograms)",
        "Freight Cost (USD)",
        "Line Item Insurance (USD)"
    ]

    for column in date_columns:
        if column in cleaned_df.columns:
            cleaned_df = clean_date_column(cleaned_df, column)

    for column in numeric_columns:
        if column in cleaned_df.columns:
            cleaned_df = clean_numeric_column(cleaned_df, column)

    cleaned_df = cleaned_df.drop_duplicates()


    return cleaned_df