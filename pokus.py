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
#import troll
#import cerburus
import gargyl
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

#Troll (Kommer snart)

# Gargyl
butikk = Butikk("Skattekammeret")
gargyl.garg_butikk(butikk)
klasser.legg_til_butikk(butikk)

gargQlog = Questlog()
gargyl.garg_quest(gargQlog, spiller)
klasser.legg_til_questlog(gargQlog)

item = Item("Onepiece", "robe", d=1)
inv.legg_til_item(item, True)

#spiller.sett_sted_tilgjengelig(0)
spiller.sett_sted_tilgjengelig(1)
spiller.sett_sted_tilgjengelig(2)
spiller.sett_sted_tilgjengelig(3)
spiller.sett_sted_tilgjengelig(4)

heltFerdig = False
valg = "tutorial"

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
        pass

    #Del 1.3: Slottet med gargyler
    if valg == "gargyl":
        valg = gargyl.gargyl_loop(spiller, inv, klasser, spellbook)

    #Test-expansion
    if valg == "test":
        skrivRegnbue()
        valg = example_expansion.enhjorning_loop(spiller, inv, klasser, spellbook)
