from matplotlib import pyplot as plt

d={}
d["Satya"]=["Tea","Football",70]
d["Smarak"]=["Tea","COD",82]
d["Arpita"]=["Coffee","Badminton",45]
d["Gayatri"]=["Coffee","Badminton",60]
d["Prakash"]=["Tea","Cricket",58]
d["Anjani"]=["Tea","Cricket",52]
d["Syed"]=["Tea","Football",68]
d["Sanjeeb"]=["Coffee","Football",57]
d["Hitesh"]=["Tea","Cricket",55]

label=["Tea","Coffee"]                  # Labels for piechart

drinks=[d[x][0] for x in d.keys()]      # First approach for extracting tea and coffee count
tea=drinks.count("Tea")                 # Counting Tea lovers
coffee=drinks.count("Coffee")           # Counting Coffee lovers

plt.subplot(1,2,1)
plt.pie((tea,coffee),labels=label,autopct="%1.1f%%")
plt.title("Drinks Preference Chart")

games=list(set([d[x][1] for x in d.keys()]))        # Extracting all games type
nums=[d[x][1] for x in d.keys()]                    # Extracting all students games preference
ns=[nums.count(i) for i in games]                   # Counting the games preferences

plt.subplot(1,2,2)
plt.pie(ns,labels=games,autopct="%1.1f%%")
plt.title("Games Prference Chart")
plt.show()