today = "Saturday"
today = "Sunday"
today = "Friday"

# || does not mean 'or' 
# && does not mean 'and'


if today == "Saturday" or today == "Sunday":
    print("Have a long lie!")
elif today == "Friday":
    print("Its nearly the weekend")
else:
    print("Its a work day, get up lazy bones")

print("This will print regardless as it sits outside the block")