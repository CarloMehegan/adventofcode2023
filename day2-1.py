import re #regex

file_path = "data/day2-1.txt"
valid_games = 0

color_maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

red_max = 0
green_max = 0
blue_max = 0

def determineGameValidity(line:str) -> int:
    #use regex to get all the pairs of color and number
    pairs = re.findall(r'(\d* red|\d* green|\d* blue)', line)

    #go through the list and replace any words with their corresponding number
    for i in range(len(pairs)):
        number, color = pairs[i].split(" ")
        
        if int(number) > color_maxes[color]: #if larger than max, then invalid game
            print("INVALID BECAUSE number is", number, "color is", color)
            return 0
        
    return 1


#boilerplate code to open a file, with some error handling
try:
    with open(file_path, 'r') as file:
        #read each line
        i = 0
        for line in file:
            i += 1
            if determineGameValidity(line):
                valid_games += i

    print(f'Total sum: {valid_games}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

#correct answer: 2331