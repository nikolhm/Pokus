"""
                *~ Pokus expansion 2.0 ~*
                           av
                   Gaute Svanes Lunde
"""
import gnom
from klasser import *
from grafikk import *
from quests import *
from prosedyrer import *

#Mainloop:
def shroom_loop(spiller, inv, klasser, spellbook):
    sQlog = klasser.questlog(6)
    bQlog = klasser.questlog(7)
    vassleQlog = klasser.questlog(5)
    ferdig = False

    if not vassleQlog.hent_quest(3).progresjon():
        ferdig = intro_loop(spiller, inv, klasser, spellbook)

    while not ferdig:
        skrivLeir()
        skog_kart(sQlog)

        valg = False
        quest = False
        gaaTilButikk = False
        fight = False
        leirBaal = False
        lagre = False
        oppBakken = False
        while not valg:
            inn = input("Hvor vil du gå?\n> ").lower()

            if inn == "f":
                valg = True
                ferdig = True

            if inn == "q":
                quest = True
                valg = True

            if inn == "k":
                gaaTilButikk = True
                valg = True

            if inn == "s":
                fight = True
                valg = True

            if inn == "l":
                lagre = True
                valg = True

            if inn == "b":
                leirBaal = True
                valg = True

            if inn == "o" and sQlog.hent_quest(4).startet():
                oppBakken = True
                fight = True
                valg = True

        if leirBaal:
            leirBaal = False
            ferdig = sti(spiller, inv, klasser, spellbook)

        while quest:
            inn = sQlog.oppdrag_tilgjengelige(spiller.lvl(), "strategi-teltet").lower()
            kjellQ = sQlog.hent_quest(2)
            bjarteQ = bQlog.hent_quest(5)
            if bjarteQ.startet() and not bjarteQ.ferdig() and (inn == "3" or inn == "13"):
                if not kjellQ.ferdig() and inn == "3" or kjellQ.ferdig() and inn == "13":
                    if not kjellLoop(spiller, inv, klasser, spellbook, bjarteQ):
                        quest = False
            elif not bjarteQ.startet() and kjellQ.ferdig() and inn == "13":
                print(kjellprat())
                input("Trykk enter for å slippe unna\n> ")
            elif inn != "f" and inn != "ferdig":
                try:
                    sQlog.snakk(int(inn) - 1, spiller, inv)
                except ValueError:
                    print("\nDu må skrive et tall!\n")
            else:
                quest = False

        while gaaTilButikk:
            klasser.butikk(4).interaksjon(inv)
            gaaTilButikk = False

        antall = 0
        shrooms = False
        while fight:
            alliert = None
            minst = 1
            maks = 20
            if bQlog.hent_quest(5).ferdig():
                minst = 5
            if shrooms:
                maks = 62
            tall = randint(minst, maks)
            if tall <= 4:
                fiende = generer_banditt(spiller)
            elif tall <= 13:
                fiende = generer_tre(spiller)
            elif tall <= 16:
                fiende = generer_gnom(spiller)
            elif tall <= 19:
                fiende = generer_smaatt(spiller)
            elif tall == 20:
                fiende = generer_guffsliffsaff(spiller)
            elif tall <= 62:
                fiende = generer_shroom(spiller)

            #genererer alliert
            if shrooms:
                if randint(1, 3) == 1:
                    alliert = Fiende(["Gufsne Gry", "Kjipe Knut", "Trøtte Tare", "Tafatte Terje"][randint(0, 3)], \
                    "alliert", Loot(), hp=800+(randint(0, spiller.lvl())*10), a=200, d=120, kp=150+randint(0, 50))
                elif randint(0, 1):
                    alliert = Fiende(["Gale Gro", "Kjappe Kim", "Listige Ludvig", "Modige Mona"][randint(0, 3)], \
                    "alliert", Loot(), hp=1900+(randint(0, spiller.lvl())*30), a=300, d=270, kp=300+randint(0, 60), bonusKp=10)
                else:
                    alliert = Fiende(["Symmetriske Sara", "Magiske Mikkel", "Mirakuløse Marte", "Suverene Sigurd"][randint(0, 3)], \
                    "alliert", Loot(), hp=4000+(randint(0, spiller.lvl())*70), a=1000+randint(0, 100), d=600, \
                    kp=600+randint(0, 150), bonusKp=30, weapon=400)

            fight = angrip(spiller, fiende, inv, klasser, spellbook, alliert)
            if fight:
                antall += 1
            elif shrooms and not spiller.dead():
                fight = oppBakkenLoop(spiller, inv, klasser, spellbook)
            if fight and oppBakken and not sQlog.hent_quest(4).ferdig() and antall == 4:
                skrivTekanne()
                print("""
        ** Med dine suverene sporeferdigheter finner du ut at noen
        har vært her for ikke så lenge siden, til tross for at
        tekannen som står på kok over bålet gir fra seg en svært
        særegen og distraherende lukt. Du nærmer deg! **""")
                input("\nTrykk enter for å gå videre\n> ")
            elif fight and oppBakken and sQlog.hent_quest(4).ferdig() and antall == 4:
                print("    ** Du nærmer deg shroomsenes tilholdsplass **")
                input("\nTrykk enter for å fortsette\n> ")
            if fight and oppBakken and antall == 7:
                fight = oppBakkenLoop(spiller, inv, klasser, spellbook)
                shrooms = fight
                oppBakken = False

        while lagre:
            minnestein(spiller, inv, klasser)
            lagre = False

    if ferdig:
        return verdenskart(spiller)

def intro_loop(spiller, inv, klasser, spellbook):
    skrivBaal()
    print("\n    **", spiller.navn(), """kommer til et utbrent leirbål. Det er blod på bakken, og
    spor etter kamp. Det virker ikke som om det er lenge siden noen var her,
    men det er vanskelig å si hvor de gikk. Hovedstien deler seg til høyre
    og venstre **.
    """)

    input("Trykk enter for å fortsette\n> ")
    print("""\n * En banditt kommer løpende ut fra ingensteds *

    Banditt: Du er en av dem, er du ikke? Jeg skal finne dem! Jeg har fått
    torturert ut noen veibeskrivelser av en ynkelig rotte, og nå slipper
    ingen av dere unna! Og min enmanns-massakre starter med deg!\n""")
    pause()
    if not angrip(spiller, generer_banditt(spiller), inv, klasser, spellbook):
        return True
    clear_screen()
    print("\n" + spiller.navn() + " finner en lapp på banditten! På den står det:")
    print("\n    Hold høyre!\n\nForan deg har du to stier, og du må velge en.")

    return sti(spiller, inv, klasser, spellbook)

def sti(spiller, inv, klasser, spellbook):
    vassleQlog = klasser.questlog(5)
    shroomQlog = klasser.questlog(6)
    while True:
        if vassleQlog.hent_quest(3).progresjon():
            skrivBaal()
        #Sti 1
        print("\nStien deler seg")
        valg1 = input("Hvor vil du gå? (h/v)\n> ")
        while valg1.lower() not in {"h", "v", "høyre", "venstre"}:
            valg1 = input("Hvor vil du gå? Skriv 'høyre' eller 'venstre':\n> ")
        h1 = False
        tekst = spiller.navn() + " tar til venstre med første veideling\n"
        if valg1.lower() in {"h", "høyre"}:
            h1 = True
            tekst =  spiller.navn() + " tar til høyre med første veideling\n"
        print(tekst)
        if randint(1, 3) == 3 and not angrip(spiller, generer_banditt(spiller), inv, klasser, spellbook):
            return True

        #Sti 2
        print("Stien deler seg igjen.")
        valg2 = input("Hvor vil du gå? (h/v)\n> ")
        while valg2.lower() not in {"h", "v", "høyre", "venstre"}:
            valg2 = input("Hvor vil du gå? Skriv 'høyre' eller 'venstre':\n> ")
        h2 = False
        tekst = spiller.navn() + " tar til venstre med andre veideling\n"
        if valg2.lower() in {"h", "høyre"}:
            h2 = True
            tekst =  spiller.navn() + " tar til høyre med andre veideling\n"
        print(tekst)
        if randint(1, 3) == 3 and not angrip(spiller, generer_banditt(spiller), inv, klasser, spellbook):
            return True

        #Sti 3
        print("Stien deler seg igjen.")
        valg3 = input("Hvor vil du gå? (h/v)\n> ")
        while valg3.lower() not in {"h", "v", "høyre", "venstre"}:
            valg3 = input("Hvor vil du gå? Skriv 'høyre' eller 'venstre':\n> ")
        h3 = False
        tekst = spiller.navn() + " tar til venstre med tredje veideling\n"
        if valg3.lower() in {"h", "høyre"}:
            h3 = True
            tekst =  spiller.navn() + " tar til høyre med tredje veideling\n"
        print(tekst)
        if randint(1, 3) == 3 and not angrip(spiller, generer_banditt(spiller), inv, klasser, spellbook):
            return True

        if not h1 and not h2 and not h3:
            print("\n\n    **Du fant stien som fører til ekspedisjonsleiren!**\n\n")
            input("Trykk enter for å fortsette\n> ")
            vassleQlog.hent_quest(3).progresser()
            return False

        elif h1 and h2 and h3:
            print("""\n           ** Du fant en avrevet side fra en gammel bok! På den står det: **
            ---
             _  _  .-'   '-.
            (.)(.)/         \\
             /66            ;   jgs
            o_\\\\-mm-......-mm`~~~~~~~~~~~~~

            ...Rotter har en tendens til å glemme forskjellen på høyre og venstre
            når de blir utsatt for smerte. En som f.eks sier "hold høyre" mener
            da egentlig "hold venstre". En annen nyttig faktaopplysning omhandler...
            ---
            På en eller annen måte finner du veien tilbake til leirbålet du var med
            sist.\n""")
            pause()
        elif h1 and not h2 and h3:
            print("""\n\n        *Du fant et skilt hvor det står "BANDITT-LEIR"* """)
            if shroomQlog.hent_quest(0).startet():
                print("\nDu går inn til leiren.")
                input("\nTrykk enter for å fortsette\n> ")
                return banditt_loop(spiller, inv, klasser, spellbook)
            else:
                print("\nDet er ikke en banditt-leir", spiller.navn(), "er på jakt etter.")
                print("Du bestemmer deg for å dra tilbake til leirbålet.")
                pause()
        elif not h1 and h2 and not h3 and shroomQlog.hent_quest(0).startet():
            print("Blindvei! Du får en følelse av at rotters stedsans ikke er helt bra.")
            print("Kanksje du kan prøve det motsatte? Du drar tilbake til leirbålet.")
            pause()
        else:
            print("Blindvei! På en eller annen måte finner du veien tilbake til leirbålet.")
            pause()

