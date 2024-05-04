from matplotlib import pyplot as plt
import pandas as pd

# extracting pass and fail students and displaying in piechart..
df = pd.read_excel(r"D:/Book4.xlsx",index_col=False)
counts = df["Result"].value_counts()
Pass = counts.get("Pass", 0)
Fail = counts.get("Fail", 0)
plt.figure(figsize=(7,7))
plt.pie([Pass,Fail], labels=["Pass","Fail"],autopct="%1.1f%%")
plt.title('Result of NPTEL exam')
plt.show()