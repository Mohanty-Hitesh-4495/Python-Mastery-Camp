# In this example, the Pandas Series is demonstrated 
# with various functionalities such as:
# 1. indexing,
# 2. slicing,
# 3. arithmetic operations,
# 4. handling missing values. 

import pandas as pd

# Creating a Series from a list
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Pandas Series:")
print(series)

# Indexing and slicing
print("\nIndexing and slicing:")
print(series[0])        # Accessing by index
print(series[1:3])      # Slicing
print(series[[1, 3]])   # Fancy indexing

# Arithmetic operations
print("\nArithmetic operations:")
print(series * 2)       # Scalar multiplication
print(series + series)  # Element-wise addition

# Handling missing values
print("\nHandling missing values:")
data_with_nan = [1, 2, None, 4, 5]
series_with_nan = pd.Series(data_with_nan)
print(series_with_nan)

# Comparison with Python list
python_list = [1, 2, 3, 4, 5]
print("\nComparison with Python list:")
print("Python List:", python_list)
