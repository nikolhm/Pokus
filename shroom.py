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
                sti = True
                valg = True

        if sti:
            sti = False
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
                banditt_loop(spiller, inv, klasser, spellbook)
                return False
            else:
                print("\nDet er ikke en banditt-leir", spiller.navn(), "er på jakt etter.")
                print("Du bestemmer deg for å dra tilbake til leirbålet.")
        elif not h1 and h2 and not h3 and shroomQlog.hent_quest(0).startet():
            print("Blindvei! Du får en følelse av at rotters stedsans ikke er helt bra.")
            print("Kanksje du kan prøve det motsatte? Du drar tilbake til leirbålet.")
        else:
            print("Blindvei! På en eller annen måte finner du veien tilbake til leirbålet.")

def banditt_loop(spiller, inv, klasser, spellbook):
    pass

def angrip(spiller, fiende, inv, klasser, spellbook):
    skriv_ut(spiller, fiende)
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

def generer_enhjorning(spiller):
    loot = Loot()
    fiende = Fiende(navn="Enhjørning", race="enhjørning", loot=loot, \
    hp=20 + 20 * randint(1, spiller.lvl()), \
    a=20 + randint(0, 10 * spiller.lvl()), \
    d=30 + randint(0, 10 * spiller.lvl()), \
    kp=50 + randint(0, 3 * spiller.lvl()), bonusKp=2, ending="en")

    dynamiskLoot(loot, fiende, spiller)
    print("\n" + spiller.navn(), "har møtt på en enhjørning!")

    skrivEnhjorning()
    return fiende

def generer_banditt(spiller):
    loot = Loot()
    loot.legg_til_item(500, 50)
    fiende = Fiende("Banditt", "menneske", loot, hp=1400, a=250, d=170, ending="en")
    print("\n" + spiller.navn(), "har møtt på en banditt!")
    #skrivBanditt()
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

def skog_kart(qlog):
    print("""
    Velkommen til stallen! Her er stedene du kan dra:
    Regnbuen (r)               Dra til foten av regnbuen og bekjemp de korrupte enhjørningene
    Butikken (k)               Kjøp det du trenger hos "Over Regnbuen"-supertilbudsbutikk
    Utenfor (q)                Se om noen utenfor trenger din hjelp""")
    if qlog.hent_qLog()[1].startet() and not qlog.hent_qLog()[1].ferdig():
        print("    Quest-sted 1 (1)           Dra til quest-instans nummer 1!")
    if qlog.hent_qLog()[2].startet():
        print("    Quest-sted 2 (2)           Dra til quest-instans nummer 2!")
    print("    Ut i verden (f)            Viser deg kart over alle stedene du kan dra\n")

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

def skog_quest(qlog, spiller):
    navn = spiller.navn()

    #q1
    desk1 = shroom_q1(navn)
    ferdigDesk1 = shroom_q1_ferdig(navn)
    q1 = Quest(desk1, ferdigDesk1, 7, 15, "Zip")
    q1.legg_til_reward(xp=10000, gull=300, hp=30, kp=30)
    q1.legg_til_progresjonTekst("Banditt-leir funnet: ")
    q1.legg_til_svarTekst("\nVil du gå på bandittjakt?     (ja/nei)\n> ")
    qlog.legg_til_quest(q1)

def banditt_quest(qlog, spiller):
    navn = spiller.navn()
