from array import *
#Empty 2D Array
T = []

#Create a temporary array
while True:
    choice = input("Press any key to add to an array: ")
    if choice == "":
        for arr in T:
            for elem in arr:
                print(elem,end = " ")
            print()
        print("Program ends ")
        break
    else:
        tempArray = []
        while True:
            elem = input("Enter a value to Add to temporary Array and ENTER to END: ")
            if elem == "":
                # T.append(tempArray)
                if len(T) ==0:
                    #insert default at zero index
                    T.insert(0, tempArray)
                    break
                else:
                    index = int(input("Enter the position: "))
                    T.insert(index, tempArray)
                break
            else:
                tempArray.append(elem)
                continue
  