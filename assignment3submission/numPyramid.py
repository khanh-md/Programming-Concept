# Driver: Khanh Dong U14837275
# Navigator: Peter Abdulmasih U65094253
# This program creates a "number pyramid" by incrementing each new line (the number of lines are inputted at the beginning) with a growing
# list of numbers, each decreasing towards the middle and increasing towards the outside.

numLines = int(input("Enter the number of lines (must be between 1 and 9): "))                  # Asks user for the number of lines.
temp = 1
rightInc = 2
leftInc = 1
numberLine = 2
if 1 <= numLines <= 9:                                                                          # If the user inputs a value greater than or equal to 1 and less than or equal to 9.
    print("")                                                                                   # Prints a blank line, so that the program reads the if statement condition.

else:                                                                                           # Otherwise...
    while numLines < 1 or numLines > 9:                                                         # While the user inputs a value less than 1 or greater than 9
        numLines = int(input("Enter the number of lines (must be between 1 and 9): "))          # Takes input again.

for row in range(0, numLines):
    space = numLines - row         # Number of space is 1 less than number of lines
    for spaces in range(1, space): # Add space at the beginning and decreased each row
        print(end = " ")

    for x in range (0, temp): # Go to 1
        print(leftInc, end = "")
        leftInc = leftInc - 1

    for y in range (0, temp-1): # Right side start from 2
        if temp >= 2:
            print(rightInc, end = "")
            rightInc = rightInc + 1
    temp = temp + 1
    rightInc = 2
    leftInc = numberLine
    numberLine = numberLine + 1
    print('') # Go to a new row

