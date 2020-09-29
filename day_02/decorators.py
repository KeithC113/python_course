def say_hello(): 
    return "Hello World!"

# print (say_hello)

hi = say_hello # without() makes it a function object

# some_function is a call back
# function_caller is a HIGHER order function 
#  higher order function takes in a function as an argument
def function_caller(some_function):
    return some_function()

# print(function_caller(hi))


def outer_function():
    def inner_function():
        return "Hello from inner function"
    return inner_function()
# print (outer_function())

def make_pretty(callback):
    def wrapper():
        print("Iam doing some more cool functionality")
        callback()
    return wrapper 

@make_pretty
def bare_bones_business():
    print("Iam doing the core ordinary work")

# bare_bones_business()
# bare_bones_business()
# make_pretty(bare_bones_business)
# fancy_business = make_pretty(bare_bones_business)
# fancy_business()

# from timing_function import timing_function

# @timing_function
# def cool_function():
#     num_list = []
#     for num in (range(0,100000)):
#         num_list.append(num)
#     print(f'sum of all numbers: {sum(num_list)}')

# print(cool_function())

from timing_function import timing_function

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

print(my_function())