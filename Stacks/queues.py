class Queue:

    def __init__(self):
       self.queue = list()

    def addtoq(self,dataval):
# Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    
# Pop method to remove element
    def removefromq(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No elements in Queue")

customerQueue = Queue()

customerQueue.addtoq(10)
customerQueue.addtoq(20)
customerQueue.addtoq(30)
customerQueue.addtoq(40)
print(customerQueue.addtoq(50))
print(customerQueue.removefromq())
