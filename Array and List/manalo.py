import random

# Initialize an empty list to store Bingo cards
Bingo = []

# Function to generate random numbers for a Bingo row
def numberGenerator(min, max, row):
    counter = 0
    while True:
        randomNum = random.randint(min, max)
        if randomNum not in row:
            row.append(randomNum)
            counter += 1
        if counter == 5:
            # Once we have 5 unique numbers, add the row to the Bingo card
            Bingo.append(row)
            break

# Function to print the Bingo card
def bingoCard():
    print("B\tI\tN\tG\tO")
    for i in range(5):
        for row in Bingo:
            print(row[i], end="\t")
        print()

while True:
    # Ask the user for input to generate a Bingo card or exit
    choice = input("Press Enter to generate a Bingo Card or type 'exit' to quit: ")
    if choice.lower() == "exit":
        print("Program Terminated")
        break
    else:
        # Reset the Bingo card and generate numbers for each letter column
        Bingo = []
        B = []
        I = []
        N = []
        G = []
        O = []
        numberGenerator(1, 15, B)  # Generate numbers for the 'B' column
        numberGenerator(16, 30, I)  # Generate numbers for the 'I' column
        numberGenerator(31, 45, N)  # Generate numbers for the 'N' column
        N[2] = "FREE"  # Mark the center cell as 'FREE'
        numberGenerator(46, 60, G)  # Generate numbers for the 'G' column
        numberGenerator(61, 75, O)  # Generate numbers for the 'O' column

        # Print the generated Bingo card
        print("Your Bingo Card is:")
        bingoCard()