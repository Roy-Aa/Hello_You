from cgi import print_arguments
from secrets import choice
from time import sleep
from turtle import Turtle, back
from xmlrpc.server import SimpleXMLRPCDispatcher

def stop():
    sleep(99999999)

def dood():

    while True:
        print("""
        █▄█ █▀█ █ █   ▄▀█ █▀█ █▀▀   █▀▄ █▀▀ ▄▀█ █▀▄
         █  █▄█ █▄█   █▀█ █▀▄ ██▄   █▄▀ ██▄ █▀█ █▄▀
        """)
        sleep(4)    
        print("Je hebt helaas niet de goede keuzes gemaakt en hebt het niet overleeft...")
        sleep(1.5)
        print("Wil je het nog een keer proberen zodat je het toch in Nederland komt?")

        opnieuw = input("Ja\nNee\n")

        if opnieuw == "Ja":
            print("Oke!")
            break

        if opnieuw == "Nee":
            print("Oke jammer!")
            stop()

def Nederland():
    print("Je bent er eindelijk alleen ziet dat het al 11 uur in de avond is en je hebt geen idee wat je moet doen. Je gaat naar het internet en zoekt... ")
    choicea = input("A = Opvangcentrum vluchtelingen\nB = Hotel Nederland")

    if choicea == "A":
        print("Je komt op een website die vluchtelingen opvangt in Nederland en je besluit er naar toe te gaan")
        sleep(3)
        print("Ze vangen je op en zorgen goed voor je\nJe leert de taal en krijgt een baan als postbezorger.")
        sleep(3)
        print("""
                    
        ░██████╗░███████╗███████╗███████╗██╗░░░░░██╗░█████╗░██╗████████╗███████╗███████╗██████╗░██████╗░
        ██╔════╝░██╔════╝██╔════╝██╔════╝██║░░░░░██║██╔══██╗██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗
        ██║░░██╗░█████╗░░█████╗░░█████╗░░██║░░░░░██║██║░░╚═╝██║░░░██║░░░█████╗░░█████╗░░██████╔╝██║░░██║
        ██║░░╚██╗██╔══╝░░██╔══╝░░██╔══╝░░██║░░░░░██║██║░░██╗██║░░░██║░░░██╔══╝░░██╔══╝░░██╔══██╗██║░░██║
        ╚██████╔╝███████╗██║░░░░░███████╗███████╗██║╚█████╔╝██║░░░██║░░░███████╗███████╗██║░░██║██████╔╝
        ░╚═════╝░╚══════╝╚═╝░░░░░╚══════╝╚══════╝╚═╝░╚════╝░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░
        
        """)
        sleep(2)
        print("Je hebt de goede keuzes gemaakt en hebt het overleeft!")
        sleep(2)
        print("Leuk dat je het verhaal gespeeld hebt als je nog tips hebt hoor ik het graag!")
        sleep(9999)

    if choicea == "B":
        print("Je vind een hotel en besluit er naar toe tegaan.\nJe komt aan en ziet iemand achter de balie je probeert te communiceren maar het lukt niet.")
        sleep(4)
        print("De vrouw achter de balie vertrouwd het niet helemaal en belt de politie...")
        sleep(3)
        print("De politie is er en je word meegenomen omdat je niet de taal spreekt en geen legitimatiebewijs bij je hebt.")
        sleep(3)
        print("Uiteindelijk word je terug gestuurd en opgevangen door een stel Russen...")
        dood()

def reis():
    print("Je gaat richting Nederland rijden en ziet ongeveer op de helft van je reis een parkeerplaats waar je kan slapen...")
    sleep(2)

    choice6 = input("A = Naar de parkeerplaats gaan en slapen\nB = Door rijden en niet slapen\n")

    if choice6 == "A":
        print("Je rijd de parkeerplaats op en gaat slapen.........")
        sleep(3)
        print("Je word wakker gemaakt door een enorme herrie en ziet allemaal russische voertuigen op de parkeerplaats.")
        sleep(3)
        print("Ze schieten iedereen neer!")
        sleep(2)
        print("Wat nu!?")

        choice7 = input("A = Verstoppen\nB = Weg rijden\n")

        if choice7 == "A":
            print("Je gaat op de achterbank liggen met een deken over je heen....")
            sleep(3)
            print("Ze lopen langs je en je probeert zo stil mogelijk te zijn")
            sleep(2)
            print("Russische soldaat: Здесь никого нет (Hier zit niemand)")
            sleep(2)
            print("Ze rijden weg en je besluit om ook weg te gaan richting Nederland.")
            Nederland()

        if choice7 == "B":
            print("Je start de auto en rijd naar de ingang.")
            sleep(2)
            print("Je komt aan alleen staan er Russische soldaten te wachten op je...")
            sleep(2)
            print("Ze trekken je uit de auto en leggen je op de grond.")
            sleep(2)
            print("Russische soldaat: Пойдемте! (Meekomen)")
            sleep(2)
            print("Je word tegen de muur gezet en overleeft het niet...")
            dood()

    if choice6 == "B":
        print("Je rijd door.....")
        sleep(3)
        Nederland()

