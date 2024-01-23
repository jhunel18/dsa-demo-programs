class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def display(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            return "The node is not existing"
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        lastVal = self.headval
        while lastVal.nextval:
            lastVal = lastVal.nextval
        lastVal.nextval = NewNode

bookLinkedList = LinkedList()

while True:
    choice = input("Press any key to continue: ")

    if choice == "":
        print("The List is empty.")
        break
    else:
        menu = input("\nBOOKS\n1. Insert a book At Beginning\n2. Insert a book In Between\n3. Insert a book at End\n4. Display Books\nEnter your choice: ")
        
        if menu == '1':
            e1 = input("Enter a book: ")
            bookLinkedList.AtBeginning(e1)
            print("Book:  " + e1 + " is added at the beginning\n")
        elif menu == '2':
            pos = int(input("Enter the position after which you want to insert: "))
            e2 = input("Enter a book: ")
            current_node = bookLinkedList.headval
            count = 1
            while current_node and count < pos:
                current_node = current_node.nextval
                count += 1
            if current_node is None:
                print("Library Position not found")
            else:
                bookLinkedList.InBetween(current_node, e2)
                print("Book " + e2 + " is added in between\n")
        elif menu == '3':
            e3 = input("Enter a book: ")
            bookLinkedList.AtEnd(e3)
            print("Book " + e3 + " is added at the end\n")
        elif menu == '4':
            print("\nDisplaying Linked List:")
            bookLinkedList.display()
            continue
        else:
        	print("Invalid Input")
        	break