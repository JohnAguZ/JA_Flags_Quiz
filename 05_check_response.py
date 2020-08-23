import random
import csv

# Open file
all_flags = open("flag_codes.csv", "r")

# Read data into a list
csv_all_flags = csv.reader(all_flags)

# Create a dictionary to hold the data

all_flags = {
    'AB': 'Antigua and Barbuda',
    'AE': 'United Arab Emirates',
    'AF': 'Afghanistan'
}

# get random item from dictionary
# from: https://kite.com/python/answers/how-to-get-a-random-entry-from-a-dictionary-in-python#:
# ~:text=Use%20random.,Call%20random.

flag_list = list(all_flags.items())
secret_flag = random.choice(flag_list)
flag_pic = (secret_flag[0])
var_filename = flag_pic + "-flag.gif"

for item in range(1, 11):
    secret_flag = random.choice(flag_list)

    question = secret_flag[0]
    ask = input("What is the country name for {}".format(question))
    answer = secret_flag[1]

