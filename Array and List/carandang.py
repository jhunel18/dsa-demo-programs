import random  # Import the random module to generate random numbers

Bingo = []  # Create an empty list to store Bingo cards

def numberGenerator(min_val, max_val, row):
    counter = 0  # Initialize a counter variable to keep track of the number of unique numbers generated
    while True:  # Create an infinite loop
        randomNum = random.randint(min_val, max_val)  # Generate a random number within the specified range
        if randomNum not in row:  # Check if the random number is not already in the row
            row.append(randomNum)  # Append the unique random number to the row
            counter += 1  # Increment the counter
        if counter == 5:  # If we've added 5 unique numbers, exit the loop
            Bingo.append(row)  # Append the row to the Bingo list
            break

while True:  # Create an outer loop that keeps generating Bingo cards until the user exits
    choice = input("Press any key to generaute Bingo Card (or press Enter to exit): ")  # Ask the user to press any key to generate a Bingo card or press Enter to exit
    if choice != "":  # Check if the user entered anything other than Enter
        Bingo = []  # Reset the Bingo card list

        B = []  
        I = []  
        N = [] 
        G = []  
        O = []  
        numberGenerator(1, 15, B)  # Generate numbers for the B column using the numberGenerator function
        numberGenerator(16, 30, I)  
        numberGenerator(46, 60, G)  
        numberGenerator(61, 75, O)  

        # Generate numbers for the N column without the "FREE" space
        numberGenerator(31, 45, N)

        # Insert "FREE" in the center of the N column
        N.insert(2, "FREE")

        print("\nGenerated BINGO Card:")
        print("   B     I     N    G     O")
        for i in range(5):  # Iterate over 5 rows to print the Bingo card
            # Print the numbers in each row separated by spaces
            print("{:4d}  {:4d}  {:4}  {:4d}  {:4d}".format(B[i], I[i], N[i], G[i], O[i]))

    else:  
        break
