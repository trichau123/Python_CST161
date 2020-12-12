import csv

a = []
b = []
with open('BankTrans.csv') as file:
    reader = csv.reader(file)

    count = 0

    for row in reader:
        print(row)
        a.append(row)

        if(count > 5):
           break

        count += 1

with open('BankCusts.csv') as file:
    reader = csv.reader(file)

    count = 0

    for row in reader:
        print(row)
        b.append(row)

        if(count > 5):
           break

        count += 1

print(a)
print("********")
print(b)

print(a[0][0],"    ",b[0][1], "     ",b[0][2],"     ",a[0][1], "     ","Amount   ", "Old",b[0][3], "      New Balance" )
for i in range (1,len(a)):
    trans = "withdrawal"
    if float(a[i][1]) > 0 :
        trans = "deposit"
    print(a[i][0],"      ",b[i][1], "         ",b[i][2],"           ",trans,"          ",a[i][1], "        ", b[i][3], "         ", float(b[i][3])+float(a[i][1]))
