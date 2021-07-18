# Class name always starts with Capital letters
class Employee:
    empCount = 0 # empCount is a class variable

    def __init__(self,first,second,salary):
        # self --> Represents instance of a class
        # self -->
        # first,second,salary are class attributes
        self.first = first
        self.second = second
        self.salary = salary
        Employee.empCount +=1

    def displaySomething(self):
        print("This is a method inside a class")

    def get_salary(self, name):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary


obj1 = Employee("Sumit","Kumar",25000)
print(print(obj1.salary))


print("present salary",obj1.get_salary("Sumit"))
obj1.set_salary(30000)
print("Updated Salary",obj1.get_salary("Sumit"))