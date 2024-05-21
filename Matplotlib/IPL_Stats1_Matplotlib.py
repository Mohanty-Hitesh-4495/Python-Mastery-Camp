# Plot the score of both the teams over by over 
# And 5 over by 5 over...
# RCB     SRH
# 12      8
# 10      10
# 12      11
# 11      15
# 18      10
# 20      12
# 21      15
# 10      10

from matplotlib import pyplot as plt

rcb=[12,10,12,11,18,20,21,10,16,15]
srh=[8,10,11,15,10,12,15,10,12,26]

rcbscore=[sum(rcb[:i]) for i in range(0,len(rcb)+1)]      # Cummulative sum of run each over by over...
srhscore=[sum(srh[:i]) for i in range(0,len(srh)+1)]

# rcbscore=[sum(rcb[:i]) for i in range(5,len(rcb)+1,5)]      # Cummulative sim of run 5 over by 5 over...
# srhscore=[sum(srh[:i]) for i in range(5,len(srh)+1,5)]

plt.title("RCB Vs SRH")
plt.plot(range(0,11),rcbscore,label="RCB",marker="o")
plt.plot(range(0,11),srhscore,label="SRH",marker="o")
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.grid()
plt.legend()
plt.show()