"""
                *~ Pokus expansion 2.0 ~*
                           av
                   Gaute Svanes Lunde
"""

from klasser import *
from grafikk import *
from quests import *
from prosedyrer import *

#Mainloop:
def shroom_loop(spiller, inv, klasser, spellbook):
    qlog = klasser.questlog(6)
    vassleQlog = klasser.questlog(5)
    ferdig = False

    if not vassleQlog.hent_quest(3).progresjon():
        ferdig = intro_loop(spiller, inv, klasser, spellbook)

    while not ferdig:
        skog_kart(qlog)

        valg = False
        quest = False
        gaaTilButikk = False
        fight = False
        leirBaal = False
        lagre = False
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

            if inn == "r":
                fight = True
                valg = True

            if inn == "l":
                lagre = True
                valg = True

            if inn == "b":
                leirBaal = True
                valg = True

        if leirBaal:
            leirBaal = False
            ferdig = sti(spiller, inv, klasser, spellbook)

        while quest:
            inn = qlog.oppdrag_tilgjengelige(spiller.lvl(), "stuffs").lower()
            if inn != "f" and inn != "ferdig":
                try:
                    qlog.snakk(int(inn) - 1, spiller, inv)
                except ValueError:
                    print("\nDu må skrive et tall!\n")
            else:
                quest = False

        while gaaTilButikk:
            klasser.butikk(4).interaksjon(inv)
            gaaTilButikk = False

        while fight:
            if randint(1, 2) == 1:
                fiende = generer_enhjorning(spiller)
            else:
                fiende = generer_fisk(spiller)

            skriv_ut(spiller, fiende)
            fight = angrip(spiller, fiende, inv, klasser, spellbook)

        while lagre:
            minnestein(spiller, inv, klasser)
            lagre = False

    if ferdig:
        return verdenskart(spiller)

def intro_loop(spiller, inv, klasser, spellbook):
    print("    **", spiller.navn(), """kommer til et utbrent leirbål. Det er blod på bakken, og
    spor etter kamp. Det virker ikke som om det er lenge siden noen var her,
    men det er vanskelig å si hvor de gikk. Hovedstien deler seg til høyre
    og venstre.
    """)

    input("Trykk enter for å fortsette\n> ")
    print("""\n*En banditt kommer løpende ut fra ingensteds*

    Banditt: Du er en av dem, er du ikke? Jeg skal finne dem! Jeg har fått
    torturert ut noen veibeskrivelser av en ynkelig rotte, og nå slipper
    ingen av dere unna! Og min enmanns-massakre starter med deg!\n""")

    if not angrip(spiller, generer_banditt(spiller), inv, klasser, spellbook):
        return True
    print("\n*" + spiller.navn() + "finner en lapp på banditten! På den står det:")
    print("\n    Hold høyre!\n\nForan deg har du to stier, og du må velge en.")

    return sti(spiller, inv, klasser, spellbook)

def sti(spiller, inv, klasser, spellbook):
    vassleQlog = klasser.questlog(5)
    shroomQlog = klasser.questlog(6)
    while True:
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
            print("""\n\n        **Du fant en avrevet side fra en gammel bok! På den står det:
            ---
            ...Rotter har en tendens til å glemme forskjellen på høyre og venstre
            når de blir utsatt for smerte. En som f.eks sier "hold høyre" mener
            da egentlig "hold venstre". En annen nyttig faktaopplysning omhandler...
            ---
            På en eller annen måte finner du veien tilbake til leirbålet du var med
            sist.**""")
        elif h1 and not h2 and h3:
            print("""\n\n        *Du fant et skilt hvor det står "BANDITT-LEIR"* """)
            if shroomQlog.hent_quest(0).startet():
                print("\nDu går inn til leiren.")
                input("\nTrykk enter for å fortsette\n> ")
                return banditt_loop(spiller, inv, klasser, spellbook)
            else:
                print("\nDet er ikke en banditt-leir", spiller.navn(), "er på jakt etter.")
                print("Du bestemmer deg for å dra tilbake til leirbålet.")
        elif not h1 and h2 and not h3 and shroomQlog.hent_quest(0).startet():
            print("Blindvei! Du får en følelse av at rotters stedsans ikke er helt bra.")
            print("Kanksje du kan prøve det motsatte? Du drar tilbake til leirbålet.")
        else:
            print("Blindvei! På en eller annen måte finner du veien tilbake til leirbålet.")

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
        #skrivBandittLeir()
        banditt_kart(bQlog)

        valg = False
        quest = False
        gaaTilButikk = False
        skogen = False
        sopp = False
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

        while gaaTilButikk:
            klasser.butikk(5).interaksjon(inv)
            gaaTilButikk = False

        while skogen:
            tall = randint(1, 10)
            if tall >= 6:
                fiende = generer_banditt(spiller)
            elif tall >= 4:
                fiende = generer_kvist(spiller)
            elif tall >= 2:
                fiende = generer_mosegrodd_stein(spiller)
            else:
                fiende = generer_liten_sopp(spiller)

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
                spiller.restorer_kp(300), " konsentrasjonspoeng gjennom de magiske soppenes velsignelse.\n")
                input("Trykk enter for å fortsette\n> ")
            sopp = False

    if ferdig:
        return False

