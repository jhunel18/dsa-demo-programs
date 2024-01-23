from array import *

numArray = array('i',[])

while True:
    choice = input("Press any key to continue. ENTER to STOP: ")

    if choice == "": #If the user presses the ENTER Key
        print("Program ends")
        break
    else:
        while True:
         
         userInput = input("Press 1. Append\nPress 2. Insert\nPress 3. Find \nPress 4. View\nPress 5. Remove\n 6. Update \n>> ")
         
         if userInput == '1':
            elem = int(input("Enter the value: "))
            numArray.append(elem)
            continue
         
         elif userInput == '2':
            index = int(input("Enter the index: "))
            val = int(input("Enter the new value: "))
            numArray.insert(index, val)
            continue
         
         elif userInput == '3':
            val = int(input("Enter a value: "))
            print(numArray.index(val))
            continue
         
         elif userInput == '4':
            for elem in numArray:
               print(elem, end=" ")
               print()
         elif userInput == '5':
             val = int(input("Enter the value to remove: "))
             numArray.remove(val)
         elif userInput == '6':
            index = int(input("Enter the index: "))
            newVal = int(input("Enter new Value: "))
            numArray[index] = newVal
            print('Data updated successfully!')
         else:
           print("Invalid Input")
           continue

print("Ends")