# Driver: Tess Zitouni (U95647951)
# Navigator: Khanh Dong (U14837275)
# The function define each question as a class and put them all into a list.

from question import Question

def Trivia():
    question1 = Question("How many days are in a lunar year?", "354", "365", "243", "379", 1)
    question2 = Question("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2)
    question3 = Question("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", 4)
    question4 = Question("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3)
    question5 = Question("Which of these Winnie the Pooh characters is a donkey? ", "Pooh", "Eeyore", "Piglet", "Kanga", 2)
    question6 = Question("What is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", 4)
    question7 = Question("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", 1)
    question8 = Question("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", 3)
    question9 = Question("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", 2)
    question10 = Question("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", 4)


    question_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
    return question_list



