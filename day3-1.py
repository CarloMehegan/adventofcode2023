import re #regex

'''
this one is trickier!! but i think i got an idea
- we need to save each line in a array to make a 2d array
- then we regex find all of the numbers
- now we iterate through the numbers
    - we iterate through each digit
    - we look in all 8 adjacent spots for something that is NOT a number and NOT a period
    - yeahhh thats it thats how you do it
    - if we get through all digits of a number and dont find a symbol adjacent to any of
    them, then it is not counted to the total, return 0
'''

def determineNumberValidity(match, row_number) -> int:
    #parse the regex match
    start_position = match.start()
    end_position = match.end()
    match_text = match.group()
    #this gives us the range of digits and the full number

    #go through the number and check each digit for an adjacent symbol
    pattern = re.compile(r'[^\d.\n]') #not a digit or period or newline
    for i in range(start_position, end_position):
        #2D search
        for y in range(-1,2):
            for x in range(-1,2):
                try:
                    if pattern.match(lines[row_number + y][i + x]):
                        #if we find a symbol
                        return int(match_text) #we are done with this number, we can say its valid
                except IndexError as e:
                    print("caught an index error at", row_number + y, i + x)
                    pass
    
    #if we get to this point, we found no adjacent symbols
    print(match_text, "is not valid!")
    return 0


file_path = "data/day3-1.txt"
part_numbers_sum = 0
lines = []

#boilerplate code to open a file, with some error handling
try:
    with open(file_path, 'r') as file:
        #read each line
        for line in file:
            #add each line to a 2d array
            lines.append(line)
        
        #go through each line, and pass each number into our validity function
        i = -1
        for line in lines:
            i += 1
            pattern = re.compile(r'(\d+)') #slightly more complicated regex use today, using matches
            matches = pattern.finditer(line) #gives each match as a match object
            for match in matches:
                part_numbers_sum += determineNumberValidity(match, i)

    print(f'Total sum: {part_numbers_sum}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

#correct answer: 525119