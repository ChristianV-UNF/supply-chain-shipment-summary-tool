import pandas as pd


def load_dataset(file_path):
    """
    Load the shipment dataset from a CSV file.

    Parameters:
        file_path (str): Path to the CSV dataset.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            print(f"Error: Dataset loaded but is empty: {file_path}")
            return None

        print("Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    return None