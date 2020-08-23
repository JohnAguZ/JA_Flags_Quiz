import random
import csv

# Open file
all_flags = open("flag_codes.csv")

# Read data into a list
csv_all_flags = csv.reader(all_flags)

# Create a dictionary to hold the data

all_flags = {}

# Add the data from the list into the dictionary
# (first item in row is key, next is definition)

for row in csv_all_flags:
    all_flags[row[0]] = row[1]

print(all_flags)

# get random item from dictionary
# from: https://kite.com/python/answers/how-to-get-a-random-entry-from-a-dictionary-in-python#:
# ~:text=Use%20random.,Call%20random.


flag_list = list(all_flags.items())
secret_flag = random.choice(flag_list)
flag_pic = (secret_flag[0])
var_filename = flag_pic + "-flag.gif"


for item in range(1, 11):
    secret_flag = random.choice(flag_list)

    print(secret_flag[0], secret_flag[1])
    question = secret_flag[1]
    ask = input("What is the country name for {}".format(question))
    answer = secret_flag[0]


