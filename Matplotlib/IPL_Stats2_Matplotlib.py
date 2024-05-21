# Plot the score of both the teams over by over 
# and show wickets fallen in each and every over on plot
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

rcb = [(12, 1), (10, 0), (12, 2), (15, 0), (18, 0), (20, 3), (21, 0), (10, 1), (16, 0), (15, 0)]
srh = [(8, 2), (10, 0), (11, 2), (15, 0), (10, 0), (15, 3), (10, 2), (12, 1)]

# Padding srh list with zeros to match the length of rcb list
srh += [(0, 0)] * (len(rcb) - len(srh))

rcbscore = [rcb[i][0] for i in range(len(rcb))]  # Extracting run for each over...
srhscore = [srh[i][0] for i in range(len(srh))]

rcbwckt = [rcb[i][1] for i in range(len(rcb))]  # Extracting wickets for each over...
srhwckt = [srh[i][1] for i in range(len(srh))]

rcbcum = [sum(rcbscore[:i + 1]) for i in range(len(rcb))]  # Cumulative sum of run over by over...
srhcum = [sum(srhscore[:i + 1]) for i in range(len(srh))]

overs = range(1, len(rcb) + 1)

plt.figure(figsize=(10, 6))
plt.title("RCB Vs SRH")
plt.plot(overs, rcbcum, label="RCB", marker="o")
plt.plot(overs, srhcum, label="SRH", marker="o")
plt.xlabel("Overs")
plt.ylabel("Runs")
# plt.xlim(0,10)
plt.grid(True)

# Plotting wickets
for i, (x, y) in enumerate(zip(overs, rcbwckt), 1):
    plt.text(x, rcbcum[i - 1], f'W:{y}', ha='center', va='bottom')

for i, (x, y) in enumerate(zip(overs, srhwckt), 1):
    plt.text(x, srhcum[i - 1], f'W:{y}', ha='center', va='bottom')

plt.legend()
plt.show()
