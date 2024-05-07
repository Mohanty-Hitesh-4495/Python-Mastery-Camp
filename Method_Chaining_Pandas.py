import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1,3,2,5,4], 'B': [4,5,6,1,2]})

# Method chaining example
result = df.rename(columns={'A': 'X'}).drop(columns='B').sort_values(by='X')
print(result)
