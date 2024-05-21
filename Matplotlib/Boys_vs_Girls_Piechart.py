# 2. make a pichart for the number of boyz and girls in your section

import matplotlib.pyplot as plt

labels = ['Boys', 'Girls']
sizes = [20, 30]   

plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels)
plt.title('Number of Boys and Girls in the Section')
plt.show()
