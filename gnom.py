from klasser import *
from prosedyrer import *
from grafikk import *

#Hoved-løkke
def gnomeloop(spiller, inv, klasser, spellbook):
    qlog = klasser.questlog(1)
    vassleQlog = klasser.questlog(5)
    #Variabler brukt senere.
    goingToGaute = False
    gnomevakter = 0
    ferdig = False

    while spiller.dead() == False and ferdig == False:
        #Gir informasjon om hvilke valg man har.
        kart(qlog.hent_qLog(), vassleQlog.hent_qLog())

        #Deklererer variabler som brukes i while-løkkene.
        velg = False
        run = True
        butikk = False
        quest = False
        spir = False
        lagre = False

        #I denne while-løkken bestemmer brukeren hvor man man vil dra.
        #Man har i hovedsak tre alternativer: skogen (slåss med gnomer),
        #butikken (kjøpe ting) og "storsalen" hvor man kan ta imot og levere quest.
        while velg == False:
            inn = input("\nHvor vil du gå?\n> ").lower()

            if inn == "s":
                run = False
                velg = True
                mini_hjelp()
                input("Trykk enter for å fortsette\n> ")

            if inn == "k":
                butikk = True
                velg = True

            if inn == "q":
                quest = True
                velg = True

            if inn == "g" and qlog.hent_quest(5).startet():
                run = False
                velg = True
                goingToGaute = True

            if inn == "h" and qlog.hent_quest(5).ferdig():
                velg = True
                spir = True

            if inn == "f" and (vassleQlog.hent_quest(0).startet() or \
            vassleQlog.hent_quest(1).startet() or vassleQlog.hent_quest(2).startet()):
                velg = True
                ferdig = True

            if inn == "l":
                velg = True
                lagre = True

        #Denne løkken lar brukeren kjøpe ting i butikken.
        while butikk == True:
            klasser.butikk(0).interaksjon(inv)
            butikk = False

        #Denne løkken begynner med å liste opp alle tilgjengelige quest. Etterpå
        #kan man velge hvilke quest man vil høre mer om. Om man ikke møter kravene
        #for et quest, skjer ingenting.
        while quest == True:
            #Merk at oppdrag_tilgjengelige() er en funksjon med returverdi.
            inn = qlog.oppdrag_tilgjengelige(spiller.lvl(), "storhallen")
            if inn != "f" and inn != "ferdig":
                try:
                    qlog.snakk(int(inn) - 1, spiller, inv)
                except ValueError:
                    print("\nDu må skrive et tall!\n")
            else:
                quest = False

        #Denne løkken går gjennom Overtrollmann Vassles questlog.
        while spir:
            inn = vassleQlog.oppdrag_tilgjengelige(spiller.lvl(), "det høyeste spirtårnet")
            if inn != "f" and inn != "ferdig":
                try:
                    vassleQlog.snakk(int(inn) - 1, spiller, inv)
                except ValueError:
                    print("\nDu må skrive et tall!\n")
            else:
                spir = False
                if vassleQlog.hent_quest(3).startet():
                    spiller.sett_sted_tilgjengelig(5)

        #Denne løkken lagrer spillet.
        while lagre:
            minnestein(spiller, inv, klasser)
            lagre = False

        #Denne løkken omhandler angrepsmodus og interaksjon mellom de to klassene.
        #Løkken kjører så lenge karakteren er i livet og brukeren ikke har skrevet
        #kommandoen "løp".
        #Denne løkken inneholder en annen løkke. Den andre løkken kjører helt til
        #fienden er beseiret, så hopper den ut av løkken og genererer en ny fiende
        #i starten av den første løkken, før den hopper tilbake til den andre løkken igjen.
        while run == False:
            #Genererer fiender
            fiende = generer_gnom(spiller, gnomevakter, goingToGaute)
            #kamp-løkken
            #Her kan brukeren skrive forskjellige kommandoer etter hva den ønsker å
            #gjøre eller hvilken informasjon den vil ha opp.
            resultatListe = attack_gnom(spiller, fiende, inv, qlog, goingToGaute, gnomevakter, klasser, spellbook)
            run = resultatListe[0]
            goingToGaute = resultatListe[1]
            gnomevakter = resultatListe[2]
            if run:
                gnomevakter = 0
                goingToGaute = False

    if ferdig:
        return verdenskart(spiller)