def banditt_loop(spiller, inv, klasser, spellbook):
    sQlog = klasser.questlog(6)
    bQlog = klasser.questlog(7)
    if not sQlog.hent_quest(0).ferdig():
        print(spiller.navn(), "har møtt en banditt!")
        print("Banditten tror", spiller.navn(), "også er en banditt.")
        print("Alle smiler til deg som en felles banditt, \nmen noe er ikke som det skal i leiren.")
        input("\nTrykk enter for å fortsette\n> ")

    ferdig = False
    while not ferdig:
        skrivBandittLeir()
        banditt_kart(bQlog)

        valg = False
        quest = False
        gaaTilButikk = False
        skogen = False
        sopp = False
        duell = False
        while not valg:
            inn = input("Hvor vil du gå?\n> ").lower()

            if inn == "f":
                valg = True
                ferdig = True

            if inn == "q":
                quest = True
                valg = True

            if inn == "k":
                gaaTilButikk = True
                valg = True

            if inn == "d":
                duell = True
                valg = True

            if inn == "s":
                skogen = True
                valg = True

            if inn == "p" and bQlog.hent_quest(2).startet():
                sopp = True
                valg = True

        while quest:
            inn = bQlog.oppdrag_tilgjengelige(spiller.lvl(), "stortreet").lower()
            if inn == "2" and bQlog.hent_quest(1).progresjon() == 6 and not bQlog.hent_quest(1).progresjon_liste()[0]:
                if not ussleUlvLoop(spiller, inv, klasser, spellbook):
                    inn = "f"
            if inn != "f" and inn != "ferdig":
                try:
                    bQlog.snakk(int(inn) - 1, spiller, inv)
                except ValueError:
                    print("\nDu må skrive et tall!\n")
            else:
                quest = False
            if bQlog.hent_quest(5).ferdig():
                sQlog.hent_quest(0).progresser()
                sQlog.hent_quest(12).sett_ferdig()

        while gaaTilButikk:
            klasser.butikk(5).interaksjon(inv)
            gaaTilButikk = False

        while skogen:
            tall = randint(1, 15)
            if tall >= 14:
                fiende = generer_tre(spiller)
            elif tall >= 10:
                fiende = generer_gnom(spiller)
            elif tall >= 6:
                fiende = generer_banditt(spiller)
            elif tall >= 1:
                fiende = generer_smaatt(spiller)

            skogen = angrip(spiller, fiende, inv, klasser, spellbook)

        while sopp:
            if not bQlog.hent_quest(2).ferdig():
                print("\n    Sopp:" + Fore.RED  + """ Patetiske lille menneske, gjør som vi befaler!
          Du skal dra ut i skogen, finne et tre vi har vurdert verdig, og lage et
          totem til ære for oss! Det kan alle dere små skapninger bruke til å tilbe
          oss. Du vet at vi har vurdert et tre verdig hvis det angriper deg. Gi
          totemet til en av våre mest fanatiske tilhengere. Dra nå!

          Skulle du komme tilbake til dette hemmelige soppstedet senere, kan vi
          restorere deg til ditt fulle potensiale, men kun hvis du viser deg verdig
          vår velsignelse.\n""" + Style.RESET_ALL)
                sopp = False
                bQlog.hent_quest(2).progresser()
                input("Trykk enter for å fortsette\n> ")
            elif angrip(spiller, generer_liten_sopp(spiller), inv, klasser, spellbook):
                print("\n" + spiller.navn(), "fikk restorert", spiller.restorer(1000), "helsepoeng og", \
                spiller.restorer_kp(300), "konsentrasjonspoeng gjennom de magiske soppenes velsignelse.\n")
                input("Trykk enter for å fortsette\n> ")
            sopp = False

        while duell:
            progresjon = 6 + sum([int(bQlog.hent_quest(x).ferdig()) for x in range(6, len(bQlog.hent_qLog()))])
            try:
                q = bQlog.hent_quest(progresjon)
            except IndexError:
                print("\n        *Det er ingen flere å duellere mot her*\n")
                input("Trykk enter for å fortsette\n> ")
                duell = False
                break
            if progresjon != 11 or bQlog.hent_quest(4).startet():
                q.sett_tilgjengelig()
            else:
                print("\n      *Onde Olga godter seg med seiersinntekten du skaffet henne*")
                print("      *Det er ingen flere å duellere mot på dette tidspunktet*\n")
                input("Trykk enter for å dra tilbake\n> ")
                duell = False
                break
            if not q.startet():
                bQlog.snakk(progresjon, spiller, inv)

            if q.startet() and q.progresjon():
                bQlog.snakk(progresjon, spiller, inv)
                duell = False
                if progresjon +1 != len(bQlog.hent_qLog()) and (progresjon+1 != 11 or bQlog.hent_quest(4).startet()):
                    if input("\nVil du høre om neste duellant?\n> ").lower() in {"j", "ja", "yes", "y"}:
                        duell = True
                if bQlog.hent_quest(11).ferdig():
                    bQlog.hent_quest(4).progresser()

            elif q.startet() and inv.penger() >= 500:
                inv.penger(-500)
                print("Du blir trukket 500 gullstykker for inngangsbillett.")
                input("Trykk enter for å fortsette\n> ")
                fiende = generer_duellant(progresjon - 6, spiller)
                if angrip(spiller, fiende, inv, klasser, spellbook):
                    q.progresser()
                else:
                    duell = False

            elif q.startet():
                print("\nDu har ikke nok gullstykker til å bli med i en duell!\n")
                input("Trykk enter for å dra tilbake til leiren\n> ")
                duell = False

            else:
                duell = False

            q.sett_tilgjengelig(False)

    if ferdig:
        return False

def kjellLoop(spiller, inv, klasser, spellbook, bjarteQ):
    q = klasser.questlog(6).hent_quest(12)
    if bjarteQ.sjekk_ferdig():
        print("    Hvorfor er du fremdeles her og slenger? Se til å gi den forbaskede",\
        "\n    fingeren til den hersens banditten!")
        input("\nTrykk enter for å fortsette\n> ")
        return True
    elif q.sjekk_ferdig() and not q.ferdig():
        print("\n    Supert", spiller.navn() + "! Her har du en kopi av fingeren min!\n")
        q.reward(inv, spiller, klasser.questlog(6))
        q.sett_ferdig()
        bjarteQ.progresser()
        input("Trykk enter for å fortsette\n> ")
        return True
    elif q.startet():
        print("""    Tresorten du leter etter heter Guffsliffsaff, og finnes
    rundt omkring her i skogen. Den er relativt sjelden, men du burde støte
    på den før eller siden. Kom tilbake hit når du har funnet den, og pass
    på å ikke være borti den selv!\n""")
        input("Trykk enter for å fortsette\n> ")
        return True
    print("\n    " + spiller.navn() + """!
    Hva sier du, vil du ha fingeren min? Det er den mest uforskammede
    forespørselen jeg noensinne har hørt! Om du vil ha den, må du sloss
    mot meg først! Ved mindre...

    Jeg har en idé. Om det er sant som du sier, at dette er den eneste
    måten å få de forbeskede bandittene til å slutte å jakte oss, burde
    jeg gi deg fingeren. Og jeg tror jeg har en måte vi kan gjøre det
    på uten å ta frem kniven.""")
    input("\nTrykk enter for å fortsette\n> ")
    print("""
    Gjennom århundrer med å nøye observere tresorter, har jeg funnet en
    bemerkelsesverdig tresort som har en helt spesiell egenskap; Dens
    grener kan etterligne det de kommer i kontakt med! Det eneste du
    trenger å gjøre er å finne tresorten, temme den og ta den med til
    meg. Den kan være noe aggressiv, så pass på!\n""")
    if input("Ønsker du å hjelpe Kjedelige Kjell å beholde fingeren sin?   (ja/nei)\n> ").lower() in {"ja", "j"}:
        q.start()
        print("""\n    Strålende! Tresorten du leter etter heter Guffsliffsaff, og finnes
    rundt omkring her i skogen. Den er relativt sjelden, men du burde støte
    på den før eller siden. Kom tilbake hit når du har funnet den, og pass
    på å ikke være borti den selv!\n""")
        input("Trykk enter for å fortsette\n> ")
        return True
    elif input("\nØnsker du å angripe Kjedelige Kjell og kutte av ham fingeren?\n> ").lower() in {"ja", "j"}:
        loot = Loot()
        loot.legg_til_item(Item("Kjedelige sko", "shoes", d=100, xHp=70), 1)
        fiende = Fiende("Kjedelige Kjell", "magiker", loot, a=350, hp=3000, d=240, kp=350, bonusKp=4)
        if not angrip(spiller, fiende, inv, klasser, spellbook):
            return False
        bjarteQ.progresser()
    return True

def ussleUlvLoop(spiller, inv, klasser, spellbook):
    print("    Tusen takk " + spiller.navn() + """!
    Nå kan jeg endelig vinne hjertet til Fagre Frida! Håper ikke jeg må
    sloss mot eksen hennes, har hørt hun er ganske grusom...

    Uansett, takk for hjelpen! Dessverre kan jeg ikke etterlate noen
    løse tråder, tenk om andre skulle lært de samme kunstene av deg?
    Da ville jeg ikke vært særlig spesiell lengre! Dette har vært gøy,
    men jeg er redd det er på tide for deg å opphøre å eksistere.\n""")
    input("Trykk enter for å fortsette\n> ")
    skrivBanditt()
    print("\nUssle Ulv har knivstukket deg!")
    skade = spiller.hp() // 3
    spiller.mist_liv(skade)
    print(spiller.navn(), "mistet", skade, "liv!\n")
    loot = Loot()
    loot.legg_til_item(30, 1)
    ussleUlv = Fiende("Ussle Ulf", "snik", loot, a=800, d=80, hp=3000, kp=500, weapon=130, bonusKp=8)
    if angrip(spiller, ussleUlv, inv, klasser, spellbook):
        klasser.questlog(7).hent_quest(1).progresser_liste(0)
        return True
    return False

