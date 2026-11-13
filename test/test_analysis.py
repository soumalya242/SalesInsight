from analysis.sales_analysis import calculate_total_sales, calculate_total_profit,calculate_total_orders, calculate_total_quantity, calculate_average_order_value,get_category_sales,get_region_analysis,get_monthly_sales,get_top_products,get_monthly_profit
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

# Category-wise Sales
category_sales = get_category_sales(df)

print("\nCategory-wise Sales:")
print(category_sales)

# Regional Sales and Profit
region_analysis = get_region_analysis(df)

print("\nRegional Sales and Profit:")
print(region_analysis)

# Monthly Sales Trend
monthly_sales = get_monthly_sales(df)

print("\nMonthly Sales Trend:")
print(monthly_sales)

# Top 10 Products
top_products = get_top_products(df)

print("\nTop 10 Products by Sales:")
print(top_products)

# Monthly Profit Trend
monthly_profit = get_monthly_profit(df)

print("\nMonthly Profit Trend:")
print(monthly_profit)