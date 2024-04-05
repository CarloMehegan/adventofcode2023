import re #regex

'''
lotto part 2

we need a dictionary containing how many copies of each card we have
- starts with 1 copy of each
- then we iterate card 1 to card n
- after we get a card's score, we increment the ones we need to

then we just total all the values in the dict
'''

#seed number is the second number
def processSeed(line:str) -> int:
    
    return 0
    

file_path = "data/day5-1.txt"
total_score = 0
input_rows = []

#boilerplate code to open a file, with some error handling
try:
    with open(file_path, 'r') as file:
        #read each line
        for i, line in enumerate(file):
            input_rows.append(line.split())
            print(input_rows[i])

    print(card_dict)
    print(f'Total sum: {total_score}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

#correct answer: 76504829