def ussleUlvLoop(spiller, inv, klasser, spellbook):
    print("    Tusen takk " + spiller.navn() + """!
    Nå kan jeg endelig vinne hjertet til Fagre Frida! Håper ikke jeg må
    sloss mot eksen hennes, har hørt hun er ganske grusom...

    Uansett, takk for hjelpen! Dessverre kan jeg ikke etterlate noen
    løse tråder, tenk om andre skulle lært de samme kunstene av deg?
    Da ville jeg ikke vært særlig spesiell lengre! Dette har vært gøy,
    men jeg er redd det er på tide for deg å opphøre å eksistere.\n""")
    input("Trykk enter for å fortsette\n> ")
    print("\nUssle Ulv har knivstukket deg!")
    skade = spiller.hp() // 3
    spiller.mist_liv(skade)
    print(spiller.navn(), "mistet", skade, "liv!\n")
    loot = Loot()
    loot.legg_til_item(30, 1)
    ussleUlv = Fiende("Ussle Ulf", "snik", loot, a=400, d=200, hp=3000, kp=500, weapon=200, bonusKp=8)
    if angrip(spiller, ussleUlv, inv, klasser, spellbook):
        klasser.questlog(7).hent_quest(1).progresser_liste(0)
        return True
    return False

def angrip(spiller, fiende, inv, klasser, spellbook):
    sQlog = klasser.questlog(6)
    bQlog = klasser.questlog(7)
    skriv_ut(spiller, fiende)
    uCD = 0
    while True:
        inn = input("\nHva vil du gjøre?\n> ").lower()

        #tur angir at det er brukeren sin tur til å handle.
        tur = kommandoer(inn, spiller, fiende, inv, klasser, spellbook)

        if inn == "f" or inn == "flykt":
            print(spiller.navn(), "drar tilbake til stallen.")
            return False

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

            #Shroom bq1
            if fiende.race() == "tre" and bQlog.hent_quest(2).ferdig() and not sQlog.hent_quest(1).ferdig()\
            and randint(1, 5) == 1:
                sQlog.hent_quest(1).progresser()
                print("Du klarte å lage et totem ut av restene til", fiende.navn() + fiende.ending())

            input("Trykk enter for å fortsette\n> ")
            return True

        elif not tur:
            #Utforsk
            if fiende.race() == "snik" and fiende.kp() >= 195 and uCD >=0 and randint(1, 5) >= 3:
                print(fiende.navn() + fiende.ending(), "kastet Utforsk!")
                fiende.bruk_kons(195)
                uCD = -6
            #Restituer
            elif fiende.kp() >= 50 and randint(0, 1) == 1 and fiende.hp() < (fiende.xHp() - 90) and uCD >= 0:
                print(fiende.navn() + fiende.ending(), "kastet Restituer!")
                print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(100), "hp!")
                fiende.bruk_kons(50)
            #Vanlig angrep
            else:
                if uCD < 0:
                    print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(spiller.angrepet(fiende)), "hp!")
                else:
                    spiller.angrepet(fiende)

            #gir beskjed om karakteren døde
            if spiller.dead():
                write_player_died(spiller, "leiren")
                player_died(spiller, inv, klasser)
                return False

            #skriver ut hp og kp til karakteren og hp til fienden til neste runde.
            else:
                uCD += 1
                spiller.kons()
                fiende.gen_kons()
                skriv_ut(spiller, fiende)

def generer_mosegrodd_stein(spiller):
    loot = Loot()
    loot.legg_til_item(100, 1)
    return Fiende("Mosegrodd stein", "stein", loot,  a=100, d=100, hp=100, kp=100)

