from queues import Queue


ticketQueue = Queue(10)
anotherQueue = Queue(10)

while True:
    choice = input("Enter your choice: \n1-Enqueue\n2-Dequeue\n3-Peek\>>")
    if choice == "":
        print("You exit")
        break
    elif choice == "1":
        val = input("Enter the value to enqueue: ")
        ticketQueue.enqueue(val)
        print("Inserted Successfully")
        continue
    elif choice == "2":
        val = ticketQueue.dequeue()
        a
        #print("Removed the front")

        continue
    elif choice == "3":
        print(ticketQueue.peek())
        continue
    else:
        print("Invalid input")
        continue