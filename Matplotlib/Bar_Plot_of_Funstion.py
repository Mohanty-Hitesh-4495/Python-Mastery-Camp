# 1. plot Bar the function fx=x^2+1 in the range (2-10)

from matplotlib import pyplot as plt

disc1 = {"BBSR":(35,25),"MUM":(35,32),"CHEN":(34,30),"AHM":(33,29)}
l1=[x for x in range(2,10+1)]
l2=[(x**2)+1 for x in range(2,10+1)]
plt.bar(l1,l2)
plt.title("function f(x)=(x^2)+1 in the range (2-10)")
plt.xlabel("Value of X")
plt.ylabel("f(x)=(x^2)+1")
plt.show()

