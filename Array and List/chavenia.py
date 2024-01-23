import random

Bingo = []

def numberGenerator(min, max, letter_list, used_numbers):
    counter = 0
    while counter < 5:
        randomNum = random.randint(min, max)
        if randomNum not in letter_list and randomNum not in used_numbers:
            # Determine whether the number is in the current row or has already been used.
            letter_list.append(randomNum)
            used_numbers.add(randomNum)
            counter += 1

used_numbers = set()  # To keep track of used numbers, create a set.

while True:
    choice = input("Press Enter to generate a Bingo card, or type 'exit' to quit: ")
    if choice == "":
        if len(used_numbers) == 75:  # Verify that every number has been used.
            print("All numbers have been used. Bingo card generation complete.")
            break

        B = []
        I = []
        N = []
        G = []
        O = []

        # Generate numbers for each letter column
        numberGenerator(1, 15, B, used_numbers)
        numberGenerator(16, 30, I, used_numbers)
        numberGenerator(31, 45, N, used_numbers)
        numberGenerator(46, 60, G, used_numbers)
        numberGenerator(61, 75, O, used_numbers)

        N[2] = "N"

        bingo_card = [B, I, N, G, O]
        Bingo.append(bingo_card)
        print("\nBingo Card:")
        print("B    I    N    G    O")
        for row in range(5):
            for column in range(5):
                if column == 2 and row == 2:
                    print("FREE", end="\t")
                else:
                    print(f"{str(bingo_card[column][row]):<4}", end=" ")
            print()
    elif choice.lower() == "exit":
        # Let the user know that they have decided to leave
        print("Exiting the Bingo card generation process.")
        break
    else:
        # Notify the user of invalid input
        print("Invalid input. Press Enter to generate a Bingo card or 'exit' to quit.")

for i, card in enumerate(Bingo, start=1):
    print(f"\nBingo Card {i}:")
    print("B  I  N  G  O")
    for row in range(5):
        for column in range(5):
            if column == 2 and row == 2:
                print("N", end=" ")
            else:
                print(f"{str(card[column][row]):<4}", end=" ")
        print()
        
        
#Eroles Jhon Carlo
#Dichosa Alexis

        