from secrets import choice
from time import sleep
from turtle import Turtle, back

while True:
    print("Hoofd persoon: Jamal")
    sleep(3)
    print("Je word wakker na een leuke dag uit met je vrienden maar je hoort allemaal kabaal buiten.")
    sleep(2)
    print("Je negeert het omdat er vaak herrie is in de buurt.")
    sleep(2)
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
    sleep(3)
    print("Wat? Rakketten?")
    sleep(2)
    print("Je pakt snel je dierbaarste spullen en gaat")

    choice1 = input(" A = Naar de veiligheids bunker rennen\n B = Naar de grens rijden?\n")

    if choice1 == "A":
        print("Oke!")
        sleep(1)
        print("Je rent naar de veiligheidsbunker")
        sleep(2)
        print("Je komt aan en kan nog net naar binnen alleen zie je dat er helemaal niemand is en dat het verlaten is?")
        sleep(2)
        print("Wat doe je?")

        choice2 = input(" A = Rondkijken\n B = Weg gaan\n")

        if choice2 == "A":
            print("Je ziet niks maar vind wel een soort tekst op de muur met daarop een soort russische tekst")
            sleep(2)
            print("""            
            █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
            █░░░░░░░░░░░░░░████░░░░░░░░██░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░█
            █░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█
            █░░░░░░▄▀░░░░░░████░░░░▄▀░░██░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█
            █████░░▄▀░░██████████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██████████░░▄▀░░█░░▄▀░░█
            █████░░▄▀░░██████████░░░░▄▀▄▀▄▀░░░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░█
            █████░░▄▀░░████████████░░░░▄▀░░░░█████░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█
            █████░░▄▀░░██████████████░░▄▀░░███████░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░░░░░█
            █████░░▄▀░░██████████████░░▄▀░░███████░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░████████
            █████░░▄▀░░██████████████░░▄▀░░███████░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░░░█
            █████░░▄▀░░██████████████░░▄▀░░███████░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█
            █████░░░░░░██████████████░░░░░░███████░░░░░░██████████░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░██░░░░░░█░░░░░░█
            █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████   
                """)
            print("Het lijkt wel russisch?")
            sleep(2)
            print("Dat betekent dat de Russen hier al geweest zijn!")
            sleep(2)
            print("Je besluit weg te gaan.")
            sleep(2)
            print("Je gaat naar buiten alleen staan er Russische soldaten!")
            sleep(2)
            print("Ze zien hebben je gezien!")
            sleep(2)
            print("Wat doe je?")

            choice3 = input("A = Weg rennen\nB = Blijven staan\n")

            if choice3 == "A":
                print("Ze beginnen op je te schieten!")
                sleep(2)
                print("Je word geraakt in je been en ze lopen naar je toe.")
                sleep(2)
                print("Это за нашего солдата, которого ты похитил! (Dit is voor onze soldaat die jullie ontvoerd hebben!)")
                sleep(2)
                print("""
                                
                █▄█ █▀█ █░█   ▄▀█ █▀█ █▀▀   █▀▄ █▀▀ ▄▀█ █▀▄
                ░█░ █▄█ █▄█   █▀█ █▀▄ ██▄   █▄▀ ██▄ █▀█ █▄▀
                """)
                sleep(4)
                print("Je hebt helaas niet de goede keuzes gemaakt en hebt het niet overleeft...")
                sleep(1.5)
                print("Wil je het nog een keer proberen zodat je het toch in Nederland komt?")

                opnieuw = input("Ja\n Nee\n")

                if opnieuw == "Ja":
                    print("Oke!")
                    continue

                if opnieuw == "Nee":
                    print("Oke jammer!")
                    break

            if choice3 == "B":
                sleep(2)
                print("Russische soldaat: Что ты здесь делаешь? (Wat doe je hier?)")
                sleep(2)
                print("Russische soldaat: Убирайся! (Wegwezen!)")
                sleep(2)
                print("Je gaat terug naar huis en besluit de auto te pakken om naar de grens te rijden ")
                sleep(2)
                ###########################

        if choice2 == "B":
            sleep(1)
            print("Je hoort herrie buiten en ziet een vrachtwagen vol met soldaten naar je toe komen")
            sleep(2)
            print("Ze hebben jou ook gezien en richten op je!")
            print("Wat nu?")

            choice3 = input("A = Weg rennen\nB = Blijven staan\n")

            if choice3 == "A":
                print("Je rent weg en verstopt je.")
                sleep(2)
                print("Russische soldaat: Найти ero! (Vind hem!)")
                sleep(2)
                print("Ze lopen langs je en besluiten weg te gaan.")
                sleep(2)
                print("Je rent naar huis en pakt de auto om richting de grens te gaan.")
                ########


            if choice3 == "B":
                sleep(2)
                print("Russische soldaat: Что ты здесь делаешь? (Wat doe je hier?)")
                sleep(2)
                print("Russische soldaat: Убирайся! (Wegwezen!)")
                sleep(2)
                print("Je gaat terug naar huis en besluit de auto te pakken om naar de grens te rijden ")
                sleep(2)
                ###########################

    if choice1 == "B":
        print("Oke is goed!")
        sleep(2)
        print("Je loopt naar buiten en doet je spullen in de auto.")
        sleep(2)
        print("Je ziet allemaal vliegtuigen overvliegen van het russische leger.")
        sleep(2)
        print("Je bent nog een tas vergeten binnen!")
        sleep(1)
        print("Ga je die snel pakken of ga je weg en laat je de tas achter?")
         
        choice4 = input("A = Tas pakken\n B = Tas achter laten\n")

        if choice4 == "A":
            print("Je pakt de tas en legt hem snel in de achterbak")
            sleep(2)
            print("Je besluit richting de grens rijden.......")
            #####

        if choice4 == "B":
            print("Je laat de tas achter en gaat naar de grens")
            sleep(2)
            ############