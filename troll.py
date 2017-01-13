"""
            *~ Pokus expansion 1.1 - Troll ~*
                            av
                   Nikolas Hemer Martin
"""
#Start med å importere alle de nødvendige delfilene.
from klasser import *
from grafikk import *
from quests import *
from prosedyrer import *

#Mainloop:
def troll_loop(spiller, inv, klasser, spellbook):
    qlog = klasser.questlog(2)

    ferdig = False
    while not ferdig:
        trollKart(qlog)

        valg = False
        quest = False
        gaaTilButikk = False
        fjell = False
        base = False
        cave = False
        helvete = False
        lagre = False
        muskelbunt = False
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

            if inn == "m":
                fjell = True
                valg = True

            if inn == "l":
                lagre = True
                valg = True

            if inn == "b" and qlog.hent_quest(1).startet() and not qlog.hent_quest(1).sjekk_ferdig():
                base = True
                valg = True

            if inn == "c" and qlog.hent_quest(2).startet() and not qlog.hent_quest(2).ferdig():
                cave = True
                valg = True

            if inn == "h" and qlog.hent_quest(3).startet():
                helvete = True
                valg = True

            if inn == "n" and qlog.hent_quest(4).ferdig():
                muskelbunt = True
                valg = True

        while quest:
            #Merk at oppdrag_tilgjengelige() er en funksjon med returverdi.
            inn = qlog.oppdrag_tilgjengelige(spiller.lvl(), "badstua").lower()
            if inn != "f" and inn != "ferdig":
                try:
                    qlog.snakk(int(inn) - 1, spiller, inv)
                except ValueError:
                    print("\nDu må skrive et tall!\n")
            else:
                quest = False

            #oppdaterer vasslequests
            if qlog.hent_quest(3).ferdig():
                vassleQlog.hent_quest(0).progresser()

        while gaaTilButikk:
            klasser.butikk(1).interaksjon(inv)
            gaaTilButikk = False

        while fjell:
            fiende = generer_troll(spiller)

            skriv_ut(spiller, fiende)
            fjell = angrip(spiller, fiende, inv, klasser, spellbook)

            if fjell and qlog.hent_quest(0).startet():
                qlog.hent_quest(0).progresser()

        while lagre:
            minnestein(spiller, inv, klasser)
            lagre = False

        while base:
            gsOppdaget = 0
            clear_screen()
            print("\n    Du sniker deg mot den hemmelige basen til trollene.\n")
            print("    Trollmennene armerer deg 5 ladninger svart pulver og formler for å sette")
            print("    ladninger og sprenge dem.\n")
            pause()
            print("\n    Du sniker deg inn i hulen og kommer deg til stedet du skal plassere den første")
            print("    ladningen.\n")
            seq = ["første", "andre", "tredje", "fjerde", "femte"]
            for x in range(5):
                input("Trykk enter for å plassere den {} ladningen\n> ".format(seq[x]))
                if randint(0, 10) >= 3:
                    #oppdaget gang 1 og 2
                    if gsOppdaget < 2:
                        print("Du er blitt oppdaget! En klynge med troll kommer løpende mot deg!")
                        input("Trykk enter for å slåss for livet\n> ")
                        for y in range(3 + (2 * gsOppdaget)):
                            fiende = generer_troll(spiller)
                            skriv_ut(spiller, fiende)
                            if not angrip(spiller, fiende, inv, klasser, spellbook):
                                base = False
                                qlog.hent_quest(1).reset_progresjon()
                                break
                            clear_screen()
                            print("")

                    #oppdaget gang 3: Betaen
                    elif gsOppdaget == 2:
                        skrivStortTroll()
                        print(spiller.navn(), "har blitt funnet av betaen!")
                        loot = Loot()
                        fiende = Fiende("Beta", "troll", loot, 3000, 200, 200, kp=150)
                        fiende.return_loot().legg_til_item(500, 100)
                        skriv_ut(spiller, fiende)
                        if not angrip(spiller, fiende, inv, klasser, spellbook):
                            base = False
                            qlog.hent_quest(1).reset_progresjon()
                            break
                        clear_screen()
                        print("")
                    gsOppdaget += 1

                #neste runde
                if not base: break
                print("    Du planter den", seq[x], "ladningen og kommer deg unna.\n")
                qlog.hent_quest(1).progresser()

            #Alle ladninger er satt
            if not base: break
            print("\n\nDu har satt alle ladningene, og er klar til å sprenge hulen!\n")
            input("Trykk enter for å sprenge hulen\n> ")
            print("\n" + spiller.navn(), "sprengte hulen! Du drar tilbake til hytten.\n")
            pause()
            qlog.hent_quest(1).progresser_liste(0)
            base = False

        while cave:
            for x in range(randint(3, 10)):
                fiende = generer_troll(spiller)
                skriv_ut(spiller, fiende)
                if not angrip(spiller, fiende, inv, klasser, spellbook):
                    cave = False
                    break
            if not cave: break

            # Betaen
            skrivStortTroll()
            print(spiller.navn(), "har møtt et en beta!")
            loot = Loot()
            item = Item("Trollskriv", "trinket")
            fiende = Fiende("Beta", "troll", loot, 3000, 200, 200, kp=150)
            fiende.return_loot().legg_til_item(500, 100)
            skriv_ut(spiller, fiende)
            if angrip(spiller, fiende, inv, klasser, spellbook):
                qlog.hent_quest(2).progresser()
                print("\n*Du har nå et dokument på trollsk. Kanskje det har informasjon om trollkongen?*\n")
            while input("* Trykk enter for å fortsette *\n") != "":
                pass
            cave = False

        while helvete:
            for x in range(2):
                fiende = generer_troll(spiller, True)
                skriv_ut(spiller, fiende)
                if not angrip(spiller, fiende, inv, klasser, spellbook):
                    helvete = False
                    break
            if not helvete: break

            skrivTrollBoss()
            loot = Loot()
            item = Item("Trollkongens stav", "weapon", a=100, kp=75)
            loot.legg_til_item(item, 50)
            loot.legg_til_item(3000, 50)
            fiende = Fiende("Trollkongen", "troll", loot, 6500, 450, 250, kp=250, bonusKp=5, weapon=100)
            trollkongeDialog(spiller)
            skriv_ut(spiller, fiende)
            if angrip(spiller, fiende, inv, klasser, spellbook):
                qlog.hent_quest(3).progresser()

            helvete = False

        while muskelbunt:
            medlem = spiller.spesialisering() == "Muskelbunt"
            print(" "*4 + "Velkommen {}til Muskelbunters Fellesforening!".format("tilbake " * int(medlem)).center(65 + 20*int(not medlem), "-"))
            if medlem:
                print("\n    Som medlem tilbyr vi deg internpriser på tryllepulver!")
                print("\n    Tryllepulver           -700hp                  1300g (t)")
                print("    Meld deg ut            Fjerner spesialisering   500g (u)")
                print("\nDu har", inv.penger(), "gullstykker. Skriv 'f' eller 'ferdig' for å dra tilbake.")
                inn = input("Hva vil du gjøre?\n> ").lower().strip()
                if inn in {"f", "ferdig"}:
                    muskelbunt = False
                elif inn == "t":
                    if inv.penger() >= 1300:
                        inv.legg_til_item(Item("Tryllepulver", "damaging", dmg=700))
                        inv.penger(-1300)
                        print("Du kjøpte en neve tryllepulver for 1300 gullstykker.")
                    else:
                        print("Du har ikke råd!")
                    pause()
                elif inn == "u":
                    print("Muskelbunters Fellesforening krever 500 i gebyr for papirarbeid.")
                    inn = input("Er du sikker på at du vil melde deg ut? \nDu må betale ny medlemsavgift om du vil melde deg inn igjen.   (ja/nei)\n> ").lower().strip()
                    if inn in {"j", "ja", "sure"}:
                        if inv.penger() >= 500:
                            inv.penger(-500)
                            spiller.spesialisering(False)
                            spiller.hev_a(-160)
                            print("Du har meldt deg ut av Muskelbunters Fellesforening.")
                            muskelbunt = False
                            inv.fjern_spesialiserte_items("Muskelbunt")
                            pause()
                        else:
                            print("Du har ikke råd!")
                            pause()
            else:
                print("\n    Om du blir medlem av foreningen vår vil du nyte goder du senere vil finne ut du ikke")
                print("    kan være foruten! Som medlem av Muskelbunters Fellesforening har du tilgang til en ")
                print("    trylleformel som gjør angrepene dine sterkere i 3 runder! I tillegg til dette vil du ")
                print("    få en permanent bonus på 160 angrepspoeng, samt tilgang til vårt interne lager av")
                print("    tryllepulver til innkjøpspris. Som en muskelbunt vil du og ha kunnskapen du trenger ")
                print("    til å benytte deg av utstyr som krever muskelbunt-spesialisering, OG du får en")
                print("    relativ bonus på alle angrep gjort med sverd! Her er ditt livs største mulighet, alt")
                print("    til medlemsavgift på ynkelige 10000 gullstykker! Vet du hva, side jeg liker deg så")
                print("    godt skal du faktisk få medlemsskap for bare 8000 gullstykker, spesialpris kun for")
                print("    deg! Her er ingen unnskyldning.")
                print("\nDu har", inv.penger(), "gullstykker.")
                inn = input("Vil du bli en muskelbunt?\n> ").lower().strip()
                if inn in {"ja", "j", "yes", "ja!", "hell yes!"}:
                    if inv.penger() >= 8000 and not spiller.spesialisering():
                        inv.penger(-8000)
                        spiller.spesialisering("Muskelbunt")
                        spiller.hev_a(160)
                        print("\nGratulerer! Du er nå offisielt en muskelbunt!\n")
                        pause()
                    elif inv.penger() >= 8000:
                        print("\n    Du har allerede en spesialisering! Men frykt ikke, ønsker du likevel å bli ")
                        print("    en klartenker, kan du melde deg ut av den foreningen du for øyeblikket er ")
                        print("    medlem i og komme tilbake senere!\n")
                        muskelbunt = False
                        pause()
                    else:
                        print("Du har ikke nok gullstykker til å betale medlemsavgiften!")
                        muskelbunt = False
                        pause()
                else:
                    muskelbunt = False

    if ferdig:
        return verdenskart(spiller)

