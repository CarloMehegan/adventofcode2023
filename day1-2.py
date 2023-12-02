import re #regex

file_path = "data/day1-1.txt"
total_sum = 0

#use a dict because its a hash table and thats fast right
words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def getCalibrationValue(line:str) -> int:
    #use regex to get all digits or written out numbers
    #use "positive lookahead" to allow overlaps like "twone" to count as diff
    digits = re.findall(r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))', line)

    #go through the list and replace any words with their corresponding number
    for i in range(len(digits)):
        if digits[i] in words:
            digits[i] = words[digits[i]]

    tens_place = int(digits[0])
    ones_place = int(digits[len(digits) - 1])

    calibration_value = (tens_place * 10) + ones_place
    return calibration_value


#boilerplate code to open a file, with some error handling
try:
    with open(file_path, 'r') as file:
        #read each line
        for line in file:
            number = getCalibrationValue(line)
            total_sum += number

    print(f'Total sum: {total_sum}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")


#correct answer: 53855