def grens2():
    print("Je komt aan bij de grens en ziet een rij van honderden mensen.")
    sleep(2)
    print("Je staat ongeveer 4 uur in de rij maar je bent toch aan de beurt.")
    sleep(2)
    print("Douane: Mag ik je legitimatiebewijs zien?")

    choice5 = input("A = legitimatiebewijs geven\nB = Liegen dat je er geen een hebt\n")

    if choice5 == "A":
        print("Douane: Top dankjewel ik ga hem even door het systeem halen.")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(2)
        print("Douane: Alles klopt hier heb je je legitimatiebewijs terug en wens ik u een fijne reis!")
        reis()

    if choice5 == "B":
        print("Douane: Als u geen legitimatiebewijs kan tonen mag u niet door.")
        sleep(3)
        print("Je besluit het toch te geven omdat je echt uit het land moet...")
        reis()

def tanken():
    print("Je bent aan het rijden ziet dat je tank halvewegeneen is en je ziet een bord met tank station 300 meter.")
    sleep(2)
    print("Ga je tanken of rijd je door?")

    tanken = input("A = Tanken\nB = Door rijden\n")

    if tanken == "A":
        sleep(2)
        print("""
        ⠀⠀⠀⠀⠀⠀⡀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠰⠀⣿⣿⢋⣭⠉⣝⢻⣶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⠀⣿⠆⣼⠳⣿⢫⡄⠿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠠⠀⣿⣆⡞⣴⠓⠨⠉⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⠶⣾⢿⡻⢿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠠⠀⣟⠿⣾⢿⡿⣟⡿⣿⡃⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⢤⡶⠞⠫⢽⣏⣒⠧⠿⠟⠛⠉⠑⠻⠾⢯⣿⢿⣷⣦⣄⢀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠘⠀⣿⣿⣿⣿⣿⣯⣿⣷⠃⢸⣇⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣶⡾⣟⣿⡽⠇⠤⠂⣃⠨⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢾⣿⡀⢈⢶⣔⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠀⣿⣾⣿⣿⣿⣿⣿⣏⡇⢸⣿⡇⣀⣀⠀⢰⣶⣾⣿⢿⡏⠿⢈⡉⠉⠀⠀⠁⠀⠈⢀⠀⡀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⣏⡿⠀⠈⢾⠀⠈
    ⣤⣤⣦⣆⢀⣸⠀⣯⣟⣻⣻⣿⣿⣿⣿⡆⢸⣿⡋⠀⢀⠠⠿⠛⠉⠂⠀⡄⠀⠂⠁⡀⠠⡀⠢⠘⠀⠀⠐⠀⠪⠋⠐⢂⡄⣤⠀⣀⣀⡀⠀⠀⡀⣤⣤⣤⣤⣤⣤⠬⢤⣶⣿⣤⣾
    ⣹⣻⡿⠟⠻⣿⠀⣿⣛⣿⣿⡽⢿⣟⠟⡅⢸⣻⣽⣟⣿⣯⣴⢴⢴⣲⠆⡵⣶⣶⣤⣤⣤⡆⣦⣤⣤⣤⣶⣶⣄⣴⡖⢎⡂⢨⢿⣷⡛⣲⣿⠀⡇⣿⣁⣈⣍⠉⣡⣦⣔⡋⣬⡿⣿
    ⣽⣿⣧⢀⡀⢼⠀⣿⣞⡿⢵⣿⣷⣷⡶⠇⢰⣯⣼⣿⣿⣿⣿⣾⣼⣽⡇⢨⣿⣿⣿⣿⣯⣇⣿⣿⣿⣿⣿⣿⣶⣺⣯⣿⡆⢸⣦⣶⣿⣿⣿⠀⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏
    ⣿⣻⣿⣛⣛⣼⠀⣿⣛⣛⣚⣒⡛⢠⣷⠀⢘⣛⣻⣟⣿⣿⠿⠋⣫⣯⡀⣸⠛⠿⢀⣿⣙⡇⡏⣿⡋⠿⡿⠷⢿⠀⣯⣀⠇⢸⣿⣻⣿⣿⣿⠀⢈⣉⠿⠷⠿⣟⣻⣿⠻⣿⣛⡿⢿
    ⠁⠉⠉⠉⠉⢹⠀⡇⢀⣈⣉⠉⣉⠉⢡⠀⢈⣨⣤⣄⣤⢠⣤⡧⠿⢿⡇⢻⢠⢛⢼⡿⣿⡅⣫⡾⣵⣶⣶⡖⣾⣀⣿⣿⡆⢸⡿⣪⣧⢖⣤⠀⢸⢿⣷⣖⠲⣆⢖⡺⣽⢲⢮⣙⠿
    ⠀⠀⠀⠀⡄⣼⠀⣷⣭⢡⣤⢫⠒⣽⣾⠀⢰⡌⣽⢢⠒⣦⡄⢣⣤⣤⡄⠀⠛⠛⠀⠉⠉⠃⠉⠉⠉⠉⠉⡏⢻⡇⣯⣽⡇⢸⠙⢻⣯⠛⠛⠀⠚⠀⠉⠉⠉⠉⠉⠁⠀⠉⠊⢡⣽
    ⠀⢀⡡⢂⣠⣿⠽⡁⢀⠀⠈⠀⣒⢥⣬⣶⡼⡳⠖⠮⢞⡴⢭⣲⡥⢲⢎⡭⣱⠢⠥⡖⡖⢦⠤⣤⠠⣄⣀⣁⡈⠃⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠤⣴⢲⠳⣎⡏⢷
    ⠀⠀⠀⠁⠁⠀⠀⠀⢉⠉⠉⠉⠀⢀⠀⠉⠉⠉⠀⠀⢀⠀⠉⠀⠉⠙⠊⠹⠚⠭⣝⡾⢙⣎⢓⢮⡱⢎⠶⣩⣛⢭⡛⠴⡶⣶⢲⢦⣤⢤⣤⣴⣶⣲⢫⢏⡵⣌⢏⣬⠣⡟⣶⡹⣫
    ⠀⠄⠀⠠⠀⠀⠂⠄⠀⠀⢀⡀⠐⡀⠀⠀⠠⠐⠠⠀⠀⠀⠀⠐⠀⠀⠀⠂⠀⠄⡀⠠⠁⣄⠩⢳⣵⡫⡓⣵⢪⡖⣳⡫⣕⠞⡭⡚⢌⣳⢏⠖⣞⡕⢮⣞⣱⣎⣳⣚⡽⣜⣧⢟⡽⠀  
        """)
        print("Je gaat tanken en rijd door naar de grens")
        grens2()

    if tanken == "B":
        print("Je rijd door.....")
        grens2()