def oppBakkenLoop(spiller, inv, klasser, spellbook):
    sQlog = klasser.questlog(6)
    vassleQ = klasser.questlog(5).hent_quest(3)
    navn = spiller.navn()
    if not sQlog.hent_quest(4).ferdig():
        print("""
        ** Du sanser en sterk magisk kraft i nærheten! **\n""")
        input("Trykk enter for å gå videre\n> ")
        skrivSkjegghattShroom()
        print("        ** En levende forvokst sopp kommer bort til deg **\n")
        print(  """Skjegghatt Shroom: """ + Fore.RED + "Du er ikke velkommen her " + spiller.navn() + ".\n" + Style.RESET_ALL)
        input("Trykk enter for å fortsette\n> ")
        clear_screen()
        skrivSkjegghattShroom()
        print(spiller.navn(), "har møtt Skjegghat Shroom! Så grufullt!\n")
        loot = Loot()
        loot.legg_til_item(Item("Soppskjegg", "beard", xKp=70, ekstraKp=4), 1)
        loot.sett_loot_tekst("et soppskjegg")
        fiende = Fiende("Skjegghatt Shroom", "shroom", loot, a=350, d=600, hp=12345, kp=1000, bonusKp=30)
        if not angrip(spiller, fiende, inv, klasser, spellbook): return False
        sQlog.hent_quest(4).progresser()
        sQlog.snakk(4, spiller, inv)
        return False
    else:
        while True:
            skrivTekanne()
            print("\n    Du er i utkanten av Shroom-terretorium. Her er dine alternativer:")
            print("    --                    ~~                 ~~                    --")
            print("    Fronten (s)           Hjelp ekspedisjonsmagikerne å drepe shrooms")
            if sQlog.hent_quest(7).startet() and not sQlog.hent_quest(7).progresjon():
                print("    Pàn Tú (q)            Hør hva Pàn Tú har å si")
            if sQlog.hent_quest(9).startet():
                print("    Tjernet (t)           Snik deg bort til det magiske tjernet")
            print("    Dra tilbake (f)       Dra tilbake til ekspedisjonsleiren")
            print("    --                    ~~                 ~~                    --")
            inn = input("Hva vil du gjøre?\n> ").lower()

            #Quest 10 - forurens tjernet
            if inn == "t" and sQlog.hent_quest(9).startet():
                clear_screen()
                print("\n\n    * Du sniker deg inn til midten av shroom-terretorium * \n")
                pause()
                skrivSopp("familie")
                print("Du er blitt oppdaget av en soppfamilie!\n")
                pause()
                loot = Loot()
                item = Item("Konsentrasjonspulver", "restoring", kp=550)
                item.sett_loot_tekst("en stripe konsentrasjonspulver")
                loot.legg_til_item(item, 1)
                fiende1 = Fiende("Suillus Soppfar", "shroom", loot, hp=5000, a=300, d=400, kp=250, bonusKp=25, weapon=400)
                loot = Loot()
                item = Item("Konsentrasjonspulver", "restoring", kp=500)
                item.sett_loot_tekst("en stripe konsentrasjonspulver")
                loot.legg_til_item(item, 1)
                fiende2 = Fiende("Suillus Soppmor", "shroom", loot, hp=4000, a=600, d=10, kp=400, bonusKp=25)
                loot = Loot()
                item = Item("Konsentrasjonspulver", "restoring", kp=450)
                item.sett_loot_tekst("en stripe konsentrasjonspulver")
                loot.legg_til_item(item, 1)
                fiende3 = Fiende("Suillus Soppbarn","shroom", loot, hp=2000, a=100, d=1000, kp=1000, bonusKp=25)
                print("\n      * Dette er en kamp med flere fiender. Du kan kun angripe en fiende *")
                print("        om gangen, men alle fiendene vil angripe deg. For å skifte ")
                print("        hvilken fiende du angriper, skriv 'skift fiende', 'skift' eller")
                print("        bare 'sf'. Du bruker ikke en tur på å skifte fiende.\n")
                pause()
                skrivSopp("familie")
                if not angrip(spiller, fiende1, inv, klasser, spellbook, fiende2=fiende2, fiende3=fiende3):
                    return False
                print("\n\n    Bråket fra soppfamilien lokket flere shrooms til deg!\n")
                pause()
                stein = Fiende("Soppinfisert Stein", "stein", loot, hp=250, a=40, d=50, kp=50)
                if not angrip(spiller, generer_shroom(spiller), inv, klasser, spellbook): return False
                if not angrip(spiller, generer_shroom(spiller), inv, klasser, spellbook, fiende2=stein): return False
                if not angrip(spiller, generer_shroom(spiller), inv, klasser, spellbook, fiende2=generer_shroom(spiller)):
                    return False
                clear_screen()
                print("\n\n    * Du har nådd tjernet! Tre store shrooms vokter det! *\n")
                pause()
                fiender = generer_store_shrooms(spiller)
                if not angrip(spiller, fiender[0], inv, klasser, spellbook, fiende2=fiender[1], fiende3=fiender[2]):
                    return False
                if not vassleQ.progresjon_liste()[0]:
                    avslutningsLoop(spiller)
                    vassleQ.progresser_liste(0)
                    sQlog.hent_quest(9).progresser()
                    return False
                else:
                    print("  * Du har allerede forurenset tjernet! Du drar tilbake til fronten. *\n")
                    pause()
                    return True

            #Quest 9 - Snakk med Zap
            if inn == "s" and sQlog.hent_quest(8).startet() and not sQlog.hent_quest(8).progresjon():
                alliert = Fiende("Zap", "alliert", Loot(), hp=13000, a=560, d=320, kp=800, bonusKp=20)
                if not angrip(spiller, generer_shroom(spiller), inv, klasser, spellbook, alliert): return False
                print("""
              Zap: """ + navn + """! Så godt å se deg! Jeg vet ikke hva jeg skal gjøre!
                   Zip kom forbi her for litt siden, vi sloss, og, og- vi er forrådt! Av Zip!
                   Jeg sloss nettopp mot Zip! Vi må dra etter henne, hun kan ikke være seg
                   selv! Det må være disse udugelige, forvrengte, forbaskede forvokste soppene
                   som har tatt over sinnet hennes! Hva skal vi gjøre?\n""")
                input("Trykk enter for å fortsette\n> ")
                print("""
 Symmetriske Sara: Du må ta det rolig Zap! Det nytter ikke å kjempe mer nå, du må hvile deg!
                   Godt å se deg """ + navn + """, vi fant Zap like hysetirsk som han er nå,
                   vi tror han er i sjokk. Rapporter tilbake til Strategiske Synne, vi skal
                   ta vare på Zap!\n""")
                input("Trykk enter for å dra tilbake\n> ")
                sQlog.hent_quest(8).progresser()

            #Slåss mot shrooms ved fronten
            elif inn == "s": return True

            #Dra tilbake til leiren
            if inn == "f": return False

            #Quest 8 - Snakk med Pàn Tú sin kontakt
            if inn == "q" and sQlog.hent_quest(7).startet() and not sQlog.hent_quest(7).progresjon():
                print("""
    Pàn Tú: Din timing er upåklagelig. Vi trenger å vite hva som har skjedd
            her før alle ekspedisjonsmagikerne utsletter alle spor og alt
            levende her i skogen! Som tidligere nevnt har jeg kontakter inne
            i den åpne shroom-leiren, men kun sopp-fanatikere får gå inn i
            shroom-terretorium uten å bli angrepet av den andre leiren.
            Heldigvis har jeg fått beskjed om at et sendebud vil bli sendt
            til den åpne plassen nord for her. Kan du dra opp dit og rydde
            vekk eventuelle fiendtlige shrooms?\n""")
                if input("Vil du dra nord til sendebudet?       (ja/nei)\n> ").lower() in {"ja", "j"}:
                    for x in range(4):
                        if not angrip(spiller, generer_shroom(spiller), inv, klasser, spellbook): return False
                    skrivBanditt()
                    print("""\n
  Bjarte Banditt: """ + navn + "? " + navn + """, er det deg?
                  Hv- hvor er jeg? Hvem er jeg? HVEM ER J- """ + Fore.RED + "Hei " + navn + """.
                  Det er høyst beklagelig at vi må benytte oss av tosker som denne for
                  å kommunisere, men slik den politiske situasjonen er nå ser vi ingen
                  annen mulighet. Tiden renner ut fort, og det vi har å si er viktig,
                  så lytt nøye """ + navn + """. Vi er ikke den Bamhjertiges egne barn,
                  men man kan si vi er dens barnebarn. Vi er ikke en intensjon, men et
                  heldig uhell fremkalt av den Bamhjertiges første barn. Vi er bevis på
                  en ny sirkel av liv.\n""" + Style.RESET_ALL)
                    input("Trykk enter for å fortsette\n> ")
                    print(Fore.RED + """
                  Vi er et svar, men vi er ikke ditt svar """ + navn + """. Du vil finne det senere.
                  Vår ende er nær, men frø er plantet. En ny verden vil reise seg i
                  asken til den forrige, og tapt harmoni vil oppstå på ny.

                  Hold et åpent sinn.\n""" + Style.RESET_ALL)
                    input("Trykk enter for å fortsette\n> ")
                    clear_screen()
                    skrivSkjegghattShroom()
                    print("\n ** En shroom avbryter møtet **\n")
                    print("  Boletus Pascuus: " + Fore.RED + "Hva foregår her? Tilbe oss!\n" + Style.RESET_ALL)
                    print(spiller.navn(), "og Bjarte Banditt har møtt en fiendtlig shroom!")
                    loot = Loot()
                    fiende = Fiende("Boletus Pascuus", "shroom", loot, hp=7000, a=450, d=300, kp=500, bonusKp=15)
                    dynamiskLoot(loot, fiende, spiller)
                    loot = Loot()
                    item = Item("Bjartes sko", "shoes", xHp=400, d=-130)
                    item.sett_loot_tekst("Bjarte Banditt sine sko")
                    loot.legg_til_item(item, 50)
                    alliert = Fiende("Bjarte Banditt", "banditt", loot, hp=12000, a=450, d=-400, kp=700, bonusKp=30)
                    if not angrip(spiller, fiende, inv, klasser, spellbook, alliert): return False
                    clear_screen()
                    skrivBanditt()
                    print("\n ** Bjarte Banditt har gått fra vettet! **\n")
                    print(spiller.navn(), "har møtt Bjarte Banditt!")
                    fiende = alliert
                    if fiende.dead(): fiende.mist_liv(-4000, True)
                    if not angrip(spiller, fiende, inv, klasser, spellbook): return False
                    sQlog.hent_quest(7).progresser()
                    print("\nDu drar tilbake til utkanten av shroom-terretoriumet, men Pàn Tú er")
                    print("ikke å se. Kanskje du burde snakke med Zip?")
                    input("\nTrykk enter for å fortsette\n> ")

def avslutningsLoop(spiller):
    navn = spiller.navn()
    clear_screen()
    red = Fore.RED
    r = Style.RESET_ALL
    print("""\n
    * Shroomsene er for svake til å stoppe deg. Du går bort til tjernet. *\n
  {0:>10}: Allium Sativum Tjernum Forurensum!
              * {0} kastet Kast Hvitløk. *
              Tjernet ble forurenset!\n""".format(navn))
    pause()
    print("""
       Boletus Edulis: {}Neeeeeeeei! Det stakkers tjernet vårt! Hva har du gjort?!
                       Hvordan skal de små steinsoppene vokse opp og bli som meg
                       nå? Dette var begynnelsen på en ny sirkel av liv!\n{}""".format(red, r))
    pause()
    print("""
    Agaricus Augustus:{} Vårt fødested! Vår kilde til inspirasjon, magi, til livet
                       selv! Hvilken ondskap vil gjøre noe slikt!\n {}""".format(red, r))
    pause()
    print("""
Cantharellus Cibarius:{} Den Bamhjertige vil ikke glemme dette! Selv om han ikke
                       er vår direkte skaper, vil han beskytte oss slik han
                       beskytter alle andre! Tyranniet deres vil ende, og en
                       dag vil en stakkers kantarell som meg bli husket som en
                       martyr! Alle vil tilbe meg!\n {}""".format(red, r))
    pause()
    print("""
    Agaricus Augustus:{} Ahh, ikke han og. Dette er hvorfor den Bamhjertige ikke
                       lar oss være med på rådsmøter. Hvordan skal man gjennomføre
                       revolusjon når man konstant krever tilbedelse? Blir ikke
                       noe bedre verden av det, da er vi jo like ille som Vassle
                       selv. Dra nå {}, la oss visne i fred!\n {}""".format(red, navn, r))
    input("Trykk enter for å dra tilbake til Ekspedisjonsleiren\n> ")

