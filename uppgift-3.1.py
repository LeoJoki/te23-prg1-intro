minutes = input("Hur många minuter kommer du ringa denna månad?: ")

if int(minutes) <= 33:
    print("Kontant abonnemanget är bäst för dig")
elif int(minutes) < 66 > 33:
    print("Normal abonnemanget är bäst för dig")
elif int(minutes) >= 66:
    print("Plus abonnemanget är bäst för dig")