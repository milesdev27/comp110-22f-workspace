"""A choose your own adventure game, Horton style!"""


__author__ = "730615836"


points: int = 0
player: str = ""
floor: int = 1
turn: int = 1
SMILEY_FACE: str = "\U0001F601"
WINKY_FACE: str = "\U0001F609"
HEART_FACE: str = "\U0001F970"
STAR_STRUCK: str = "\U0001F929"
SMIRK: str = "\U0001F60F"
VOMIT: str = "\U0001F92E"
HOUSE: str = "\U0001F3E0"
UP_ARROW: str = "\U00002B06"
DOWN_ARROW: str = "\U00002B07"
DEAD: str = "\U00002620"
DANCER: str = "\U0001F57A"
RED_X: str = "\U0000274C"


def main() -> None:
    """Entrypoint to the function!"""
    greet()
    global turn
    global points
    while turn <= 10:
        print(f"Turn {turn}!")
        print(f"You are on floor {floor}.")
        print("Enter 1 to travel up a floor " + UP_ARROW)
        print("Enter 2 to travel down a floor " + DOWN_ARROW)
        print("Enter 3 to stay on the same floor")
        print("Enter 4 to exit the game")
        print(choice())
        turn_action()
        print(f"You now have {points} points! " + HEART_FACE)
        turn += 1
    print(f"You finished the game with {points} points!!")
    if points > 250:
        print("You have met great people at Horton! You win!!! " + STAR_STRUCK)
    else:
        print("You have lost the game... Goodbye." + VOMIT)
    print("Would you like to play again?")
    print("Enter 1 for yes or 2 for no.")
    play_again: int = int(input())
    if 1 < play_again < 2:
        play_again = input("Enter either 1 or 2: ")
    elif play_again == 1:
        main()
    else:
        exit()


def greet() -> None:
    """Introduction of the game!"""
    global player
    player += input("What is your name? ")
    print(f"Hello, {player}! " + SMILEY_FACE)
    print("This game takes place in Horton Hall. " + HOUSE)
    print("Your starting point is the first floor.")
    print("You will either go up a floor, down a floor, or stay on the same floor.")
    print("Horton has floors 0, 1, 2, 3, and 4. If you try to go above or below the designated floors you will die. " + SMIRK)
    print("Each floor has 10 rooms numbered 11-20, and you will choose to enter one of those rooms and gain a certain amount of points!")
    print("Since the goal is to meet new people, you cannot enter the same room twice!" + RED_X)
    print("The goal of the game is to accumulate 250 points by meeting people. " + WINKY_FACE + WINKY_FACE + WINKY_FACE + WINKY_FACE + WINKY_FACE)


def choice() -> str:
    """Up or down a floor, or stay on the same floor!"""
    global floor
    global points
    a: int = int(input("What is your choice? "))
    statement: str = ""
    if a == 1:
        statement += "You have moved up 1 floor" + UP_ARROW
        floor += 1
    if a == 2:
        statement += "You have moved down 1 floor" + DOWN_ARROW
        floor -= 1
    if a == 3:
        statement += "You have stayed on the same floor"
    if a == 4:
        print(f"You have ended the game with {points} points.")
        quit()
    if a < 0:
        print("You have dug underground and suffocated!" + DEAD)
        print(f"Your game has ended. You finished with {points} points.")
        quit()
    if a > 4:
        print("You have been eaten by killer birds on the roof!" + DEAD)
        print(f"Your game has ended. You finished with {points} points.")
        quit()
    return statement


def turn_action() -> None:
    """The action of a turn!"""
    global turn
    global floor
    global points
    print(f"You are on floor {floor}! " + SMILEY_FACE)
    if floor == 0:
        floor_0()
    if floor == 1:
        floor_1()
    if floor == 2:
        floor_2()
    if floor == 3:
        floor_3()
    if floor == 4:
        floor_4()


a_0: int = 0
b_0: int = 0
c_0: int = 0
d_0: int = 0
e_0: int = 0
f_0: int = 0
g_0: int = 0
h_0: int = 0
i_0: int = 0
j_0: int = 0


def floor_0() -> None:
    """Floor 0!"""
    global points
    global a_0
    global b_0
    global c_0
    global d_0
    global e_0
    global f_0
    global g_0
    global h_0
    global i_0
    global j_0
    print("You will now enter a room.")
    room: int = int(input("Enter a room between 11 and 20: "))
    if room < 11:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room > 20:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room == 11:
        if a_0 == 0:
            points += 4
            a_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 12:
        if b_0 == 0:
            points += 93
            b_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 13:
        if c_0 == 0:
            points += 1
            c_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 14:
        if d_0 == 0:
            points += 23
            d_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 15:
        if e_0 == 0:
            points += 52
            e_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 16:
        if f_0 == 0:
            points += -30
            f_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 17:
        if g_0 == 0:
            points += 17
            g_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 18:
        if h_0 == 0:
            points += 9
            h_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 19:
        if i_0 == 0:
            points += 41
            i_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))
    if room == 20:
        if j_0 == 0:
            points += 78
            j_0 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 11 and 20: "))

 