def angrip(spiller, fiende, inv, klasser, spellbook):
    qlog = klasser.questlog(2)
    forsterkCD = 0
    while True:

        inn = input("\nHva vil du gjøre?\n> ").lower()

        #tur angir at det er brukeren sin tur til å handle.
        tur = kommandoer(inn, spiller, fiende, inv, klasser, spellbook)

        if inn == "f" or inn == "flykt":
            print(spiller.navn(), "drar tilbake til hytta.")
            return False

        #Her sjekkes om fienden er død. Om så, får karakteren loot og xp.
        if fiende.dead():
            print("--------------------------------------------------------------------"+\
            "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
            spiller.kons()
            spiller.gi_xp(fiende.xp())
            fiende.loot(spiller, inv)
            spellbook.reset()

            #progresserer bonusquest - Rock&Troll
            if not randint(0, 49) and not qlog.hent_quest(5).sjekk_ferdig():
                print(spiller.navn(), 'fant et "Trolling Stones"-album! Kanskje noen i hytten hører på slikt?')
                qlog.hent_quest(5).progresser()

            input("Trykk enter for å fortsette\n> ")
            return True

        elif not tur:
            if fiende.oppholdt():
                print(fiende.navn() + fiende.ending(), "er oppholdt.")
            elif fiende.race() == "troll" and fiende.kp() >= 80 and not randint(0, 10):
                print(fiende.navn() + fiende.ending(), "kastet Forsterk!")
                if fiende.navn() not in {"Beta", "Trollkongen"}:
                    print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(randint(250, 300)), \
                    "hp, og forbereder seg på et kraftig slag!")
                    fiende.kp(-80)
                    fiende.a(450)
                else:
                    print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(randint(300, 500)), \
                    "hp, og forbereder seg på et kraftig slag!")
                    fiende.kp(-80)
                    fiende.a(600)

                forsterkCD = 2
            elif fiende.kp() >= 50 and randint(0, 4) == 1 and not forsterkCD:
                print(fiende.navn() + fiende.ending(), "kastet Restituer!")
                print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(randint(90, 110)), "hp!")
                fiende.kp(-50)
            else:
                skade = spiller.angrepet(fiende)

                #progresserer Smertedreper-quest
                if klasser.questlog(4).hent_quest(6).startet():
                    klasser.questlog(4).hent_quest(6).progresser(skade)

            #gir beskjed om karakteren døde
            if spiller.dead():
                input("\nDu døde! Trykk enter for å fortsette\n> ")
                spellbook.reset()
                write_player_died(spiller, "hytta")
                player_died(spiller, inv, klasser)
                return False

            #skriver ut hp og kp til karakteren og hp til fienden til neste runde.
            else:
                spiller.kons()
                fiende.gen_kons()
                skriv_ut(spiller, fiende)
                if forsterkCD > 0:
                    forsterkCD -= 1
                    if forsterkCD == 0:
                        if fiende.navn() in {"Beta", "Trollkongen"}:
                            fiende.a(-600)
                        else:
                            fiende.a(-450)

