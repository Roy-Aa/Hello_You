# Hello you opdracht 2 

from doctest import OutputChecker
J = 2022

print("Hello you!, ik ben Roy")
print("Wie ben jij?")
naam = input()
print("Hello", naam)
print("In welk jaar ben je geboren?")
geboortejaar = input()
leeftijd = J- int(geboortejaar)
print("Het is 2022 jij bent dan", leeftijd ,"jaar")