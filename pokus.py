"""
                              POKUS
                           October 2016
                      Magic Wand Productions
"""
try:
    from colorama import *
except ImportError:
    from install import install
    install("colorama")
init()
from klasser import *
from random import randint
from grafikk import *
import tutorial, gnom, troll, cerberus, gargyl, shroom, example_expansion, os

skrivTittel()
input("Trykk enter for å fortsette\n> ")
print("\033[A                             \033[A")
print("\033[A                             \033[A")
lastTidligere = load_screen()
if lastTidligere:
    spiller = Spiller(last_navn(lastTidligere))
else:
    navn = ""
    while len(navn) == 0 or "," in navn:
        navn = input("Velg et navn til karakteren din:\n> ")
        if "," in navn:
            print("Du kan ikke ha komma i navnet ditt.\n")
    spiller = Spiller(navn)

klasser = Klasser()
inv = Inventory(spiller, klasser)
spellbook = Spellbook(klasser, spiller, inv)

# Tutorial
tutorialQlog = Questlog()
tutorial.tutorial_quest(tutorialQlog, spiller)
klasser.legg_til_questlog(tutorialQlog)

# Gnom
butikk = Butikk("Kåres hokus og andre hokuspokus")
gnom.kaaresButikk(butikk)
klasser.legg_til_butikk(butikk)

gnomeQlog = Questlog()
gnom.gnomequest(gnomeQlog, spiller)
klasser.legg_til_questlog(gnomeQlog)

#Troll
butikk = Butikk("Fe Fi Fo - Familiebutikk")
troll.trollButikk(butikk)
klasser.legg_til_butikk(butikk)

trollQlog = Questlog()
troll.trollQuest(trollQlog, spiller)
klasser.legg_til_questlog(trollQlog)

#Cerberus
butikk = Butikk("Smolderbrødrenes Smie")
cerberus.cerberusButikk(butikk)
klasser.legg_til_butikk(butikk)

cerberusQlog = Questlog()
cerberus.cerberusQuest(cerberusQlog, spiller)
klasser.legg_til_questlog(cerberusQlog)

# Gargyl
butikk = Butikk("Skattekammeret")
gargyl.garg_butikk(butikk)
klasser.legg_til_butikk(butikk)

gargQlog = Questlog()
gargyl.garg_quest(gargQlog, spiller)
klasser.legg_til_questlog(gargQlog)

#Overtrollmann Vassle
vassleQlog = Questlog()
gnom.vassle_quest(vassleQlog, spiller)
klasser.legg_til_questlog(vassleQlog)

#Shroom
butikk = Butikk("Skogens skatter")
shroom.shroom_butikk(butikk)
klasser.legg_til_butikk(butikk)

skogQlog = Questlog()
shroom.skog_quest(skogQlog, spiller)
klasser.legg_til_questlog(skogQlog)

butikk = Butikk("Svartemarkedet")
shroom.banditt_butikk(butikk)
klasser.legg_til_butikk(butikk)

bandittQlog = Questlog()
shroom.banditt_quest(bandittQlog, spiller)
klasser.legg_til_questlog(bandittQlog)

if lastTidligere:
    last_fil(spiller, inv, klasser, lastTidligere)
else:
    item = Item("Onepiece", "robe", d=1)
    inv.legg_til_item(item, True)

    #spiller.sett_sted_tilgjengelig(0)
    spiller.sett_sted_tilgjengelig(1)

while True:

    #Tutorial
    if spiller.hentSted() == "tutorial":
        spiller.byttSted(tutorial.mainloop(spiller, inv, klasser, spellbook))

    #Del 1: Magi-borgen og Gaute Gnom den Grusomme
    if spiller.hentSted() == "gnom":
        spiller.byttSted(gnom.gnomeloop(spiller, inv, klasser, spellbook))

    #Del 1.1: Trollfjellet
    if spiller.hentSted() == "troll":
        spiller.byttSted(troll.troll_loop(spiller, inv, klasser, spellbook))

    #Del 1.2: Vulkanen
    if spiller.hentSted() == "cerberus":
        spiller.byttSted(cerberus.cerberus_loop(spiller, inv, klasser, spellbook))

    #Del 1.3: Slottet med gargyler
    if spiller.hentSted() == "gargyl":
        spiller.byttSted(gargyl.gargyl_loop(spiller, inv, klasser, spellbook))

    #Del 2: Den fortapte ekspedisjonen og shrooms
    if spiller.hentSted() == "shroom":
        spiller.byttSted(shroom.shroom_loop(spiller, inv, klasser, spellbook))

    #Test-expansion
    if spiller.hentSted() == "test":
        skrivRegnbue()
        spiller.byttSted(example_expansion.enhjorning_loop(spiller, inv, klasser, spellbook))
