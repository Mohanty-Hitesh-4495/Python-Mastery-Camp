# Open a text file and write your name,mobile number and location

try:
    file=open("file1.txt","w")
    file.write("Hitesh "+"7205374495 "+"Ganjam\n")
except Exception as e:
    print(e)
