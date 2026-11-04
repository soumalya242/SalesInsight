import pandas as pd


def calculate_total_sales(df):
    """
    Calculate total sales revenue.
    """

    total_sales = df["Sales"].sum()

    return total_sales