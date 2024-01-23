class Queue:

    def __init__(self, MAX_SIZE):
        self.queue = []
        self.max_size = MAX_SIZE
    
    #enqueue - add to the rear of the queue

    def enqueue(self, dataval):
        if len(self.queue) == self.max_size:
            print("Overflow condition")
        if dataval not in self.queue:
            self.queue.append(dataval)
            return True
        return False

    #dequeue - removes element at the rear
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        return 'No element in Queue'

    #peek
    def peek(self):
        return self.queue[0]