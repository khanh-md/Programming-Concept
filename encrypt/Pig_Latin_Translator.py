# Programming pair: Elizabeth Franklin (U67587808) and Khanh Dong (U14837275)
# Driver: Elizabeth Franklin
# Navigator: Khanh Dong
# Description: This file accepts a text file from the user and converts each word to pig latin.
# The translation is written to a new text file.

def translate_file():
    in1 = open(input('Please enter the name of the source file: '), 'r')
    contents = in1.read()
    in1.close()
    translated_string = ''
    for word in contents.split():
        if len(word) == 1:
            new_word = word + 'ay '
            translated_string += new_word
        else:
            new_word = word[1:] + word[0] + 'ay '
            translated_string += new_word
    return translated_string.lower()


output_name = input('Please enter your desired name for the new file: ')
out1 = open(output_name, 'w')
out1.write(translate_file())
out1.close()


