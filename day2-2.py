import re #regex

def determineColorMaxes(line:str) -> int:
    color_maxes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    #use regex to get all the pairs of color and number
    pairs = re.findall(r'(\d* red|\d* green|\d* blue)', line)

    #go through the list and replace any words with their corresponding number
    for i in range(len(pairs)):
        number, color = pairs[i].split(" ")
        
        if int(number) > color_maxes[color]:
            #update new max for that color
            color_maxes[color] = int(number)
    
    #return the "power" (all color maxes multiplied together)
    return color_maxes["red"] * color_maxes["green"] * color_maxes["blue"]


file_path = "data/day2-1.txt"
power_sum = 0

#boilerplate code to open a file, with some error handling
try:
    with open(file_path, 'r') as file:
        #read each line
        for line in file:
            power_sum += determineColorMaxes(line)

    print(f'Total sum: {power_sum}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

#correct answer: 71585