def generer_gnom(spiller, gnomevakter, goingToGaute):
    loot = Loot()
    #Vanlige gnomer i skogen
    #Lager et objekt av klassen Fiende. Fienden skaleres etter lvl til karakteren.
    if goingToGaute == False:
        fiende = Fiende("Gnom", "gnom", loot, \
        20 + 20 * randint(1, spiller.lvl()), \
        20 + randint(0, 10 * spiller.lvl()), \
        30 + randint(0, 10 * spiller.lvl()), ending="en")
        gnomLoot(fiende, loot, spiller)
        skrivGnom()
        print("\n" + spiller.navn(), "har møtt på en gnom!")

    #goingToGaute indikerer at brukeren holder på med det siste questet.
    #Da skal gnomene være en del sterkere enn de vanlige, for å gjøre kampen
    #mot Gaute Gnom den Grusomme vanskeligere.
    if goingToGaute and gnomevakter < 5:
        fiende = Fiende("Gnomevakt " + str(gnomevakter + 1), "gnom", loot, \
        220 + 20 * randint(gnomevakter, spiller.lvl()), \
        120 + randint(gnomevakter * 10, 10 * spiller.lvl()), \
        130 + randint(gnomevakter * 10, 10 * spiller.lvl()))
        gnomvaktLoot(fiende, loot, spiller)
        skrivGnom()
        print("\n" + spiller.navn(), "har møtt på Gaute Gnoms dørvakt nr.", gnomevakter + 1)

    #Når man har kommet forbi 5 vakter, møter karakteren Gaute Gnom.
    elif goingToGaute and gnomevakter == 5:
        fiende = Fiende("Gaute Gnom den Grusomme", "gnom", loot, 5000, 230, 150)
        gauteLoot(loot)
        gauteDialog(spiller)

    #Skriver ut statsene til fienden og karakteren før kampen har startet til orientering.
    skriv_ut(spiller, fiende)

    return fiende

def gnomLoot(fiende, loot, spiller):
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

    xHp = randint(0, 4 * spiller.lvl())
    d = randint(0, 2 * spiller.lvl())
    item = Item("Spiss Hatt", "hat", xHp=xHp, d=d)
    loot.legg_til_item(item, 5)

    ekstraKp = int(randint(10, 10 + spiller.lvl()) / 10)
    xHp = int(randint(1, 21 + spiller.lvl()) / 10) * 10
    xKp = int(randint(1, 10 + spiller.lvl()) / 10) * 20
    a = int(randint(1, 10 + spiller.lvl() * 2) / 10) * 5
    item = Item("Polert Stein", "trinket", ekstraKp=ekstraKp, xHp=xHp, xKp=xKp, a=a)
    loot.legg_til_item(item, 1)

def gnomvaktLoot(fiende, loot, spiller):
    tall = round(10 + fiende.xp() / 7)
    loot.legg_til_item(tall, 50)

    item = Item("Tryllepulver", "damaging", dmg=100)
    item.sett_loot_tekst("en håndfull tryllepulver")
    loot.legg_til_item(item, 2)

    kpkp = int(randint(1, spiller.lvl()) /10) *25 + 125
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 20)

    tdhp = randint(1, spiller.lvl()) * 5 + 175
    item = Item("Trolldrikk", "restoring", hp=tdhp)
    loot.legg_til_item(item, 13)

    a = randint(20, 5 * spiller.lvl())
    xKp = randint(15, 4 * spiller.lvl())
    item = Item("Tryllestav", "weapon", a=a, xKp=xKp)
    loot.legg_til_item(item, 7)

    xHp = randint(20, 5 * spiller.lvl())
    d = randint(10, 3 * spiller.lvl())
    item = Item("Spiss Hatt", "hat", xHp=xHp, d=d)
    loot.legg_til_item(item, 7)

    ekstraKp = int(randint(10, 10 + spiller.lvl()) / 10)
    xHp = int(randint(1, 21 + spiller.lvl()) / 10) * 10
    xKp = int(randint(1, 10 + spiller.lvl()) / 10) * 20
    a = int(randint(1, 10 + spiller.lvl() * 2) / 10) * 5
    item = Item("Polert Stein", "trinket", ekstraKp=ekstraKp, xHp=xHp, xKp=xKp, a=a)
    loot.legg_til_item(item, 7)

