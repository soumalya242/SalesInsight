import pandas as pd

def load_dataset(file_path):
    """
    Load the sales CSV dataset.
    """

    df = pd.read_csv(file_path, encoding="latin1")
    #convert date column into dateime format
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],format="%m/%d/%Y"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],format="%m/%d/%Y"
    )
    return df


def clean_dataset(df):
    """
    Clean and validate the sales dataset.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Check missing values
    print("Missing values:", df.isnull().sum().sum())

    # Validate Sales
    print("Negative Sales:", (df["Sales"] < 0).sum())

    # Validate Quantity
    print("Invalid Quantity:", (df["Quantity"] <= 0).sum())

    # Validate Discount
    print(
        "Invalid Discount:",
        ((df["Discount"] < 0) | (df["Discount"] > 1)).sum()
    )

    # Validate dates
    print("Invalid Order Dates:", df["Order Date"].isnull().sum())
    print("Invalid Ship Dates:", df["Ship Date"].isnull().sum())

    return df