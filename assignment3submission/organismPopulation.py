# Exercise 3

# Driver: U65094253 Peter Abdulmasih
# Navigator: U14837275 Khanh Dong

# The purpose of this program is to predict the approximate size of a population of organisms, by taking
# user input for the percentage increase and the period of time by which the number (also taken in input)
# increases by the percentage increase.

numberOfOrganisms = 0                                                                                                        # Stores the number of organisms that will be inputted by the user.
popIncrease = .0                                                                                                             # Stores the population increase that will be inputted later.
numDays = 0                                                                                                                  # Stores the number of days (period)
numDays2 = 1                                                                                                                 # Used to display each day's number in the for loop.

numberOfOrganisms = int(input("Starting number of organisms: "))                                                             # Takes the number of organisms from the user.

if(numberOfOrganisms >= 1):                                                                                                  # If the user inputs a value greater than or equal to 1

    print("")                                                                                                                # Prints a blank line, so that the program reads the if statement condition.

else:                                                                                                                        # Otherwise...

    while(numberOfOrganisms < 1):                                                                                            # While the user inputs a value less than 1...
        numberOfOrganisms = int(input("Starting number of organisms: "))                                                     # Takes input again.

popIncrease = int(input("Average daily increase (as a %): "))                                                                # Takes the population increase as a percentage.

if(popIncrease >= 1):                                                                                                        # If the user inputs a value greater than or equal to 1

    print("")                                                                                                                # Prints a blank line, so that the program reads the if statement condition.

else:                                                                                                                        # Otherwise...

    while(popIncrease < 1):                                                                                                  # While the user inputs a value less than 1...
        popIncrease = int(input("Average daily increase (as a %): "))                                                        # Takes input again.
popIncrease = popIncrease / 100                                                                                              # Turns whole percent into a decimal for calculation.

numDays = int(input("Number of days to multiply: "))                                                                         # Takes the number of days from the user

if(numDays >= 1):                                                                                                            # If the user inputs a value greater than or equal to 1

    print("")                                                                                                                # Prints a blank line, so that the program reads the if statement condition.

else:                                                                                                                        # Otherwise...

    while(numDays < 1):                                                                                                      # If the user inputs a value greater than 1.
        numDays = int(input("Number of days to multiply: "))                                                                 # Takes input again.

print("Day                                 Population")                                                                      # Prints headers
print("----------------------------------------------")                                                                      # Prints headers

for x in range(1, numDays+1):                                                                                                # Runs loop from 1 --> one more than the number of days
    print(numDays2, "                                       ",format((numberOfOrganisms), ".6f"))                            # Prints the current day (out of the total range), and formats the number of organisms printed to 6 decimal places.
    numDays2 = numDays2 + 1                                                                                                  # Increments the current day
    numberOfOrganisms = numberOfOrganisms * (popIncrease+1)                                                                  # Takes the number of organisms and multiplies it by the percentage increase.