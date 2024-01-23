class Stack:

    def __init__(self, MAX_SIZE):
        self.stack = []
        self.MAX_SIZE = MAX_SIZE

    def push_element(self, dataval): #push

        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    def peek_element(self): #display the top element
        return self.stack[-1]
    
    def pop_element(self): #pop
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