def gauteLoot(loot):
    loot.legg_til_item(1500, 20)

    item = Item("Grusom hatt", "hat", xHp=100, d=75)
    item.sett_loot_tekst("en Grusom hatt")
    loot.legg_til_item(item, 20)

    item = Item("Grusomme klær", "robe", xHp=100, d=30)
    item.sett_loot_tekst("et sett med Grusomme klær")
    loot.legg_til_item(item, 20)

    item = Item("Grusom kvist", "weapon", a=100, xKp=75)
    item.sett_loot_tekst("en Grusom kvist som ser ut til å være kapabel til å utføre magi med")
    loot.legg_til_item(item, 20)

    item = Item("Grusomme knokebeskyttere", "gloves", xHp=40, d=40)
    item.sett_loot_tekst("et par Grusomme knokebeskyttere")
    loot.legg_til_item(item, 20)

#Angrepsløkken mot gnomene. Inkluderer gnomevakter og Gaute Gnom den Grusomme.
def attack_gnom(spiller, fiende, inv, qlog, goingToGaute, gnomevakter, klasser, spellbook):
    run = False
    angrep = True
    while angrep:
        inn = input("\nHva vil du gjøre?\n> ").lower()

        #tur angir at det er brukeren sin tur til å handle.
        tur = kommandoer(inn, spiller, fiende, inv, klasser, spellbook)

        #Løper fra kampen. Går ut av begge løkkene, og drar tilbake til borgen.
        #Om man var på vei til grotten til Gaute Gnom, mistes progresjonen.
        if inn == "f" or inn == "flykt":
            angrep = False
            run = True
            if not qlog.hent_quest(5).sjekk_ferdig():
                qlog.hent_quest(5).reset_progresjon()
            print(spiller.navn(), "drar tilbake til borgen.")

        #Her sjekkes om fienden er død. Om så, får karakteren loot, xp, og
        #eventuell quest-progresjon.
        if fiende.dead():
            print("--------------------------------------------------------------------"+\
            "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
            spiller.kons()
            spiller.gi_xp(fiende.xp())
            fiende.loot(spiller, inv)

            #øker antall gnomer drept i quest 1
            if qlog.hent_quest(0).startet() and not qlog.hent_quest(0).ferdig():
                qlog.hent_quest(0).progresser()

            #Gir mulighet for sminke-drop i quest 3
            if qlog.hent_quest(2).startet() and not qlog.hent_quest(2).ferdig():
                    if randint(1, 5) == 5 and qlog.hent_quest(2).progresjon() < 6:
                        print("Du fant en av Fine Fredrikkes sminkeartikler!")
                        qlog.hent_quest(2).progresser()

            #Gir mulighet for sopp-drop
            if not qlog.hent_quest(6).ferdig() and qlog.hent_quest(6).progresjon() == 0:
                if randint(1,100) == 42:
                    qlog.hent_quest(6).progresser()
                    print("Du fant en magisk sopp! Kanskje noen i borgen trenger en slik?")

            #gir mulighet for oppgaveretter-drop
            if not qlog.hent_quest(7).ferdig() and qlog.hent_quest(7).progresjon() == 0:
                if randint(1, 10) == 10:
                    qlog.hent_quest(7).progresser()
                    print("Du fant en trylleformel som retter oppgaver. Så rart!")

            #Øker progresjonen mot Gaute Gnoms grotte.
            if goingToGaute:
                gnomevakter += 1
                qlog.hent_quest(5).progresser()

                #Øker antall "Gaute Gnom bekjempet" med 1.
                if gnomevakter == 6:
                    goingToGaute = False
                    qlog.hent_quest(5).progresser_liste(0)
                    gnomevakter = 0
                    print("\n   ","*" + spiller.navn(), "har bekjempet Gaute Gnom den Grusomme!*\n")
                    run = True

            angrep = False
            input("Trykk enter for å fortsette\n> ")

        #Om fienden ikke er død, angriper den.
        elif not tur:
            spiller.angrepet(fiende)

            #gir beskjed om karakteren døde
            if spiller.dead():
                write_player_died(spiller, "borgen")
                player_died(spiller, inv, klasser)
                angrep = False
                run = True

            #skriver ut hp og kp til karakteren og hp til fienden til neste runde.
            else:
                spiller.kons()
                fiende.gen_kons()
                skriv_ut(spiller, fiende)

    liste = [run, goingToGaute, gnomevakter]
    return liste

#Setter sortimentet for Kåres butikk.
def kaaresButikk(butikk):
    butikk.legg_til_hadeTekst("\nHa en magisk dag, og velkommen tilbake!\n")

    item = Item("Tryllepulver", "damaging", dmg=100)
    vare = Vare(item, 50, "t")
    vare.legg_til_buyText("Hvor mange never tryllepulver vil du ha?\n> ")
    butikk.legg_til_vare(vare)

    item = Item("Trolldrikk", "restoring", hp=150)
    vare = Vare(item, 150, "d")
    vare.legg_til_buyText("Hvor mange flasker med trolldrikk vil du ha?\n> ")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=100)
    vare = Vare(item, 250, "k")
    vare.legg_til_buyText("Hvor mange striper med konsentrasjonspulver vil du ha?\n> ")
    butikk.legg_til_vare(vare)

    item = Item("Oliwand 2000", "weapon", a=40, xKp=30)
    vare = Vare(item, 800, "w")
    butikk.legg_til_vare(vare)

    item = Item("Hatt:Spiss^Blå", "hat", xHp=50, d=40)
    vare = Vare(item, 800, "h")
    butikk.legg_til_vare(vare)

