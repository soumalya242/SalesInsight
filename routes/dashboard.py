from flask import Blueprint, jsonify
from database.db import db
from database.models import SalesRecord

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/api/total-sales")
def total_sales():
    result = db.session.query(
        db.func.sum(SalesRecord.sales)
    ).scalar()
    return jsonify({
        "total_sales": float(result or 0)
    })


@dashboard_bp.route("/api/kpis")
def get_kpis():
    total_sales = db.session.query(
        db.func.sum(SalesRecord.sales)
    ).scalar() or 0
    total_profit = db.session.query(
        db.func.sum(SalesRecord.profit)
    ).scalar() or 0
    total_orders = db.session.query(
        db.func.count(db.distinct(SalesRecord.order_id))
    ).scalar() or 0
    total_quantity = db.session.query(
        db.func.sum(SalesRecord.quantity)
    ).scalar() or 0
    average_order_value = (
        total_sales / total_orders if total_orders > 0 else 0
    )
    return jsonify({
        "total_sales": float(total_sales),
        "total_profit": float(total_profit),
        "total_orders": int(total_orders),
        "total_quantity": int(total_quantity),
        "average_order_value": float(average_order_value)
    })


@dashboard_bp.route("/api/category-sales")
def category_sales():
    results = db.session.query(
        SalesRecord.category,
        db.func.sum(SalesRecord.sales)
    ).group_by(
        SalesRecord.category
    ).all()
    category_data = []
    for category, sales in results:
        category_data.append({
            "category": category,
            "sales": float(sales)
        })
    return jsonify(category_data)


@dashboard_bp.route("/api/region-analysis")
def region_analysis():
    results = db.session.query(
        SalesRecord.region,
        db.func.sum(SalesRecord.sales),
        db.func.sum(SalesRecord.profit)
    ).group_by(
        SalesRecord.region
    ).all()
    region_data = []
    for region, sales, profit in results:
        region_data.append({
            "region": region,
            "sales": float(sales),
            "profit": float(profit)
        })
    return jsonify(region_data)


@dashboard_bp.route("/api/monthly-sales")
def monthly_sales():
    results = db.session.query(
        db.func.year(SalesRecord.order_date),
        db.func.month(SalesRecord.order_date),
        db.func.sum(SalesRecord.sales)
    ).group_by(
        db.func.year(SalesRecord.order_date),
        db.func.month(SalesRecord.order_date)
    ).order_by(
        db.func.year(SalesRecord.order_date),
        db.func.month(SalesRecord.order_date)
    ).all()
    monthly_data = []
    for year, month, sales in results:
        monthly_data.append({
            "month": f"{year}-{month:02d}",
            "sales": float(sales)
        })
    return jsonify(monthly_data)


@dashboard_bp.route("/api/top-products")
def top_products():
    results = db.session.query(
        SalesRecord.product_name,
        db.func.sum(SalesRecord.sales).label("total_sales")
    ).group_by(
        SalesRecord.product_name
    ).order_by(
        db.desc("total_sales")
    ).limit(10).all()
    product_data = []
    for product_name, sales in results:
        product_data.append({
            "product_name": product_name,
            "sales": float(sales)
        })
    return jsonify(product_data)


@dashboard_bp.route("/api/monthly-profit")
def monthly_profit():
    results = db.session.query(
        db.func.year(SalesRecord.order_date),
        db.func.month(SalesRecord.order_date),
        db.func.sum(SalesRecord.profit)
    ).group_by(
        db.func.year(SalesRecord.order_date),
        db.func.month(SalesRecord.order_date)
    ).order_by(
        db.func.year(SalesRecord.order_date),
        db.func.month(SalesRecord.order_date)
    ).all()
    monthly_data = []
    for year, month, profit in results:
        monthly_data.append({
            "month": f"{year}-{month:02d}",
            "profit": float(profit)
        })
    return jsonify(monthly_data)