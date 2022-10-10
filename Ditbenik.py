# Opdracht 3 Hello you
from ast import While
from asyncore import loop
from cmath import pi

J = 2022
L = 16

print("Hello you!, ik ben Roy")
print("Wie ben jij?")
naam = input()
print("Hello", naam)
print("In welk jaar ben je geboren?")
geboortejaar = input()
leeftijd = J- int(geboortejaar)
print("Het is 2022 jij bent dan", leeftijd ,"jaar")

while True:
    print("Ik ben een nieuwkomer op het Mediacollege Amsterdam. Om mij beter te leren kennen stel ik een aantal vragen over mij.")
    print("Beantwoord deze met A, B of C.")
    print("Hoe oud ben ik?")

    vraag1 = input("A = 15\nB = 16\nC = 17\n")

    print(vraag1)
    if vraag1 == "A":
        print("Nope probeer het nog een keer! :/")

    elif vraag1 == "B":
        print("Dat klopt!")

    elif vraag1 == "C":
        print("Nee niet goed het antwoord was", L)

    print("Waar woon ik?")

    vraag2 = input("A = Heemskerk\nB = Beverwijk\nC = Haarlem\n")

    print(vraag2)
    if vraag2 == "A":
        print("Nee maar het is wel dichtbij!")

    elif vraag2 == "B":
        print("Ja dat klopt!")

    elif vraag2 == "C":
        print("Nee niet eens dichbij!")

    print("Welk vervoer gebruik ik?")

    vraag3 = input("A = Openbaar vervoer\nB = Auto\nC = Fiets\n")

    print(vraag3)
    if vraag3 == "A":
        print("Yes helemaal goed!")

    elif vraag3 == "B":
        print("Nee probeer het nog eens!")

    elif vraag3 == "C":
        print("Nee niet goed :c")

    print("Wil je deze quiz nog een keer doen? ")

    JN = input("Type J voor ja en N voor nee.\n")

    print(JN)
    if JN == "N":
        print("Oke!")
        break

    elif JN == "J":
        print("Leuk dat je het nog een keer wilt doen!")
        continue