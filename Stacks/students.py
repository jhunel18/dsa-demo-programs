from stacks import Stack

stackStudents = Stack(10)

while True:
    choice = input("Press ENTER to STOP any key to CONTINUE: ")
    if(choice == ""):
        break
    else:
        while True:
            menu = int(input("Enter the operation in Stack: "))
            if(menu == 1):
                print("Push an Item")
                elem = input("Enter the element to add: ")
                stackStudents.add(elem)
                print("Element " + elem + " is added.")
                continue
            elif(menu == 2):
                print("Pop an element: ")
                elem = stackStudents.removeTop()
                print("Element "+ elem + " is removed.")
                continue
            elif(menu == 3):
                print("View the top element: ")
                elem = stackStudents.peek()
                print("The current top element is " + elem)
                continue
            else:
                print("Invalid Input")
                break