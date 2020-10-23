numset = [1,2,3]
alphaset = ['A','B','C']
for i in numset:
  for j in alphaset:
    print(i,j)
count1 = 0
print("While")
while (count1 <3):
  count2 = 0
  while (count2<3):
    print(numset[count1],alphaset[count2])
    count2 += 1
  count1 += 1
