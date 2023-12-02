import re #regex

file_path = "data/day1-1.txt"
total_sum = 0

def getCalibrationValue(line:str) -> int:
    #use regex to get a list of every digit 0-9 in the string
    digits = re.findall(r'\d', line)

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


#correct answer: 54634