print(type("Hello World"))
print(type(4))
print(type(True))
print(type(False))
print(type(None))


# Strings 
print ("Hello World"[0])
# Splice 0-5 
print ("Hello World"[0:5]) 
# "Hello World" [0] = "Y" # no!!!!
print("Hello" + " " + "World!!!!")
print (len("Hello World")) # Print length of the string
print (ord("a"))

#  integers
print (3+ 4)
print (5 -2)
print (9 %2) 
print (10/2)
print(4/3)
print(type(4/3))


# floats/converts
print(type(float(10)))
print(type(str(10)))
print(int(5.7))

#  boolean 

coffee_time = True 
if coffee_time: 
     print("Coffee time!!")

print(type(2 == 4))
print (type(1 ==1))

# Types
my_name= "Keith"
my_name= 10
print(my_name)

# my_variable = "5" + 10 

a,b,c = 10, 5, 9 
# Same as 
a = 10 
b = 5
c = 9 

print(c)

#  Task 
first_name = "Keith"
last_name = "Campbell"
year_of_birth = 1974


username = first_name[0:3] + last_name[0:3] + str(year_of_birth)

print(username)