def grens():
    print("Zo we zijn er bijna.........")
    sleep(2)
    print("Je bent al bijna 2 uur onderweg en begint moe te worden.")

    choice5 = input("A = Slapen\nB = Door rijden\n")

    if choice5 == "A":
        print("Je gaat even langs de weg staan en neemt even een dutje.")
        sleep(2)
        print("Je word wakker en rijd door....")
        sleep(2)
        tanken()
        ###

    if choice5 =="B":
        print("Je rijd door...")
        sleep(2)
        tanken()
        ###



#### START
while True:
    print("""
        
    █   █▀▀  ▀█▀  █▀█ █▀█ ▀   █▀▀ █▀▀ █▄▄ █▀█ █ █ █ █▄▀    ▄▀█ █   █   █▀▀ █▀▀ █▄█
    █▄▄ ██▄   █   █▄█ █▀▀ ▄   █▄█ ██▄ █▄█ █▀▄ █▄█ █ █ █    █▀█ █▄▄ █▄▄ ██▄ ██▄ █▀█

    █ █ █▀█ █▀█ █▀▀ █▀▄ █   █▀▀ ▀█▀ ▀█▀ █▀▀ █▀█ █▀
    █▀█ █▄█ █▄█ █▀  █▄▀ █▄▄ ██▄  █   █  ██▄ █▀▄ ▄█
    """)
    sleep(4)
    print("Hoofd persoon: Jamal\n")
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

    choice1 = input("A = Naar de veiligheids bunker rennen\nB = Naar de grens rijden?\n")

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
                dood()


            if choice3 == "B":
                sleep(2)
                print("Russische soldaat: Что ты здесь делаешь? (Wat doe je hier?)")
                sleep(2)
                print("Russische soldaat: Убирайся! (Wegwezen!)")
                sleep(2)
                print("Je gaat terug naar huis en besluit de auto te pakken om naar de grens te rijden ")
                sleep(2)
                grens
                ###

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
                grens()
                ###


            if choice3 == "B":
                sleep(2)
                print("Russische soldaat: Что ты здесь делаешь? (Wat doe je hier?)")
                sleep(2)
                print("Russische soldaat: Убирайся! (Wegwezen!)")
                sleep(2)
                print("Je gaat terug naar huis en besluit de auto te pakken om naar de grens te rijden ")
                sleep(2)
                grens()
                ###

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
         
        choice4 = input("A = Tas pakken\nB = Tas achter laten\n")

        if choice4 == "A":
            print("Je pakt de tas en legt hem snel in de achterbak")
            sleep(2)
            print("Je besluit richting de grens rijden.......")
            grens()
            ###

        if choice4 == "B":
            print("Je laat de tas achter en gaat naar de grens")
            sleep(2)
            grens()
            ###