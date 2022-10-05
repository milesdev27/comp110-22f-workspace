"""A choose your own adventure game, Horton style!"""


__author__ = "730615836"


from unittest.mock import NonCallableMagicMock


points: int = 0
player: str = ""
floor: int = 1
turn: int = 1


def main() -> None:
    """Entrypoint to the function!"""
    greet()
    global turn
    global points
    while turn <= 10:
        print(f"Turn {turn}!")
        print("Enter 1 to travel up a floor")
        print("Enter 2 to travel down a floor")
        print("Enter 3 to stay on the same floor")
        print("Enter 4 to exit the game")
        print(choice(input("What is your choice? ")))
        turn_action()
        print(f"You now have {points} points")
        turn += 1
    print(f"You finished the game with {points} points")
    if points > 250:
        print("You have met great people at Horton! You win!!!")
    else:
        print("You have lost the game... Goodbye.")

    
    

    
def greet() -> None:
    """Introduction of the game!"""
    global player
    player += input("What is your name? ")
    print(f"Hello, {player}!")
    print("This game takes place in Horton Hall.")
    print("Your starting point is the first floor.")
    print("You will either go up a floor, down a floor, or stay on the same floor.")
    print("Horton has floors 0, 1, 2, 3, and 4. If you try to go above or below the designated floors you will die.")
    print("Each floor has 10 rooms numbered 11-20, and you will choose to enter one of those rooms")
    print("Your choices will affect the outcome of the game")
    print("The goal of the game is to accumulate as many points as possible by meeting new people in Horton. ;)")


def choice(a: str) -> str:
    """Up or down a floor, or stay on the same floor!"""
    a = int(a)
    global floor
    global points
    statement: str = ""
    if a == 1:
        statement += "You have moved up 1 floor"
        floor += 1
    if a == 2:
        statement += "You have moved down 1 floor"
        floor -= 1
    if a == 3:
        statement += "You have stayed on the same floor"
    if a == 4:
        print(f"You have ended the game with {points} points.")
        quit()
    if a < 0:
        print("You have dug underground and suffocated!")
        print(f"Your game has ended. You finished with {points} points.")
        quit()
    if a > 4:
        print("You have been eaten by killer birds!")
        print(f"Your game has ended. You finished with {points} points.")
        quit()
    return statement


