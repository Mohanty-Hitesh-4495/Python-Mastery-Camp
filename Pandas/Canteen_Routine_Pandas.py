import pandas as pd
import random as rd

foodtime = ["BreakFast","Lunch","Tiffin","Dinner"]
mon = ["Idli","Rajma-Chawal","Tea/Coffee-Biscuit","Lemon Rice"]
tue = ["Dosa","Egg Curry-Rice","Chowmin","Curry-Khichadi"]
wed = ["Puri","Chicken-Rice","Maggie","Biryani"]
thu = ["Upma","Chole-Bhature","Cutllete","Pulav"]
fri = ["Wada","Fish-Rice","Sandwich","Sabji-Roti"]
sat = ["Omlette","Besan Raita","Manchurian","AlooParatha"]

df = pd.DataFrame({"Day/Time":foodtime,"Monday":mon,"Tuesday":tue,"Wednesday":wed,"Thursday":thu,"Friday":fri,"Saturday":sat})
df.to_excel(r"D:\Book1.xlsx",index=False)







""" name=["Hitesh","Prakash","Anjani"]
mobile=["7205374495","4568974465","7856984565"]
city=["Aska","Bhadrak","Paradeep"]
D={}
D["Name"]=name
D["Mobile"]=mobile
D["City"]=city
df=pd.DataFrame(D)
print(df)
df.to_excel(r"D:/Book3.xlsx",index=False) """