def generer_kvist(spiller):
    loot = Loot()
    a = randint(0, 4 * spiller.lvl())
    xKp = randint(0, 3 * spiller.lvl())
    item = Item("Superkvist", "weapon", a=a, xKp=xKp)
    loot.legg_til_item(item, 100)
    fiende = Fiende(navn="Kvist", race="tre", loot=loot, \
    hp=20 + 20 * randint(1, spiller.lvl()), \
    a=20 + randint(0, 10 * spiller.lvl()), \
    d=30 + randint(0, 10 * spiller.lvl()), \
    kp=50 + randint(0, 3 * spiller.lvl()), bonusKp=2, ending="en")
    print("\n" + spiller.navn(), "har møtt på en levende kvist!")

    #skrivKvist()
    return fiende

def generer_tre(spiller):
    pass

def generer_banditt(spiller):
    loot = Loot()
    fiende = Fiende("Banditt", "menneske", loot, hp=1400, a=250, d=170, ending="en")
    bandittLoot(loot, fiende, spiller)
    skrivBanditt()
    print("\n" + spiller.navn(), "har møtt på en banditt!")
    return fiende

def generer_liten_sopp(spiller):
    loot = Loot()
    loot.legg_til_item(100, 1)
    return Fiende("Liten sopp", "shroom", loot, a=100, d=100, hp=100, kp=100)

def bandittLoot(loot, fiende, spiller):
    loot.legg_til_item(100, 60)

    kpkp = int(randint(1, spiller.lvl()) /10) *25 + 100
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 8)

    a = randint(40, 40 + 5 * spiller.lvl())
    item = Item("Sverd", "weapon", a=a, blade=True)
    item.sett_loot_tekst("et sverd")
    loot.legg_til_item(item, 5)

