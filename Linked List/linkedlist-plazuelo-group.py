class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def display(self):
        if self.headval is None:
            print("Linked List is empty.")
        else:
            elements = []
            printval = self.headval
            while printval is not None:
                elements.append(printval.dataval)
                printval = printval.nextval
            print(elements)

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def InBetween(self, prevdata, newdata):
        if prevdata is None:
            print("Previous node not found.")
            return

        current = self.headval
        while current is not None:
            if current.dataval == newdata:
                print(f"Data '{newdata}' already exists in the Linked List.")
                return
            if current.dataval == prevdata:
                NewNode = Node(newdata)
                NewNode.nextval = current.nextval
                current.nextval = NewNode
                return
            current = current.nextval

        print(f"Node with data '{prevdata}' not found in the Linked List.")

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return

        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = NewNode


myLinkedList = LinkedList()

while True: #choices
    print("\n1. At Beginning\n2. Display\n3. In Between\n4. At End\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter data for At Beginning: ")
        myLinkedList.AtBeginning(data)
    elif choice == "2":
        myLinkedList.display()
    elif choice == "3":
        prev_data = input("Enter data of the node after which to insert: ")
        new_data = input("Enter new data: ")
        myLinkedList.InBetween(prev_data, new_data)
    elif choice == "4":
        data = input("Enter data for At End: ")
        myLinkedList.AtEnd(data)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Display the final linked list
print("Final Linked List:")
myLinkedList.display()