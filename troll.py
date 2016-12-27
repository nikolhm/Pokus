"""
                *~ Troll- expansion ~*

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
        cave = False
        helvete = False
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

            if inn == "m":
                fjell = True
                valg = True

            if inn == "l":
                lagre = True
                valg = True

            if inn == "c" and qlog.hent_quest(1).startet() and not qlog.hent_quest(1).ferdig():
                cave = True
                valg = True

            if inn == "h" and qlog.hent_quest(2).startet():
                helvete = True
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

        while gaaTilButikk:
            klasser.butikk(1).interaksjon(inv)
            gaaTilButikk = False

        while fjell:
            fiende = generer_troll(spiller)

            skriv_ut(spiller, fiende)
            fjell = angrip(spiller, fiende, inv, klasser, spellbook)

            if fjell and qlog.hent_quest(0).startet():
                qlog.hent_quest(0).progresser()

        #Denne løkken lagrer spillet.
        while lagre:
            minnestein(spiller, inv, klasser)
            lagre = False

        while cave:
            #Fiende 1
            fiende = generer_troll(spiller)
            skriv_ut(spiller, fiende)
            if not angrip(spiller, fiende, inv, klasser, spellbook):
                cave = False
                break
            #qlog.hent_quest(1).progresser()

            #Fiende 2
            fiende = generer_troll(spiller)
            skriv_ut(spiller, fiende)
            if not angrip(spiller, fiende, inv, klasser, spellbook):
                cave = False
                break
            #qlog.hent_quest(1).progresser_liste(0)

            #Fiende 3
            skrivStortTroll()
            print(spiller.navn(), "har møtt et enormt troll!")
            loot = Loot()
            item = Item("Trollskriv", "trinket")
            fiende = Fiende("Enormt troll", "troll", loot, 1000, 200, 200, kp=150)
            fiende.return_loot().legg_til_item(500, 100)
            skriv_ut(spiller, fiende)
            if angrip(spiller, fiende, inv, klasser, spellbook):
                qlog.hent_quest(1).progresser()
                print("\n*Du har nå et dokument på trollsk. Kanskje det har informasjon om trollkongen?*\n")
            while input("* Trykk enter for å fortsette *\n") != "":
                pass
            cave = False

        "Quest nummer 3 skal slå en boss, og er satt i egen instans."
        while helvete:
            skrivTrollBoss()
            loot = Loot()
            item = Item("Trollkongens stav", "weapon", a=200, kp=200)
            loot.legg_til_item(item, 50)
            loot.legg_til_item(3000, 50)
            fiende = Fiende("Trollkongen", "trollmagiker", loot, 2500, 300, 250, kp=100, bonusKp=5, weapon=60)

            print("        " + spiller.navn(), """har møtt sisteboss! Han forklarer alt,
        korrupsjonen av trollene osv. Han snakker så lenge at det
        burde egentlig blitt lagt til en egen prosedyre.\n""")
            skriv_ut(spiller, fiende)
            if angrip(spiller, fiende, inv, klasser, spellbook):
                qlog.hent_quest(2).progresser()

            helvete = False

    if ferdig:
        return verdenskart(spiller)

def angrip(spiller, fiende, inv, klasser, spellbook):
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
            input("Trykk enter for å fortsette\n> ")
            return True

        elif not tur:
            if fiende.kp() >= 50 and randint(0, 1) == 1:
                print(fiende.navn() + fiende.ending(), "kastet Restituer!")
                print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(100), "hp!")
                fiende.bruk_kons(50)
            else:
                spiller.angrepet(fiende)

            #gir beskjed om karakteren døde
            if spiller.dead():
                write_player_died(spiller, "stallen")
                player_died(spiller, inv, klasser)
                return False

            #skriver ut hp og kp til karakteren og hp til fienden til neste runde.
            else:
                spiller.kons()
                fiende.gen_kons()
                skriv_ut(spiller, fiende)

def generer_troll(spiller):
    loot = Loot()
    fiende = Fiende(navn="Troll", race="troll", loot=loot, \
    hp=20 + 20 * randint(1, spiller.lvl()), \
    a=20 + randint(0, 10 * spiller.lvl()), \
    d=30 + randint(0, 10 * spiller.lvl()), \
    kp=50 + randint(0, 3 * spiller.lvl()), bonusKp=2, ending="et")

    "Setter fiendens loot i en egen prosedyre."
    dynamiskLoot(loot, fiende, spiller)
    print("\n" + spiller.navn(), "har møtt på et troll!")

    "Om det finnes ascii-art til fienden, printes den ut her."
    skrivTroll()
    return fiende

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

def statiskLoot(loot):
    loot.legg_til_item(500, 50)

    item = Item("Trollhode", "hat", xHp=70, d=60)
    item.sett_loot_tekst("et trollhode")
    loot.legg_til_item(item, 25)

    item = Item("Trollskinn-kjole", "robe", xHp=20, d=100)
    loot.legg_til_item(item, 25)

def trollKart(qlog):
    skrivHytte()
    print("""
    Velkommen til fjellhytta! Her er stedene du kan dra:
    Fjellet (m)                Gå på fjelltur og forsvar deg mot perverse troll
    Butikken (k)               Kjøp det du trenger hos "Fe Fi Fo - Familiebutikk"
    Badstua (q)                Se om de rynkete gamle trollmennene trenger noe hjelp""")
    if qlog.hent_qLog()[1].startet() and not qlog.hent_qLog()[1].ferdig():
        print("    Minen (c)                  Invader det mørke, dype hjemmet til trollfolket!")
    if qlog.hent_qLog()[2].startet():
        print("    Helvetesgapet (h)          Konfronter trollkongen!")
    print("    Minnesteinen (l)           Lagre sjelen din i borgens lokale minnestein")
    print("    Ut i verden (f)            Viser deg kart over alle stedene du kan dra\n")

def trollButikk(butikk):
    butikk.legg_til_hadeTekst("\nVelkommen tilbake! Og pass deg for troll!\n")

    item = Item("Tryllepulver", "damaging", dmg=100)
    vare = Vare(item, 50, "t")
    butikk.legg_til_vare(vare)

    item = Item("Trolldrikk", "restoring", hp=300)
    vare = Vare(item, 400, "d")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=200)
    vare = Vare(item, 500, "k")
    butikk.legg_til_vare(vare)

    item = Item("Tryllestav", "weapon", a=200, xKp=45)
    vare = Vare(item, 3000, "w")
    butikk.legg_til_vare(vare)

    item = Item("Sverd", "weapon", a=300, xHp=20)
    vare = Vare(item, 9000, "v")
    butikk.legg_til_vare(vare)

    item = Item("Falskt skjegg", "beard", xKp=30, ekstraKp=3)
    vare = Vare(item, 1100, "g")
    butikk.legg_til_vare(vare)

def trollQuest(qlog, spiller):
    navn = spiller.navn()

    desk1 = quests.troll_q1(navn)
    ferdigDesk1 = quests.troll_q1_ferdig(navn)
    q1 = Quest(desk1, ferdigDesk1, 25, 15, "Rolf Rynkerumpe")
    q1.legg_til_reward(xp=5000, gull=2000)
    q1.legg_til_progresjonTekst("Troll slaktet: ")
    q1.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q1)


    #q2
    """Her skal tre forskjellige fiender bekjempes. Hver har sin egen progresjon.
    Ved fullførelse av dette questet, skal det neste questet settes tilgjengelig (Quest-chains)."""
    desk2 = quests.troll_q2(navn)
    ferdigDesk2 = quests.troll_q2_ferdig(navn)
    q2 = Quest(desk2, ferdigDesk2, 1, 16, "Zip")
    item = Item("Trollskjegg", "beard", xKp=80, ekstraKp=20)
    q2.legg_til_reward(xp=1000, gull=2500, item=item, settTilgjengelig=True, settTilgjengeligIndeks=2)
    q2.legg_til_progresjonTekst("Digert troll drept: ")
    q2.legg_til_svarTekst("\nVil du drepe det store trollet?    (ja/nei)\n> ")
    qlog.legg_til_quest(q2)

    #q3
    desk3 = quests.troll_q3(navn)
    ferdigDesk3 = "Kjempebra " + navn + "! Nå kan jeg endelig ta av meg dette skjegget og dra hjem!"
    q3 = Quest(desk3, ferdigDesk3, 1, 16, "Zip", tilgjengelig=False)
    q3.legg_til_reward(xp=5000, gull=2000)
    q3.legg_til_progresjonTekst("Trollkongen bekjempet: ")
    q3.legg_til_svarTekst("\nTa ned Trollkongen!    (ja/nei)\n> ")
    qlog.legg_til_quest(q3)
