# 1. what are the attributes in excel
# 2. number of rows and columns ()
# 3. fill the data those are not available as "Age"=18 and "voters"=yes/no

import pandas as pd

df = pd.read_excel(r"D:/Book5.xlsx")

print("Existing Dataframe:\n",df)
attributes = df.columns.to_list()

print("\n1. Attributes:\n",attributes)
(rows,columns)=df.shape

print("\n2. Dimension (row,col):\n(",rows,",",columns,")")

df["Age"]=df["Age"].fillna(18)

df.loc[df["Age"]<18, "Voter"] ="No"
df.loc[df["Age"]>=18, "Voter"] ="Yes"

df.to_excel(r"D:/Book5.xlsx",index=False)

df=pd.DataFrame(df)
print(df)

