# lists (are like arrays)

my_food=["spam", "ham", "eggs"]
my_numbers=[1,3,4,6,10]

print(my_food[0]) #spam
print(my_food[2]) #eggs
print(my_food[-1]) #eggs
# print(my_food[5])
print(my_food[0:2]) #spam & ham
print(len(my_food)) #3  
print(sum(my_numbers)) #24
# print(sum(my_food))  #error
my_food.append("lettuce") 
print(my_food) 

stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]

stops.insert(0, "Queen Street")
print(stops)

print(stops.index("Croy"))

stops.insert(4,"Polmont")
print(stops)

stops.remove("Haymarket")
print(stops)

stops.clear() # invoke the clear function 
print(stops)

#Dictionaries (are like hashes)

user = {
    "name" :"Christine",
    "age": 40,
    45: 42
}

print(user["name"])
user["email"] ="christine@email.com"
print(user[45])

beatles = [
    {"name": "John", "instrument": "Guitar"},
    {"name": "Paul", "instrument": "Bass"},
    {"name": "Ringo", "instrument": "Drums"},
    {"name": "George", "instrument": "Guitar"}
]

# print out Paul's name
print(beatles[1]["name"])

me = {
    "name": "Keith", 
    "age": 46,
    "students": ["John", "Paul"]
}
print(me["students"])

#Tuples

person = ("Michael", 42, "Instructor", True) # Tuples are ( brackets

print(type(person))

print(person[1])

# person[3] = False # tuples are immutable

print(person.count("Michael")) # prints number of instances 

fruits = ("apple", "banana", "apple", "orange")

print(fruits.count("apple")) # 2
print(person.index("Instructor")) #1
print(len(person)) #4

# Named tuples 
from collections import namedtuple

Person = namedtuple("Person", "name age job_title")

me = Person("Keith", 21, "instructor")
niall = Person("Niall", 21, None)

print(me.name) #dot notation is better than index notation 

