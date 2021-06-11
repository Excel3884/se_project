

class Employee():
    def __init__(self, name, lastname, id, salary, month):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.salary = salary
        self.month = month

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary=salary

    def getID(self):
        return id

    def getMonth(self):
        return self.month
    
    
