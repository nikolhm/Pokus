"""
                              POKUS
                           October 2016
                      Magic Wand Productions
"""
from klasser import *
from random import randint
from grafikk import *
import tutorial
import gnom
import troll
import cerberus
import gargyl
import shroom
import example_expansion

klasser = Klasser()
spiller = Spiller(input("Velg et navn til karakteren din:\n> "))
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
butikk = Butikk("Sleipe Max: Magi og Porno")
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


item = Item("Onepiece", "robe", d=1)
inv.legg_til_item(item, True)

#spiller.sett_sted_tilgjengelig(0)
spiller.sett_sted_tilgjengelig(1)
spiller.sett_sted_tilgjengelig(2)
spiller.sett_sted_tilgjengelig(3)
spiller.sett_sted_tilgjengelig(4)

heltFerdig = False
valg = "cerberus"

skrivTittel()
while not heltFerdig:

    #Tutorial
    if valg == "tutorial":
        valg = tutorial.mainloop(spiller, inv, klasser, spellbook)

    #Del 1: Magi-borgen og Gaute Gnom den Grusomme
    if valg == "gnom":
        skrivSlott()
        valg = gnom.gnomeloop(spiller, inv, klasser, spellbook)

    #Del 1.1: Trollfjellet
    if valg == "troll":
        valg = troll.troll_loop(spiller, inv, klasser, spellbook)

    #Del 1.2: Vulkanen
    if valg == "cerberus":
        valg = cerberus.cerberus_loop(spiller, inv, klasser, spellbook)

    #Del 1.3: Slottet med gargyler
    if valg == "gargyl":
        valg = gargyl.gargyl_loop(spiller, inv, klasser, spellbook)

    #Del 2: Den fortapte ekspedisjonen og shrooms
    if valg == "shroom":
        valg = shroom.shroom_loop(spiller, inv, klasser, spellbook)

    #Test-expansion
    if valg == "test":
        skrivRegnbue()
        valg = example_expansion.enhjorning_loop(spiller, inv, klasser, spellbook)