def turn_action() -> None:
    """The action of a turn!"""
    global turn
    global floor
    global points
    print(f"You are on floor {floor}")
    if floor == int(0):
        floor_0()
    if floor == int(1):
        floor_1()
    if floor == int(2):
        floor_2()
    if floor == int(3):
        floor_3()
    if floor == int(4):
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
    print("You will now enter a room.")
    room: int = input("Enter a room between 11 and 20: ")
    global points
    if int(room) < 11:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) > 20:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) == 11:
        global a_0
        if a_0 == 0:
            points += 4
            a_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 12:
        global b_0
        if b_0 == 0:
            points += 93
            b_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 13:
        global c_0
        if c_0 == 0:
            points += 1
            c_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 14:
        global d_0
        if d_0 == 0:
            points += 23
            d_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 15:
        global e_0
        if e_0 == 0:
            points += 52
            e_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 16:
        global f_0
        if f_0 == 0:
            points += -30
            f_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 17:
        global g_0
        if g_0 == 0:
            points += 17
            g_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 18:
        global h_0
        if h_0 == 0:
            points += 9
            h_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 19:
        global i_0
        if i_0 == 0:
            points += 41
            i_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")
    if int(room) == 20:
        global j_0
        if j_0 == 0:
            points += 78
            j_0 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 11 and 20: ")

 
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
    print("You will now enter a room.")
    room: int = input("Enter a room between 111 and 120: ")
    global points
    if int(room) < 111:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) > 120:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) == 111:
        global a_1
        if a_1 == 0:
            points += 62
            a_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 112:
        global b_1
        if b_1 == 0:
            points += 1000
            b_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 113:
        global c_1
        if c_1 == 0:
            points += -43
            c_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 114:
        global d_1
        if d_1 == 0:
            points += 1500
            d_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 115:
        global e_1
        if e_1 == 0:
            points += -100
            e_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 116:
        global f_1
        if f_1 == 0:
            points += 33
            f_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 117:
        global g_1
        if g_1 == 0:
            points += 8
            g_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 118:
        global h_1
        if h_1 == 0:
            points += 0
            h_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 119:
        global i_1
        if i_1 == 0:
            points += 42
            i_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")
    if int(room) == 120:
        global j_1
        if j_1 == 0:
            points += -33
            j_1 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 111 and 120: ")


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
    room: int = input("Enter a room between 211 and 220: ")
    global points
    if int(room) < 211:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) > 220:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) == 211:
        global a_2
        if a_2 == 0:
            points += 2
            a_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 212:
        global b_2
        if b_2 == 0:
            points += -500
            b_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 213:
        global c_2
        if c_2 == 0:
            points += 7
            c_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 214:
        global d_2
        if d_2 == 0:
            points += -1000
            d_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 215:
        global e_2
        if e_2 == 0:
            points += 5
            e_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 216:
        global f_2
        if f_2 == 0:
            points += 4
            f_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 217:
        global g_2
        if g_2 == 0:
            points += -1
            g_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 218:
        global h_2
        if h_2 == 0:
            points += 8
            h_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 219:
        global i_2
        if i_2 == 0:
            points += 4
            i_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")
    if int(room) == 220:
        global j_2
        if j_2 == 0:
            points += -4
            j_2 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 211 and 220: ")


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
    """Floor 3"""
    room: int = input("Enter a room between 311 and 320: ")
    global points
    if int(room) < 311:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) > 320:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) == 311:
        global a_3
        if a_3 == 0:
            points += 7
            a_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 312:
        global b_3
        if b_3 == 0:
            points += 33
            b_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 313:
        global c_3
        if c_3 == 0:
            points += 27
            c_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 314:
        global d_3
        if d_3 == 0:
            points += -40
            d_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 315:
        global e_3
        if e_3 == 0:
            points += 72
            e_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 316:
        global f_3
        if f_3 == 0:
            points += -50
            f_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 317:
        global g_3
        if g_3 == 0:
            points += 22
            g_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 318:
        global h_3
        if h_3 == 0:
            points += 18
            h_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 319:
        global i_3
        if i_3 == 0:
            points += 19
            i_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")
    if int(room) == 320:
        global j_3
        if j_3 == 0:
            points += 34
            j_3 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 311 and 320: ")


a_4: int = 0
b_4: int = 0
c_4: int = 0
d_4: int = 0
e_4: int = 0
f_4: int = 0
g_4: int = 0
h_4: int = 0
i_4: int = 0
j_4: int = 0

def floor_4() -> None:
    """Floor 4"""
    room: int = input("Enter a number between 411 and 420: ")
    global points
    if int(room) < 411:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) > 420:
        room: int = input("That room number doesn't exist. Please enter a real room: ")
    if int(room) == 411:
        global a_4
        if a_4 == 0:
            points += -10
            a_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 412:
        global b_4
        if b_4 == 0:
            points += -9
            b_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 413:
        global c_4
        if c_4 == 0:
            points += -8
            c_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 414:
        global d_4
        if d_4 == 0:
            points += -7
            d_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 415:
        global e_4
        if e_4 == 0:
            points += -6
            e_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 416:
        global f_4
        if f_4 == 0:
            points += -5
            f_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 417:
        global g_4
        if g_4 == 0:
            points += -4
            g_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 418:
        global h_4
        if h_4 == 0:
            points += -3
            h_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 419:
        global i_4
        if i_4 == 0:
            points += -2
            i_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    if int(room) == 420:
        global j_4
        if j_4 == 0:
            points += -100
            j_4 += 1
        else:
            print("You have already entered this room, try again.")
            room: int = input("Enter a room between 411 and 420: ")
    

if __name__ == "__main__":
    main()