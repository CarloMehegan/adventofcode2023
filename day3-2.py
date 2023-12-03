import re #regex

'''
ok this one sucks
find all asterisk symbols with exactly two numbers adjacent to them
and then multiply the values of the two numbers together
and sum all of these values

how do i count how many numbers are adjacent to each asterisk?
- i do the 2d search
- all numbers are at most 3 digits long, so all numbers adjacent to the asterisk
will definitely be within the -3,-1 and 3, 1 box centered around the asterisk
- if i find a digit, ill search 2 to the left and 2 to the right of it to find the full digit
- how do i make sure that i dont count the same number twice?
- do i need to create a 3x7 array to store all the numbers i find, then check how many there are?

could work
- iterate through all asterisks
- create a array of length 3 with a 7-long string of dots in each index
- look for adjacent digits and add them to the array
- every time we find one of these digits, check to the left for another number, if we find, add to array and check again
- do the same by going to the right
- once we have looked at all adjacent positions, go thru the array and count the number of numbers
- doing it this way makes it so repeated numbers dont count multiple times, they only show up in the array once
- if theres two numbers then we multiply and return
also we cant just count how many numbers are within the 3x7 around the asterisk bc there might be extras
'''

def determineNumberValidity(match, row_number) -> int:
    #parse the regex match
    asterisk_position = match.start()

    pattern = re.compile(r'\d') #look for numbers

    #all numbers will be within this range
    #we will fill in numbers as we find them
    #then count them up at the end
    search_array = [
        ".......",
        "...*...",
        "......."
    ]

    #2D search adjacent cells
    for y in range(-1,2):
        for x in range(-1,2):
            try:
                #relative x and y here are for the search_array
                relative_y = y + 1
                relative_x = x + 3
                center = lines[row_number + y][asterisk_position + x]
                print("center is", center)
                if pattern.match(center):
                    search_array[relative_y] = search_array[relative_y][:relative_x] + center + search_array[relative_y][relative_x+1:]
                    #add this to the array, then check the left
                    left_1 = lines[row_number + y][asterisk_position + x - 1]
                    if pattern.match(left_1):
                        search_array[relative_y] = search_array[relative_y][:relative_x-1] + left_1 + search_array[relative_y][relative_x+1-1:]
                        #add and then check the next left which could be the hundreds place
                        left_2 = lines[row_number + y][asterisk_position + x - 2]
                        if pattern.match(left_2):
                            search_array[relative_y] = search_array[relative_y][:relative_x-2] + left_2 + search_array[relative_y][relative_x+1-2:]
                    
                    #now lets check the right as well
                    right_1 = lines[row_number + y][asterisk_position + x + 1]
                    if pattern.match(right_1):
                        search_array[relative_y] = search_array[relative_y][:relative_x+1] + right_1 + search_array[relative_y][relative_x+1+1:]
                        #add and then check the next left which could be the hundreds place
                        right_2 = lines[row_number + y][asterisk_position + x + 2]
                        if pattern.match(right_2):
                            search_array[relative_y] = search_array[relative_y][:relative_x+2] + right_2 + search_array[relative_y][relative_x+1+2:]

                #wow this is ugly
                #WOW thats ugly
                #but it worked
                
            except IndexError as e:
                print("caught an index error at", row_number + y, asterisk_position + x)
                pass
    
    
    #ok now we should have all the adjacent numbers contained inside of search_array
    #lets iterate through each line and match all the numbers
    num_matches = 0
    gear_ratio = 1
    for line in search_array:
        pattern = re.compile(r'(\d+)') #regex captures each number
        matches = pattern.finditer(line) #gives each match as a match object
        for match in matches:
            num_matches += 1
            gear_ratio *= int(match.group())

    if num_matches == 2:
        print("found a gear with gear ratio", gear_ratio)
        return gear_ratio
    else:
        print("not a valid gear, has", num_matches, "adjacent numbers")
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
            #slightly more complicated regex use today, using matches
            pattern = re.compile(r'\*')
            matches = pattern.finditer(line) #gives each match as a match object
            for match in matches:
                part_numbers_sum += determineNumberValidity(match, i)

    print(f'Total sum: {part_numbers_sum}')

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

#correct answer: 76504829