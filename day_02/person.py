class Person: 
    # __init__ is name of constructor
    def __init__(self, name, age, height): # construtor
        self.name = name # instance variables
        self.age = age
        self.height = height

    def talk(self):
        return "Hi, my name is " + self.name + "!" + ". I am " + str(self.height)


# not inside the class

new_person = Person("Charlotte", 46, 6)

#  self is the new person object atached to the self object
#  always pass self in the constructor

# print(new_person.name)
# print(new_person.talk())

class Employee(Person): # inherits from the Person class 

    def __init__(self, employee_number, name, age, height):
        self.employee_number = employee_number
        super().__init__(name, age, height)

    def get_employee_number(self): 
        return self.employee_number

new_employee = Employee (9999, "Keith", 21, 5.9)

print(new_employee.name) 
print(new_employee.talk())

