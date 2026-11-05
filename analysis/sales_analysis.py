import pandas as pd
import plotly.express as px

def calculate_total_sales(df):
    """
    Calculate total sales revenue.
    """

    total_sales = df["Sales"].sum()

    return total_sales


def calculate_total_profit(df):
    """
    Calculate total profit.
    """

    total_profit = df["Profit"].sum()

    return total_profit


def calculate_total_orders(df):
    """
    Calculate the number of unique orders.
    """

    total_orders = df["Order ID"].nunique()

    return total_orders


def calculate_total_quantity(df):
    """
    Calculate total quantity of products sold.
    """

    total_quantity = df["Quantity"].sum()

    return total_quantity


def calculate_average_order_value(df):
    """
    Calculate average revenue per unique order.
    """

    total_sales = df["Sales"].sum()
    total_orders = df["Order ID"].nunique()

    average_order_value = total_sales / total_orders

    return average_order_value

def get_category_sales(df):
    """
    Calculate total sales by product category.
    """

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )
    return category_sales


def get_region_analysis(df):
    """
    Calculate total sales and profit by region.
    """

    region_analysis = (
        df.groupby("Region")[["Sales", "Profit"]]
        .sum()
        .sort_values(by="Sales", ascending=False)
    )

    return region_analysis


def get_monthly_sales(df):
    """
    Calculate total sales for each month.
    """
    df = df.copy()
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Year-Month"] = df["Order Date"].dt.to_period("M")
    monthly_sales = (
        df.groupby("Year-Month")["Sales"]
        .sum()
    )
    return monthly_sales

def get_top_products(df, limit=10):
    """
    Get top products based on total sales.
    """

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(limit)
    )

    return top_products

def get_monthly_profit(df):
    """
    Calculate total profit for each month.
    """

    df = df.copy()

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    df["Year-Month"] = df["Order Date"].dt.to_period("M")

    monthly_profit = (
        df.groupby("Year-Month")["Profit"]
        .sum()
    )

    return monthly_profit


def create_monthly_sales_chart(df):
    """
    Create a line chart showing monthly sales.
    """

    monthly_sales = get_monthly_sales(df)

    chart_data = monthly_sales.reset_index()

    chart_data["Year-Month"] = chart_data["Year-Month"].astype(str)

    fig = px.line(
        chart_data,
        x="Year-Month",
        y="Sales",
        title="Monthly Sales Trend",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales ($)"
    )

    return fig