import random 

Bingo = [] #create a empty list that will eventually hold the bingo card.

#Function for random number 
def randomNum(min, max, row):
    counter = 0

    while True:
        randomNum = random.randint(min, max)
        if randomNum in row:  #This is to check that the same number is not added to the row more than once.
            continue
        else:
            row.append(randomNum)
            counter += 1 
            if counter == 5: #If the counter reaches 5, the code will break 
                Bingo.append(row)
                break  

#Ask user to press any key to enter to the Bingo Card  
choice = input ("Press any key to Enter generator Bingo Card: ") 

#Initializes five empty lists which will represent the columns on the Bingo card.
B = []
I = []
N = []
G = []
O = []
#Calls randomNum 5 times, specifying the range of numbers for each column.
randomNum(1,15,B)
randomNum(16,30,I)
randomNum(31,45,N)
randomNum(46,60,G)
randomNum(61,75,O)

#Generate the Bingo Card
print("B \tI \tN \tG \tO") # This will print each letter of BINGO cards
for x in range(len(Bingo)):
    #Specify the index of each letter.
    b = Bingo[0]
    i = Bingo[1]
    n = Bingo[2]
    g = Bingo[3]
    o = Bingo[4]
    
    Bingo[2][2] = "FREE" #This part will input the "FREE" at the center of square
    print(f"{b[x]} \t{i[x]} \t{n[x]} \t{g[x]} \t{o[x]}") # Will print the whole output of Bingo Card in tabular format.
    
