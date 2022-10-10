from secrets import choice
from time import sleep

print("Hoofd persoon: Jamal")
sleep(3)
print("Je word wakker na een leuke dag uit met je vrienden.")
print("Je pakt wat te eten en drinken om even wakker te worden en zet de tv aan om het nieuws te kijken om te zien wat er de laatste tijd allemaal gebeurd is.")
sleep(3)
print("""\

██████╗░██████╗░███████╗░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░  ███╗░░██╗███████╗░██╗░░░░░░░██╗░██████╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░  ████╗░██║██╔════╝░██║░░██╗░░██║██╔════╝
██████╦╝██████╔╝█████╗░░███████║█████═╝░██║██╔██╗██║██║░░██╗░  ██╔██╗██║█████╗░░░╚██╗████╗██╔╝╚█████╗░
██╔══██╗██╔══██╗██╔══╝░░██╔══██║██╔═██╗░██║██║╚████║██║░░╚██╗  ██║╚████║██╔══╝░░░░████╔═████║░░╚═══██╗
██████╦╝██║░░██║███████╗██║░░██║██║░╚██╗██║██║░╚███║╚██████╔╝  ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░██████╔╝
╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░╚═════╝░    
    """)
sleep(3)
print("Rusland heeft rakketten gelanceerd op ons land omdat wij volgens hun een soldaat van hun ontvoerd hadden.")
sleep(3)
print("Maar volgens de overheid klopt hier helemaal niks van en liegt Rusland zodat zij ons land kunnen overnemen!")
sleep(3)
print("Wij verzoeken ook het land te verlaten of een veiligheids bunker op te zoeken!")
sleep(2)
print("Wat? Rakketten?")
sleep(1)
print("Je pakt snel je dierbaarste spullen en gaat")

choice1 = input(" A = Naar de veiligheids bunker rennen\n B = Naar de grens rijden?\n")

if choice1 == "A":
    print("Oke!")
    print("Je rent naar de bunker ")

if choice1 == "B":
    print("Oke is goed!")
    print("Je loopt naar buiten en ziet in een keer dat je auto banden zijn gestolen!")


