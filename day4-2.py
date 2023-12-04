import re #regex

'''
lotto part 2

we need a dictionary containing how many copies of each card we have
- starts with 1 copy of each
- then we iterate card 1 to card n
- after we get a card's score, we increment the ones we need to

then we just total all the values in the dict
'''

def getLottoScore(line:str) -> int:
    winning_numbers_pattern = re.compile(r':\s*([\d\s]+)\s*\|')
    winning_numbers_match = re.findall(winning_numbers_pattern, line)
    #we use list comprehension here its a little janky
    #i still dont really get how list comprehension works but im trying it
    winning_numbers = [list(map(int, match.split())) for match in winning_numbers_match][0]
    # print(winning_numbers)

    given_numbers_pattern = re.compile(r'\|\s*([\d\s]+)')
    given_numbers_match = re.findall(given_numbers_pattern, line)
    given_numbers = [list(map(int, match.split())) for match in given_numbers_match][0]
    # print(given_numbers)

    #at this point we have the winning numbers and the given numbers in separate arrays
    score = 0
    for num in given_numbers:
        if num in winning_numbers:
            score+=1
    return score
    

file_path = "data/day4-1.txt"
total_score = 0

#more list comprehension or i guess dict comprehension
#this generates keys from 1 to 203 (203 is the length of the input)
#and initializes the value at each key to 1, bc we start with 1 copy of each card
card_dict = {i: 1 for i in range(1, 204)}
# print(card_dict)

#boilerplate code to open a file, with some error handling
try:
    with open(file_path, 'r') as file:
        #read each line
        for i, line in enumerate(file):
            score = getLottoScore(line)
            print("card", i+1, "has a score of", score, "and there are", card_dict[i+1], "copies of it")
            for dict_index in range(i+2, min(i+2+score, 204)):
                #ex. if card is 1 and card 1's score is 3
                #then we iterate through cards 2 to 4
                if dict_index <= 203:
                    card_dict[dict_index] += card_dict[i+1] #card_dict[i+1] is num of copies of the card

    for i in range(1, 204):
        total_score += card_dict[i]

    print(card_dict)
    print(f'Total sum: {total_score}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

#correct answer: 76504829