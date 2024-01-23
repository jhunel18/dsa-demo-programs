import random

Bingo= [] # Initialize an empty list for the Bingo card.

# Function to generate a row of Bingo numbers.
def numberGenerator(min, max,row):
    counter = 0
    while True:
        randomNum = random.randint(min, max,)
        if randomNum not in row: #Add unique random number to the row
            row.append(randomNum)
            counter += 1
        if counter == 5: # Once it have 5 numbers in the row add to the Bingo card.
            Bingo.append(row)
            break
  # function to print the Bingo card.
def printBingoCard():
        for column in "BINGO":
            print(column, end = "\t") # Print the column and separated by the tab.
        print()
    
        for i in range(5):
             for row in Bingo: # Iterate through each row in the Bingo card.
                print(row[i], end = "\t") # Print the number in the current row and column, separated by the tab.
             print()


while True:
    choice = input("Press any key to generate Bingo Card: ")
    if choice == "":
       break    
    else:
        Bingo = []
        B = []
        I = []
        N = [] # Initialize empty arraylists for each letter in "BINGO".
        G = []
        O = []
# Generate numbers for each letter's and add them to the arraylist. 
        numberGenerator (1,15,B)
        numberGenerator (16, 30,I)
        numberGenerator (31,45, N)
        N[2] = "FREE" # The middle in N is marked as "FREE"
        numberGenerator (46,60, G)
        numberGenerator (61,75, O)
        
        print("Your card is: ")
        printBingoCard() # Print the Bingo card.