import random
gameRecord=[]
totalGames = 0
cmpScore = 0
userScore = 0
 
while True:
    totalGames+=1
    userOption=0;
    while True:
        userChoice = input("Enter your choice Rock(R) Paper(P) Scissors(S) : ");
        if userChoice.upper() == 'R' :
            userOption = "Rock";
            break
        elif userChoice.upper() == 'P' :
            userOption = "Paper";
            break
        elif userChoice.upper() == 'S' :
            userOption = "Scissors";
            break
        else :
            print("Invalid option. Setting to Scissors")
    computerChoice = random.randint(1,3);
    computerOption=0;
    if computerChoice == 1 :
        computerOption = "Rock";
    elif computerChoice == 2 :
        computerOption = "Paper";
    elif computerChoice == 3 :
        computerOption = "Scissors";
     
    print("You selected : "+userOption)
    print("Computer selected : "+computerOption)
     
    if(userOption=="Rock" and computerOption=="Scissors" or
        userOption=="Paper" and computerOption=="Rock" or userOption=="Scissors" and computerOption=="Paper") :
        print("You wins")
        userScore+=1
        win = 1
    elif userOption==computerOption:
        print("Match Draw")
        win = 0
    else:
        print("Computer wins")
        cmpScore+=1
        win = 2
     
    row = [totalGames,win]
    gameRecord.append(row)
     
    playAgain = input("Do you want to play again ? Enter y to continue...")
    if playAgain!='y' and playAgain!='Y':
        break
