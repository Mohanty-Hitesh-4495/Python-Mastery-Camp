from matplotlib import pyplot as plt
# import random as rnd
import numpy as np
l=np.random.randn(1000)
plt.hist(l,bins=10,color='green',edgecolor='black')
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.show()