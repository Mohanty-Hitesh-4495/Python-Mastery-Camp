from matplotlib import pyplot as plt
# 3. make a barplot of student roll vs attendence of five students
# 4. make a bar plot of your attentence in a particular subject assuming 1 for present and 0 for absent



disc1 = {"BBSR":(35,25),"MUM":(35,32),"CHEN":(34,30),"AHM":(33,29)}
l1=[(35,25),(35,32),(34,30),(33,29)]
ht=[32,45,38,29]
lt=[15,28,19,16]
l2=["BBSR","MUM","CHEN","AHM"]
plt.bar(l2,ht)
plt.bar(l2,lt)
plt.show()