def angrip(spiller, fiende, inv, klasser, spellbook, alliert=None, fiende2=None, fiende3=None):
    sQlog = klasser.questlog(6)
    bQlog = klasser.questlog(7)
    fiende1 = fiende
    fiender = [fiende1]
    if alliert: alliert.skriv_ut()
    skriv_ut(spiller, fiende)
    if fiende2:
        fiende2.skriv_ut()
        fiender.append(fiende2)
    if fiende3:
        fiende3.skriv_ut()
        fiender.append(fiende3)
    uCD = 0 #utforsk CoolDown
    bundetCD = 0
    pantu = False
    target = fiende
    while True:
        #tur angir at det er brukeren sin tur til å handle.
        if bundetCD > 0:
            tur = False
            inn = ""
            print(spiller.navn(), "er bundet fast.")
        else:
            inn = input("\nHva vil du gjøre?\n> ").lower()
            tur = kommandoer(inn, spiller, fiende, inv, klasser, spellbook)

        if inn == "f" or inn == "flykt":
            print(spiller.navn(), "drar tilbake til leiren.")
            return False

        #Skift fiende - kun når det er flere fiender til stedet.
        if inn in {"skift fiende", "skift", "sf", "bytt fiende", "bf"} and fiende2:
            print("    ------------------------- SKIFT FIENDE -------------------------")
            print("    Fiende 1: {:55s} {}".format(fiende1.skriv_ut(True), " DØD" * int(fiende1.dead())))
            print("    Fiende 2: {:55s} {}".format(fiende2.skriv_ut(True), " DØD" * int(fiende2.dead())))
            if fiende3:
                print("    Fiende 3: {:55s} {}".format(fiende3.skriv_ut(True), " DØD" * int(fiende3.dead())))
            print("    ------------------------- *****~***** -------------------------")
            inn = input("\nHvem vil du angripe?\n> ").lower()
            if inn in {"fiende 1", "fiende1", "1", fiende1.navn()}:
                if fiende1.dead(): print("Denne fienden er død!")
                else:
                    fiende = fiende1
                    print("Du angriper nå", fiende1.navn())
            if inn in {"fiende 2", "fiende2", "2", fiende2.navn()}:
                if fiende2.dead(): print("Denne fienden er død!")
                else:
                    fiende = fiende2
                    print("Du angriper nå", fiende2.navn())
            if fiende3 and inn in {"fiende 3", "fiende3", "3", fiende3.navn()}:
                if fiende3.dead(): print("Denne fienden er død!")
                else:
                    fiende = fiende3
                    print("Du angriper nå", fiende3.navn())

        if inn in {"tillkall sussesopp", "sussesopp", "tilkall", "ts"} and sQlog.hent_quest(13).ferdig() \
        and spiller.kp() >= 200:
            if alliert:
                print("Du har allerede en alliert i denne kampen!")
            else:
                alliert = Fiende("Psilocybe Semilanceata", "alliert", Loot(), hp=800, a=300, d=500, kp=1500, bonusKp=22, ending="en")
                print(spiller.navn(), "tilkalte en magisk sopp til å hjelpe i kampen!")
                spiller.bruk_kons(200)
                tur = False

        #alliert gjør sin tur
        if alliert and not tur and not fiende.dead():
            if alliert.kp() >= 70 and spiller.hp() / spiller.xHp() <= 0.6 and randint(0, 3) == 0:
                print(alliert.navn() + alliert.ending(), "kastet en Hjelpende Hånd! Du kjenner en hånd massere deg på ryggen.")
                print(spiller.navn(), "restorerte", spiller.restorer(randint(290, 320 + round(alliert.xKp() / 2))), "liv.")
                alliert.kp(-70)
            elif alliert.kp() >= 70 and alliert.hp() / alliert.xHp() <= 0.6 and randint(0, 3) == 0:
                print(alliert.navn() + alliert.ending(), "kastet Restituer!")
                print(alliert.navn() + alliert.ending(), "restorerte", alliert.restorer(300), "liv.")
                alliert.kp(-70)
            elif alliert.kp() >= 150 and spiller.kp() / spiller.xKp() <= 0.35 and randint(0, 5) == 0:
                print(alliert.navn() + alliert.ending(), "kastet Konsentrert Hjelp!")
                print(spiller.navn(), "restorerte", spiller.restorer_kp(300), "kp.")
                alliert.kp(-150)
            elif alliert.kp() >= 130 and not randint(0, 10):
                print(alliert.navn() + alliert.ending(), "kastet Full Kraft!")
                fiende.mist_liv(alliert.a())
                alliert.kp(-130)
            else:
                print(alliert.navn(), "angrep", fiende.navn() + fiende.ending() + ".")
                fiende.angrepet(alliert.a(), alliert.weapon_dmg(), angriper=alliert)

        #Her sjekkes om fienden er død. Om så, får karakteren loot og xp.
        if fiende.dead():
            print("--------------------------------------------------------------------"+\
            "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
            spiller.kons()
            spiller.gi_xp(fiende.xp())
            fiende.loot(spiller, inv)

            #Quests:
            #Banditt q1:
            if fiende.navn() == "Banditt" and bQlog.hent_quest(0).startet() and not \
            bQlog.hent_quest(0).ferdig() and randint(0, 2) == 1:
                print("Du fant et av Lugubre Lasses lommeur!")
                bQlog.hent_quest(0).progresser()

            #Banditt q6:
            if fiende.navn() == "Kjedelige Kjell":
                print("Du kutter av fingeren til Kjedelige Kjell.")
                print("Du får 3 ondhetspoeng.")
                spiller.evil_points(3)

            #Shroom q2
            if fiende.race() == "gnom" and sQlog.hent_quest(1).startet() and \
            not sQlog.hent_quest(1).ferdig() and randint(1, 6) >= 4:
                sQlog.hent_quest(1).progresser()
                print("Du fant en av de stjålne forsyningene!")

            #Shroom q3
            q = sQlog.hent_quest(2)
            if q.startet():
                if fiende.navn() == "Barsk Bøk" and not q.progresjon():
                    print("Du nedtegner dine oppdagelser med den barske bøken.")
                    q.progresser()
                elif fiende.navn() == "Fiffig Furu" and not q.progresjon_liste()[0]:
                    print("Du nedtegner dine oppdagelser med den fiffige furuen.")
                    q.progresser_liste(0)
                elif fiende.navn() == "Brysom Bjørk" and not q.progresjon_liste()[1]:
                    print("Du nedtegner dine oppdagelser med den brysomme bjørken.")
                    q.progresser_liste(1)
                elif fiende.navn() == "Ondskapsfull Osp" and not q.progresjon_liste()[2]:
                    print("Du nedtegner dine oppdagelser med den ondskapsfulle ospen.")
                    q.progresser_liste(2)
                elif fiende.navn() == "Rasende Rogn" and not q.progresjon_liste()[3]:
                    print("Du nedtegner dine oppdagelser med den rasende rognen.")
                    q.progresser_liste(3)

            #Shroom q6
            if sQlog.hent_quest(5).startet() and not sQlog.hent_quest(5).ferdig():
                sQlog.hent_quest(5).progresser()

            #Shroom bq1
            if fiende.race() == "tre" and bQlog.hent_quest(2).ferdig() and \
            not sQlog.hent_quest(10).sjekk_ferdig() and randint(1, 5) == 1:
                sQlog.hent_quest(10).progresser()
                print("Du klarte å lage et totem ut av restene til", fiende.navn() + fiende.ending())

            #Shroom bq2
            if not sQlog.hent_quest(11).sjekk_ferdig() and sQlog.hent_quest(7).ferdig() \
            and (fiende.race() == "shroom" and randint(1, 5) == 1 or randint(1, 100) == 42):
                print("Du fant biter av en hemmelig korrenspondanse fra {}!".format(["Zip", "Pàn Tú"][randint(0, 1)]))
                sQlog.hent_quest(11).progresser()

            #Shroom q13
            if fiende.race() == "guffsliffsaff" and sQlog.hent_quest(12).startet() \
            and not sQlog.hent_quest(12).progresjon():
                sQlog.hent_quest(12).progresser()
                print("Du plukker opp de tamme restene av guffsliffsaff-grenen.")

            #Shroom bq3
            if not sQlog.hent_quest(13).sjekk_ferdig() and sQlog.hent_quest(7).ferdig() \
            and randint(1, 50) == 42:
                print("Du fant en magisk kosesopp! Kankje noen i leiren savner den?")
                sQlog.hent_quest(13).progresser()

            input("Trykk enter for å fortsette\n> ")
            fiender.remove(fiende)
            if not fiende1.dead():
                fiende = fiende1
            elif fiende2 and not fiende2.dead():
                fiende = fiende2
            elif fiende3 and not fiende3.dead():
                fiende = fiende3
            if fiende.dead():
                return True

        #Fiendens tur
        if not tur:
            target = fiende
            for i in range(len(fiender)):
                fiende = fiender[i]
                #oppholdt
                if fiende.oppholdt():
                    print(fiende.navn() + fiende.ending(), "er oppholdt.")
                    continue

                #Alliert
                if alliert and randint(0, 3) == 0:
                    if fiende.kp() >= 450 and randint(0, 10) == 0:
                        print(fiende.navn() + fiende.ending(), "kastet Avskjær Hjelp!")
                        alliert.mist_kp(1000)
                        fiende.kp(-450)
                    else:
                        alliert.angrepet(fiende.a(), fiende.weapon_dmg(), angriper=fiende)

                #Guffsliffsaff - spiller til tre
                elif fiende.navn() == spiller.navn() + " v2" and fiende.hp() <= int(fiende.xHp() / 4):
                    print("Guffsliffsaffen er for svak til å opprettholde formen sin!")
                    print("Guffsliffsaffen transformerer seg igjen.")
                    fiende = generer_guffsliffsaff(spiller, "kvist", fiende)
                    fiender = [fiende]
                    fiende1 = fiende
                    target = fiende
                    input("Trykk enter for å fortsette\n> ")
                #Shrooms - Bakkekontakt
                elif fiende.race() == "shroom" and fiende.kp() >= 350 and fiende.hp() <= 800 and not randint(0, 6):
                    print(fiende.navn() + fiende.ending(), "kastet Bakkekontakt!", \
                    fiende.navn() + fiende.ending(), "suger opp næring fra bakken!")
                    print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(randint(50, 85) * 10), "liv.")
                    fiende.kp(-350)
                #Shrooms - binde fast
                elif fiende.race() == "shroom" and fiende.kp() >= 300 and bundetCD <= 0 and randint(1, 17) == 4:
                    print(fiende.navn() + fiende.ending(), "har tilkalt røtter fra bakken som binder deg fast!")
                    bundetCD = 2
                    fiende.kp(-300)
                #Tre fiender-system: soppfamilie og sistebossene
                #heal
                elif fiende.navn() in {"Suillus Soppbarn", "Agaricus Augustus"} and not fiende1.dead() and \
                fiende.kp() >= 450 and randint(1, 3) == 1 and fiende1.hp() <= fiende1.xHp() - 500:
                    print(fiende.navn(), "kastet Motivér!")
                    print(fiende1.navn(), "restorerte", fiende1.restorer(1000), "liv.")
                    fiende.kp(-450)
                #Intensivèr
                elif fiende.navn() in {"Suillus Soppbarn", "Agaricus Augustus"} and fiende.kp() >= 500 \
                and randint(1, 15) == 1:
                    print(fiende.navn(), "kastet Intensivér!")
                    fiende.kp(-500)
                    for f in fiender:
                        f.a(20)
                        print(f.navn(), "fikk 20 angrepspoeng.")
                #distraher
                elif fiende.navn() in {"Suillus Soppbarn", "Agaricus Augustus"} and fiende.kp() >= 230 \
                and randint(1, 10) == 1:
                    print(fiende.navn(), "kastet Distraher!")
                    print(spiller.navn(), "mistet", spiller.mist_kp(randint(150, 230)), "kp.")
                    fiende.kp(-230)
                #felles røykepause
                elif fiende.navn() in {"Suillus Soppbarn", "Agaricus Augustus"} and fiende.kp() >= 280 \
                and randint(1, 4) == 1:
                    print(fiende.navn(), "kastet Felles Røykepause")
                    fiende.kp(-280)
                    for f in fiender:
                        print(f.navn(), "restorerte", f.restorer(250), "liv, og fikk lungebetennelse.")
                #Solidifiser
                elif fiende.navn() in {"Cantharellus Cibarius", "Suillus Soppfar"} and fiende.kp() >= 200 \
                and randint(1, 7) == 2:
                    fiende.kp(-200)
                    fiende.d(30)
                    print(fiende.navn(), "kastet Solidifiser!")
                    print(fiende.navn(), "fikk 30 defensivpoeng.")
                #Raseri
                elif fiende.navn() in {"Suillus Soppmor", "Boletus Edulis"} and fiende.kp() >= 350 \
                and randint(1, 8) == 1:
                    fiende.kp(-350)
                    print(fiende.navn(), "kastet Raseri!")
                    print(spiller.navn(), "mistet", spiller.mist_liv(400), "liv av raseriet.")
                #Untouchable shroom
                elif fiende.navn() in {"Suillus Soppmor", "Boletus Edulis"} and fiende.kp() >= 250 \
                and randint(1, 7) == 1 and ("Suillus Soppbarn" in fiender or "Agaricus Augustus" in fiender):
                    fiende.kp(-250)
                    if fiende.navn() == "Suillus Soppmor":
                        print(fiende.navn(), "kastet Beskytt Barn!")
                        print(fiende3.navn(), "går i ett med jorden for to runder.")
                        fiende3.set_untouchable(True, 2)
                    else:
                        print(fiende.navn(), "kastet Beskytt Sjampinjong!")
                        print(fiende2.navn(), "går i ett med jorden for to runder.")
                        fiende2.set_untouchable(True, 2)
                #Trær
                elif fiende.race() == "tre" and fiende.kp() >= 230 and randint(1, 8) == 4:
                    print(fiende.navn() + fiende.ending(), "kastet Rotfest!")
                    fiende.kp(-230)
                    fiende.d(50)
                    print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(380), "liv og fikk 50 ekstra defensivpoeng.")
                #Utforsk
                elif fiende.race() == "snik" and fiende.kp() >= 195 and uCD >=0 and randint(1, 5) >= 3:
                    print(fiende.navn() + fiende.ending(), "kastet Utforsk!")
                    fiende.bruk_kons(195)
                    uCD = -6
                #Smidige Sandra - Duell
                elif fiende.navn() == "Smidige Sandra":
                    if fiende.untouchableCD():
                        print("Smidige Sandra restorerte 800 hp.")
                        fiende.restorer(800)
                        fiende.kp(-15)
                    elif fiende.hp() < 900 and fiende.kp() >= 100 and not fiende.untouchableCD():
                        print("Smidige Sandra har sklidd inn i mørket for to runder!")
                        fiende.set_untouchable(True, 2)
                        fiende.kp(-100)
                    elif fiende.kp() >= 150 and randint(1, 4) == 1 and bundetCD <= 0:
                        print("Smidige Sandra har bundet deg fast!")
                        bundetCD = 3
                        fiende.kp(-150)
                    else:
                        spiller.angrepet(fiende)
                #Store Sture - Duell
                elif fiende.navn() == "Store Sture":
                    if fiende.kp() >= 50 and fiende.hp() <= fiende.xHp() - 210 and randint(1, 5) == 3:
                        print("Store Sture dunket deg med et kjøttstykke og spiste det!")
                        print(fiende.navn(), "restorerte", fiende.restorer(250), "hp.")
                        print(spiller.navn(), "mistet", spiller.mist_liv(50), "liv.")
                        fiende.kp(-50)
                    else:
                        spiller.angrepet(fiende)
                #Kraftige Klara - Duell
                elif fiende.navn() == "Kraftige Klara":
                    if fiende.kp() >= 50 and randint(1, 7) != 1:
                        fiende.kp(-50)
                        fiende.a(500)
                        print("Kraftige Klara varmet opp musklene!")
                        print("Kraftige Klara fikk 500 angrepspoeng.")
                    else:
                        spiller.angrepet(fiende)
                #Teite Tim - Duell
                elif fiende.navn() == "Teite Tim":
                    if fiende.kp() >= 200 and randint(1, 15) == 7 and fiende.hp() < fiende.xHp() - 400:
                        print("Teite Tim kastet Super Restituer!")
                        print("Teite Tim restorerte", fiende.restorer(500 + randint(0, 120)), "liv.")
                        fiende.kp(-200)
                    elif fiende.kp() >= 350 and randint(1, 10) == 1 and spiller.kp() >= 150:
                        print("Teite Tim kastet Distraher!")
                        print(spiller.navn(), "mistet", spiller.mist_kp(500 + randint(0, 80)), "kp.")
                        fiende.kp(-350)
                    elif fiende.kp() >= 200 and randint(1, 15) == 1:
                        print("Teite Tim gjorde en strategisk vurdering av kampen!")
                        print("Teite TIm fikk 50 angrepspoeng.")
                        fiende.a(50)
                        fiende.kp(-200)
                    elif fiende.kp() >= 50 and randint(1, 8) == 1 and uCD >= 0:
                        print("Teite Tim kastet Restituer!")
                        print("Teite Tim restorerte", fiende.restorer(150 + randint(0, 50)), "liv.")
                        fiende.kp(-50)
                    else:
                        if uCD < 0:
                            print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(spiller.angrepet(fiende)), "hp!")
                        else:
                            spiller.angrepet(fiende)
                #Onde Olga - Duell
                elif fiende.navn() == "Onde Olga":
                    if fiende.kp() >= 315 and randint(1, 7) == 1 and not fiende.untouchableCD():
                        print(fiende.navn() + fiende.ending(), "kastet RockNoRoll!")
                        print(fiende.navn() + fiende.ending(), "er blitt til stein!")
                        fiende.kp(-315)
                        fiende.set_untouchable(True, 5)
                    elif fiende.kp() >= 140 and randint(1, 6) == 1 and fiende.hp() < fiende.xHp() - 200:
                        print("Onde Olga kastet Restituer!")
                        print("Onde Olga restorerte", fiende.restorer(randint(250, 450)), "liv.")
                        fiende.kp(-140)
                    elif fiende.kp() >= 350 and randint(1, 2 + round(13 * (fiende.hp() / fiende.xHp()))) == 1:
                        print("Onde Olga mante frem en kampstein og kastet den på deg!")
                        print(spiller.navn(), "mistet", spiller.mist_liv(randint(500, 750)), "liv!")
                        fiende.kp(-350)
                    else:
                        spiller.angrepet(fiende)
                #Restituer
                elif fiende.kp() >= 50 and randint(0, 2) == 1 and fiende.hp() < (fiende.xHp() - 90) and uCD >= 0:
                    print(fiende.navn() + fiende.ending(), "kastet Restituer!")
                    if fiende.race() in {"shroom"} or fiende.navn() in {"Bjarte Banditt"}:
                        print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(randint(160, 340)), "hp.")
                    else:
                        print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(randint(90, 140)), "hp.")
                    fiende.bruk_kons(50)
                #Guffsliffsaff
                elif fiende.navn() == "Guffsliffsaff" and fiende.kp() >= 60 and randint(1, 3) == 1:
                    print(fiende.navn() + fiende.ending(), "tok på deg!")
                    print(fiende.navn() + fiende.ending(), "transformerer seg.")
                    input("Trykk enter for å fortsette\n> ")
                    fiende = generer_guffsliffsaff(spiller, True)
                    fiende1 = fiende
                    fiender = [fiende]
                    target = fiende
                #Vanlig angrep
                else:
                    if uCD < 0:
                        print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(spiller.angrepet(fiende)), "hp!")
                    else:
                        spiller.angrepet(fiende)

                #Pàn Tú - legger til alliert
                if fiende.navn() == "Skjegghatt Shroom" and fiende.hp() / fiende.xHp() <= 0.82 \
                and not pantu and not spiller.dead():
                    pantu = True
                    alliert = Fiende("Pàn Tú", "alliert", Loot(), hp=25000, a=470, d=100, kp=700, bonusKp=30)
                    print("""\n
            I kampens hete legger du merke til at to skikkelser observerer kampen fra
            avstand. Den ene skikkelsen hvisker noe til den andre, før den sporløst
            fordufter i løse luften. Skikkelsen som er igjen stormer bort til deg
            for å hjelpe.

                          ** Pàn Tú har blitt med i kampen! **\n""")
                    input("Trykk enter for å fortsette kampen\n> ")
                    if spiller.fuglelukt():
                        print("\n\n    Pàn Tú rynker på nesen og synes du lukter... Fugleaktig.\n")
                        input("Ikke bry deg om det og trykk enter for å fortsette\n> ")

                #gir beskjed om karakteren døde
                if spiller.dead():
                    input("\nDu døde! Trykk enter for å fortsette\n> ")
                    write_player_died(spiller, "leiren")
                    player_died(spiller, inv, klasser)
                    return False

                #git beskjed om den allierte døde
                if alliert and alliert.dead():
                    if alliert.navn() in {"Pàn Tú", "Symmetriske Sara", "Magiske Mikkel", "Zap"}:
                        print(alliert.navn() + alliert.ending(), "hviler seg på sidelinjen.")
                    else:
                        print(alliert.navn() + alliert.ending(), "døde! En magisk paraply henter", \
                        alliert.navn() + alliert.ending(), "til en uviss fremtid.")
                    print("\n     **", alliert.navn() + alliert.ending(), "har forsvunnet fra kampen! **")
                    alliert = None
                    input("\nTrykk enter for å fortsette\n> ")

            #skriver ut hp og kp til karakteren og hp til fienden til neste runde.
            uCD += 1
            bundetCD -= 1
            spiller.kons()
            fiende = target
            if alliert:
                alliert.gen_kons()
                alliert.skriv_ut()
            spiller.skriv_ut()
            if not fiende1.dead():
                fiende1.gen_kons()
                fiende1.skriv_ut()
            if fiende2 and not fiende2.dead():
                fiende2.gen_kons()
                fiende2.skriv_ut()
            if fiende3 and not fiende3.dead():
                fiende3.gen_kons()
                fiende3.skriv_ut()
            if bundetCD > 0:
                input("Trykk enter for å fortsette\n> ")

