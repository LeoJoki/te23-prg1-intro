print("Räkna ut hur mycket mil din bil åkt och hur mycket bensin den använt per mil med detta program")
mil = 0
mätare_nu= input("Mätarställning idag?: ")
mätare_då = input("Mätarställning för ett år sedan?: ")
bensin = input("Antal liter bensin förbrukat i år?: ")
mil = float(mätare_nu) - float(mätare_då)
bpm = float(bensin) / float(mil)
rbpm = round(bpm, 2)
print(f"Du har kört {mil} mil och förbrukat {rbpm} bensin per mil.")