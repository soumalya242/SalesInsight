import pandas as pd



def read_uploaded_csv(file):
    """
    Read uploaded CSV files using common encodings.
    """

    encodings = ["utf-8-sig", "utf-8", "latin1"]

    for encoding in encodings:
        try:
            file.seek(0)

            df = pd.read_csv(
                file,
                encoding=encoding
            )

            return df

        except UnicodeDecodeError:
            continue

    raise ValueError(
        "Unable to read CSV file. Please check its encoding."
    )

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


def validate_uploaded_dataset(df):

    # Required columns
    required_columns = [
        "Order ID",
        "Order Date",
        "Ship Date",
        "Customer ID",
        "Customer Name",
        "Segment",
        "Region",
        "Category",
        "Sub-Category",
        "Product ID",
        "Product Name",
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    # Check missing columns
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        return False, {
            "error": "Missing required columns",
            "missing_columns": missing_columns
        }

    # Check empty dataset
    if df.empty:
        return False, {
            "error": "The uploaded CSV contains no records."
        }

    # Check missing values in required columns
    missing_values = df[required_columns].isnull().sum()
    missing_values = missing_values[missing_values > 0]

    if not missing_values.empty:
        return False, {
            "error": "Missing values found",
            "missing_values": missing_values.to_dict()
        }

    # Check numeric columns
    numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        if df[column].isnull().any():
            return False, {
                "error": f"Invalid numeric values in {column}"
            }

    # Check valid quantity
    if (df["Quantity"] <= 0).any():
        return False, {
            "error": "Quantity must be greater than zero."
        }

    # Check valid discount
    if ((df["Discount"] < 0) | (df["Discount"] > 1)).any():
        return False, {
            "error": "Discount must be between 0 and 1."
        }

    # Check sales
    if (df["Sales"] < 0).any():
        return False, {
            "error": "Sales cannot be negative."
        }

    return True, {
        "message": "Dataset validation successful!",
        "total_records": len(df),
        "duplicate_records": int(df.duplicated().sum())
    }
