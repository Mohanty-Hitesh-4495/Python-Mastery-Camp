from matplotlib import pyplot as plt

d={}                                     # creating a dictionary  
d[1]=[20,"M",50,"Football"]              # key(roll)->age,gender,weight,game   
d[2]=[2,"F",55,"Football"]
d[3]=[18,"F",58,"Cricket"]
d[4]=[16,"F",60,"Badminton"]
d[5]=[15,"M",45,"Chess"]

age=["Voter","Non-Voter"]                               # labeling: voters and non-voters 
vl=["1" if d[x][0]>=18 else "0" for x in d.keys()]      # Extracting voter and non voters count
voters=vl.count("1")                                    # separeting voters
nonvoters=vl.count("0")                                 # separeting non-voters

plt.subplot(2,2,1)                                      # Subplot-1/4
plt.title("Vote Eligibility")
plt.pie((voters,nonvoters),labels=age,autopct="%1.1f%%")    # ploting voters-nonvoters pie-chart

gender=["M","F"]                                        # labeling: male and female
vl=["1" if d[x][1]=="M" else "0" for x in d.keys()]     # extracting male and female from dictionary
male=vl.count("1")                                      # Male count
female=vl.count("0")                                    # Female count    

plt.subplot(2,2,2)                                      # Subplot-2/4
plt.title("Gender Distribution")
plt.pie((male,female),labels=gender,autopct="%1.1f%%")  # ploting voters-nonvoters pie-chart

roll=[x for x in d.keys()]                              # Extracting Roll numbers
weight=[d[i][2] for i in d.keys()]                      # Extracting weight of students from ictionary

plt.subplot(2,2,3)                                      # Subplot-3/4
plt.title("Weight Graph")                               
plt.bar(roll,weight)                                    # ploting a bar graph of roll number and weight of those roll
plt.xlabel("Roll number")
plt.ylabel("Weight")
plt.grid(axis="y")


games=list(set([d[x][3] for x in d.keys()]))            # extracting games in set 
nums=[d[x][3] for x in d.keys()]                        # all games
ns=[nums.count(i) for i in games]                       # counting the same games

plt.subplot(2,2,4)                                      # Subplot-1/4
plt.pie(ns,labels=games,autopct="%1.1f%%")              # ploting a pie chart of liked games by students
plt.title("Game Likes")
plt.show()