a_1: int = 0
b_1: int = 0
c_1: int = 0
d_1: int = 0
e_1: int = 0
f_1: int = 0
g_1: int = 0
h_1: int = 0
i_1: int = 0
j_1: int = 0


def floor_1() -> None:
    """Floor 1!"""
    global points
    global a_1
    global b_1
    global c_1
    global d_1
    global e_1
    global f_1
    global g_1
    global h_1
    global i_1
    global j_1
    print("Floor 1 is the best floor in Horton. There may be a jackpot room, so choose carefully! " + SMILEY_FACE)
    print("You will now enter a room.")
    room: int = int(input("Enter a room between 111 and 120: "))
    if room < 111:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room > 120:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room == 111:
        if a_1 == 0:
            points += 62
            a_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 112:
        if b_1 == 0:
            points += 1000
            b_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 113:
        if c_1 == 0:
            points += -43
            c_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 114:
        if d_1 == 0:
            print("JACKPOT!!!!! YOU HAVE ENTERED THE BEST ROOM ON CAMPUS!!! YOU MEET MILES, ELI AND ALL OF THEIR FRIENDS!!! TIME TO CELEBRATE!!! " + STAR_STRUCK + DANCER)
            points += 1500
            d_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 115:
        if e_1 == 0:
            points += -100
            e_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 116:
        if f_1 == 0:
            points += 33
            f_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 117:
        if g_1 == 0:
            points += 8
            g_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 118:
        if h_1 == 0:
            points += 0
            h_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 119:
        if i_1 == 0:
            points += 42
            i_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))
    if room == 120:
        if j_1 == 0:
            points += -33
            j_1 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 111 and 120: "))


a_2: int = 0
b_2: int = 0
c_2: int = 0
d_2: int = 0
e_2: int = 0
f_2: int = 0
g_2: int = 0
h_2: int = 0
i_2: int = 0
j_2: int = 0


def floor_2() -> None:
    """Floor 2!"""
    global points
    global a_2
    global b_2
    global c_2
    global d_2
    global e_2
    global f_2
    global g_2
    global h_2
    global i_2
    global j_2
    room: int = int(input("Enter a room between 211 and 220: "))
    if room < 211:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room > 220:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room == 211:
        if a_2 == 0:
            points += 2
            a_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 212:
        if b_2 == 0:
            points += -500
            b_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 213:
        if c_2 == 0:
            points += 7
            c_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 214:
        if d_2 == 0:
            points += -1000
            d_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 215:
        if e_2 == 0:
            points += 5
            e_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 216:
        if f_2 == 0:
            points += 4
            f_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 217:
        if g_2 == 0:
            points += -1
            g_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 218:
        if h_2 == 0:
            points += 8
            h_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 219:
        if i_2 == 0:
            points += 4
            i_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))
    if room == 220:
        if j_2 == 0:
            points += -4
            j_2 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 211 and 220: "))


a_3: int = 0
b_3: int = 0
c_3: int = 0
d_3: int = 0
e_3: int = 0
f_3: int = 0
g_3: int = 0
h_3: int = 0
i_3: int = 0
j_3: int = 0


def floor_3() -> None:
    """Floor 3!"""
    global points
    global a_3
    global b_3
    global c_3
    global d_3
    global e_3
    global f_3
    global g_3
    global h_3
    global i_3
    global j_3
    room: int = int(input("Enter a room between 311 and 320: "))
    global points
    if room < 311:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room > 320:
        room = int(input("That room number doesn't exist. Please enter a real room: "))
    if room == 311:
        if a_3 == 0:
            points += 7
            a_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 312:
        if b_3 == 0:
            points += 33
            b_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 313:
        if c_3 == 0:
            points += 27
            c_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 314:
        if d_3 == 0:
            points += -40
            d_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 315:
        if e_3 == 0:
            points += 72
            e_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 316:
        if f_3 == 0:
            points += -50
            f_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 317:
        if g_3 == 0:
            points += 22
            g_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 318:
        if h_3 == 0:
            points += 18
            h_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 319:
        if i_3 == 0:
            points += 19
            i_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))
    if room == 320:
        if j_3 == 0:
            points += 34
            j_3 += 1
        else:
            print("You have already entered this room, try again.")
            room = int(input("Enter a room between 311 and 320: "))


def floor_4() -> None:
    """Floor 4, the weird one!"""
    print("Floor 4 is magic, the rooms are randomized every turn. This means you never know what type of person you'll meet.")
    print("You could get lucky, meet someone great, and gain a lot of points. Or you could meet someone awful, catch a disease, and lose a lot of points.")
    print("Since this floor is randomized, you can enter the same room multiple times.")
    room: int = int(input("Enter a room between 411 and 420: "))
    global points
    import random
    if 410 < room < 421:
        points += random.randint(-500, 500)
    else:
        room = int(input("That room number doesn't exist. Please enter a real room: "))


if __name__ == "__main__":
    main()