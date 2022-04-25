#Driver - Khanh Dong (50%) U14837275
#Navigator - Adam Bricha (50%) U9233-5585

#This program simulates a race between a tortoise and a hare. The program randomizes postions for the tortoise and the
#hare. If the tortoise reaches postion 50 before the hare then it wins and vise versa. The program takes note of how long
#it takes to complete the race and prints it in the output.



import random

def turtle(pos_t):
    t = random.randint(1, 11)
    #pos_t=0
    if t < 6:
        pos_t += 3
    elif t < 8:
        pos_t -= 5
        if pos_t <= 0:
            pos_t = 1
    else:
        pos_t += 1
    return pos_t


def hare(pos_h):
    h = random.randint(1, 11)
    #pos_h=0
    if h < 3:
        pos_h += 0
    elif h < 5:
        pos_h += 7
    elif h < 6:
        pos_h -= 10
        if pos_h <= 0:
            pos_h = 1
    elif h < 9:
        pos_h += 1
    else:
        pos_h -= 2
        if pos_h <= 0:
            pos_h = 1
    return pos_h


def race():
    pt = 0
    ph = 0
    time = 0
    print("ON YOUR MARK... GET SET...")
    print("GO!!!!!")
    print("AND THEY'RE OFF!")
    print('')
    for time in range(50):
        pt += turtle(0)
        ph += hare(0)
        lists = " " * 50
        race_track = list(lists)
        time += 1
        if ph > 48 or pt > 48:
            break
        else:
            race_track[ph] = "H"
            race_track[pt] = "T"
            if ph == pt:
                race_track[ph] = "OW"
                new_track = "".join(race_track)
                print(new_track)

                continue
            else:
                new_track = "".join(race_track)
                print(new_track)

    if pt >= ph:
        print("Tortoise wins!!")
    else:
        print('Hare wins. Yay!')
    print("Time of Race:", time, "seconds")


race()
