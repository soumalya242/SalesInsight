import pandas as pd

from analysis.sales_analysis import create_monthly_sales_chart


# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_superstore.csv")

# Create monthly sales chart
fig = create_monthly_sales_chart(df)

# Display chart in browser
fig.show()