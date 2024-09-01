print("welcome to my computer quiz!")
plyaing = input("Do you want to play? ")
if plyaing.lower() != "yes":
   quit()
print("Okay let's play:)")
score = 0
anwser = input("what does CPU stand for? ")
if anwser.lower() == "central processing unit":
  print('correct!')
  score += 1
else:
   print('incorrect!')
anwser = input("what does GPU stand for? ")
if anwser.lower() == "graphics processing unit":
   print('correct!')
   score += 1
else:
   print('Incorrect!')
anwser = input("what does RAM stand for? ")
if anwser.lower() == "random access memory":
   print('correct!')
   score += 1
else:
   print('Incorrect!')
print("you got " + str(score)+ " qustion correct!")
print("you got " + str((score / 4) * 100 ) + "%.")