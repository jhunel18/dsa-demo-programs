# Import the 'random' module which provides functions to generate random numbers.
import random

# Define a function 'numberGenerator' that takes three arguments: min, max, and row.
def numberGenerator(min, max, row):
    # Initialize a counter to keep track of how many numbers have been generated and added to 'row'.
    counter = 0
    
    # Start an infinite loop.
    while True:
        # Generate a random number between 'min' and 'max'.
        randomNum = random.randint(min, max)
        
        # Check if 'randomNum' is not already in 'row'.
        if randomNum not in row:
            # If not, append it to 'row'.
            row.append(randomNum)
            # Increment the counter.
            counter += 1
        
        # If counter reaches 5, exit the loop.
        if counter == 5:
            break

# Define a function 'generateBingoCard'.
def generateBingoCard():
    # Initialize empty lists for each letter group.
    B = []
    I = []
    N = []
    G = []
    O = []

    # Generate numbers for each group using 'numberGenerator'.
    numberGenerator(1, 15, B)
    numberGenerator(16, 30, I)
    numberGenerator(46, 60, G)
    numberGenerator(61, 75, O)

    # Generate numbers for the 'N' group.
    numberGenerator(31, 45, N)

    # Create a dictionary 'card' with keys 'B', 'I', 'N', 'G', and 'O' and their respective lists.
    card = {'B': B, 'I': I, 'N': N, 'G': G, 'O': O}

    # Return the dictionary 'card'.
    return card

# Define a function 'printBingoCard' that takes a 'card' as an argument.
def printBingoCard(card):
    # Define a list of labels for the columns.
    labels = ['B', 'I', 'N', 'G', 'O']

    # Print the labels separated by tabs.
    for label in labels:
        print(label, end="\t")
    print()

    # Loop through rows.
    for i in range(5):
        # Loop through labels.
        for label in labels:
            # Check if it's the center cell (label 'N' and row 2).
            if label == 'N' and i == 2:
                print("FREE", end="\t")
            else:
                # Print the corresponding number from the 'card'.
                print(card[label][i], end="\t")
        print()

# Start an infinite loop.
while True:
    # Prompt the user for input.
    choice = input("Press any key to generate Bingo Card (or press space to exit): ")
    
    # If the user presses space, break out of the loop and end the program.
    if choice == " ":
        break
    else:
        # Generate a Bingo Card and print it.
        bingoCard = generateBingoCard()
        print("Your Bingo Card is:")
        printBingoCard(bingoCard)