def generer_troll(spiller, sterk=False):
    loot = Loot()
    fiende = Fiende(navn="Troll", race="troll", loot=loot, \
    hp=120 + 40 * randint(1, spiller.lvl()) + 500 * int(sterk), \
    a=20 + randint(0, 10 * spiller.lvl()) + 40 * int(sterk), \
    d=30 + randint(0, 10 * spiller.lvl()) + 60 * int(sterk), \
    kp=50 + randint(0, 3 * spiller.lvl()), bonusKp=2, ending="et")
    dynamiskLoot(loot, fiende, spiller)
    skrivTroll()
    print("\n" + spiller.navn(), "har møtt på et troll!")
    return fiende

def dynamiskLoot(loot, fiende, spiller):
    tall = round(10 + fiende.xp() / 10)
    loot.legg_til_item(tall, 60)

    dmg = 150 + randint(0, int(spiller.lvl() / 2.5)) * 25
    item = Item("Tryllepulver", "damaging", dmg=dmg)
    item.sett_loot_tekst("en håndfull tryllepulver")
    loot.legg_til_item(item, 10)

    kpkp = int(randint(1, spiller.lvl()) /10) *25 + 100
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 10)

    tdhp = randint(1, spiller.lvl()) * 5 + 175
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

    xHp = randint(15, 4 * spiller.lvl())
    d = randint(15, 2 * spiller.lvl())
    item = Item("Trollhode", "hat", xHp=xHp, d=d)
    item.sett_loot_tekst("et trollhode")
    loot.legg_til_item(item, 5)

    xHp = randint(0, 2 * spiller.lvl())
    d = int(randint(0, 4 * spiller.lvl()) /10) *10
    item = Item("Trollskinn-kjole", "robe", xHp=xHp, d=d)
    loot.legg_til_item(item, 5)

