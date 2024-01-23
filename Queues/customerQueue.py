from queues import Queue

customer = Queue()

customer.enqueue("Customer 1")
customer.enqueue("Customer 2")
print(customer.peek())