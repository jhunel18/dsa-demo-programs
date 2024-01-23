import random

Bingo = []

def randomNumber(min, max): #function that appandens the temporary array to the permanent "Bingo Array"
    row = []
    counter = 0
    while True:
        randNum = random.randint(min, max)
        if randNum in row: #If the random number is already in the array, jump out and generate new random number to append
            continue
        else:
            row.append(randNum)
            counter += 1 #counter = counter + 1
            if counter == 5: #if the counter reaches 5, append the row into the Bingo array
                Bingo.append(row)
                break
        

choice = input("Enter any key to Generate Bingo Card: ") #asks the user to type any key to proceed

randomNumber(1, 15)
randomNumber(16,30) 
randomNumber(31,45)
randomNumber(46,60)
randomNumber(61,75)

print(" B\t I\t N\t G\t O")

for num in range( len(Bingo)): # iterate every number in the range of the length of the array which is 5
    B = Bingo[0] #named the index 0 of Bingo array, 'B' and so on..
    I = Bingo[1]
    N = Bingo[2]
    G = Bingo[3]
    O = Bingo[4]
    Bingo[2][2] = 'FREE'
    print(f"|{B[num]}|\t|{I[num]}|\t|{N[num]}|\t|{G[num]}|\t|{O[num]}|") #print the iterated position of the element until it terminates

#Jayvee Crujido
#Princess Jocel Plazuelo