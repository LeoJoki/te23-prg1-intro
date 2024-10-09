##Lägg till game mode där man möter bottar och levlar up efter fights för att se hur långt man kan komma

from random import randint
from colorama import Fore, Back, Style

input(f"""{Style.DIM + Fore.RED}
            ____________  ___  _    _ _     
      ______| ___ \ ___ \/ _ \| |  | | |______
 ____|      | |_/ / |_/ / /_\ \ |  | | |      \ 
     |______| ___ \    /|  _  | |/\| | |______/
            | |_/ / |\ \| | | \  /\  / |____
            \____/\_| \_\_| |_/\/  \/\_____/{Fore.RESET}""")


while True:
    main_menu = input(f"""{Fore.RESET}
    1: {Fore.BLUE}Single Player{Fore.RESET}
    2: {Fore.MAGENTA}Multiplayer{Fore.RESET}
    3: {Fore.GREEN}Regler och förklaringar{Fore.RESET}
    4: {Fore.RED}Stäng av{Fore.RESET}
    """)

    if main_menu == "3":
        print("""Förklaring av Singleplayer: 'Slåss mot rundor av fiender och levla upp för att bli starkare. Hur långt kan du komma?'
Förklaring av Multiplayer: 'Du och en vän väljer en klass och slåss mot varandra i en episk strid.'
Förklaring av Klass Förmågor: 'Alla klasser har en unik förmåga. I Single Player så kan du använda förmågan en gång per fight.
                               I Multiplayer så kommer klass förmågor tillbaks varranan runda'""")

    if main_menu == "4":
        break

    if main_menu == "1":
        print("Single Player är WiP")
        p1_name = input(Fore.RESET + "Spelare 1, vad är ditt namn?: ")

        while True:
            p1_class_choice = input(f"""{p1_name}, välj en klass:
                1:{Fore.RED} Krigare, Förmåga: Gör 1d4 extra skada{Fore.RESET}
                2:{Fore.BLUE} Helare, Förmåga: Gör att båda spelare ignorerar rundans skada{Fore.RESET}
                3:{Fore.MAGENTA} Tjuv, Förmåga: Byt plats på tärningskasten{Fore.RESET}
                4:{Fore.YELLOW} Gambler, Förmåga: 1/10 chans att antingen direkt vinna eller förlora{Fore.RESET}
                """)
            if p1_class_choice == "1":
                p1_class = "Krigare"
                break
            elif p1_class_choice == "2":
                p1_class = "Helare"zx<
                break
            elif p1_class_choice == "3":
                p1_class = "Tjuv"
                break
            elif p1_class_choice == "4":
                p1_class = "Gambler"
                break
            elif p1_class_choice == "5":
                while True:
                    print("Du är shit")
            else:
                print("Du skrev inte ett giltigt nummer, välj en klass.")
        
        fighter_bonus = randint(1,4)

        com_name= randint(1,10)
        if com_name == 1:
            com_name = "Jeff"
        if

        p1_life = 10
        com_life = 10

        p1_ability = True

        dice_one = """                    _____________
                    |           |
                    |           |
                    |     *     |
                    |           |
                    |___________|"""

        dice_two = """                    _____________
                    |           |
                    |     *     |
                    |           |
                    |     *     |
                    |___________|"""

        dice_three = """                    _____________
                    |           |
                    |   *       |
                    |     *     |
                    |       *   |
                    |___________|"""

        dice_four = """                    _____________
                    |           |
                    |   *   *   |
                    |           |
                    |   *   *   |
                    |___________|"""

        dice_five = """                    _____________
                    |           |
                    |   *   *   |
                    |     *     |
                    |   *   *   |
                    |___________|"""

        dice_six = """                    _____________
                    |           |
                    |   *   *   |
                    |   *   *   |
                    |   *   *   |
                    |___________|"""

        game = True
        game_round = 0


        while game:
            game_round += 1
            print(f"{Fore.BLUE}Runda {game_round} börjar nu!{Fore.RESET}")
            print(f"""{Fore.GREEN}{p1_class} {p1_name}s liv: {p1_life}
         {com_name}s liv: {com_life}{Fore.RESET}""")

            input(f"{p1_class} {p1_name}, tryck på enter för att rulla tärningen")
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
            print(f"{Fore.BLUE}{p1_class} {p1_name} fick en {p1_roll}a{Fore.RESET}")


    if main_menu == "2":

        p1_name = input(Fore.RESET + "Spelare 1, vad är ditt namn?: ")

        while True:
            p1_class_choice = input(f"""{p1_name}, välj en klass:
                1:{Fore.RED} Krigare, Förmåga: Gör 1d4 extra skada{Fore.RESET}
                2:{Fore.BLUE} Helare, Förmåga: Gör att båda spelare ignorerar rundans skada{Fore.RESET}
                3:{Fore.MAGENTA} Tjuv, Förmåga: Byt plats på tärningskasten{Fore.RESET}
                4:{Fore.YELLOW} Gambler, Förmåga: 1/10 chans att antingen direkt vinna eller förlora{Fore.RESET}
                """)
            if p1_class_choice == "1":
                p1_class = "Krigare"
                break
            elif p1_class_choice == "2":
                p1_class = "Helare"
                break
            elif p1_class_choice == "3":
                p1_class = "Tjuv"
                break
            elif p1_class_choice == "4":
                p1_class = "Gambler"
                break
            elif p1_class_choice == "5":
                while True:
                    print("Du är shit")
            else:
                print("Du skrev inte ett giltigt nummer, välj en klass.")

        p2_name = input("Spelare 2, vad är ditt namn?: ")

        while True:
            p2_class_choice = input(f"""{p2_name}, välj en klass:
                1:{Fore.RED} Krigare, Förmåga: Gör 1d4 extra skada{Fore.RESET}
                2:{Fore.BLUE} Helare, Förmåga: Gör att båda spelare ignorerar rundans skada{Fore.RESET}
                3:{Fore.MAGENTA} Tjuv, Förmåga: Byt plats på tärningskasten{Fore.RESET}
                4:{Fore.YELLOW} Gambler, Förmåga: 1/10 chans att antingen direkt vinna eller förlora{Fore.RESET}
                """)
            if p2_class_choice == "1":
                p2_class = "Krigare"
                break
            elif p2_class_choice == "2":
                p2_class = "Helare"
                break
            elif p2_class_choice == "3":
                p2_class = "Tjuv"
                break
            elif p2_class_choice == "4":
                p2_class = "Gambler"
                break
            else:
                print("Du skrev inte ett giltigt nummer, välj en klass.")

        fighter_bonus = randint(1,4)

        p1_life = 10
        p2_life = 10

        p1_ability = True
        p2_ability = True

        dice_one = """                    _____________
                    |           |
                    |           |
                    |     *     |
                    |           |
                    |___________|"""

        dice_two = """                    _____________
                    |           |
                    |     *     |
                    |           |
                    |     *     |
                    |___________|"""

        dice_three = """                    _____________
                    |           |
                    |   *       |
                    |     *     |
                    |       *   |
                    |___________|"""

        dice_four = """                    _____________
                    |           |
                    |   *   *   |
                    |           |
                    |   *   *   |
                    |___________|"""

        dice_five = """                    _____________
                    |           |
                    |   *   *   |
                    |     *     |
                    |   *   *   |
                    |___________|"""

        dice_six = """                    _____________
                    |           |
                    |   *   *   |
                    |   *   *   |
                    |   *   *   |
                    |___________|"""

        game = True
        game_round = 0


        while game:
            game_round += 1
            print(f"{Fore.BLUE}Runda {game_round} börjar nu!{Fore.RESET}")
            print(f"""{Fore.GREEN}{p1_class} {p1_name}s liv: {p1_life}
        {p2_class} {p2_name}s liv: {p2_life}{Fore.RESET}""")

            if game_round % 2 == 1:
                p1_ability = True
                p2_ability = True
                pass 

            input(f"{p1_class} {p1_name}, tryck på enter för att rulla tärningen")
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
            print(f"{Fore.BLUE}{p1_class} {p1_name} fick en {p1_roll}a{Fore.RESET}")

            input(f"{p2_class} {p2_name}, tryck på enter för att rulla tärningen")
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
            print(f"{Fore.BLUE}{p2_class} {p2_name} fick en {p2_roll}a{Fore.RESET}")

            if p1_ability == True:
                p1_use_ability = input(f"{Fore.BLUE}{p1_class} {p1_name} vill du använda din klass förmåga? Y/N: {Fore.RESET}")
                if p1_use_ability == "y":
                    if p1_class == "Tjuv":
                        temp = p1_roll
                        p1_roll = p2_roll
                        p2_roll = temp
                        p1_ability = False
                        print(f"{p1_class} {p1_name} bytte plats på rullningarna!")
                    elif p1_class == "Krigare":
                        p1_roll = p1_roll + fighter_bonus
                        p1_ability = False
                        print(f"{p1_class} {p1_name} lade till {fighter_bonus} till sin rullning för total {p1_roll}!")
                    elif p1_class == "Helare":
                        p1_roll = 0
                        p2_roll = 0
                        p1_ability = False
                        print(f"{p1_class} {p1_name} helade sina skador!")
                    elif p1_class == "Gambler":
                        gamble = randint(1,10)
                        print(f"{p1_class} {p1_name} försökte spela med sit liv och fick en {gamble}a")
                        if gamble == 10:
                            p2_life = 0
                        elif gamble == 1:
                            p1_life = 0
                        p1_ability = False
                elif p1_use_ability == "n":
                    print(f"{Fore.BLUE}{p1_class} {p1_name} valde att inte använda sin klass förmåga{Fore.RESET}")
            
            if p2_ability == True:
                p2_use_ability = input(f"{Fore.BLUE}{p2_class} {p2_name} vill du använda din klass förmåga? Y/N: {Fore.RESET}")
                if p2_use_ability == "y":
                    if p2_class == "Tjuv":
                        temp = p2_roll
                        p2_roll = p1_roll
                        p1_roll = temp
                        p2_ability = False
                        print(f"{p2_class} {p2_name} bytte plats på rullningarna!")
                    elif p2_class == "Krigare":
                        p2_roll = p2_roll + fighter_bonus
                        p2_ability = False
                        print(f"{p2_class} {p2_name} lade till {fighter_bonus} till sin rullning för totalt {p2_roll}!")
                    elif p2_class == "Helare":
                        p1_roll = 0
                        p2_roll = 0
                        p2_ability = False
                        print(f"{p2_class} {p2_name} helade sina skador!")
                    elif p2_class == "Gambler":
                        gamble = randint(1,10)
                        print(f"{p2_class} {p2_name} försökte spela med sit liv och fick en {gamble}a")
                        if gamble == 10:
                            p1_life = 0
                        elif gamble == 1:
                            p2_life = 0
                        p2_ability = False
                elif p2_use_ability == "n":
                    print(f"{Fore.BLUE}{p2_class} {p2_name} valde att inte använda sin klass förmåga{Fore.RESET}")


            if p1_roll > p2_roll:
                print(f"{p1_class} {p1_name} vinner med slaget {p1_roll}")
                p2_life -= p1_roll - p2_roll
            elif p2_roll > p1_roll:
                print(f"{p2_class} {p2_name} vinner med slaget {p2_roll}")
                p1_life -= p2_roll - p1_roll
            else:
                print(f"båda spelare fick lika, inga liv förlorade")

            if p1_life <= 0: 
                print(f"Vi har en vinnare! {p2_name} har besegrat {p1_name} i strid på {game_round} rundor!")
                game = False

            if p2_life <= 0:
                print(f"Vi har en vinnare! {p1_name} har besegrat {p2_name} i strid på {game_round} rundor!")
                game = False