def dynamiskLoot(loot, fiende, spiller):
    tall = round(10 + fiende.xp() / 10)
    loot.legg_til_item(tall, 60)

    item = Item("Tryllepulver", "damaging", dmg=100)
    item.sett_loot_tekst("en håndfull tryllepulver")
    loot.legg_til_item(item, 17)

    kpkp = int(randint(1, spiller.lvl()) /10) *25 + 100
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 8)

    tdhp = randint(1, spiller.lvl()) * 5 + 145
    item = Item("Trolldrikk", "restoring", hp=tdhp)
    loot.legg_til_item(item, 13)

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
    Altså (r)                  Dra til foten av regnbuen og bekjemp de korrupte enhjørningene
    ikke helt (k)              Kjøp det du trenger hos "Over Regnbuen"-supertilbudsbutikk
    Ferdig enda (q)            Se om noen utenfor trenger din hjelp
    Leirbålet (b)              Dra tilbake til det forlatte leirbålet
    Minnesteinen (l)           Graver din progresjon i skogens omtrent-funksjonelle minnestein""")
    """if qlog.hent_qLog()[1].startet() and not qlog.hent_qLog()[1].ferdig():
        print("    Quest-sted 1 (1)           Dra til quest-instans nummer 1!")
    if qlog.hent_qLog()[2].startet():
        print("    Quest-sted 2 (2)           Dra til quest-instans nummer 2!")"""
    print("    Ut i verden (f)            Viser deg kart over alle stedene du kan dra\n")

def banditt_kart(qlog):
    print("""
    Velkommen til banditt-leiren! Her er stedene du kan dra:
    Skogen (s)                 Se hvem du finner i utkanten av leiren
    Stortreet (q)              Dra til det største treet og hør bandittenes forpinte bønner om hjelp
    Svartemarkedet (k)         Få en god pris på Gundis utvalgte favorittbytter
    Duellringen (d)            Test dine ferdigheter i bandittenes interne duellring""")
    if qlog.hent_qLog()[2].startet():
        print("    Soppstedet (p)             Dra til det hemmelige soppstedet")
    #if qlog.hent_qLog()[3].startet():
    #    print("    Quest-sted 2 (2)           Dra til quest-instans nummer 2!")
    print("    Leirbålet (f)              Dra tilbake til det forlatte leirbålet\n")

def shroom_butikk(butikk):
    butikk.legg_til_hadeTekst("\nVelkommen tilbake! Og se opp for gangster-fiskene!\n")

    item = Item("Tryllepulver", "damaging", dmg=100)
    vare = Vare(item, 50, "t")
    butikk.legg_til_vare(vare)

    item = Item("Trolldrikk", "restoring", hp=300)
    vare = Vare(item, 400, "d")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=150)
    vare = Vare(item, 500, "k")
    butikk.legg_til_vare(vare)

    item = Item("Tryllestav", "weapon", a=60, xKp=45)
    vare = Vare(item, 1000, "w")
    butikk.legg_til_vare(vare)

    item = Item("Sverd", "weapon", a=100, xHp=20)
    vare = Vare(item, 3000, "v")
    butikk.legg_til_vare(vare)

    item = Item("falskt skjegg", "beard", xKp=30, ekstraKp=3)
    vare = Vare(item, 1100, "g")
    butikk.legg_til_vare(vare)

def banditt_butikk(butikk):
    butikk.legg_til_hadeTekst("\nVelkommen tilbake! Og se opp for gangster-fiskene!\n")

    item = Item("Tryllepulver", "damaging", dmg=100)
    vare = Vare(item, 50, "t")
    butikk.legg_til_vare(vare)

    item = Item("Trolldrikk", "restoring", hp=300)
    vare = Vare(item, 400, "d")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=150)
    vare = Vare(item, 500, "k")
    butikk.legg_til_vare(vare)

    item = Item("Tryllestav", "weapon", a=60, xKp=45)
    vare = Vare(item, 1000, "w")
    butikk.legg_til_vare(vare)

    item = Item("Sverd", "weapon", a=100, xHp=20)
    vare = Vare(item, 3000, "v")
    butikk.legg_til_vare(vare)

    item = Item("falskt skjegg", "beard", xKp=30, ekstraKp=3)
    vare = Vare(item, 1100, "g")
    butikk.legg_til_vare(vare)

def skog_quest(qlog, spiller):
    navn = spiller.navn()

    #q1
    desk1 = shroom_q1(navn)
    ferdigDesk1 = shroom_q1_ferdig(navn)
    q1 = Quest(desk1, ferdigDesk1, 1, 15, "Zip")
    q1.legg_til_reward(xp=10000, gull=300, hp=30, kp=30)
    q1.legg_til_progresjonTekst("Banditt-angrep stoppet: ")
    q1.legg_til_svarTekst("\nVil du gå på bandittjakt?     (ja/nei)\n> ")
    qlog.legg_til_quest(q1)

    #bq1
    deskBq1 = shroom_bq1(navn)
    ferdigDeskBq1 = shroom_bq1_ferdig(navn)
    bq1 = Quest(deskBq1, ferdigDeskBq1, 1, 1, "Fanatiske Ferdinand", bonus=True, resetIfDead=True)
    item = Item("Forkastet totem", "trinket", xKp=50, xHp=60, ekstraKp=3, d=20)
    bq1.legg_til_reward(xp=6000, item=item, gp=2)
    bq1.legg_til_progresjonTekst("Totem funnet: ")
    bq1.legg_til_svarTekst("Vil du fortelle Fanatiske Ferdinand at han er hjernevasket?   (ja/nei)\n> ")
    bq1.legg_til_ekstra_tekst("Hvaaaa? Det kan umulig stemme? De- dette, men, hvorfor? Hvem er jeg? HVEM ER JEG??")
    bq1.legg_til_alt_desk("Vil du gi totemet til Fanatiske Ferdinand?\n> ")
    item = Item("Fanatisk stav", "weapon", a=200, d=-10, xHp=-30)
    bq1.legg_til_alt_reward(ep=3, kp=50, xp=6000, item=item)
    qlog.legg_til_quest(bq1)

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
    q2.legg_til_reward(xp=5000, gull=600, item=item)
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
    q4.legg_til_reward(xp=3000, kp=10)
    q4.legg_til_progresjonTekst("Fiender distrahert: ")
    q4.legg_til_svarTekst("\nVil du trene deg opp til å bli en mester-banditt?     (ja/nei)\n> ")
    qlog.legg_til_quest(q4)

    #q5
    desk5 = banditt_q5(navn)
    ferdigDesk5 = banditt_q5_ferdig(navn)
    q5 = Quest(desk5, ferdigDesk5, 1, 26, "Fagre Frida")
    q5.legg_til_reward(xp=3000, kp=10)
    q5.legg_til_progresjonTekst("Onde Olga bekjempet: ")
    q5.legg_til_svarTekst("\nVil du, min helt, utfordre eksen min til duell?     (ja/nei)\n> ")
    qlog.legg_til_quest(q5)

    #q6
    desk6 = banditt_q6(navn)
    ferdigDesk6 = banditt_q6_ferdig(navn)
    q6 = Quest(desk6, ferdigDesk6, 1, 28, "Bjarte Banditt")
    q6.legg_til_reward(xp=10000, gull=300, hp=30, kp=30)
    q6.legg_til_progresjonTekst("Kjedelige Kjells finger kuttet: ")
    q6.legg_til_svarTekst("\nVil du 'ordne' Kjedelige Kjell?     (ja/nei)\n> ")
    qlog.legg_til_quest(q6)