def trollKart(qlog):
    skrivHytte()
    print("""
    Velkommen til fjellhytta! Her er stedene du kan dra:
    Fjellet (m)                Gå på fjelltur og forsvar deg mot perverse troll
    Butikken (k)               Kjøp det du trenger hos "Fe Fi Fo - Familiebutikk"
    Badstua (q)                Se om de rynkete gamle trollmennene trenger noe hjelp""")
    if qlog.hent_qLog()[1].startet() and not qlog.hent_qLog()[1].sjekk_ferdig():
        print("    Hulen (b)                  Snik deg inn den hemmelige basen til trollene!")
    if qlog.hent_qLog()[2].startet() and not qlog.hent_qLog()[2].ferdig():
        print("    Minen (c)                  Invader det mørke, dype hjemmet til trollfolket!")
    if qlog.hent_qLog()[3].startet():
        print("    Helvetesgapet (h)          Konfronter trollkongen!")
    if qlog.hent_qLog()[4].ferdig():
        print("    Nabodimensjonshytten (n)   Transporter deg til Muskelbunters Fellesforenings hovedkontor")
    print("    Minnesteinen (l)           Lagre sjelen din i hyttens lokale minnestein")
    print("    Ut i verden (f)            Viser deg kart over alle stedene du kan dra\n")

def trollButikk(butikk):
    butikk.legg_til_hadeTekst("\nVelkommen tilbake! Og pass deg for troll!\n")

    item = Item("Tryllepulver", "damaging", dmg=250)
    vare = Vare(item, 300, "t")
    butikk.legg_til_vare(vare)

    item = Item("Trolldrikk", "restoring", hp=300)
    vare = Vare(item, 400, "d")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=150)
    vare = Vare(item, 500, "k")
    butikk.legg_til_vare(vare)

    item = Item("Tryllestav", "weapon", a=85, xKp=45)
    vare = Vare(item, 2000, "w")
    butikk.legg_til_vare(vare)

    item = Item("Sverd", "weapon", a=90, xHp=20)
    vare = Vare(item, 2500, "v")
    butikk.legg_til_vare(vare)

    item = Item("Fjellstøvler", "shoes", xKp=30, d=40)
    vare = Vare(item, 2800, "ø")
    butikk.legg_til_vare(vare)

def trollkongeDialog(spiller):
    navn = spiller.navn()
    print("""   Det er du! Du som drepte så mange av mine barn ved hytta!
    Du som sprengte vesthulen! Du som tok ned to av mine næreste! Du som
    angrep minen! En magiker tusen ganger bedre enn deg har gitt meg magiske
    evner, og jeg kommer ikke til å skuffen ham nå. Jeg har ventet på en
    hvilken som helst sjanse til å finne deg, ta deg og rive ut alle
    innvollene dine! Vel, det trengte jeg ikke å gjøre. Du kom til meg!
    Du kommer aldri til å slippe unna!\n""")