def generer_store_shrooms(spiller):
    fiender = []
    skrivSopp("tre")
    print("Du har møtt tre store shrooms!")

    #Cantharellus Cibarius
    loot = Loot()
    fiende = Fiende("Cantharellus Cibarius", "shroom", loot, hp=20000, a=1000, d=400, kp=340, bonusKp=5, weapon=100)
    fiender.append(fiende)
    loot.legg_til_item(randint(4000, 6000), 25)
    loot.legg_til_item(Item("Kantarellhatt", "hat", d=250, xHp=350, xKp=25), 25)
    loot.legg_til_item(Item("Kantarellkledning", "robe", d=340, xHp=250), 25)
    loot.legg_til_item(Item("Kant-handsker", "gloves", d=170, xHp=150, ekstraKp=1), 25)

    #Agaricus Augustus
    loot = Loot()
    fiende = Fiende("Agaricus Augustus", "shroom", loot, hp=7500, a=140, d=10, kp=700, bonusKp=45)
    fiender.append(fiende)
    loot.legg_til_item(randint(2000, 4000), 25)
    loot.legg_til_item(Item("Sjampinjong", "weapon", a=130, xKp=320, ekstraKp=4), 25)
    loot.legg_til_item(Item("Agaricus Stercus", "trinket", a=30, d=25, xKp=360, ekstraKp=8), 25)
    loot.legg_til_item(Item("Sjampskjegg", "beard", xKp=250, ekstraKp=6), 25)

    #Boletus Edulis
    loot = Loot()
    fiende = Fiende("Boletus Edulis", "shroom", loot, hp=4500, a=700, d=130, kp=400, bonusKp=15)
    fiender.append(fiende)
    loot.legg_til_item(randint(3000, 5000), 25)
    loot.legg_til_item(Item("Steinstav", "weapon", a=380, xKp=140), 25)
    loot.legg_til_item(Item("Steinsverd", "weapon", a=430, blade=True), 25)
    loot.legg_til_item(Item("Steinsko", "shoes", a=140, xKp=20, d=100, xHp=50), 25)

    return fiender

