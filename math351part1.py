'''
This file finds gaps in the data and prints
what rows they are. Used in part 1.
'''

import re #use regular expressions to find commas

file_path = "data/occupancy.txt"

#boilerplate code to open a file, with some error handling
with open(file_path, 'r') as file:
    #read each line
    for i, line in enumerate(file):
        extra_commas = re.findall(r',,|,\n', line) #look for ",," or ",\n"
        if len(extra_commas) != 0: #if there's a match, print it
            print("found an extra comma in row", i+1)