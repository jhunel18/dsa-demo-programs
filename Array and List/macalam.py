import random

def generatebingocard():
    bingoCard = []


    def numberGenerator(min, max, row):
        counter = 0
        while True:
            randomNum = random.randint(min, max)
            if randomNum not in row:
                row.append(randomNum)
                counter += 1
            if counter == 5:
                bingoCard.append(row)
                break

    B = []
    I = []
    N = []
    G = []
    O = []

    numberGenerator(1, 15, B)
    numberGenerator(16, 30, I)
    numberGenerator(31, 45, N)
    N[2] = "FREE"
    numberGenerator(46, 60, G)
    numberGenerator(61, 75, O)

    return bingoCard

def printBingoCard(card):
    print("B\tI\tN\tG\tO")
    for i in range(5):
        for row in card:
            print(row[i], end="\t")
        print()

while True:
    choice = input("Press any number to generate a Bingo Card or press enter to quit: ")
    if choice == "":
        print("Exiting program......")
        break
    else:
        bingocardresult = generatebingocard()
        print("Your Bingo Card is:")
        printBingoCard(bingocardresult)