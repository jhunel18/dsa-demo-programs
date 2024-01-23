import random 

Bingo = []

def numberGenerator(min,max,row):
    counter = 0
    while True:
        randomNum = random.randint(min,max)
        #No duplicate number
        if randomNum not in row:  
            row.append(randomNum)
            counter +=1         
        if counter == 5:
            #In N column, replacing the middle part of the row as free
            if min == 31 and max == 45:
                row[2] = "Free"
            Bingo.append(row)
            break
        else:
            continue

#To have Columns         
def printBingoCard():
    for col in range(5):
        for row in Bingo:
            print(row[col], end = "\t")
        print()        
        
while True:
    choice = input("Press any key to generate Bingo Card(or press enter to program ends): ")
    
    if choice == "":
        break
        
    else:
        #Regenerate the Bingo Card
        B = []
        I = []
        N = []
        G = []
        O = []
        
        numberGenerator(1, 15, B)
        numberGenerator(16, 30, I)
        numberGenerator(31, 45, N)
        numberGenerator(46, 60, G)
        numberGenerator(61, 71, O)       
       
        print("Bingo Card: ")
        print("\nB         I         N        G       O  ")
        printBingoCard()
        break