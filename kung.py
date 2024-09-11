from random import randint

play_game = True

p1_wins = 0
p2_wins = 0

while play_game:
    input("spelare ETT tryck på enter för att rulla tärningen")
    p1_roll = randint(1, 6)
    print(f"spelare ETT fick en {p1_roll}a")

    input("spelare TVÅ tryck på enter för att rulla tärningen")
    p2_roll = randint(1, 6)
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
