
import pandas as pd

df = pd.read_excel(r"D:/Book5.xlsx")      # Reads the Excel-sheet  

header=df.columns.to_list()               # Extracting all Attributes of dataframe  
print(header)

data=list(df[header[0]])                  # Extracting All Names from Excel  
print(data)

rows,columns = df.shape                   # Extracting number of rows and columns from dataframe
print(rows,columns)                       # printing Dimension of Dataframe

ndf=df.fillna(18)                         # filling empty cells in dataframe
print(df)                                 # old dataframe having empty cell
print(ndf)                                # new dataframe filled 5 in every empty column