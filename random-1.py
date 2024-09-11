# bestäm om det är udda eller jämnt
# rulla tärningar
# vinnaren bestäms

from random import randint


rule = input("Udda eller Jämnt: ")
computer = randint(1,6)
player = randint(1,6)
if rule == "udda":
    # logik
    computer_result = computer % 2
    player_result = player % 2
    print(f"Datorn rullade {computer_result} och spelaren rullade {player_result}, spelregeln var {rule}")

else: 
    computer_result = computer % 2
    player_result = player % 2