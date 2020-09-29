#  print numbers from 1-10

# numbers = range(1,11)

# for number in numbers:
#     print(number) # this will print a range object
#                         # (genrator)
#                         # (not a list which means we cant do list stuff) 

# #  Generator that generates all even numbers 

def generate_evens(max): 
    index = 0
    while index <= max: 
        if index % 2 == 0:
            yield index # gives something back but not return  
        index += 1 

# for number in generate_evens(1000): 
#     print(number)

print(list(generate_evens(10)))
