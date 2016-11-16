from prosedyrer import *
from klasser import *
from grafikk import *

#VIKTIG! Ikke bruk denne filen som mal for senere expansions!

def mainloop(spiller, inv, klasser, spellbook):
    inn = input("\nVil du spille tutorial?\n> ").lower()
    while inn != "ja" and inn != "j" and inn != "nei" and inn != "n":
        inn = input("Skriv 'ja' for å starte tutorial\n> ").lower()
    if inn == "nei" or inn == "n":
        spiller.hev_a(40)
        spiller.hev_d(40)
        print("\n"+spiller.navn()," er en lovende ung magiker ute på jakt etter eventyr. En dag kommer ",\
        spiller.navn()," til en magisk borg omringet \nav en fortryllende skog! Mon tro hvilke utfordringer og eventyr som venter der?", sep="")
        input("\nTrykk enter for å fortsette\n> ")
        return "gnom"

    qlog = klasser.questlog(0)
    navn = spiller.navn()
    print("\n                   ~BLOD! MASSE BLOD OVERALT!~\n")
    print("   ", navn, """ser seg rundt. Kanskje det ikke er SÅ mye blod, men det sildrer
    blod fra pannen, og en mann og en kvinne ligger blødende på gulvet i
    midten av rommet. De våkner til samtidig, og stirrer på""", navn + ".\n")
    input(navn + ": Hva skjedde? Hvor er jeg? *Trykk enter for å fortsette*\n> ")
    print("""\n    Zip: Husker du ingenting? Vi må komme oss bort herfra fort!
    Zap: Zip, jeg kan ikke bevege meg, jeg tror benet er brukket!
    Zip: Kan du ikke bruke magi? Kjapp deg, vi må forte oss!
    Zap: Jeg klarer ikke! Zip, vi må finne på noe annet, jeg tror kanskje
         nøttene utenfor kan løse problemet! Kan du gå ut og finne noen?
    Zip: Jeg drar ikke fra deg!""", navn + ", kan du dra ut og lete?\n")
    input(navn + ": Jeg er ikke særlig god på å løse nøtter! Fikk f.eks aldri til Rubik's cube...\n*Trykk enter for å fortsette*\n> ")
    print("""
    Zap: Ikke slike nøtter, faktiske nøtter! Det kan være du må sloss med noen
         ekorn over dem.\n""")
    input(navn + """: Ekorn? Hva skjedde med å begynne med rotter? Ekorn er alt for søte
til å drepe! Dessuten aner jeg ikke hvordan jeg sloss med noe som helst!
*Trykk enter for å fortsette*\n> """)
    print("""
    Zip: Rottene er i streik. Og hva mener du med at du ikke vet hvordan du sloss?
         Var det ikke du som nettopp med en hånd på ryggen bekjempet den stor-
    Zap: AAAAARG det gjør vondt! Vi har ikke tid til dette!""")
    qlog.snakk(0, spiller, inv)
    while not qlog.hent_quest(0).startet():
        print("\n    Det sto ganske tydelig, skriv 'JA' for å godta oppdraget...\n    Og nei, du kommer ikke videre uten å godta oppdraget!\n")
        qlog.snakk(0, spiller, inv)
    input("\n" + navn + " løper ut døren, og kommer ut i en skog. Trehytten " + navn + """ kom ut
fra er grovt brent, og har et stort hull i taket. """ + navn + " ser seg rundt.\n*Trykk enter for å fortsette*\n> ")
    print("""\nDu fant en nøtt! Og den er beskyttet av et ekorn!\nPlutselig kan du høre Zip sin stemme i hodet -
    \n    Zip: ~skt- zzjup- .. zzeeelo? Hallo? Kan du høre meg? Dårlig dekning her inne.
         Du er altså nå på et oppdrag! Du kan være på flere oppdrag samtidig. Om du
         lurer på hvilke oppdrag du har aktive, kan du skrive 'oppdrag' eller 'q'
         for å se aktive oppdrag. Prøv det nå!~""")
    inn = input("\nHva vil du gjøre?\n> ").lower()
    while inn != "oppdrag" and inn != "q":
        inn = input("Skriv 'q' eller 'oppdrag' for å se aktive oppdrag\n> ").lower()
    for qlogs in klasser.alle_questlogger():
        qlogs.skriv_ut(spiller)
    input("\n*Trykk enter for å fortsette*\n> ")
    print("""    ~Supert! La oss nå angripe dette ekornet! Jeg la merke til at du fortsatt
    har et sverd, selv om det er ganske slitt og sløvt. Bruk det! Sverd har
    den egenskapen at de stort sett tar like mye liv. Angrip ekornet ved å
    skrive 'a' eller 'angrip'!~""")
    item = Item("Brukket stav", "weapon", a=3)
    inv.legg_til_item(item)
    item = Item("Slitt sverd", "weapon", a=5, blade=True)
    inv.legg_til_item(item, True)

    loot = Loot()
    item = Item("Nøtt", "various")
    loot.legg_til_item(item, 100)
    fiende = Fiende("Nusselig ekorn", "dyr", loot, 30, 10, 0)
    print("\n" + navn, "har møtt et nusselig ekorn!")
    skriv_ekorn1()
    skriv_ut(spiller, fiende)

    while not fiende.dead():
        inn = input("\nHva vil du gjøre?\n> ").lower()
        while inn != "a" and inn != "angrip":
            if inn == "q" or inn == "oppdrag":
                for qlogs in klasser.alle_questlogger():
                    qlogs.skriv_ut(spiller)
            inn = input("\nSkriv 'a' eller 'angrip' for å angripe\n> ").lower()
        angrip_fiende(spiller, fiende, inv)
    print("--------------------------------------------------------------------"+\
    "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
    spiller.gi_xp(fiende.xp())
    fiende.loot(spiller, inv)
    qlog.hent_quest(0).progresser()
    spiller.restorer(100)
    input("\n*Trykk enter for å fortsette*\n> ")
    print("""    ~Det viste den nok! Har du fått med deg nøtten? Sjekk om den er blant
    inventaret ditt ved å skrive 'inventar' eller 'i'!~""")
    inn = input("\nHva vil du gjøre?\n> ").lower()
    while inn != "i" and inn != "inventar":
        if inn == "q" or inn == "oppdrag":
            for qlogs in klasser.alle_questlogger():
                qlogs.skriv_ut(spiller)
        inn = input("\nSkriv 'inventar' eller 'i' for å se inventaret ditt\n> ").lower()
    inv.skriv_inv()
    input("\n*Trykk enter for å fortsette*\n> ")
    qlog.snakk(0, spiller, inv)

    inv.bruk_item(item)
    print("""
    Zap: Tusen takk """ + navn + """! Håper dette løser problemet!
    *Zap spiser nøtten*
    *Zap begynner å skjelve*
    Zip: Jeg hater når du gjør dette Zap. En dag kommer du til å angre på at
         du utnytter nøtteallergien din når du havner i kjipe situasjoner.
    Zap: *Hikst* *Hark* Blææææ det er ikke nok! Jeg må har mer!
    Zip: *Sukk* """ + navn + """, det ser ut til at vi nok en gang må kalle
         på din ekspertise.\n""")
    input(navn + " går ut for å finne nok en nøtt. Trykk enter for å fortsette\n> ")
    print("""
    Zip: Alright, da er det på tide å prøve oss på litt magi. Jeg la merke til
         at du har en brukket tryllestav på deg, bruk den! For å bruke den,
         må du først bytte til den. Gjør det ved å skrive 'b' eller 'bytt',
         deretter skriver du nummeret på kategorien 'Våpen', så våpenet du
         vil bytte til. Gjør det nå!\n""")
    inn = input("Hva vil du gjøre?\n> ").lower()
    while inn != "b" and inn != "bytt":
        inn = input("Skriv 'b' eller 'bytt', deretter nummeret på kategorien 'Våpen', så våpenet du vil bytte til.\n> ").lower()
    while inv.har_type("weapon").blade():
        kategorier()
        try:
            kategori = int(input("Hvilken kategori vil du bytte innenfor?\n> "))
            if kategori < 8 and kategori > 0:
                x = inv.skriv_kategori(kategori)
                if x != 1:
                    indeks = int(input("Hva vil du bytte til? Skriv nummeret til høyre\n> "))
                    item = inv.bytt_til(kategori, indeks)
                    input("Du har byttet til " + item.navn() + ". Trykk enter for å fortsette.\n> ")
                else:
                    print("Du har ingen ting innenfor den kategorien.")
                    input("Trykk enter for å fortsette.\n> ")
            else:
                print("Ugyldig kategori")
                input("Trykk enter for å fortsette.\n> ")
        except ValueError:
            None
        except IndexError:
            print("Ugyldig kategori")
        if inv.har_type("weapon").blade():
            print("Skriv nummeret på kategorien 'Våpen', så våpenet du vil bytte til.")
            input("Trykk enter for å fortsette\n> ")
    print("""\n    ~Strålende! Du la kanskje merke til at det sto 'a' og  et tall ved
    siden av navnet på våpnene? Det markerer hvor mange angrepspoeng man får i
    bonus av det våpenet. Med sverd og andre nærkampsvåpen, er det antall
    angrepspoeng våpenet gir i bonus som er hovedindikator på hvor mye skade
    du kan gjøre. Når du bruker en tryllestav eller andre magiske våpen, er det
    din totale mengde angrepspoeng som angir hvor mye skade du kan gjøre. For å
    se hvor mye angrepspoeng du har, skriv 'e' eller 'egenskaper' for å se alle
    egenskapene dine. Prøv det nå!~\n""")
    inn = input("Hva vil du gjøre?\n> ").lower()
    while inn != "e" and inn != "egenskaper":
        inn = input("Skriv 'e' eller 'egenskaper' for å se alle egenskapene dine.\n> ").lower()
    print("")
    spiller.stats()
    input("\n*Trykk enter for å fortsette*\n> ")
    print("""
    ~Der har du det! Merk at når du utfører magi er det mye mer tilfeldig hvor
    mye skade du gjør, men oftest kan man potensielt gjøre mer skade med magi.~\n""")

    loot = Loot()
    fiende = Fiende("Grufullt ekorn", "dyr", loot, 50, 10, 0)
    print(navn, "har møtt et grufullt ekorn!\n")
    skriv_ekorn2()
    print("\n    ~Det ser ut til at du får teste teorien i praksis! Så beleilig...~\n")
    skriv_ut(spiller, fiende)
    while not fiende.dead():
        inn = input("\nHva vil du gjøre?\n> ").lower()
        while inn != "a" and inn != "angrip":
            if inn == "e" or inn == "egenskaper":
                spiller.stats()
            if inn == "i" or inn == "inventar":
                inv.skriv_inv()
            inn = input("\nSkriv 'a' eller 'angrip' for å angripe\n> ").lower()
        angrip_fiende(spiller, fiende, inv)
    print("--------------------------------------------------------------------"+\
    "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
    spiller.gi_xp(fiende.xp())
    spiller.restorer(100)
    input("\n*Trykk enter for å fortsette*\n> ")
    print("""
    ~Gratulerer! Du er nå på nivå to! Hver gang du går opp et nivå, får du
    mer angrepspoeng, defensivpoeng, konsentrasjonspoeng og helsepoeng.
    Legg merke til at angrepspoeng ofte forkortes til 'a', defensivpoeng
    til 'd', konsentrasjonspoeng til 'kp' og helsepoeng til 'hp'. Etterhvert
    som du kommer på høyere nivåer vil du lære deg trylleformler som kan hjelpe
    deg under kamp, men disse krever en viss mengde konsentrasjonspoeng. Du
    kan fornye konsentrasjonspoengene ved å angripe på andre måter.~\n""")
    input(navn + ": Forstått! Men hva gjør defensivpoeng og helsepoeng? *Trykk enter for å fortsette*\n> ")
    print("""
    ~Flere defensivpoeng vil gi deg økt sannsynlighet for å redusere skaden
    fienden gjør på deg. Flere helsepoeng øker mengden skade du kan ta før du
    dør. Ikke dø! Jeg har hørt skumle historier fra de som har dødd, og det
    høres ikke ut som en behagelig opplevelse. Apropos, fort deg tilbake så
    vi kan komme oss bort herfra!~\n""")
    input(navn + " går tilbake til hytten. *Trykk enter for å fortsette*\n> ")
    print("""
    Zap: *Hark* *spytt* *gumle* Vrrraaaaasj MER! MER! GI MEG MER!
    Zip: Zap, virkelig, skjerp deg! Hvordan skal nøtteallergien din
         kurere et brukkent bein? Kan vi ikke bare komme oss avgårde?
    Zap: MEEEEEEER!!! JEG MÅ HA MER!!! DET ER INGEN VEI UTENOM!!
    Zip: Jeg begynner å gå lei av dette.""", navn + """, det ser ut til at vi må
         hardere til verks. Gå ut og finn den største nøtten i skogen!\n""")
    input("Enda en gang går " + navn + " ut i skogen på nøttejakt. *Trykk enter for å fortsette*\n> ")

    loot = Loot()
    item = Item("Tryllepulver", "damaging", dmg=100)
    item.sett_loot_tekst("en håndfull tryllepulver")
    loot.legg_til_item(item, 100)
    fiende = Fiende("Mistenkelig ekorn", "dyr", loot, 15, 3, 4)
    print("\n" + navn, "har møtt et Mistenkelig ekorn!")
    skriv_ekorn1()
    skriv_ut(spiller, fiende)
    while not fiende.dead():
        inn = input("\nHva vil du gjøre?\n> ").lower()
        while inn != "a" and inn != "angrip":
            if inn == "e" or inn == "egenskaper":
                spiller.stats()
            if inn == "i" or inn == "inventar":
                inv.skriv_inv()
            inn = input("\nSkriv 'a' eller 'angrip' for å angripe\n> ").lower()
        angrip_fiende(spiller, fiende, inv)
    print("--------------------------------------------------------------------"+\
    "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
    spiller.gi_xp(fiende.xp())
    fiende.loot(spiller, inv)
    spiller.restorer(100)
    input("Trykk enter for å fortsette\n> ")

    loot = Loot()
    fiende = Fiende("Gigantisk ekorn", "dyr", loot, 100, 20, 100)
    print("\n" + navn, "har møtt et gigantisk ekorn!")
    skriv_ekorn3()
    print("""
    ~Det er et stykke stort ekorn! Det vokter helt sikkert en gigantisk nøtt!
    Hmm, det ser ut til at defensiv-nivået til dette ekornet er skyhøyt! Du har
    nok ikke mye sjanse mot det med vanlige angrep. Var det tryllepulver du
    fant på det mistenkelige ekornet i sted? Tryllepulver og magiske
    trylleformler gjør en bestemt mengde skade uansett defensivnivået til
    fienden. Du kan se hvilke angrepsmetoder og trylleformler du kan bruke
    ved å skrive 's' eller 'formler'. Prøv det nå!~\n""")
    inn = input("Hva vil du gjøre?\n> ").lower()
    while inn != "s" and inn != "formler":
        inn = input("Skriv 's' eller 'formler' for å se hvilke angrepsmetoder og trylleformler du kan bruke\n> ").lower()
    spellbook.skriv_spellbook()
    input("\nTrykk enter for å fortsette\n> ")
    print("""
    ~Siden du ikke har lært noen trylleformler enda, er det kun tryllepulver du
    kan bruke mot ekornet. Bruk tryllepulver ved å skrive 't' eller 'tryllepulver'!~\n""")

    skriv_ut(spiller, fiende)
    while not fiende.dead():
        inn = input("\nHva vil du gjøre?\n> ").lower()
        while inn != "a" and inn != "angrip" and inn != "t" and inn != "tryllepulver":
            if inn == "e" or inn == "egenskaper":
                spiller.stats()
            if inn == "s" or inn == "formler":
                spellbook.skriv_spellbook()
            if inn == "i" or inn == "inventar":
                inv.skriv_inv()
            inn = input("\nSkriv 't' eller 'tryllepulver' for å kaste en neve tryllepulver på ekornet.\n> ").lower()
        if inn == "t" or inn == "tryllepulver":
            spellbook.tryllepulver(fiende)
        else:
            angrip_fiende(spiller, fiende, inv)
    print("--------------------------------------------------------------------"+\
    "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
    spiller.gi_xp(fiende.xp())
    print(navn, "fant en gigantisk nøtt på det gigantiske ekornet!")
    spiller.restorer(100)
    input("\n    ~Det burde holde! Kom tilbake til hytten.~ *Trykk enter for å fortsette*\n> ")

    print("""
    Zap: WRAAAAAAAA ADRENALIN!!!!! SÅ MYE ADRENALIN!!!!!
    Zip: Nettopp ja...
    Zap: Tusen takk""", navn + """! Nå, la oss komme oss avgårde!""")
    qlog.snakk(1, spiller, inv)
    while not qlog.hent_quest(1).startet():
        print("\n    Skriv 'ja' for å godta oppdraget.\n")
        qlog.snakk(1, spiller, inv)
    input("\nTrykk enter for å dra videre.\n> ")
    print("""Etter en lang reise kommer""", navn, """frem til en magisk borg omringet av en fortryllende
skog.""", navn, "finner Overtrollmann Vassle på toppen av et spir høyt \nover resten av borgen.\n")
    input("Trykk enter for å fortsette\n> ")
    qlog.hent_quest(1).progresser()
    qlog.snakk(1, spiller, inv)

    return "gnom"

def angrip_fiende(spiller, fiende, inv):
    weapon = inv.har_type("weapon")
    if weapon and weapon.blade():
        fiende.angrepet(spiller.a(), inv.hent_weaponA())
    else:
        fiende.angrepet(spiller.a())

    spiller.angrepet(fiende)
    if spiller.dead():
        spiller.restorer(60)
        print("Zip restorerte 60 hp på", spiller.navn(), "ved magi!")
    skriv_ut(spiller, fiende)

def tutorial_quest(qlog, spiller):
    desk1 = "    Zip: OK, jeg skal vise deg hva du skal gjøre underveis, bare gå!\n"
    ferdigdesk1 = "    ~Strålende! Kom tilbake til hytten med nøtten!~\n"
    q1 = Quest(desk1, ferdigdesk1, 1, 1, "Zip")
    q1.legg_til_reward(xp=10)
    q1.legg_til_progresjonTekst("Nøtter samlet: ")
    q1.legg_til_svarTekst("*Skriv 'ja' for å godta oppdraget*\n> ")
    qlog.legg_til_quest(q1)

    desk2 = """    Zip: Kan du bruke magi nå?
    Zap: Jeg tror det! Adrenalinet var nok til å få tilbake magien min.
    Zip: Med beinet ditt, tror jeg det er best om vi flyr rett til Gale Gizly.
    Zap: Sant nok. """ + spiller.navn() + """, kan du gi beskjed til Overtrollmann Vassle
         at vi fullførte oppdraget, men ikke har tid til å møte ham i person?\n"""

    ferdigdesk2 = """    Hrmph, hva gjør du her? Kun topp-magikere er tillat her!\n\n"""\
     + spiller.navn() + """: Beklager herr Overtrollmann! Jeg skulle gi beskjed fra Zip og Zap
at de fullførte, men ikke hadde tid til å møte deg personlig grunnet skade.

    De fullførte? Dette er jo strålende! Hmm, du ser ut som en kapabel magiker """ + spiller.navn()\
    + """!\n    Bli her på borgen en stund og lær deg noen knep! Kanskje du også kan hjelpe
    noen av de andre her på borgen som trenger hjelp? Men først, la meg gjøre turen hit
    bryet verdt med å vise deg noen av mine personlige kampteknikker...

    *Overtrollmann Vassle viser deg kampteknikker. Du føler deg kraftigere!*
    """

    q2 = Quest(desk2, ferdigdesk2, 1, 1, "Zap")
    q2.legg_til_reward(a=40, d=40)
    q2.legg_til_svarTekst("*Skriv 'ja' for å godta oppdraget*\n> ")
    qlog.legg_til_quest(q2)
