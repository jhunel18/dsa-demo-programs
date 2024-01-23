import random
#Empty array
Bingo = []

def numberGenerator(min, max, row): # Define a function to generate random numbers
    counter = 0
    while True:
        randomNum = random.randint(min, max)
        if randomNum not in row:  # Ensure no duplicate numbers
            row.append(randomNum) #append
            counter += 1
        if counter == 5:
            #if min == 31 and max == 45:  # Check if it's the N column
            row[2] = "FREE"  # Replace the middle element with "Free"
            Bingo.append(row) # Add the row to the Bingo card
            break 
# Define a function to print the Bingo card
def printBingoCard():
    for col in range(5):
        for row in Bingo:
            print(row[col], end="\t")
        print()

while True:
   choice = input("Press any key to generator Bingo Card: ")
   if choice == " ":
       break
   else:
        Bingo = []  # Reset Bingo card
        B = []
        I = []
        N = []
        G = []
        O = []
        numberGenerator(1, 15, B) 
        numberGenerator(16, 30, I)
        numberGenerator(31, 45, N)
        numberGenerator(46, 60, G)
        numberGenerator(61, 75, O)

        print("Your Bingo Card is: \n B       I         N        G       O  ")
        printBingoCard()