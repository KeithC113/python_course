import csv

class Winner:
    #  data class to store data about one winner
    def __init__(self, index, year, age, name, movie):
        self.index = int(index)
        self.year = int(year) 
        self.age = int(age) 
        self.name = name 
        self.movie = movie

    def values(self):
        return [self.index, self.year, self.age, self.name, self.movie]

winners = []
count = 1 # so we know at what position to append our new data to the file

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)

    next(reader) #skips the first 
    for row in reader:
        count +=1
        current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
        winners.append(current_winner)

with open("oscars.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    # Write header row: 
    writer.writerow(["Index", "Year", "Age", "Name", "Movie"])

    for winner in winners:
        winner.age +=1 
        writer.writerow(winner.values())
        

# with open("oscars.csv", "a") as csvfile:
#     writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
#     new_winner = Winner(count, 2020, 50, "Renee Zellweger", "Judy")
#     writer.writerow(winners.values())  

# for winner in winners:
#     print(f"{winner.name} won the oscar for {winner.movie}")
#     print(f"{winner.name} was born near or during {winner.year - winner.age}")

eighties_winners = [winner for winner in winners if winner.year >= 1980 and winner.year <= 1989]

#  list of all ainners in the eighties 
for winner in eighties_winners:
    print(f"{winner.name} won in {winner.year}")

#  age of oldest oscar winner 
max_age = 0 
for winner in winners:
    if winner.age > max_age:
        max_age = winner.age
print(f"oldest oscar winner was {max_age} years old when they won")

# list of all meryl streeps oscar winners 
meryls_best_ones = [winner for winner in winners if winner.name == "Meryl Streep"]
for meryl in meryls_best_ones: 
    print(f"{meryl.movie} in {meryl.year}")

    