def trollQuest(qlog, spiller):
    navn = spiller.navn()

    #q1
    desk1 = troll_q1(navn)
    ferdigDesk1 = troll_q1_ferdig(navn)
    q1 = Quest(desk1, ferdigDesk1, 25, 15, "Rolf Rynkerumpe")
    q1.legg_til_reward(xp=3000, gull=500, settTilgjengelig=True, settTilgjengeligIndeks=1)
    q1.legg_til_progresjonTekst("Troll slaktet: ")
    q1.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q1)

    #q2
    desk2 = troll_q2(navn)
    ferdigDesk2 = troll_q2_ferdig(navn)
    q2 = Quest(desk2, ferdigDesk2, 5, 15, "Senile Sverre", tilgjengelig=False)
    q2.legg_til_reward(xp=3500, gull=700, settTilgjengelig=True, settTilgjengeligIndeks=2)
    q2.legg_til_progresjonTekst("Ladninger satt: ")
    q2.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    q2.legg_til_progresjon(1)
    q2.legg_til_progresjonTekstListe("Hule sprengt: ", 0)
    qlog.legg_til_quest(q2)

    #q3
    desk3 = troll_q3(navn)
    ferdigDesk3 = troll_q3_ferdig(navn)
    q3 = Quest(desk3, ferdigDesk3, 1, 16, "Zip", tilgjengelig=False)
    item = Item("Trollskjegg", "beard", xKp=30, ekstraKp=2)
    q3.legg_til_reward(xp=5000, gull=800, item=item, settTilgjengelig=True, settTilgjengeligIndeks=3)
    q3.legg_til_progresjonTekst("Digert troll drept: ")
    q3.legg_til_svarTekst("\nVil du drepe det store trollet?    (ja/nei)\n> ")
    qlog.legg_til_quest(q3)

    #q4
    desk4 = troll_q4(navn)
    ferdigDesk4 = troll_q4_ferdig(navn)
    q4 = Quest(desk4, ferdigDesk4, 1, 16, "Zip", tilgjengelig=False)
    q4.legg_til_reward(xp=10000, gull=1000)
    q4.legg_til_progresjonTekst("Trollkongen bekjempet: ")
    q4.legg_til_svarTekst("\nVil du ta ned Trollkongen?    (ja/nei)\n> ")
    qlog.legg_til_quest(q4)

    #muskelbunt-quest
    desk = muskelbunt_intro(navn)
    ferdigDesk = muskelbunt_intro_ferdig(navn)
    q = Quest(desk, ferdigDesk, 75000, 20, "Maja Muskelbunt")
    q.legg_til_reward(xp=10000, gull=5000, a=50)
    q.legg_til_progresjonTekst("Helsepoeng tatt: ")
    q.legg_til_svarTekst("\nØnsker du å søke om å spesialisere deg som Muskelbunt?    (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #bq1
    deskBq1 = troll_bq1(navn)
    ferdigDeskBq1 = troll_bq1_ferdig(navn)
    bq1 = Quest(deskBq1, ferdigDeskBq1, 1, 1, "Tonedøve Tord", bonus=True, resetIfDead=True)
    item = Item("Tung gitar", "weapon", a=125, d=50, blade=True)
    bq1.legg_til_reward(gull=300, ekstraKp=1, item=item, gp=2)
    bq1.legg_til_ekstra_tekst("    Tusen takk " + spiller.navn() + """! Jeg vet ikke hva jeg skulle gjort uten denne himmelske lyden!
    Ta gitaren min! Jeg er ikke så flink til å spille uansett...\n""")
    bq1.legg_til_progresjonTekst('"Trolling Stones"-album funnet: ')
    bq1.legg_til_svarTekst("Vil du gi albumet til Tonedøve Tord?   (ja/nei)\n> ")
    bq1.legg_til_alt_desk("Vil du brenne CD-en med det kristne gnomkorets julemusikk?\n> ")
    bq1.legg_til_alt_reward(gull=300, ekstraKp=1, item=item, ep=2)
    bq1.legg_til_alt_ekstra_tekst("    Tusen takk " + spiller.navn() + """! Jeg vet ikke hva jeg skulle gjort uten denne himmelske lyden!
    Ta gitaren min! Jeg er ikke så flink til å spille uansett...\n""")
    qlog.legg_til_quest(bq1)
