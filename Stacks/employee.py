class Employee:

    def __init__(self, name, ratePerHour,  age):
        self.name = name
        self.ratePerHour = ratePerHour #186.90
        self.age = age
        
    def printInfo(self):
        print("Employee's name: " + self.name)
        print("Employee's Rate Per Hour: " + str(self.ratePerHour))
        print("Employee's Age: " + str(self.age))
    
    def computeSalary(self, hoursWorked):
        return self.ratePerHour * hoursWorked
    
