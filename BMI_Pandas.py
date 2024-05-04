import pandas as pd

df = pd.read_excel(r"D:/Book2.xlsx",index_col=False)
# print([x for (x,y) in zip(df["Name"],df["Age"]) if y>=21])
df["Weight"]=[23,56,89]
df["Height"]=[123,142,133]
bmi=[(((x/y)**2)*1000) for (x,y) in zip(df["Weight"],df["Height"])]
df["BMI"]=bmi
print(df)
df.to_excel(r"D:/Book2.xlsx",index=False)