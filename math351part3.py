'''
This file processes the csv, then uses the data
to perform the hypothesis tests in part 3.
Most of this file is similar to file 2
'''

import re #use regular expressions to find commas

file_path = "data/occupancy.txt"
occupancy_dict = {}

#boilerplate code to open a file, with some error handling
with open(file_path, 'r') as file:
    #read each line
    for i, line in enumerate(file):
        row = line.split(",") #save the cells in each row as cells in a list
        row[3] = row[3].strip() #remove newline from the end of the row
        #print(row)

        date = row[1]
        occupancy = int(row[2])  # Convert occupancy to an integer
        time = row[3]

        #make sure data is already in dict
        if date not in occupancy_dict:
            occupancy_dict[date] = []
        
        occupancy_dict[date].append((time, occupancy))
        
#print a few example days to make sure it worked
print(occupancy_dict['8/24/2023'])
print("\n")
print(occupancy_dict['9/15/2023'])

#at this point we have the times stored in this table
#lets remove am/pm ambiguity

#go through each day in the dict
for day in occupancy_dict:
    print(day, occupancy_dict[day])

    is_it_afternoon_yet = False

    #go through each record in the day
    for i, occupancy_tuple in enumerate(occupancy_dict[day]):
        time, occupancy = occupancy_tuple
        # print("time is", time)
        hour, minute = time.split(":")
        hour = int(hour)

        #iterate until we find an afternoon time (1pm-5pm)
        #after we find one, then it continues to be afternoon til the end of the day
        is_it_afternoon_yet = \
            (hour == 1 or hour == 2 or hour == 3 or hour == 4 or hour == 5) \
            or (is_it_afternoon_yet == True)

        #if it is afternoon, we add 12 to the hour
        if is_it_afternoon_yet == True:
            #use mod 24 to make sure midnight becomes 0:00
            hour = (hour + 12) % 24

        #reconstruct time
        updated_time = str(hour) + ":" + str(minute)
        
        if is_it_afternoon_yet == True:
            print("updated a time:", day, time, "at", i, "became", updated_time)
        else:
            print("kept a time:", day, time, "at", i, "stayed", updated_time)
        occupancy_dict[day][i] = (updated_time, occupancy)
        



#so we have a updated occupancy dict
#now we want to go through the data and filter just the ones before 4:01pm (before 16:01)
#and then lets print a list of those occupancies, comma separated
#go through each day in the dict
first_half_recordings = []
second_half_recordings = []

#list containing 7 lists
#days[0] = monday, days[6] = sunday
days_of_the_week = [0 for _ in range(7)]

days_of_the_week[0] = []
days_of_the_week[1] = []
days_of_the_week[2] = []
days_of_the_week[3] = []
days_of_the_week[4] = []
days_of_the_week[5] = []
days_of_the_week[6] = []

day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


from datetime import datetime
#also we need the days of the week again and i forgot about them
#but its ok we have the dates themselves so we can get the day from that

for day in occupancy_dict:
    print(day, occupancy_dict[day])

    #go through each record in the day
    for i, occupancy_tuple in enumerate(occupancy_dict[day]):
        time, occupancy = occupancy_tuple
        # print("time is", time)
        hour, minute = time.split(":")

        #get day of the week
        #monday is 0, sunday is 6
        #weekdays is 0-4
        date_object = datetime.strptime(day, "%m/%d/%Y")
        day_of_the_week = date_object.weekday()

        days_of_the_week[day_of_the_week].append(int(occupancy))

        if day_of_the_week >= 0 and day_of_the_week <= 4:
            if int(hour) > 8 and int(hour) < 16: #between 9:00am and 3:59pm
                first_half_recordings.append(int(occupancy))
            elif int(hour) >= 16 and int(hour) <= 21: #between 4:00pm and 9:59pm
                second_half_recordings.append(int(occupancy))
                #fridays open til midnight, but not counting that
            
print("first half of the day:", first_half_recordings)
print("second half of the day:", second_half_recordings)

from statistics import mean, variance, stdev
print("first half of the day\nn =", len(first_half_recordings))
print("mean =", mean(first_half_recordings))
print("stdev =", stdev(first_half_recordings))
print("variance =", variance(first_half_recordings))

print("second half of the day\nn =", len(second_half_recordings))
print("mean =", mean(second_half_recordings))
print("stdev =", stdev(second_half_recordings))
print("variance =", variance(second_half_recordings))

for i in range(7):
    print("\n" + day_names[i])
    print(days_of_the_week[i])
    print("n =", len(days_of_the_week[i]))
    print("mean =", mean(days_of_the_week[i]))
    print("stdev =", stdev(days_of_the_week[i]))
    print("variance =", variance(days_of_the_week[i]))


print("\n")

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#redoing the tests for part 2 but with scipy ====================================

# Perform independent samples t-test
t_statistic, p_value = stats.ttest_ind(first_half_recordings, second_half_recordings)
# Print the results
print("T-statistic:", t_statistic)
print("P-value:", p_value)
# Check if the difference is statistically significant
if p_value < 0.05:
    print("The difference is statistically significant.")
else:
    print("The difference is not statistically significant.")
# Perform Bartlett's test for equal variances
statistic, p_value = stats.bartlett(first_half_recordings, second_half_recordings)
# Print the results
print("Test Statistic:", statistic)
print("P-value:", p_value)
# Check if the difference in variances is statistically significant
if p_value < 0.05:
    print("The difference in variances is statistically significant.")
else:
    print("The difference in variances is not statistically significant.")




# tests for part 3 =================================================

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
p_value_matrix = np.ones((len(days), len(days)))

for i in range(7):
    for j in range(7):
        if i < j: #avoid redundant tests

            t_statistic, p_value = stats.bartlett(days_of_the_week[i], days_of_the_week[j])
            p_value_matrix[i, j] = 0.025
            p_value_matrix[j, i] = p_value  #since the test is symmetric, we fill both sides
            
        elif i == j:
            p_value_matrix[i, j] = 0.025


# Visualize the p-value matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(p_value_matrix, annot=True, fmt=".4f", xticklabels=days, yticklabels=days, cmap="coolwarm", vmin=0, vmax=0.05)
plt.title("P-value Matrix: Two-sample Variance Test")
plt.show()


