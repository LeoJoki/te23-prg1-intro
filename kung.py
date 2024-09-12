from random import randint

play_game = True

p1_wins = 0
p2_wins = 0

dice_one = """            _____________
            |           |
            |           |
            |     *     |
            |           |
            |___________|"""

dice_two = """            _____________
            |           |
            |     *     |
            |           |
            |     *     |
            |___________|"""

dice_three = """            _____________
            |           |
            |   *       |
            |     *     |
            |       *   |
            |___________|"""

dice_four = """            _____________
            |           |
            |   *   *   |
            |           |
            |   *   *   |
            |___________|"""

dice_five = """            _____________
            |           |
            |   *   *   |
            |     *     |
            |   *   *   |
            |___________|"""

dice_six = """            _____________
            |           |
            |   *   *   |
            |   *   *   |
            |   *   *   |
            |___________|"""

while play_game:
    input("spelare ETT tryck på enter för att rulla tärningen")
    p1_roll = randint(1, 6)
    if p1_roll == 1:
        print(f"{dice_one}")
    if p1_roll == 2:
        print(f"{dice_two}")
    if p1_roll == 3:
        print(f"{dice_three}")
    if p1_roll == 4:
        print(f"{dice_four}")
    if p1_roll == 5:
        print(f"{dice_five}")
    if p1_roll == 6:
        print(f"{dice_six}")
    print(f"spelare ETT fick en {p1_roll}a")

    input("spelare TVÅ tryck på enter för att rulla tärningen")
    p2_roll = randint(1, 6)
    if p2_roll == 1:
        print(f"{dice_one}")
    if p2_roll == 2:
        print(f"{dice_two}")
    if p2_roll == 3:
        print(f"{dice_three}")
    if p2_roll == 4:
        print(f"{dice_four}")
    if p2_roll == 5:
        print(f"{dice_five}")
    if p2_roll == 6:
        print(f"{dice_six}")
    print(f"spelare TVÅ fick en {p2_roll}a")

    if p1_roll > p2_roll:
        print(f"spelare ETT vinner med slaget {p1_roll}")
        p1_wins += 1
    elif p2_roll > p1_roll:
        print(f"spelare TVÅ vinner med slaget {p2_roll}")
        p2_wins += 1
    else:
        print(f"båda spelare fick lika, spela igen")
    
    if p1_wins == 3:
        play_game = False
        print("spelare ETT har vunnit spelet!")
    elif p2_wins == 3:
        play_game = False
        print("spelare TVÅ har vunnit spelet!")



#_____________
#|           |
#|           |
#|     *     |
#|           |
#|___________|

#_____________
#|           |
#|     *     |
#|           |
#|     *     |
#|___________|

#_____________
#|           |
#|   *       |
#|     *     |
#|       *   |
#|___________|

#_____________
#|           |
#|   *   *   |
#|           |
#|   *   *   |
#|___________|

#_____________
#|           |
#|   *   *   |
#|     *     |
#|   *   *   |
#|___________|

#_____________
#|           |
#|   *   *   |
#|   *   *   |
#|   *   *   |
#|___________|