import os

from load_data import load_dataset


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "supply_delivery_history.csv")

    df = load_dataset(file_path)

    if df is not None:
        print("\nDataset Preview:")
        print(df.head())

        print("\nDataset Shape:")
        print(df.shape)


if __name__ == "__main__":
    main()