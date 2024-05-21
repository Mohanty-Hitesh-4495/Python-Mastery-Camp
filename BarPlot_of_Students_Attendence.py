# 3. make a barplot of student roll vs attendence of five students

from matplotlib import pyplot as plt

students = {
    33:86,
    34:56,
    35:71,
    36:93,
    37:62,
}

roll = [key for key in students.keys()]
attendence = [value for value in students.values()]
colours = ["red","blue","yellow","green","orange"]

plt.title("Bar Plot of Student's Attendence")
plt.bar(roll,attendence,color=colours)
plt.xlabel("Roll Numbers")
plt.ylabel("Attendence")
plt.xlim(32,38)
plt.ylim(0,100)
plt.show()