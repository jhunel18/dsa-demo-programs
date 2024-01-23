from queues import Queue

studentQueue = Queue() #instance self.queue = []

while True:
    choice = input("Press any key to continue and ENTER to STOP: ")
    if choice == "":
        print("Program ends")
        break
    else:
        while True:
            userInput = int(input("Press 1. Enqueue\n2. Dequeue\n3. Peek\n>> "))
            if userInput == 1:
                elem = input("Enter the data: ")
                studentQueue.enqueue(elem)
                print("Data Inserted Successfully!")
                continue
            elif userInput == 2:
                studentQueue.dequeue()
                print("Data deleted")
                continue
            elif userInput == 3:
                print(studentQueue.peek())
                continue
            else:
                print("Invalid Input")
                continue
            
print("Program terminated")