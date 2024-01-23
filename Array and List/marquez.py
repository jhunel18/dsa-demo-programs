import random

#function to generate random numbers for a row without duplicates
def numberGenerator(min, max, row):
    counter = 0
    while True:
        randomNum = random.randint(min, max)
        if randomNum not in row: #to avoid any duplications of the numbers, this code will generate if the number is not already in the row, if does then it appends the number
            row.append(randomNum)
            counter += 1
            if counter == 5:
                break

# Function to print the Bingo card with "FREE" in the center
def bingoCard(Bingo):
    print("B \tI \tN \tG \tO")
    for i in range(5):
        for row in Bingo:
            if i == 2 and row is Bingo[2]:  #this condition add "FREE" in the center of the N, 'i' represents the index of the inside array while 'Bingo[2]' represents the row or index of the main array
                print("FREE", end="\t")
            else:
                print(row[i], end="\t") #this will print the numbers in landscape display, the row indicates the index then shall end with a tab function
        print()

Bingo = [] #declaration of empty list of the Bingo

while True:
    choice = input("Press any key to generate a Bingo Card or Enter to exit: ")
    if choice == "":
        print("Bingo! Program ends.")
        break
    else:
        B = []
        I = []
        N = []
        G = []
        O = []

        numberGenerator(1, 15, B) #calls the function numberGenerator
        numberGenerator(16, 30, I)
        numberGenerator(31, 45, N)
        numberGenerator(46, 60, G)
        numberGenerator(61, 75, O)
        Bingo = [B, I, N, G, O] #declaration of the list

        bingoCard(Bingo) #calls the bingocard function