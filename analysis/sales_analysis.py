import pandas as pd


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