import random

# Initialize an empty list to store the bingo card
Bingo = []

# Function to generate a random number within a range and add it to a row
def numGenerator(min, max, row):
    counter = 0
    while True:
        randomNum = random.randint(min, max)
        # Check if the number is not already in the row
        if randomNum not in row:  
            row.append(randomNum)
            counter += 1
            if counter == 5:
                # When 5 unique numbers are generated, add the row to the bingo card
                Bingo.append(row)
                break
            

# Main loop for generating the bingo card
while True:
    choice = input("Press any key to generate Bingo Card: ")
    if choice == " ":
        break
    else:
        # Initialize lists for B, I, N, G, and O columns
        B = []
        I = []
        N = []
        G = []
        O = []

        # Generate numbers for B, I, G, and O columns
        numGenerator(1, 15, B)
        numGenerator(16, 30, I)
        numGenerator(31, 45, N)
        # Free space in the middle of the card (N[2]) is set to 0
        N[2] = 0
        numGenerator(46, 60, G)
        numGenerator(61, 75, O)

        # Display the Bingo card
        print("B\tI\tN\tG\tO")
        for i in range(5):
            for column in Bingo:
                print(column[i], end="\t")
            print()
        break  # Exit the loop after generating and displaying the card