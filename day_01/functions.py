def say_hello():
    return "Hello, World"

print(say_hello()) 

def set_alarm(day):
    # day = "Mday"
    if (day == "Saturday" or day == "Sunday"):
        return None
    else:
        return "07:00"
print (set_alarm("Monday"))
print (set_alarm("Sunday"))

# local variables/ block scoped 
name = "Keith"
def say_hello():
    name = "Gregor"
    print ("Hi, " + name)

say_hello()
print(name)

# Default arguments (have to be declared first)
def add(a, b = 2):
    return a + b 

print(add(3,10))
print(add(7))

result = add(b=3, a=2)
print(result)

#We need to do positional arguments before keyword arguments 
result = add(a=-2) #0
# result = add(b=3) # error as nothing assigned to a
result = add(2, b=4) # 6
# result = add(b=4,2) # error as positional arguments first
result = add(a=2, 4)
print(result)


