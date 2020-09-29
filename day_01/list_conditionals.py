numbers = range(1,11)

evens_squared = []

for number in numbers:
    if number % 2 == 0:
        evens_squared.append(number * number)
print(evens_squared)



# list comprehension template 

#  Result = [expression for item in list if condition]

evens_squared = [number * number for number in numbers if number % 2 ==0]
print(evens_squared)