# Driver: Tess Zitouni (U95647951)
# Navigator: Khanh Dong (U14837275)
# The function ask 10 trivia questions to 2 players, then compare the scores together.


from question import Question
from trivia import Trivia

def main():
    player1 = 0
    player2 = 0
    turn = 0
    question_list = Trivia()
    for n in range(0,10):
        if turn == 0:
            print("Question for the first player")
        else:
            print("Question for the second player")
        print(question_list[n])

        user_choice = int(input('Enter your solution (a number between 1 and 4): '))
        while user_choice<1 or user_choice>4:
            user_choice = int(input('Invalid number. Please enter again (a number between 1 and 4):'))
            
        if user_choice == question_list[n].get_correct():
            print("This is the correct answer.\n")
            if turn == 0:
                player1 += 1
            elif turn == 1:
                player2 += 1

        if user_choice != question_list[n].get_correct():
            print("That is incorrect. The correct answer is {}.\n".format(question_list[n].get_correct()))

    # alternates turns
        if turn == 0:
            turn = 1
        elif turn == 1:
            turn = 0

    print('The first player earned {} points.'.format(player1))
    print('The second player earned {} points.'.format(player2))
    if player1 > player2:
        print('The first player wins the game.')
    elif player1 < player2:
        print('The second player wins the game.')
    elif player1 == player2:
        print('It is a tie!')

main()

