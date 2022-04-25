# Assignment 5
# Driver - Khanh Dong - U14837275
# Navigator - Ameena Mohammed - U39296299

# The program ask for the numbers and the limit, before comparing each number with the limit and return numbers that are below it.

def main():
    num_list = []
    num_loop = int(input("How many numbers will you compare? "))
    for x in range(num_loop):
        number = int(input("Enter a number: "))
        num_list.append(number)

    limit = int(input("What is the limit? "))
    less_limit(num_list, limit)


def less_limit(num_list, limit):
    below_limit = []
    for number in num_list:
        if number < limit:
            below_limit.append(number)
        else:
            continue
    if below_limit != []:
        print("{} are less than limit {}".format(below_limit, limit))
    else:
        print("There are no number below the limit {}".format(limit))

main()
