störst = int(input("Skriv ett postitivt tal, ett negativt tal skriver ut det största och minsta talet: "))
minst = int(input("Skriv ett postitivt tal, ett negativt tal skriver ut det största och minsta talet: "))

while True:
    tal = int(input("Skriv ett postitivt tal, ett negativt tal skriver ut det största och minsta talet: "))
    if störst<tal:
        störst=tal
    if tal>0:
        if minst>tal:
            minst=tal
    if tal<0:
        print(f"Ditt minsta tal var {minst} och ditt största tal var {störst}.")
        break
