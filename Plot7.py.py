from matplotlib import pyplot as plt

d={}
d["Satya"]=["Tea","Football",70]
d["Smarak"]=["Tea","COD",82]
d["Arpita"]=["Coffee","Badminton",45]
d["gayatri"]=["Coffee","Ludo",60]
d["Satyajit"]=["Tea","Cricket",28]

label=["Tea","Coffee"]             # Labels for piechart

drinks=[d[x][0] for x in d.keys()]      # First approach for extracting tea and coffee count
tea=drinks.count("Tea")
coffee=drinks.count("Coffee")

plt.subplot(2,1,1)
plt.pie((tea,coffee),labels=label,autopct="%1.1f%%")

games=list(set([d[x][1] for x in d.keys()]))        #
nums=[d[x][1] for x in d.keys()]
ns=[nums.count(i) for i in games]

plt.subplot(2,1,2)
plt.pie(ns,labels=games,autopct="%1.1f%%")
plt.show()