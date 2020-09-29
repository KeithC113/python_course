# Meet the Beatles:

beatles = [
    {"name": "John Lennon", "birth_year": 1940, "death_year": 1980, "instrument": "piano"},
    {"name": "Paul McCartney", "birth_year": 1942, "death_year": None, "instrument": "bass"},
    {"name": "George Harrison", "birth_year": 1943, "death_year": 2001, "instrument": "guitar"},
    {"name": "Ringo Starr", "birth_year": 1940, "death_year": None, "instrument": "drums"}
]

#  list of type dictionary - 4 dictionaries 

# Use the `beatles` list above to answer the following questions:

# 1. John Lennon also plays guitar. Access the `instrument` key in his dictionary and change its value:

beatles[0]["instrument"] = beatles[0]["instrument"] + ", guitar"

print(beatles[0]["instrument"])


# 2. Write a function which takes in the list of band members as a parameter,
#    and returns a list of all the Beatles' names:
# Expected result: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr']

def list_of_names(people):
    # names = []
    # for person in people:
    #     names.append(person["name"])
    # return names

    return [person["name"] for person in people]

print (list_of_names(beatles))


# 3. Write a function which takes in the list of band members as a parameter,
#    and returns a list of the members who are still alive
#    (i.e. they have no value for `death_year`)
#    Return the full dictionary for each member
# Expected result: [
#    {'name': 'Paul McCartney', 'birth_year': 1942, 'death_year': None, 'instrument': 'bass'},
#    {'name': 'Ringo Starr', 'birth_year': 1940, 'death_year': None, 'instrument': 'drums'}
# ]

def get_living(people): 
    return[person for person in people if person["death_year"] == None]

    # living_people =[]
    # for person in people:
    #     if person["death_year"] == None

print(get_living(beatles))


# 4. Combine the above two functions to return the names of all the members who are alive:
# Expected result: ['Paul McCartney', 'Ringo Starr']

print(list_of_names(get_living(beatles)))
