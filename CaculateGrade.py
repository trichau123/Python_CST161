import random

aGrades = []
print("Welcome to Agrades system: ")
list = ""
for i in range(7):
  a = random.randint(0,100)
  aGrades.append(a)
  list +=   " " + str(a) 
print(list)

examCount = len(aGrades) - 1
print(examCount)

def sum():
  aSum = 0
  for i in range(7):
    aSum +=   aGrades[i]
  return aSum
Sm = sum()
print("Sum ",Sm)
finalExam = aGrades[6]
totalPoints  = Sm - finalExam
print("Total Points: ", totalPoints)
testAverage = totalPoints/ examCount
print("test Average", testAverage)
finalAverage = 0.6*testAverage + finalExam*0.4
print("final Average ", finalAverage)
