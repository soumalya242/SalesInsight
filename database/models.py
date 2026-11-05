from database.db import db


class SalesRecord(db.Model):
    __tablename__ = "sales_records"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    ship_date = db.Column(db.Date)
    customer_id = db.Column(db.String(50))
    customer_name = db.Column(db.String(150))
    segment = db.Column(db.String(50))
    region = db.Column(db.String(50))
    category = db.Column(db.String(50))
    sub_category = db.Column(db.String(100))
    product_id = db.Column(db.String(50))
    product_name = db.Column(db.String(255))
    sales = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Float)
    profit = db.Column(db.Float)


class Upload(db.Model):
    __tablename__ = "uploads"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )
    total_records = db.Column(db.Integer, default=0)