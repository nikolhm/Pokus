"""
                *~ Pokus expansion 1.2 ~*
                           av
                    Gaute og Nikolas
"""
#Start med å importere alle de nødvendige delfilene.
from klasser import *
from grafikk import *
from quests import *
from prosedyrer import *

#Mainloop:
def cerberus_loop(spiller, inv, klasser, spellbook):
    qlog = klasser.questlog(2)

    ferdig = False
    while not ferdig:
        enhjorning_kart(qlog)

        valg = False
        quest = False
        gaaTilButikk = False
        vulkan = False
        questInstans1 = False
        questInstans2 = False
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

            if inn == "v":
                vulkan = True
                valg = True

            if inn == "1" and qlog.hent_quest(1).startet() and not qlog.hent_quest(1).ferdig():
                questInstans1 = True
                valg = True

            if inn == "2" and qlog.hent_quest(2).startet():
                questInstans2 = True
                valg = True

        while quest:
            #Merk at oppdrag_tilgjengelige() er en funksjon med returverdi.
            inn = qlog.oppdrag_tilgjengelige(spiller.lvl(), "utenfor stallen").lower()
            if inn != "f" and inn != "ferdig":
                try:
                    qlog.snakk(int(inn) - 1, spiller, inv)
                except ValueError:
                    print("\nDu må skrive et tall!\n")
            else:
                quest = False

        while gaaTilButikk:
            klasser.butikk(2).interaksjon(inv)
            gaaTilButikk = False

        while vulkan:
            if randint(1, 2) == 1:
                fiende = generer_enhjorning(spiller)
            else:
                fiende = generer_fisk(spiller)

            skriv_ut(spiller, fiende)
            vulkan = angrip(spiller, fiende, inv, klasser, spellbook)

            if vulkan and qlog.hent_quest(0).startet():
                qlog.hent_quest(0).progresser()

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
            if fiende.kp() >= 90 and not randint(0, 10) and not fiende.burning() and True: #fiende.race() == "cerberus":
                if randint(0, 1):
                    print(fiende.navn() + fiende.ending(), "satte fyr på seg selv!")
                    fiende.a(50)
                    fiende.d(70)
                    fiende.sett_burning()
                else:
                    print(fiende.navn() + fiende.ending(), "satte fyr på", spiller.navn() + "!")
                    print(spiller.navn(), "mistet", spiller.mist_liv(round(spiller.xHp() * 0.05)), "liv fra flammene.")
                    spiller.sett_burning(CD=3, dmg=round(spiller.xHp() * 0.05))
                fiende.kp(-90)

            elif fiende.kp() >= 50 and randint(0, 100) == 1:
                print(fiende.navn() + fiende.ending(), "kastet Restituer!")
                print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(randint(90, 110)), "hp!")
                fiende.kp(-50)
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
                if fiende.burning():
                    print(fiende.navn() + fiende.ending(), "brenner!")

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

def generer_fisk(spiller):
    loot = Loot()
    fiende = Fiende("Fisk", "fisk", loot, 700, 200, 150, weapon=50, ending="en")
    statiskLoot(loot)
    print("\n" + spiller.navn(), "har møtt på en kampklar fisk!")
    skrivFisk()
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

    item = Item("Fiskehode", "hat", xHp=70, d=60)
    item.sett_loot_tekst("et fiskehode")
    loot.legg_til_item(item, 25)

    item = Item("Fiskeskjell-kjole", "robe", xHp=20, d=100)
    loot.legg_til_item(item, 25)

def enhjorning_kart(qlog):
    skrivVulkan()
    print("""
    Velkommen til hulen! Her er stedene du kan dra:
    Vulkanen (v)               Dra til vulkanen og sloss mot helvetes søte biskevisker :)
    Butikken (k)               Kjøp det du trenger hos "Smolderbrødrenes Smie"
    Utenfor (q)                Se om noen utenfor trenger din hjelp""")
    """if qlog.hent_qLog()[1].startet() and not qlog.hent_qLog()[1].ferdig():
        print("    Quest-sted 1 (1)           Dra til quest-instans nummer 1!")
    if qlog.hent_qLog()[2].startet():
        print("    Quest-sted 2 (2)           Dra til quest-instans nummer 2!")"""
    print("    Ut i verden (f)            Viser deg kart over alle stedene du kan dra\n")

def cerberusButikk(butikk):
    butikk.legg_til_hadeTekst("\nLykke til bror!\n")

    item = Item("Tryllepulver", "damaging", dmg=100)
    vare = Vare(item, 50, "t")
    butikk.legg_til_vare(vare)

    item = Item("Trolldrikk", "restoring", hp=300)
    vare = Vare(item, 400, "d")
    butikk.legg_til_vare(vare)

    item = Item("Konsentrasjonspulver", "restoring", kp=250)
    vare = Vare(item, 1000, "k")
    butikk.legg_til_vare(vare)

    item = Item("Generisk stav", "weapon", a=100, xKp=55)
    vare = Vare(item, 2000, "w")
    butikk.legg_til_vare(vare)

    item = Item("Vulkansverd", "weapon", a=300, blade=True)
    vare = Vare(item, 1000, "v")
    butikk.legg_til_vare(vare)

    item = Item("Runkehansker", "gloves", xKp=80, xHp=80)
    vare = Vare(item, 4500, "h")
    butikk.legg_til_vare(vare)

def cerberusQuest(qlog, spiller):
    navn = spiller.navn()

    desk1 = ""
    ferdigDesk1 = ""
    q1 = Quest(desk1, ferdigDesk1, 5, 15, "Turi Testquest-holder")
    q1.legg_til_reward(xp=5000, gull=2000)
    q1.legg_til_progresjonTekst("Fiender bekjempet: ")
    q1.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q1)
