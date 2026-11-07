
import pandas as pd

from analysis.data_cleaning import validate_uploaded_dataset


# Load the cleaned Superstore dataset
file_path = "data/processed/cleaned_superstore.csv"

df = pd.read_csv(file_path)

# Run validation
is_valid, result = validate_uploaded_dataset(df)

print("Validation Status:", is_valid)
print("Validation Result:", result)
