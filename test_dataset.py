from analysis.data_cleaning import load_dataset, clean_dataset

# Define the dataset path
file_path = "data/raw/Sample - Superstore.csv"

# Load dataset
df = load_dataset(file_path)
# Clean the dataset
df = clean_dataset(df)

# Save cleaned dataset
output_path = "data/processed/cleaned_superstore.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")

# # Display first 5 rows
# print(df.head())

# # Display dataset shape
# print("\nDataset Shape:", df.shape)

# # Display unique orders
# print("Unique Orders:", df["Order ID"].nunique())


# print("\nDate Column Data Types:")
# print(df[["Order Date", "Ship Date"]].dtypes)

# print("\nFirst 5 Order Dates:")
# print(df["Order Date"].head())

# #cheack the invaild data
# print("\nNegative Sales:")
# print((df["Sales"] < 0).sum())

# print("\nInvalid Quantity:")
# print((df["Quantity"] <= 0).sum())

# print("\nInvalid Discount:")
# print(((df["Discount"] < 0) | (df["Discount"] > 1)).sum())

# print("\nNegative Profit:")
# print((df["Profit"] < 0).sum())


# # Final dataset summary

# print("\nFinal Dataset Summary")

# print("Total Records:", len(df))

# print("Unique Orders:", df["Order ID"].nunique())

# print("Total Sales:", df["Sales"].sum())

# print("Total Profit:", df["Profit"].sum())

# print("Total Quantity:", df["Quantity"].sum())

# print("Negative Profit Records:", (df["Profit"] < 0).sum())