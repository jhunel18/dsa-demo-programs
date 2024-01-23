from stacks import Stack

AStack = Stack(10)
BStack = Stack(10)
while True:
    choice = input("Enter your choice\n1 - Push\nRedo-Pop : ")
    if choice == '1':
        while True:
            
            menu = input("Enter your choice\n 1 - Peek \n 2- Push \n 3- Pop \n : ")
            if(menu == '1'):
                print("Top Element of Stack A: " + AStack.peek())
                continue
            elif(menu == '2'):
                elem = input("Enter the value: ")
                AStack.add(elem)
                continue
            elif menu == '3':
                a = AStack.removeTop()
                BStack.add(a)
                print("Top Element of Stack B: " + BStack.peek())
                continue
            else:
                print("Invalid Input")
                break      