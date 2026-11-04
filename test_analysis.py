from analysis.sales_analysis import calculate_total_sales
import pandas as pd


# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_superstore.csv")

# Calculate total sales
total_sales = calculate_total_sales(df)

print("Total Sales:", round(total_sales, 2))