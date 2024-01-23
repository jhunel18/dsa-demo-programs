import random

Bingo = []

def numberGenerator(min, max, card_list, displayed_numbers):
    counter = 0
    while counter < 5:
        randomNum = random.randint(min, max)
        #Checks if the generated number is not already in the card list and has not been displayed before.
        if randomNum not in card_list and randomNum not in displayed_numbers: 
            card_list.append(randomNum)
            displayed_numbers.add(randomNum)
            counter += 1
            

displayed_numbers = set()

while True:
    choice = input("\nChoices:\nPress Enter to generate a Bingo card \nPress 'x' to stop generating \n>>")
    if choice == "":
       #if the length of the numbers is 75 the program will end
        if len(displayed_numbers) == 75: 
            print("\nNumbers are all generated. Generating Bingo Card completed.")
            break
         
        B = []
        I = []
        N = []
        G = []
        O = []
        #Calls the function numberGenerator to generate numbers on each letter
        numberGenerator(1, 15, B, displayed_numbers)
        numberGenerator(16, 30, I, displayed_numbers)
        numberGenerator(31, 45, N, displayed_numbers)
        numberGenerator(46, 60, G, displayed_numbers)
        numberGenerator(61, 75, O, displayed_numbers)
        
        # putting Free in the 3rd line or center of letter N
        N[2] = "Free"

        bingo_card = [B, I, N, G, O]
        Bingo.append(bingo_card)
        #Displays the Bingo card in a tabular format.
        print("\nB\tI\tN\tG\tO")
        for row in range(5):
            for column in range(5):
                if column == 2 and row == 2:
                    print("Free", end="\t")
                else:
                    print(f"{str(bingo_card[column][row]):<4}",end="\t")
            print()
            #if the user type 'x' the program will terminate
    elif choice.lower() == "x":
        break     
        print()
        #if the user press another key word it will be invalid and the program will continue
    else:
        print("\nInvalid input.  ")

for i, card in enumerate(Bingo, start=1):
    print(f"\nGENERATED BINGO CARD {i}: ")
    print("B\tI\tN\tG\tO")
    for row in range(5):
        for column in range(5):

            #the word Free will be displayed
            if column == 2 and row == 2:
                print("Free", end="\t")
            else:
                print(f"{str(card[column][row]):<4}", end="\t")
        print()