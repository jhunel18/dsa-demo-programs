import random
#import random module

#Main array to store BINGO Numbers
Bingo = []

#Number Generator for each letter
def numberGenerator(min,max,row):
    counter = 0
#counter to limit each row in BINGO
    while True:
        randomNum = random.randint(min,max)
#condition to print unique random numbers
        if randomNum in row:
            continue
        else:
            row.append(randomNum)
            counter +=1
            if counter == 5:
                Bingo.append(row)
                break
#Bingo card printer function
def printBingoCard():
#for loop to go through each element in the array of the array
    for col in range(5):
        for row in Bingo:
            print(row[col], end="\t")
        print()        
#Condition to generate Bingo Card
while True:
    choice = input("Press any key to generate Bingo Card: ")
    if choice == "":
        break
    else:
        B = []
        I = []
        N = []
        G = []
        O = []
#implement the functions
        numberGenerator(1,15, B)
        numberGenerator(16,30, I)
        numberGenerator(31,45, N)
        numberGenerator(46,60, G)
        numberGenerator(61,75, O)       
       
        print("Bingo Card:\nB\tI\tN\tG\tO")
#Replace middle of en the word "FREE"
        Bingo[2][2] = "FREE"
#implement bingo card printer function
        printBingoCard()
        break