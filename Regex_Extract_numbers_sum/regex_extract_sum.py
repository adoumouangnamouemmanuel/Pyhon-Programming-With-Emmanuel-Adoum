import re

#user input the file name
fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "./Regex_Extract_numbers_sum/data_regex.txt"

#open the file
file_handle = open(fname)

#extract the numbers and compute the sum
sum = 0
for line in file_handle:
    line = line.strip()
    numbers = re.findall("([0-9]+)", line)
    for number in numbers:
        sum += int(number)

print("The sum of these numbers is: ", sum)