#använd print för att skriva ut en hälsning
print("Hallojsan!")

#använd den inbyggda funktionen input, för att fråga efter användarens namn
name = input("Vad är ditt namn?: ")

#använd f för att formatera print och skriv ut en hälsning med användarens namn
if name == "Leo":
    print(f"Homobög")
else:
    print(f"Hej {name}! Du existerar!")


age = input("Hur gammal är du?: ")

if int(age) >= 18:
    print("Gammal🤣")
else:
    print("wow så ung")