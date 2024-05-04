# Student
# Roll      Marks in 10th      Marks in 12th     Marks in B-Tech
# 2             60.4                70              56.12
# 3             45.15               78.2            56.15
# 4             28.2                56.7            89.12
# 5             85.1                45.25           56.23


from matplotlib import pyplot as plt

student={   2:{"10th":83.6,"12th":50,"B-Tech":91},
            3:{"10th":95,"12th":60,"B-Tech":92},
            4:{"10th":81,"12th":75.16,"B-Tech":85}
        }
# roll=int(input("Enter the Roll number:"))
# if roll in student.keys():  
plt.ylim(25,100)
plt.plot(list(student[2].keys()),list(student[2].values()),marker="o",label = "Srinibash")
plt.plot(list(student[3].keys()),list(student[3].values()),marker="o",label = "Rahul")
plt.plot(list(student[4].keys()),list(student[4].values()),marker="o",label = "Hitesh")

plt.title("Students Career Performance")
plt.xlabel("Exam Names")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()