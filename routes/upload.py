
import os
import uuid

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
from analysis.data_cleaning import (
    read_uploaded_csv,
    validate_uploaded_dataset
)
from database.db import db
from database.models import Upload, SalesRecord


upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = os.path.join("data", "uploads")


@upload_bp.route("/api/upload", methods=["POST"])
def upload_csv():

    if "file" not in request.files:
        return jsonify({"error": "No file selected"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.lower().endswith(".csv"):
        return jsonify({"error": "Only CSV files are allowed"}), 400

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    original_name = secure_filename(file.filename)
    unique_name = f"{uuid.uuid4().hex}_{original_name}"

    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    # Read uploaded CSV
    df = read_uploaded_csv(file)

    # Validate dataset
    is_valid, result = validate_uploaded_dataset(df)

    if not is_valid:
        return jsonify(result), 400

    # Save file only if validation succeeds
    df.to_csv(file_path, index=False)

    try:
        db.session.query(SalesRecord).delete()

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

        db.session.add_all(records)

        upload_record = Upload(
                filename=original_name,
                total_records=len(records)
            )

        db.session.add(upload_record)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": f"Database import failed: {str(e)}"
        }), 500

    return jsonify({
            "message": "File uploaded successfully!",
            "filename": original_name
        }), 200