def generer_shroom(spiller):
    loot = Loot()
    weapon = 0
    if randint(1, 10) == 10:
        weapon = 300 + randint(0, round(spiller.a() / randint(9, 10)) + 50)
    fiende = Fiende(["Inocybe Relicina", "Geoglossum Umbratile", "Entoloma Jubatum", \
    "Scutellinia Olivascens", "Mitrula Paludosa", "Russula Farinipes", "Coprinus Acuminatus", \
    "Ripartites Tricholoma", "Coprinus Miser", "Cantharellus Borealis", "Mycena Cinerella", \
    "Plicaria Trachycarpa", "Crinipellis Scabella", "Manita Muscaria"][randint(0, 13)], \
    "shroom", loot, \
    hp=2000 + randint(0, round(spiller.xHp() / 10) + (spiller.lvl() * 90)), \
    a=350 + randint(0, (spiller.lvl() * 20) + round(spiller.a() / randint(7, 10))), \
    d=300 + randint(0, round(spiller.d() / 1.6) + (spiller.lvl() * 3)), \
    kp=400 + randint(0, round(spiller.xKp() / 2.2) + spiller.lvl() * 6), \
    bonusKp=15 + randint(0, int(spiller.ekstraKp()/10)) * 5, \
    weapon=weapon)

    loot.legg_til_item(round(fiende.xp() / 10), 55)

    loot.legg_til_item(Item("Sopphatt", "hat", \
    d=randint(10, spiller.lvl() * 4), \
    xHp=randint(20, spiller.lvl() * 8)), 6)

    loot.legg_til_item(Item(fiende.navn().split()[0] + "-stav", "weapon", \
    a=randint(0, 6 * spiller.lvl()), \
    xKp=randint(0, 5 * spiller.lvl())), 6)

    loot.legg_til_item(Item("Slegge", "weapon", \
    a=randint(10, spiller.lvl() * 10), \
    xHp=randint(0, 4)*10, blade=True), 6)

    item = Item("Konsentrasjonspulver", "restoring", kp=randint(15, spiller.lvl() + 5)*10)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 12)

    item = Item("Trolldrikk", "restoring", hp=300 + randint(0, spiller.lvl())*10)
    loot.legg_til_item(item, 15)

    skrivSopp(fiende.navn())
    print(spiller.navn(), "har møtt en", fiende.navn() + "!")
    return fiende

def generer_smaatt(spiller):
    tall = randint(1, 3)
    loot = Loot()
    if tall == 1:
        loot.legg_til_item(randint(100, 300), 92)
        item = Item("Fossil", "trinket", a=30, xKp=75, xHp=25, ekstraKp=randint(3, 5))
        loot.legg_til_item(item, 8)
        skrivMoseStein()
        print(spiller.navn(), "har møtt på en levende stein!")
        fiende =  Fiende("Mosegrodd stein", "stein", loot,  a=randint(90, 190), d=100, hp=randint(900, 1100), kp=randint(100, 110))
        dynamiskLoot(loot, fiende, spiller)
        return fiende
    elif tall == 2:
        a = randint(0, 4 * spiller.lvl())
        xKp = randint(0, 3 * spiller.lvl())
        item = Item("Superkvist", "weapon", a=a, xKp=xKp)
        loot.legg_til_item(item, 15)
        loot.legg_til_item(randint(150, 230), 85)
        fiende = Fiende(navn="Kvist", race="tre", loot=loot, \
        hp=20 + 20 * randint(1, spiller.lvl()), \
        a=20 + randint(0, 10 * spiller.lvl()), \
        d=30 + randint(0, 10 * spiller.lvl()), \
        kp=50 + randint(0, 3 * spiller.lvl()), bonusKp=2, ending="en")
        skrivTre(kvist=True)
        dynamiskLoot(loot, fiende, spiller)
        print("\n" + spiller.navn(), "har møtt på en levende kvist!")
        return fiende
    elif tall == 3:
        return generer_liten_sopp(spiller)

def generer_liten_sopp(spiller):
    loot = Loot()
    item = Item("Fotsopp", "shoes", d=randint(30, spiller.lvl()*4), xKp=60)
    loot.legg_til_item(item, 20)
    loot.legg_til_item(randint(90, 350), 92)
    skrivSopp("liten")
    print(spiller.navn(), "har møtt på en liten sopp!")
    fiende =  Fiende("Liten sopp", "shroom", loot, \
    a=randint(100, 200), \
    d=randint(100, 600), \
    hp=500 + randint(0, spiller.lvl())*10, \
    kp=randint(80, 150))
    dynamiskLoot(loot, fiende, spiller)
    return fiende

def generer_tre(spiller):
    tall = randint(1, 5)
    loot = Loot()
    fiende = None
    skrivTre()
    if tall == 1:
        fiende = Fiende("Barsk Bøk", "tre", loot, hp=800 + (int(spiller.lvl()/30) * 400) + randint(0, 400), \
        a=600, d=350, kp=80+randint(0, 50), weapon=100+randint(0, 50 + int(spiller.lvl()/30) * 150))
        print(spiller.navn(), "har møtt på en Barsk Bøk!")
    elif tall == 2:
        fiende = Fiende("Fiffig Furu", "tre", loot, hp=600+randint(0, 450), \
        a=600, d=150, kp=280+randint(0, 50) + int(spiller.lvl()/30) * 150, weapon=80+randint(0, 50) + \
        int(spiller.lvl()/30) * 100)
        print(spiller.navn(), "har møtt på en Fiffig Furu!")
    elif tall == 3:
        fiende = Fiende("Brysom Bjørk", "tre", loot, hp=1800+randint(0, 400), \
        a=200 + int(spiller.lvl()/30) * round(spiller.d() / 3), d=80+randint(0, 50), kp=80+randint(0, 50))
        print(spiller.navn(), "har møtt på en Brysom Bjørk!")
    elif tall == 4:
        fiende = Fiende("Ondskapsfull Osp", "tre", loot, hp=900+randint(0, 400 + int(spiller.lvl()/30) * 150), \
        a=600, d=80, kp=80+randint(0, 50), weapon=70+randint(0, 50) + int(spiller.lvl()/30) * 150)
        print(spiller.navn(), "har møtt på en Ondskapsfull Osp!")
    elif tall == 5:
        fiende = Fiende("Rasende Rogn", "tre", loot, hp=500+randint(0, 600 + int(spiller.lvl() / 30) * 150), \
        a=400+randint(0, 70) + (int(spiller.lvl() / 30) * 150), d=10 + (int(spiller.lvl() / 30) * 80), \
        kp=40+randint(0, 50))
        print(spiller.navn(), "har møtt på en Rasende Rogn!")
    loot.legg_til_item(75+round(fiende.xp()/15), 100)
    dynamiskLoot(loot, fiende, spiller)

    item = Item("Silkehansker", "gloves", \
    xHp=randint(80, 120 + (spiller.lvl()*2)), \
    xKp=randint(0, 2 + int(spiller.lvl()/10))*10, \
    d=randint(0, 2) * 25)
    loot.legg_til_item(item, 10)

    a = randint(30, 5 * spiller.lvl())
    xKp = randint(0, 4 * spiller.lvl())
    ekstraKp = 0
    if not randint(0, 9): ekstraKp = randint(1, 1 + int(spiller.lvl()/30))
    item = Item("Bladpyntet stav", "weapon", a=a, xKp=xKp, ekstraKp=ekstraKp)
    loot.legg_til_item(item, 10)
    return fiende

def generer_gnom(spiller):
    fiende = Fiende("Gnom", "gnom", Loot(), \
    600 + 10 * randint(round(spiller.lvl()/2), spiller.lvl()), \
    80 + randint(0, 4 * spiller.lvl()) + int(spiller.lvl() / 30) * 150, \
    70 + randint(0, 2 * spiller.lvl()) + int(spiller.lvl() / 30) * 100, ending="en")
    gnom.gnomLoot(fiende, fiende.return_loot(), spiller)
    skrivGnom()
    print("\n" + spiller.navn(), "har møtt på en gnom!")
    return fiende

def generer_guffsliffsaff(spiller, b=False, fSpiller=None):
    loot = Loot()
    item = Item("ID-stjeler", "beard", xHp=randint(0, 4)*10, xKp=randint(2, 8)*10, ekstraKp=randint(0, 1 + int(spiller.lvl()/10)))
    loot.legg_til_item(item, 6)
    if not b:
        skrivGuffsliffsaff()
        print(spiller.navn(), "har møtt på en Guffsliffsaff!")
        fiende = Fiende("Guffsliffsaff", "guffsliffsaff", loot, a=150, hp=2300, d=130, kp=200, bonusKp=7, ending="en")
        dynamiskLoot(loot, fiende, spiller)
        return fiende
    elif b is "kvist":
        fiende = Fiende("Guffsliffsaff-gren", "guffsliffsaff", loot, a=175, hp=2300, d=100, kp=200, bonusKp=7, ending="en")
        fiende.mist_liv(2300 - round((fSpiller.hp() / fSpiller.xHp()) *2300), stille=True)
        dynamiskLoot(loot, fiende, spiller)
        return fiende
    fiende = Fiende(spiller.navn() + " v2", "guffsliffsaff", loot, a=spiller.a(), hp=spiller.xHp(),\
    d=spiller.d(), kp=spiller.xKp(), bonusKp=spiller.ekstraKp()-5)
    dynamiskLoot(loot, fiende, spiller)
    return fiende

