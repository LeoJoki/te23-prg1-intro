#Äpple kostar 7 kr Päron kostar 13 kr
#kolla hur mycket de sålde
#kolla vem som solde mest
#printa vinnaren

def input_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print("Felaktig inmatning, skriv ett heltal.")

d1a = input_int("Hur många äpplen sålde Axel första dagen?: ")
d1p = input_int("Hur många päron sålde Petra första dagen?: ")

d2a = input_int("Hur många äpplen sålde Axel andra dagen?: ")
d2p = input_int("Hur många päron sålde Petra andra dagen?: ")

d3a = input_int("Hur många äpplen sålde Axel tredje dagen?: ")
d3p = input_int("Hur många päron sålde Petra tredje dagen?: ")

apple_cost = 7
pear_cost = 13

apples = int(d1a)+int(d2a)+int(d3a)
pears = int(d1p)+int(d2p)+int(d3p)

axel_sold = apples * apple_cost
petra_sold = pears * pear_cost

if petra_sold < axel_sold:
    print(f"Axel tjänade mest med {axel_sold}kr")
elif petra_sold > axel_sold:
    print(f"Petra tjänade mest med {petra_sold}kr")
elif petra_sold == axel_sold:
    print(f"Axel och Petra solde lika mycket med {axel_sold}kr")