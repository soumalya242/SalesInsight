import pandas as pd


# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_superstore.csv")

# Display basic information
print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

#catagorywise sale
category_sales = df.groupby("Category")["Sales"].sum()
#sorting sales
category_sales = category_sales.sort_values(ascending=False)
#print categorywise sales
print("\nCategorywise sales: ")
print(category_sales)

# Region-wise Sales and Profit Analysis
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

# Sort by Sales (highest to lowest)
region_analysis = region_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\nRegion-wise Sales and Profit:")
print(region_analysis)

# Monthly Sales Analysis

# Extract year and month from Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year-Month"] = df["Order Date"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = df.groupby("Year-Month")["Sales"].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

# Top 10 Products by Sales

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:")
print(top_products)

# Monthly Profit Analysis

monthly_profit = (
    df.groupby("Year-Month")["Profit"]
    .sum()
)

print("\nMonthly Profit Trend:")
print(monthly_profit)