def generer_duellant(nr, spiller):
    fiende = None
    loot = Loot()
    skrivHodeskalle()
    if nr == 0:
        item = Item("Patricks Poncho", "robe", d=40, xHp=70)
        item.sett_loot_tekst("Patetiske Patrick sin poncho")
        loot.legg_til_item(item, 1)
        fiende = Fiende("Patetiske Patrick", "menneske", loot, a=300, hp=2350, d=200)
    elif nr == 1:
        loot.legg_til_item(1050, 1)
        fiende = Fiende("Store Sture", "menneske", loot, a=400, hp=10000, d=600, kp=200, bonusKp=1)
    elif nr == 2:
        item = Item("Sandras Sko", "shoes", d=100, xHp=40, xKp=20)
        item.sett_loot_tekst("Smidige Sandra sine sko")
        loot.legg_til_item(item, 1)
        fiende = Fiende("Smidige Sandra", "menneske", loot, a=450, hp=2700, d=400, kp=450, bonusKp=10)
    elif nr == 3:
        item = Item("Klaras hansker", "gloves", a=80, d=50, xHp=70)
        item.sett_loot_tekst("Kraftige Klara sine hansker")
        loot.legg_til_item(item, 1)
        fiende = Fiende("Kraftige Klara", "menneske", loot, a=1200, hp=2337, d=-1200, kp=50)
    elif nr == 4:
        item = Item("Teit ting", "trinket", a=45, xHp=50, xKp=40, ekstraKp=5)
        item.sett_loot_tekst("Teite Tims teite ting")
        loot.legg_til_item(item, 1)
        fiende = Fiende("Teite Tim", "snik", loot, a=550, hp=6666, d=500, kp=700, bonusKp=12)
    elif nr == 5:
        item = Item("Ondskap", "trinket", a=-200, d=-200, xHp=-230, xKp=500, ekstraKp=13)
        item.sett_loot_tekst("Ondskap")
        loot.legg_til_item(item, 1)
        fiende = Fiende("Onde Olga", "gargyl", loot, a=2000, hp=5734, d=666, kp=1000, bonusKp=20, weapon=450)
    print(spiller.navn(), "møter denne gangen", fiende.navn(), "i duellringen! Hvem vil vinne?\n")
    return fiende

def generer_banditt(spiller):
    loot = Loot()
    fiende = Fiende("Banditt", "menneske", loot, \
    hp=randint(90, 120 + spiller.lvl())*10, \
    a=randint(100, 150), \
    d=randint(50, 160), ending="en")
    bandittLoot(loot, fiende, spiller)
    skrivBanditt()
    print("\n" + spiller.navn(), "har møtt på en banditt!")
    return fiende

def bandittLoot(loot, fiende, spiller):
    loot.legg_til_item(randint(round(fiende.xp()/10) - 100, round(fiende.xp()/10) + 400), 60)

    kpkp = int(randint(1, spiller.lvl()) /10) *25 + 150
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 8)

    item = Item("Trolldrikk", "restoring", hp=200 + randint(0, spiller.lvl())*10)
    loot.legg_til_item(item, 15)

    dynamiskLoot(loot, fiende, spiller)

def dynamiskLoot(loot, fiende, spiller):
    tall = round(10 + fiende.xp() / 10)
    loot.legg_til_item(tall, 30)

    kpkp = int(randint(1, spiller.lvl()) /4) *25 + 125
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 10)

    tdhp = randint(1, spiller.lvl()) * 10 + 250
    item = Item("Trolldrikk", "restoring", hp=tdhp)
    loot.legg_til_item(item, 15)

    a = randint(0, 4 * spiller.lvl())
    xKp = randint(0, 3 * spiller.lvl())
    item = Item("Tryllestav", "weapon", a=a, xKp=xKp)
    loot.legg_til_item(item, 5)

    a = randint(40, 40 + 5 * spiller.lvl())
    item = Item("Sverd", "weapon", a=a, blade=True)
    item.sett_loot_tekst("et sverd")
    loot.legg_til_item(item, 5)

    xHp = randint(0, 4 * spiller.lvl())
    d = randint(0, 2 * spiller.lvl())
    item = Item("Spiss Hatt", "hat", xHp=xHp, d=d)
    loot.legg_til_item(item, 5)

def skog_kart(qlog):
    print("""
    Velkommen til ekspedisjonsleiren! Her er stedene du kan dra:
    Skogen (s)                 Utforsk området utenfor ekspedisjonsleiren
    Strategi-teltet (q)        Diskuter strategi med de andre i ekspedisjonen
    Butikken (k)               Se gjennom nødrasjonene og spesial-utstyret""")
    if qlog.hent_quest(4).startet():
        print("    Opp bakken (o)             Dra opp bakken og dypere inn i skogen")
    print("""    Leirbålet (b)              Dra tilbake til det forlatte leirbålet
    Minnesteinen (l)           Graver din progresjon i skogens omtrent-funksjonelle minnestein
    Ut i verden (f)            Viser deg kart over alle stedene du kan dra\n""")

def banditt_kart(qlog):
    print("""
    Velkommen til banditt-leiren! Her er stedene du kan dra:
    Skogen (s)                 Se hvem du finner i utkanten av leiren
    Stortreet (q)              Dra til det største treet og hør bandittenes forpinte bønner om hjelp
    Svartemarkedet (k)         Få en god pris på Gundis utvalgte favorittbytter
    Duellringen (d)            Test dine ferdigheter i bandittenes interne duellring""")
    if qlog.hent_qLog()[2].startet():
        print("    Soppstedet (p)             Dra til det hemmelige soppstedet")
    print("    Ekspedisjonsleiren (f)     Dra tilbake til ekspedisjonsleiren\n")

def shroom_butikk(butikk):
    butikk.legg_til_hadeTekst("\nVelkommen tilbake! Og vær forsiktig der ute!\n")

    item = Item("Trolldrikk", "restoring", hp=400)
    vare = Vare(item, 500, "d")
    butikk.legg_til_vare(vare)

    item = Item("Trolldrikk", "restoring", hp=750)
    vare = Vare(item, 1600, "d2")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=250)
    vare = Vare(item, 1000, "k")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=750)
    vare = Vare(item, 3000, "k2")
    butikk.legg_til_vare(vare)

    item = Item("Ekspedisjonsstav", "weapon", a=170, xKp=80)
    vare = Vare(item, 25000, "w")
    butikk.legg_til_vare(vare)

    item = Item("Eks. sverd", "weapon", a=430, xHp=80, blade=True)
    vare = Vare(item, 34000, "e")
    butikk.legg_til_vare(vare)

    item = Item("Støvler", "shoes", d=90, xHp=100)
    vare = Vare(item, 8000, "ø")
    butikk.legg_til_vare(vare)

def banditt_butikk(butikk):
    butikk.legg_til_hadeTekst("\nKom deg ut! Hvis ikke skal kjøpe og ikke skal selge, pell deg!\n")

    item = Item("Trolldrikk", "restoring", hp=600)
    vare = Vare(item, 900, "d")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=415)
    vare = Vare(item, 1700, "k")
    butikk.legg_til_vare(vare)

    item = Item("Bandittmaske", "beard", xKp=40, ekstraKp=4, xHp=25)
    vare = Vare(item, 11000, "m")
    butikk.legg_til_vare(vare)

    item = Item("Hvite hansker", "gloves", xKp=-60, d=125, xHp=250)
    vare = Vare(item, 14800, "h")
    butikk.legg_til_vare(vare)

    item = Item("Svart kappe", "robe", xKp=15, d=200, xHp=350)
    vare = Vare(item, 27000, "p")
    butikk.legg_til_vare(vare)

