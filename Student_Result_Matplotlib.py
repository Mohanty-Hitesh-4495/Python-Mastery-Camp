import matplotlib.pyplot as plt

d = {
    1: ['P', 'F', 'P'],
    2: ['F', 'P', 'P'],
    3: ['F', 'P', 'P'],
    4: ['P', 'P', 'P'],
    5: ['P', 'F', 'F'],
    6: ['F', 'F', 'F'],
    7: ['P', 'F', 'F'],
    8: ['P', 'F', 'F'],
    9: ['P', 'P', 'P'],
    10: ['F', 'P', 'F']
}

roll = [x for x in d.keys()]
result = [d[x] for x in d.keys()]
passcount = [x.count('P') for x in result]

at1 = len([x for x in passcount if x >= 1])
at2 = len([x for x in passcount if x >= 2])
at3 = len([x for x in passcount if x >= 3])

plt.bar(['Pass in 1 subject', 'Pass in 2 subjects', 'Pass in 3 subjects'], [at1, at2, at3])
plt.title("Student Passing Exams")
plt.ylabel("Number of Students")
plt.ylim(0,10)
plt.show()
