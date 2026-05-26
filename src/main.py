from load_data import load_dataset


def main():

    file_path = "../data/supply_delivery_history.csv"

    df = load_dataset(file_path)

    if df is not None:
        print("\nDataset Preview:")
        print(df.head())

        print("\nDataset Shape:")
        print(df.shape)


if __name__ == "_main_":
    main()