def skog_quest(qlog, spiller):
    navn = spiller.navn()

    #q1
    desk = shroom_q1(navn)
    ferdigDesk = shroom_q1_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 20, "Zip")
    q.legg_til_reward(xp=16000, gull=3000, hp=30, kp=30, settTilgjengelig=True, settTilgjengeligIndeks=4)
    q.legg_til_progresjonTekst("Banditt-angrep stoppet: ")
    q.legg_til_svarTekst("\nVil du gå på bandittjakt?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q2
    desk = shroom_q2(navn)
    ferdigDesk = shroom_q2_ferdig(navn)
    q = Quest(desk, ferdigDesk, 13, 22, "Uheldige Ulrik")
    q.legg_til_reward(xp=10000, gull=700, hp=50, settTilgjengelig=True, settTilgjengeligIndeks=3)
    q.legg_til_progresjonTekst("Forsyninger funnet: ")
    q.legg_til_svarTekst("\nVil du hjelpe meg finne forsyningene?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q3
    desk = shroom_q3(navn)
    ferdigDesk = shroom_q3_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 23, "Kjedelige Kjell", resetIfDead=True)
    q.legg_til_reward(xp=12003, gull=2500, kp=45, settTilgjengelig=True, settTilgjengeligIndeks=12)
    q.legg_til_progresjonTekst("Barsk Bøk oppdaget: ")
    q.legg_til_progresjon(1)
    q.legg_til_progresjonTekstListe("Fiffig Furu oppdaget: ", 0)
    q.legg_til_progresjon(1)
    q.legg_til_progresjonTekstListe("Brysom Bjørk oppdaget: ", 1)
    q.legg_til_progresjon(1)
    q.legg_til_progresjonTekstListe("Ondskapsfull Osp oppdaget: ", 2)
    q.legg_til_progresjon(1)
    q.legg_til_progresjonTekstListe("Rasende Rogn oppdaget: ", 3)
    q.legg_til_svarTekst("\nEr du like spent som meg på å undersøke trærne?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q4
    desk = shroom_q4(navn)
    ferdigDesk = shroom_q4_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 24, "Uheldige Ulrik", tilgjengelig=False)
    q.legg_til_reward(xp=10000, hp=250)
    q.legg_til_progresjonTekst("Kent Kokk rekruttert: ")
    q.legg_til_svarTekst("\nKan du rekruttere Kent Kokk?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q5
    desk = shroom_q5(navn)
    ferdigDesk = shroom_q5_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 29, "Strategiske Synne", tilgjengelig=False)
    q.legg_til_reward(xp=10000, hp=100, kp=40, settTilgjengelig=True, settTilgjengeligIndeks=[5, 7])
    q.legg_til_progresjonTekst("Pàn Tú funnet: ")
    q.legg_til_svarTekst("\nKan du dra etter henne?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q6
    desk = shroom_q6(navn)
    ferdigDesk = shroom_q6_ferdig(navn)
    q = Quest(desk, ferdigDesk, 20, 30, "Strategiske Synne", tilgjengelig=False)
    q.legg_til_reward(xp=10000, settTilgjengelig=True, settTilgjengeligIndeks=9)
    q.legg_til_progresjonTekst("Shrooms drept: ")
    q.legg_til_svarTekst("\nKan du være med i slakten?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q7
    desk = shroom_q7(navn)
    ferdigDesk = shroom_q7_ferdig(navn)
    q = Quest(desk, ferdigDesk, 7, 30, "Magiske Mikkel")
    q.legg_til_reward(xp=11000)
    q.legg_til_ekstra_tekst("Magiske Mikkel har forbedret teknikken din, Opphold er nå mer effektiv!")
    q.legg_til_progresjonTekst("Opphold runder aktiv: ")
    q.legg_til_svarTekst("\nVil du forbedre teknikken din?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q8
    desk = shroom_q8(navn)
    ferdigDesk = shroom_q8_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 32, "Zip", tilgjengelig=False)
    q.legg_til_reward(xp=13000, settTilgjengelig=True, settTilgjengeligIndeks=[8, 11, 13])
    q.legg_til_progresjonTekst("Pàn Tús kontakt møtt: ")
    q.legg_til_svarTekst("\nKan jeg stole på deg " + navn + "?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q9
    desk = shroom_q9(navn)
    ferdigDesk = shroom_q9_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 32, "Strategiske Synne", tilgjengelig=False)
    q.legg_til_reward(xp=13000)
    q.legg_til_progresjonTekst("Zap snakket med: ")
    q.legg_til_svarTekst("\nVil du finne Zap?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q10
    desk = shroom_q10(navn)
    ferdigDesk = shroom_q10_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 36, "Strategiske Synne", tilgjengelig=False)
    q.legg_til_reward(xp=25000)
    q.legg_til_progresjonTekst("Tjern Forurenset: ")
    q.legg_til_svarTekst("\nKan du stoppe denne galskapen " + navn + "?     (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #bq1
    deskBq = shroom_bq1(navn)
    ferdigDeskBq = shroom_bq1_ferdig(navn)
    bq = Quest(deskBq, ferdigDeskBq, 1, 1, "Fanatiske Ferdinand", bonus=True, resetIfDead=True)
    item = Item("Forkastet totem", "trinket", xKp=50, xHp=60, ekstraKp=3, d=20)
    bq.legg_til_reward(xp=6000, item=item, gp=2)
    bq.legg_til_progresjonTekst("Totem funnet: ")
    bq.legg_til_svarTekst("Vil du fortelle Fanatiske Ferdinand at han er hjernevasket?   (ja/nei)\n> ")
    bq.legg_til_ekstra_tekst("Hvaaaa? Det kan umulig stemme? De- dette, men, hvorfor? Hvem er jeg? HVEM ER JEG??")
    bq.legg_til_alt_desk("Vil du gi totemet til Fanatiske Ferdinand?\n> ")
    item = Item("Fanatisk stav", "weapon", a=200, d=-10, xHp=-30)
    bq.legg_til_alt_reward(ep=3, kp=50, xp=6000, item=item)
    qlog.legg_til_quest(bq)

    #bq2
    deskBq = shroom_bq2(navn)
    ferdigDeskBq = "    Har du noe informasjon? Fortell!\n"
    bq = Quest(deskBq, ferdigDeskBq, 5, 1, "Simon Sporfinner", bonus=True, resetIfDead=True, tilgjengelig=False)
    bq.legg_til_reward(xp=14000)
    bq.legg_til_progresjonTekst("korrespondanser funnet: ")
    bq.legg_til_svarTekst("Vil du gi informasjonen til Simon Sporfinner?   (ja/nei)\n> ")
    bq.legg_til_ekstra_tekst(shroom_bq2_tekst())
    bq.legg_til_alt_desk("Vil du drepe Simon Sporfinner på gøy?\n> ")
    bq.legg_til_alt_ektra_tekst("Du drepte Simon Sporfinner. Alle er for opptatt til å merke noe.")
    item = Item("Sporerstøvler", "shoes", a=-20, d=130, xHp=30)
    bq.legg_til_alt_reward(ep=3, xp=14000, item=item)
    qlog.legg_til_quest(bq)

    #q13
    q = Quest("", "", 1, 15, "Kjedelige Kjell", bonus=True, tilgjengelig=False, resetIfDead=True)
    q.legg_til_reward(xp=5000, gp=2)
    q.legg_til_progresjonTekst("Guffsliffsaff-gren funnet: ")
    qlog.legg_til_quest(q)

    #bq3
    deskBq = shroom_bq3(navn)
    ferdigDeskBq = "    NUSSESUSSESOPPOLINEN MIN hvor har du vært? GI HAM TIL MEG!\n"
    bq = Quest(deskBq, ferdigDeskBq, 1, 1, "Rotete Randi", bonus=True, resetIfDead=True, tilgjengelig=False)
    bq.legg_til_reward(xp=18000, gp=2)
    bq.legg_til_progresjonTekst("Sussesopp funnet: ")
    bq.legg_til_svarTekst("Vil du gi sussesoppen til Rotete Randi?   (ja/nei)\n> ")
    bq.legg_til_ekstra_tekst(shroom_bq3_tekst())
    bq.legg_til_alt_desk("Vil du tvinge sussesoppen til å adlyde deg istedenfor?\n> ")
    bq.legg_til_alt_ektra_tekst(shroom_bq3_tekst())
    bq.legg_til_alt_reward(ep=3, xp=14000)
    qlog.legg_til_quest(bq)

def banditt_quest(qlog, spiller):
    navn = spiller.navn()

    #q1
    desk1 = banditt_q1(navn)
    ferdigDesk1 = banditt_q1_ferdig(navn)
    q1 = Quest(desk1, ferdigDesk1, 4, 20, "Lugubre Lasse", resetIfDead=True)
    q1.legg_til_reward(xp=3000, gull=1000, hp=30, kp=30)
    q1.legg_til_progresjonTekst("Lommeur funnet: ")
    q1.legg_til_svarTekst("\nKan du hjelpe meg å stjele tilbake lommeurene mine?     (ja/nei)\n> ")
    qlog.legg_til_quest(q1)

    #q2
    desk2 = banditt_q2(navn)
    ferdigDesk2 = banditt_q2_ferdig(navn)
    q2 = Quest(desk2, ferdigDesk2, 6, 22, "Ussle Ulf")
    item = Item("Usselt sverd", "weapon", blade=True, a=200, xHp=-150, ekstraKp=-2)
    q2.legg_til_reward(xp=5000, gull=600, item=item, settTilgjengelig=True, settTilgjengeligIndeks=4)
    q2.legg_til_progresjonTekst("Utforsk kastet: ")
    q2.legg_til_progresjon(1)
    q2.legg_til_progresjonTekstListe("Ussle Ulf undervist: ", 0)
    q2.legg_til_svarTekst("\nKan du lære meg hvordan få bedre helse ved å utforske innmaten til fienden?     (ja/nei)\n> ")
    qlog.legg_til_quest(q2)

    #q3
    desk3 = banditt_q3(navn)
    ferdigDesk3 = banditt_q3_ferdig(navn)
    q3 = Quest(desk3, ferdigDesk3, 1, 23, "Godtroende Gudleif")
    q3.legg_til_reward(xp=3000, kp=10)
    q3.legg_til_progresjonTekst("Soppsted besøkt: ")
    q3.legg_til_svarTekst("\nEr du klar for å åpne sinnet ditt mot høyere makter?     (ja/nei)\n> ")
    qlog.legg_til_quest(q3)

    #q4
    desk4 = banditt_q4(navn)
    ferdigDesk4 = banditt_q4_ferdig(navn)
    q4 = Quest(desk4, ferdigDesk4, 8, 25, "Taktiske Tore")
    q4.legg_til_reward(xp=13000, kp=30, ekstraKp=1)
    q4.legg_til_progresjonTekst("Fiender distrahert: ")
    q4.legg_til_svarTekst("\nVil du trene deg opp til å bli en mester-banditt?     (ja/nei)\n> ")
    qlog.legg_til_quest(q4)

    #q5
    desk5 = banditt_q5(navn)
    ferdigDesk5 = banditt_q5_ferdig(navn)
    q5 = Quest(desk5, ferdigDesk5, 1, 26, "Fagre Frida", tilgjengelig=False)
    q5.legg_til_reward(xp=20000, kp=10, ekstraKp=3, hp=30, gull=2000)
    q5.legg_til_progresjonTekst("Onde Olga bekjempet: ")
    q5.legg_til_svarTekst("\nVil du, min helt, utfordre eksen min til duell?     (ja/nei)\n> ")
    qlog.legg_til_quest(q5)

    #q6
    desk6 = banditt_q6(navn)
    ferdigDesk6 = banditt_q6_ferdig(navn)
    q6 = Quest(desk6, ferdigDesk6, 1, 28, "Bjarte Banditt")
    q6.legg_til_reward(xp=16000, gull=5000, hp=30, kp=30)
    q6.legg_til_progresjonTekst("Kjedelige Kjells finger kuttet: ")
    q6.legg_til_svarTekst("\nVil du 'ordne' Kjedelige Kjell?     (ja/nei)\n> ")
    qlog.legg_til_quest(q6)

    #duell_q1
    desk = banditt_dq7(navn)
    ferdigDesk = banditt_dq7_ferdig(navn)
    dq7 = Quest(desk, ferdigDesk, 1, 1, "Onde Olga", tilgjengelig=False)
    dq7.legg_til_reward(xp=3000, gull=1000)
    dq7.legg_til_progresjonTekst("Patetiske Patrick overvunnet: ")
    dq7.legg_til_svarTekst("\nEr du klar for duellringen?     (ja/nei)\n> ")
    qlog.legg_til_quest(dq7)

    #duell_q2
    desk = banditt_dq8(navn)
    ferdigDesk = banditt_dq8_ferdig(navn)
    dq8 = Quest(desk, ferdigDesk, 1, 1, "Onde Olga", tilgjengelig=False)
    dq8.legg_til_reward(xp=4000, gull=1500, hp=150, d=40)
    dq8.legg_til_progresjonTekst("Store Sture overvunnet: ")
    dq8.legg_til_svarTekst("\nEr du klar for duellringen?     (ja/nei)\n> ")
    qlog.legg_til_quest(dq8)

    #duell_q3
    desk = banditt_dq9(navn)
    ferdigDesk = banditt_dq9_ferdig(navn)
    dq9 = Quest(desk, ferdigDesk, 1, 1, "Onde Olga", tilgjengelig=False)
    dq9.legg_til_reward(xp=6000, gull=2000, kp=50)
    dq9.legg_til_progresjonTekst("Smidige Sandra overvunnet: ")
    dq9.legg_til_svarTekst("\nEr du klar for duellringen?     (ja/nei)\n> ")
    qlog.legg_til_quest(dq9)

    #duell_q4
    desk = banditt_dq10(navn)
    ferdigDesk = banditt_dq10_ferdig(navn)
    dq10 = Quest(desk, ferdigDesk, 1, 1, "Onde Olga", tilgjengelig=False)
    dq10.legg_til_reward(xp=8000, gull=3000, a=50, kp=10)
    dq10.legg_til_progresjonTekst("Kraftige Klara overvunnet: ")
    dq10.legg_til_svarTekst("\nEr du klar for duellringen?     (ja/nei)\n> ")
    qlog.legg_til_quest(dq10)

    #duell_q5
    desk = banditt_dq11(navn)
    ferdigDesk = banditt_dq11_ferdig(navn)
    dq11 = Quest(desk, ferdigDesk, 1, 1, "Onde Olga", tilgjengelig=False)
    dq11.legg_til_reward(xp=12000, gull=5000, hp=10, kp=10, ekstraKp=2)
    dq11.legg_til_progresjonTekst("Teite Tim overvunnet: ")
    dq11.legg_til_svarTekst("\nEr du klar for duellringen?     (ja/nei)\n> ")
    qlog.legg_til_quest(dq11)

    #duell_q6
    desk = banditt_dq12(navn)
    ferdigDesk = banditt_dq12_ferdig(navn)
    dq12 = Quest(desk, ferdigDesk, 1, 1, "Onde Olga", tilgjengelig=False)
    dq12.legg_til_reward(xp=17000, gull=7000, hp=50, kp=40, d=15, a=15, ekstraKp=1)
    dq12.legg_til_progresjonTekst("Onde Olga overvunnet: ")
    dq12.legg_til_svarTekst("\nEr du klar for duellringen?     (ja/nei)\n> ")
    qlog.legg_til_quest(dq12)
