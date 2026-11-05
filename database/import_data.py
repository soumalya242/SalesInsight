import pandas as pd

from app import app
from database.db import db
from database.models import SalesRecord


def import_sales_data():
    # Load cleaned CSV file
    df = pd.read_csv("data/processed/cleaned_superstore.csv")
    print("Dataset loaded successfully!")
    print("Total records:", len(df))
    # Prepare records for database insertion
    records = []
    for _, row in df.iterrows():
        record = SalesRecord(
            order_id=str(row["Order ID"]),
            order_date=pd.to_datetime(row["Order Date"]).date(),
            ship_date=pd.to_datetime(row["Ship Date"]).date(),
            customer_id=row["Customer ID"],
            customer_name=row["Customer Name"],
            segment=row["Segment"],
            region=row["Region"],
            category=row["Category"],
            sub_category=row["Sub-Category"],
            product_id=row["Product ID"],
            product_name=row["Product Name"],
            sales=float(row["Sales"]),
            quantity=int(row["Quantity"]),
            discount=float(row["Discount"]),
            profit=float(row["Profit"])
        )
        records.append(record)
    print("Records prepared:", len(records))
        # Insert records into MySQL
    with app.app_context():
        # Check whether records already exist
        existing_records = db.session.query(SalesRecord).count()
        if existing_records > 0:
            print("Database already contains sales records.")
            print("Existing records:", existing_records)
            return
        try:
            db.session.add_all(records)

            db.session.commit()

            print("Data imported successfully!")
            print("Records inserted:", len(records))
        except Exception as e:
            db.session.rollback()
            print("Error importing data:", e)
            raise


if __name__ == "__main__":
    import_sales_data()