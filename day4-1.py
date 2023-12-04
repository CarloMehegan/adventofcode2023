import re #regex

'''
lotto

one of the first ideas that comes to mind is using sets
- store the winning numbers in a set
- iterate through the other numbers and check if they are in the set
'''

def getLottoScore(line:str) -> int:
    winning_numbers_pattern = re.compile(r':\s*([\d\s]+)\s*\|')
    winning_numbers_match = re.findall(winning_numbers_pattern, line)
    #we use list comprehension here its a little janky
    #i still dont really get how list comprehension works but im trying it
    winning_numbers = [list(map(int, match.split())) for match in winning_numbers_match][0]
    print(winning_numbers)

    given_numbers_pattern = re.compile(r'\|\s*([\d\s]+)')
    given_numbers_match = re.findall(given_numbers_pattern, line)
    given_numbers = [list(map(int, match.split())) for match in given_numbers_match][0]
    print(given_numbers)

    #at this point we have the winning numbers and the given numbers in separate arrays
    score = 0
    for num in given_numbers:
        if num in winning_numbers:
            if score == 0:
                score += 1
            else:
                score *= 2
    return score
    

file_path = "data/day4-1.txt"
total_score = 0

#boilerplate code to open a file, with some error handling
try:
    with open(file_path, 'r') as file:
        #read each line
        for line in file:
            total_score += getLottoScore(line)

    print(f'Total sum: {total_score}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

#correct answer: 25651