# TASK ONE:
# find the sum total total of the values in this list
# find the average (mean) value of the values in this list
ages = [5, 15, 64, 27, 84, 26]

print (sum(ages))# sum is inbuilt function 

total = 0 
for age in ages:
    total = total+ age
print(total)

print(sum(ages)/len(ages))
print(total/len(ages))

# TASK TWO:
# use a list comprehension to:
    # build a new list with the first letter from each word
    # convert each letter to lower case
words = ["The", "quick", "brown", "fox",
         "jumped", "over", "the", "lazy", "dog"]

new_list = []
for word in words:
    new_list.append(word.lower()[0])
print(new_list)

new_list = [letter[0:1].lower() for letter in words] 
print(new_list)

# TASK THREE:
# Search through the list and check if the name "Jack" is included. 
# Print out an appropriate message.
pupils = ["Alison", "James", "Stephen", "Mandy", "Jack", "Henry"]

if "Jack" not in pupils:
    print ("no Jack in class")

found = False 
for pupil in pupils: 
    if pupil =="Jack":
        found = True

if found:
    print("Jack attack")
else:
    print("Jack's back!!")

