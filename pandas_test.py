import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [30, 25]})

# Display the first few rows
print(df.head())

# Display summary statistics
print(df.describe())

# Access a specific column
print(df['Name'])

# Filter rows based on condition
print(df[df['Age'] > 26])
