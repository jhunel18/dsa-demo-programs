import random 

Bingo = [] # Initialize an empty list to store Bingo cards.

def numberGenerator(min, max, row):
    counter = 0
    while True:
        randomNum = random.randint(min, max)
        if randomNum not in row:
            row.append(randomNum)
            counter += 1
        if counter == 5:
            Bingo.append(row)
            break

def printBingoCard():
    print("B\tI\tN\tG\tO") # Print the column headers for the Bingo card.
    for i in range(5):# Iterate through each column.
        for row in Bingo: # Iterate through each row in the Bingo card.
            print(row[i], end="\t")
        print()

while True:
    choice = input("Press Enter to generate a Bingo Card or type 'exit' to quit: ")
    if choice.lower() == "exit":
        break
    else:
        Bingo = [] # Reset the 'Bingo' list to empty.
        B = [] # Create empty lists for each column (B, I, N, G, O).
        I = []
        N = []
        G = []
        O = []
        numberGenerator(1, 15, B)
        numberGenerator(16, 30, I)
        numberGenerator(31, 45, N)
        N[2] = "FREE" # Replace the center cell with "FREE."
        numberGenerator(46, 60, G)
        numberGenerator(61, 75, O)

        print("Your Bingo Card is:") # Print the generated Bingo card.
        printBingoCard()