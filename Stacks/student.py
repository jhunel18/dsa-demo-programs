class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def displayInfo(self):
        print("ID : " + str(self.id))
        print("Name : " + self.name)
    
    def computeTuition(self, units, pricePerUnit):
        print(units * pricePerUnit)

s = Student(112, "Jhunel")
s.displayInfo()
s.computeTuition(23, 12)
s.computeTuition(21, 20)