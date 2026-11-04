from analysis.sales_analysis import calculate_total_sales, calculate_total_profit,calculate_total_orders, calculate_total_quantity, calculate_average_order_value
import pandas as pd


# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_superstore.csv")

# Calculate total sales
total_sales = calculate_total_sales(df)

print("Total Sales:", round(total_sales, 2))


# Calculate total profit
total_profit = calculate_total_profit(df)

print("Total Profit:", round(total_profit, 2))

# Calculate total orders
total_orders = calculate_total_orders(df)

print("Total Orders:", total_orders)

# Calculate total quantity
total_quantity = calculate_total_quantity(df)

print("Total Quantity:", total_quantity)

# Calculate average order value
average_order_value = calculate_average_order_value(df)

print("Average Order Value:", round(average_order_value, 2))