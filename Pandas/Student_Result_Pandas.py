import pandas as pd
import random as rd

# creating the Excelsheet for students randomly... 
D = {}
gen = ["Male","Female"]
res = ["Pass","Fail"]
roll = range(1,51)

D["Roll"] = roll
D["Gender"] = [gen[rd.randint(0,1)] for j in roll]
D["Result"] = [res[rd.randint(0,1)] for j in roll]

df = pd.DataFrame(D)
print(df)
df.to_excel(r"D:/Book4.xlsx",index=False)




