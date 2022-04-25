# Driver: Khanh Dong U14837275
# Navigator: Peter Abdulmasih U65094253
# The program allows player to have 10 guesses to find the correct number between 1-100

import random
point = 1    # Count the number of guesses
correct_num = random.randint(1, 100)

user = int(input("Guess a number between 1 and 100 (inclusive): "))
while user < 1 or user > 100:
    point += 1
    user = int(input("Very funny. Enter a number between 1 and 100 (inclusive): "))


while point <= 10:
    if user < correct_num:     # For when the guess is lower
        point += 1
        user = int(input("Too low. Enter another guess: "))
        while user < 1 or user > 100:
            point += 1
            user = int(input("Very funny. Enter a number between 1 and 100 (inclusive): "))
    if user > correct_num:     # For when the guess is higher
        point += 1
        user = int(input("Too high. Enter another guess: "))
        while user < 1 or user > 100:
            point += 1
            user = int(input("Very funny. Enter a number between 1 and 100 (inclusive): "))
    else:
        break

if user == correct_num: # Determine the outcome after the loop ends
    print("You guessed it right!! You got it in {:.0f} guesses!".format(point))
else:
    print("Sorry, the number was {:.0f}".format(correct_num))


