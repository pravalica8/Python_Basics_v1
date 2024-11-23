# Classes are user defined blueprint or prototype
# Calculator : Sum, multiplication, division,percentage
# A class will have methods , variables, class variables, instance variables, constructors etc.

class Calculator:
    num = 100

    def getData(self):
        print(" I am now executing as method in class")

obj = Calculator() # syntax to create objects in python
obj.getData()
print(obj.num)