#Setter inn questene for gnomeborgen.
def gnomequest(qlog, spiller):
    #q1
    desk1 = quests.q1(spiller.navn())
    ferdigDesk1 = quests.q1ferdig(spiller.navn())
    q1 = Quest(desk1, ferdigDesk1, 10, 1, "Mette Merkelig")
    q1.legg_til_reward(xp=500, gull=100)
    q1.legg_til_progresjonTekst("Gnomer myrdet: ")
    q1.legg_til_svarTekst("Vil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q1)


    #q2
    desk2 = quests.q2(spiller.navn())
    ferdigDesk2 = quests.q2ferdig(spiller.navn())
    q2 = Quest(desk2, ferdigDesk2, 300, 3, "Gale Gizly")
    q2.legg_til_reward(xp=1000, gull=120, hp=20, settTilgjengelig=True, settTilgjengeligIndeks=4)
    q2.legg_til_progresjonTekst("Helsepoeng restorert: ")
    q2.legg_til_svarTekst("Vil du hjelpe meg?    (ja/nei)\n> ")
    qlog.legg_til_quest(q2)

    #q3
    desk3 = quests.q3(spiller.navn())
    ferdigDesk3 = quests.q3ferdig(spiller.navn())
    q3 = Quest(desk3, ferdigDesk3, 6, 5, "Fine Fredrikke", resetIfDead=True)
    q3.legg_til_reward(xp=2000, kp=15)
    q3.legg_til_progresjonTekst("Sminkeartikler funnet: ")
    q3.legg_til_svarTekst("Vil du hjelpe meg bli borgens vakreste igjen?    (ja/nei)\n> ")
    qlog.legg_til_quest(q3)

    #q4
    desk4 = quests.q4(spiller.navn())
    ferdigDesk4 = quests.q4ferdig(spiller.navn())
    q4 = Quest(desk4, ferdigDesk4, 5, 9, "Magiske Mikkel")
    q4.legg_til_reward(xp=4000, ekstraKp=5)
    q4.legg_til_ekstra_tekst(spiller.navn()+" har lært en kraftigere versjon av 'vind'!")
    q4.legg_til_progresjonTekst("Vindkast utført: ")
    q4.legg_til_svarTekst("Vil du bli en superawesome magiker?    (ja/nei)\n> ")
    qlog.legg_til_quest(q4)

    #q5
    desk5 = quests.q5(spiller.navn())
    ferdigDesk5 = quests.q5ferdig(spiller.navn())
    q5 = Quest(desk5, ferdigDesk5, 3, 11, "Gale Gizly", tilgjengelig=False)
    item = Item("Svart skjegg", "beard", xKp=5, ekstraKp=1)
    q5.legg_til_reward(xp=8000, item=item)
    q5.legg_til_ekstra_tekst(spiller.navn() + " har lært et nytt spesialangrep, 'konsentrer energi' (ke)!")
    q5.legg_til_progresjonTekst("Super restituer utført: ")
    q5.legg_til_svarTekst("Vil du lære hemmeligheten?    (ja/nei)\n> ")
    qlog.legg_til_quest(q5)

    #q6
    desk6 = quests.q6(spiller.navn())
    ferdigDesk6 = quests.q6ferdig(spiller.navn())
    q6 = Quest(desk6, ferdigDesk6, 5, 15, "Symmetriske Sara", resetIfDead=True)
    q6.legg_til_reward(xp=10000, gull=2000, hp=50, kp=40, ekstraKp=2)
    q6.legg_til_progresjonTekst("Gautes gnomevakter bekjempet: ")
    q6.legg_til_svarTekst("Vil konfrontere Gaute Gnome den Grusomme?    (ja/nei)\n> ")
    q6.legg_til_progresjon(1)
    q6.legg_til_progresjonTekstListe("Gaute Gnom den Grusomme bekjempet: ", 0)
    qlog.legg_til_quest(q6)

    #bq1
    deskBq1 = quests.bonus_q1(spiller.navn())
    ferdigDeskBq1 = quests.bonus_q1ferdig(spiller.navn())
    bq1 = Quest(deskBq1, ferdigDeskBq1, 1, 1, "Rotete Randi", bonus=True, resetIfDead=True)
    item = Item("Superspiss hatt", "hat", xHp=70, d=55)
    bq1.legg_til_reward(gull=300, ekstraKp=1, item=item, gp=2)
    bq1.legg_til_ekstra_tekst("Tusen takk " + spiller.navn() + "! Tusen hjertelig takk! Endelig er jeg gjenforent med min kjære sopp!\n")
    bq1.legg_til_progresjonTekst("Magisk sopp funnet: ")
    bq1.legg_til_svarTekst("Vil du gi den magiske soppen til Rotete Randi?   (ja/nei)\n> ")
    bq1.legg_til_alt_desk("Vil du fortære soppen foran ansiktet hennes?\n> ")
    bq1.legg_til_alt_reward(ep=3, ekstraKp=1, xp=3000)
    qlog.legg_til_quest(bq1)

    #bq2
    deskBq2 = quests.bonus_q2(spiller.navn())
    ferdigDeskBq2 = quests.bonus_q2ferdig(spiller.navn())
    bq2 = Quest(deskBq2, ferdigDeskBq2, 1, 1, "Mirakuløse Marte", bonus=True, resetIfDead=True)
    item = Item("Begynnerstav", "weapon", a=10, xKp=10)
    bq2.legg_til_reward(xp=300, item=item, gp=2)
    bq2.legg_til_ekstra_tekst("Supert! Her har du en tryllestav som takk! Det er en nybegynnerstav, men du trenger en for å gjøre mer avansert magi.\n")
    bq2.legg_til_progresjonTekst("Magisk oppgaveretter funnet: ")
    bq2.legg_til_svarTekst("Vil du gi den magiske oppgaveretteren til Mirakuløse Marte?   (ja/nei)\n> ")
    bq2.legg_til_alt_desk("Vil du rive den opp og kaste den på ansiktet hennes?\n> ")
    bq2.legg_til_alt_reward(ep=3)
    qlog.legg_til_quest(bq2)

def gauteDialog(spiller):
    skrivGaute()
    print("""\n\n***Du har funnet hulen til Gaute Gnom den Grusomme!***\n\n""")
    input("Trykk enter for å fortsette\n> ")
    print("\n\n    Gaute Gnom: Velkommen til min hule,",spiller.navn() + """!
    Siden jeg skal drepe deg nå, kan jeg avsløre mine dypeste hemligheter for
    deg, uten å ha noen grunn for å tenke at du kommer til å bekjempe meg og
    si videre at jeg egentlig jobber for en mye kraftigere magiker enn deg, og
    slike ting. Så, her er min historie: Det begynte en sommerdag i november
    da jeg skulle ut for å samle nøtter til moren min...\n\n""" + spiller.navn(), \
    """blir søvnig og begynner å sove.""")
    input("Trykk enter for å fortsette\n> ")
    print("""\n    ... også sa hun til meg at hun ikke likte meg likevel, men jeg kunne jo ikke
    si det til mine buddys, for det er svært sett ned på i gnomemiljøet, samtidig
    som dramaet med jazz-damen utspilte seg...\n""")
    input("Trykk enter for å fortsette\n> ")
    print("    SOVER DU?!?!? Hvordan våger du?? Jeg skal vise deg jeg!\n")
    input("Trykk enter for å slåss mot Gaute Gnom den Grusomme\n> ")

#Skriver ut hvilke steder man kan dra når man er i borgen (hvilemodus).
def kart(qListe, qListeVassle):
    skrivSlott()
    print("""
    Velkommen til magi-borgen! Her er stedene du kan dra:
    Skogen (s)                 Dra ut i skogen og bekjemp de onde gnomene
    Butikken (k)               Kjøp det du trenger hos "Kåres hokus og andre hokuspokus"
    Storhallen (q)             Se om noen i storhallen trenger din hjelp""")
    if qListe[5].startet():
        print("    Gaute Gnom's hule (g)      Konfronter Gaute Gnom den Grusomme!")
    if qListe[5].ferdig():
        print("    Det høyeste spiret (h)     Besøk kontoret til Overtrollmann Vassle")
    print("    Minnesteinen (l)           Lagre sjelen din i borgens lokale minnestein")
    if qListeVassle[0].startet() or qListeVassle[1].startet() or qListeVassle[2].startet():
        print("    Ut i verden (f)            Viser deg kart over alle stedene du kan dra")

def vassle_quest(qlog, spiller):
    #troll
    desk1 = quests.vassle_troll(spiller.navn())
    ferdigDesk1 = quests.vassle_troll_ferdig(spiller.navn())
    q1 = Quest(desk1, ferdigDesk1, 1, 15, "Overtrollmann Vassle", sted="Fjellhytta")
    q1.legg_til_reward(xp=20000, gull=5000, hp=100, kp=70, ekstraKp=2, settTilgjengelig=True, settTilgjengeligIndeks=3)
    q1.legg_til_progresjonTekst("Ubalanse med fjellhytta gjennbalansert: ")
    q1.legg_til_svarTekst("Vil du undersøke ubalansen med fjellhytta?    (ja/nei)\n> ")
    qlog.legg_til_quest(q1)

    #cerberus
    desk2 = quests.vassle_cerberus(spiller.navn())
    ferdigDesk2 = quests.vassle_cerberus_ferdig(spiller.navn())
    q2 = Quest(desk2, ferdigDesk2, 1, 15, "Overtrollmann Vassle", sted="Vulkanen")
    q2.legg_til_reward(xp=20000, gull=5000, hp=100, kp=70, ekstraKp=2, settTilgjengelig=True, settTilgjengeligIndeks=3)
    q2.legg_til_progresjonTekst("Ubalanse med vulkanen gjennbalansert: ")
    q2.legg_til_svarTekst("Vil du undersøke ubalansen med vulkanen?    (ja/nei)\n> ")
    qlog.legg_til_quest(q2)

    #gargyl
    desk3 = quests.vassle_gargyl(spiller.navn())
    ferdigDesk3 = quests.vassle_gargyl_ferdig(spiller.navn())
    q3 = Quest(desk3, ferdigDesk3, 1, 15, "Overtrollmann Vassle", sted="Slottet")
    q3.legg_til_reward(xp=20000, gull=5000, hp=100, kp=70, ekstraKp=2, settTilgjengelig=True, settTilgjengeligIndeks=3)
    q3.legg_til_progresjonTekst("Ubalanse med slottet gjennbalansert: ")
    q3.legg_til_svarTekst("Vil du undersøke ubalansen med slottet?    (ja/nei)\n> ")
    qlog.legg_til_quest(q3)

    #shroom
    avslutningstekst = """
    Gratulerer! Du har spilt ferdig kapittel 1 av Pokus!
    Da er det bare å bite negler og håpe spent på at
    kapittel 2 ser dagens lys.\n"""
    desk4 = quests.vassle_shroom(spiller.navn())
    ferdigDesk4 = quests.vassle_shroom_ferdig(spiller.navn())
    q4 = Quest(desk4, ferdigDesk4, 1, 20, "Overtrollmann Vassle", sted="Ekspedisjonen", tilgjengelig=False)
    q4.legg_til_reward(xp=45000, gull=5000, hp=100, kp=70, ekstraKp=2)
    q4.legg_til_progresjonTekst("Ekspedisjon funnet: ")
    q4.legg_til_progresjon(1)
    q4.legg_til_progresjonTekstListe("Ubalanse i skogen gjennbalansert: ", 0)
    q4.legg_til_svarTekst("Vil du redde dagen, skogen og kanskje verden?    (ja/nei)\n> ")
    q4.legg_til_ekstra_tekst(avslutningstekst)
    qlog.legg_til_quest(q4)
