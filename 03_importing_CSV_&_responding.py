import random
import csv
import re

# Open file
all_flags = open("flag_codes.csv", "r")

# Read data into a list
csv_all_flags = csv.reader(all_flags)


# Create a dictionary to hold the data
flags_dictionary = {}

# Add the data from the list into the dictionary
# (First item in row is the code and the next is the full name)
for row in csv_all_flags:
    flags_dictionary[row[1]] = row[0]

print(flags_dictionary)

flags_list = list(flags_dictionary.items())
random_entry = random.choice(flags_list)
print(random_entry)
