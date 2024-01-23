from stacks import Stack

riceStack = Stack(10)

while True:
    choice = input("Enter your choice: ")
    if choice == "":
        print("Program ends")
        break
    elif choice == '1':
        print("Push an element: ")
        elem = input("Enter an element: ")
        riceStack.push_element(elem)
        continue
    elif choice == '2':
        print("Peek an element")
        print(riceStack.peek_element())
        continue
    elif choice == '3':
        print("Pop and element: ")
        riceStack.pop_element()
        continue
    else:
        print("Invalid Input")
        continue        