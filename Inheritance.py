class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark")

    def justPrint(self):
        print("Printing from Parent Class")

class Cat(Dog):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Meow...")

obj = Cat("anyName",5,"blue")
obj.speak()
obj.justPrint()