import pandas as pd

# Create a DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum
grouped = df.groupby('Category').sum()

print("Original DataFrame:")
print(df)
print("\nGrouped DataFrame:")
print(grouped)
