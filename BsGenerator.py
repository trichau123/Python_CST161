import worklist
bl = True
adv = []
adj = []
verb = []
noun = []

rows, cols = (160, 4) 
#a = [['0']*cols]*rows
a = [['*' for l in range (4)] for i in range (160)]


while bl:
    userInput = input("Do you want to continue")
    if (userInput == "No" or userInput == "no"):
        bl = False
        break
# a [0][0] , a [0][1], a [0][2], a[0][3]
# a [1][0] , a [1][1], a [1][2], a[1][3]
# a [ last element of adverbs][]


    for z in range(160):
        if (z<32):
            a[z][3] = worklist.aAdverbs[z]
        if (z<90):
            a[z][0] = worklist.aNouns[z]
        if (z<98):
            a[z][1] = worklist.verb[z]
        a[z][2] = worklist.aAdjectives[z]
    print("Noun   ","Verb   ","Adjective   ","Adverb")
    for k in range (len(worklist.aAdjectives)):
       print(a[k][0],"   ",a[k][1],"   ",a[k][2],"   ",a[k][3])

    
