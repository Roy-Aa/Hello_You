from ast import While
from re import A
from secrets import choice
from time import sleep

#Opdracht 4 Hello You!

while True:
    print("Je word wakker na een lange nacht ergens in het bos. Vervolgens sta je op en besluit je een weg naar huis te zoeken je komt een pad tegen.")
    sleep(0.5)
    print("Wat doe je?")
    choice1 = input(" A = Verder lopen over het pad\n B = Verder door het bos lopen\n")

    if choice1 == "A":
        print("Oke!")
        sleep(1)
        print("Je komt bij een afgelegen huis uit. Je ziet allemaal criminelen voor het huis met wapens!")
        sleep(1)
        print("Wat doe je?")

        choice2 = input("A = Weg gaan\nB = Uit zoeken wat er gaande is\n")

        if choice2 == "A":
            print("Doen we!")
            sleep(0.5)
            print("Een van de criminelen ziet je!")
            sleep(0.5)
            print("Wat nu?")
            choice3 = input("A = Handen omhoog\nB = Weg rennen\n")

            if choice3 == "A":
                print("Shit!")
                sleep(0.5)
                print("Crimineel: Wat doe je hier wegwezen!!!")
                sleep(0.5)
                print("Je besluit weg te gaan en alles te vergeten.")
                print("""\
                                    
                    ▀█▀ █░█ █▀▀   █▀▀ █▄░█ █▀▄
                    ░█░ █▀█ ██▄   ██▄ █░▀█ █▄▀
                    """)
                print("Helaas heb je het niet overleeft. Wil je het nog een keer proberen? ")

                JN = input("Type J voor ja en N voor nee.\n")
                if JN == "N":
                    print("Oke!")
                    break
                elif JN == "J":
                    print("Leuk dat je het nog een keer wilt doen!")
                    continue

            elif choice3 == "B":
                print("Rennen!")
                sleep(0.5)
                print("Je word geraakt en overleeft het niet...")
                print("""\
                    
                █▄█ █▀█ █░█   ▄▀█ █▀█ █▀▀   █▀▄ █▀▀ ▄▀█ █▀▄
                ░█░ █▄█ █▄█   █▀█ █▀▄ ██▄   █▄▀ ██▄ █▀█ █▄▀
                """)
                sleep(1)
                print("Helaas heb je het niet overleeft. Wil je het nog een keer proberen? ")

                JN = input("Type J voor ja en N voor nee.\n")
                if JN == "N":
                    print("Oke!")
                    break
                elif JN == "J":
                    print("Leuk dat je het nog een keer wilt doen!")
                    continue

        elif choice2 == "B":
            print("Is goed!")
            sleep(0.5)
            print("Het lijkt op een of andere wapen deal?")
            print("Je bedenkt dat je een telefoon bij je had. Bel je de politie of ga je weg?")
            choice4 = input("A = Politie bellen\nB = Weg gaan\n")
            
            if choice4 == "A":
                print("Oke!")
                sleep(0.5)
                print("Bzzzzzz.....")
                sleep(1)
                print("Even later komt de politie en worden de criminelen opgepakt. Het blijkt dat het zwaar gezochte criminelen zijn en je krijgt een beloning van $10.000!")
                print("""\
                                    
                    ▀█▀ █░█ █▀▀   █▀▀ █▄░█ █▀▄
                    ░█░ █▀█ ██▄   ██▄ █░▀█ █▄▀
                    """)
                print("Helaas heb je het niet overleeft. Wil je het nog een keer proberen? ")

                JN = input("Type J voor ja en N voor nee.\n")
                if JN == "N":
                    print("Oke!")
                    break
                elif JN == "J":
                    print("Leuk dat je het nog een keer wilt doen!")
                    continue

            elif choice4 == "B":
                print("Alles wat er gebeurd is vergeet je en de weg naar huis heb je gevonden. Alles is weer normaal...")
                print("""\
                                    
                    ▀█▀ █░█ █▀▀   █▀▀ █▄░█ █▀▄
                    ░█░ █▀█ ██▄   ██▄ █░▀█ █▄▀
                    """)
                print("Helaas heb je het niet overleeft. Wil je het nog een keer proberen? ")

                JN = input("Type J voor ja en N voor nee.\n")
                if JN == "N":
                    print("Oke!")
                    break
                elif JN == "J":
                    print("Leuk dat je het nog een keer wilt doen!")
                    continue



    elif choice1 == "B":
        print("Oke!")
        sleep(1)
        print("Je komt een groep wolfen tegen die je aanvallen")
        sleep(1)
        print("""\
        
    █▄█ █▀█ █░█   ▄▀█ █▀█ █▀▀   █▀▄ █▀▀ ▄▀█ █▀▄
    ░█░ █▄█ █▄█   █▀█ █▀▄ ██▄   █▄▀ ██▄ █▀█ █▄▀
        """)
    
        print("Helaas heb je het niet overleeft. Wil je het nog een keer proberen? ")
    
        JN = input("Type J voor ja en N voor nee.\n")
        if JN == "N":
            print("Oke!")
            break

        elif JN == "J":
            print("Leuk dat je het nog een keer wilt doen!")
            continue
