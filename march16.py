# read the score of two teams and sanswer the following :
# 1. who won the match
# 2. how many runs was scored in the match
# 3. how many bowls was bowled
# 4. how many wickets fall 

""" 
input format :
18.5 100
19.5 182/5
18 191
"""

over1,score1 = input("Enter the Score of CSK team : ").split(" ")
if '/' not in score1 :
    score1 +='/10'
run1,wkt1 = score1.split('/')

over2,score2 = input("Enter the Score of MI team : ").split(" ")
if '/' not in score2 :
    score2 +='/10'
run2,wkt2 = score2.split('/')


if run1 > run2:
    print("1. Result : Winner team is CSK :)")
elif run1 < run2:
    print("1. Result : Winner team is MI :)")
else:
    print("1. Result :Match-Draw")

print("2. Total Run Scored in Match : ",int(run1)+int(run2))

ov1,bal1 = over1.split('.')
ov2,bal2 = over2.split('.')

print("3. Total Numbers of Bowls : ",(int(ov1)+int(ov2))*6+int(bal1)+int(bal2))

