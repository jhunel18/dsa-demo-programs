from array import *

array1 = array('i',[])

while True:
    choice = input("Enter your choice: ")

    if choice == "":
        print("Program ends")
        break
    elif choice == '1':
        #Append
        val = int(input("Enter a value: "))
        array1.append(val)
        continue
    elif choice == '2':
        #print the value
        for elem in array1:
            print(elem)
        continue
    elif choice == '3':
        print("Insert")
        continue
    elif choice == '4':
        print("Remove")
        continue
    elif choice == '5':
        print("Update")
        continue
    else:
        print("Invalid Input")
        break