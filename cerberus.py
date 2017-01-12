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
from troll import generer_troll
from gnom import generer_gnom

#Mainloop:
def cerberus_loop(spiller, inv, klasser, spellbook):
    qlog = klasser.questlog(3)

    ferdig = False
    if not qlog.hent_quest(0).startet():
        fiende = generer_hellhound(spiller, True)
        ferdig = not angrip(spiller, fiende, inv, klasser, spellbook, intro=True)

    while not ferdig:
        cerberus_kart(qlog)

        valg = False
        quest = False
        gaaTilButikk = False
        vulkan = False
        lagre = False
        hule = False
        klartenker = False
        south = False
        cerberus = False
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

            if inn == "l":
                lagre = True
                valg = True

            if inn == "i" and qlog.hent_quest(5).ferdig():
                klartenker = True
                valg = True

            if inn == "h" and qlog.hent_quest(2).startet():
                hule = True
                valg = True

            if inn == "s" and qlog.hent_quest(3).startet():
                hule = True
                valg = True
                south = True

            if inn == "c" and qlog.hent_quest(4).startet():
                cerberus = True
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

        while lagre:
            minnestein(spiller, inv, klasser)
            lagre = False

        while vulkan:
            fiende = generer_vulkan_fiende(spiller)
            vulkan = angrip(spiller, fiende, inv, klasser, spellbook)

        while hule:
            clear_screen()
            if south:
                print("\n    {} drar mot den sørlige krystallhulen.\n".format(spiller.navn()))
            else:
                print("\n    {} drar mot {}krystallhulen.\n".format(\
                spiller.navn(), "den nordlige " * int(qlog.hent_quest(3).startet())))
            pause()
            for x in range(randint(3, 6)):
                if not angrip(spiller, generer_vulkan_fiende(spiller), inv, klasser, spellbook):
                    hule = False
                    south = False
                    break
            if not hule: break
            clear_screen()
            print("\n    " + spiller.navn(), "har nådd frem til hulen!\n")
            if not qlog.hent_quest(3).startet():
                print("    Du ser deg rundt. Det er krystaller overalt i hulen, og det virker som om de ")
                print("    gjør helveteshundene sterkere! Du ser en gedigen krystall i enden av hulen, ")
                print("    kanskje Forsker Frederikk er interessert i den? Du begir deg mot den.\n")
            else:
                print("    Du begir deg innover mot senteret av hulen.\n")
            pause()
            for x in range(randint(4, 5)):
                if not angrip(spiller, generer_hellhound(spiller, sterk=True), inv, klasser, spellbook, hule=True):
                    hule = False
                    south = False
                    break
            if not hule: break
            clear_screen()
            if not qlog.hent_quest(2).sjekk_ferdig():
                print("\n    " + spiller.navn(), "har fått tak i den gedigne krystallen!")
                print("    Du drar tilbake til forsknigslaben.\n")
                qlog.hent_quest(2).progresser()
                pause()
                hule = False
                south = False
                break
            elif not qlog.hent_quest(3).progresjon() and qlog.hent_quest(3).startet() and not south or\
            not qlog.hent_quest(3).progresjon_liste()[0] and qlog.hent_quest(3).startet() and south:
                print("    Du er i posisjon til å utplassere duppedingsen!")
            if angrip(spiller, generer_beta(spiller, 1 + int(south)), inv, klasser, spellbook, hule=True) \
            and (qlog.hent_quest(3).startet() and not qlog.hent_quest(3).progresjon() and not south or \
            not qlog.hent_quest(3).progresjon_liste()[0] and qlog.hent_quest(3).startet() and south):
                if south:
                    qlog.hent_quest(3).progresser_liste(0)
                    south = False
                else:
                    qlog.hent_quest(3).progresser()
                print("    minoritetsladningsbærer-hvadetnåvarigjen er suksessfullt plassert!\n")
                print("    Du drar tilbake til forskningslaben.\n")
                pause()
            hule = False
            south = False

        while cerberus:
            print(spiller.navn(), "drar innover mot kjernen til vulkanen.\n")
            pause()
            for x in range(2):
                fiende = generer_hellhound(spiller)
                if not angrip(spiller, fiende, inv, klasser, spellbook):
                    cerberus = False
                    break
                print(spiller.navn(), "går dypere inn mot vulkanens kjerne.\n")
                pause()
            if not cerberus: break
            cerberusDialog(spiller)
            fiende = generer_cerberus(spiller)
            if angrip(spiller, fiende, inv, klasser, spellbook):
                qlog.hent_quest(4).progresser()
            cerberus = False

        while klartenker:
            medlem = spiller.spesialisering() == "Klartenker"
            print(" "*4 + "Velkommen {}til de Klartenkendes Forening!".format("tilbake " * int(medlem)).center(65 + 20*int(not medlem), "-"))
            if medlem:
                print("\n    Som medlem tilbyr vi deg internpriser på konsentrasjonspulver!")
                print("\n    Konsentrasjonspulver   +700kp                  2500g (k)")
                print("    Meld deg ut            Fjerner spesialisering   500g (u)")
                print("\nDu har", inv.penger(), "gullstykker. Skriv 'f' eller 'ferdig' for å dra tilbake.")
                inn = input("Hva vil du gjøre?\n> ").lower().strip()
                if inn in {"f", "ferdig"}:
                    klartenker = False
                elif inn == "k":
                    if inv.penger() >= 2500:
                        inv.legg_til_item(Item("Konsentrasjonspulver", "restoring", kp=700))
                        inv.penger(-2500)
                        print("Du kjøpte en stripe konsentrasjonspulver for 2500 gullstykker.")
                    else:
                        print("Du har ikke råd!")
                    pause()
                elif inn == "u":
                    print("De Klartenkendes Forening krever 500 i gebyr for papirarbeid.")
                    inn = input("Er du sikker på at du vil melde deg ut? \nDu må betale ny medlemsavgift om du vil melde deg inn igjen.   (ja/nei)\n> ").lower().strip()
                    if inn in {"j", "ja", "sure"}:
                        if inv.penger() >= 500:
                            inv.penger(-500)
                            spiller.spesialisering(False)
                            spiller.hev_kp(-250)
                            print("Du har meldt deg ut av Foreningen for Klartenkere.")
                            klartenker = False
                            inv.fjern_spesialiserte_items("Klartenker")
                            pause()
                        else:
                            print("Du har ikke råd!")
                            pause()
            else:
                print("\n    Dersom du er fremtidsrettet nok til å bli medlem av foreningen vår, vil du ha tilgang ")
                print("    til en eksklusiv trylleformel som regenererer ekstra konsentrasjonspoeng over tid! Og ")
                print("    om dette i seg selv ikke har overbevist deg om at klartenkere helt klart triumferer")
                print("    alle andre spesialiseringer, vil du og få en permanent bonus på 250 konsentrasjonspoeng,")
                print("    samt tilgang til prima-kvalitets pulver som får konsentrasjonen din rett opp igjen,")
                print("    selvfølgelig til en ekstra god pris! I tillegg til dette vil du og ha mulighet til å")
                print("    bruke ting du finner på din ferd som kun en klartenker vil vite hvordan skal brukes!")
                print("    Det eneste du trenger å gjøre, er å betale en minimal medlemsavgift på 8000 gullstykker, ")
                print("    et skikkelig kupp!")
                print("\nDu har", inv.penger(), "gullstykker.")
                inn = input("Vil du bli en klartenker?\n> ").lower().strip()
                if inn in {"ja", "j", "yes", "ja!", "hell yes!"}:
                    if inv.penger() >= 8000 and not spiller.spesialisering():
                        inv.penger(-8000)
                        spiller.spesialisering("Klartenker")
                        spiller.hev_kp(250)
                        print("\nGratulerer! Du er nå offisielt en Klartenker!\n")
                        pause()
                    elif inv.penger() >= 8000:
                        print("\n    Du har allerede en spesialisering! Men frykt ikke, ønsker du likevel å bli ")
                        print("    en klartenker, kan du melde deg ut av den foreningen du for øyeblikket er ")
                        print("    medlem i og komme tilbake senere!\n")
                        klartenker = False
                        pause()
                    else:
                        print("Du har ikke nok gullstykker til å betale medlemsavgiften!")
                        klartenker = False
                        pause()
                else:
                    klartenker = False

    if ferdig:
        return verdenskart(spiller)

def angrip(spiller, fiende, inv, klasser, spellbook, intro=False, hule=False):
    qlog = klasser.questlog(3)
    skriv_ut(spiller, fiende)
    hoder = 1 + 2 * int(fiende.navn() == "Cerberus")
    while True:
        inn = input("\nHva vil du gjøre?\n> ").lower()
        skadeTatt = spiller.hp()

        #tur angir at det er brukeren sin tur til å handle.
        tur = kommandoer(inn, spiller, fiende, inv, klasser, spellbook)

        if inn == "f" or inn == "flykt":
            print(spiller.navn(), "drar tilbake til forskningslaben.")
            return False

        #Her sjekkes om fienden er død. Om så, får karakteren loot og xp.
        if fiende.dead():
            print("--------------------------------------------------------------------"+\
            "\nDu vant!", fiende.navn() + fiende.ending(), "er overvunnet!",spiller.navn(),"får",fiende.xp(),"erfaringspoeng.")
            spiller.kons()
            spiller.gi_xp(fiende.xp())
            fiende.loot(spiller, inv)
            spellbook.reset()

            #progresserer quests
            if qlog.hent_quest(1).startet() and not qlog.hent_quest(1).sjekk_ferdig() \
            and not randint(0, 3) and fiende.navn() == "Helveteshund":
                print("Denne hunden er merket med Obsidian-logo! Du drar den med deg tilbake til forskningslaben.")
                pause()
                qlog.hent_quest(1).progresser()
                return False

            input("Trykk enter for å fortsette\n> ")
            return True

        elif not tur:
            if hule:
                print(spiller.navn(), "mistet", spiller.mist_kp(randint(15, 30)), "kp fra krystallene.")

            if hoder == 3 and fiende.hp() / fiende.xHp() <= 2/3 and randint(1, 10) >= 4 \
            or hoder == 2 and fiende.hp() / fiende.xHp() <= 1/3 and randint(1, 10) >= 4:
                print(fiende.navn(), "mistet et hode!")
                hoder -= 1

            for x in range(hoder):
                if fiende.oppholdt():
                    print(fiende.navn() + fiende.ending(), "er oppholdt.")
                elif fiende.kp() >= 90 and (not randint(0, 5) or intro) and not fiende.burning() and fiende.race() == "cerberus":
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

                #progresserer Smertedreper-quest.
                if klasser.questlog(4).hent_quest(6).startet():
                    klasser.questlog(4).hent_quest(6).progresser(spiller.hp() - skadeTatt)

                #gir beskjed om karakteren døde
                if spiller.dead():
                    input("\nDu døde! Trykk enter for å fortsette\n> ")
                    spellbook.reset()
                    write_player_died(spiller, "forskningslaben")
                    player_died(spiller, inv, klasser)
                    return False

            #skriver ut hp og kp til karakteren og hp til fienden til neste runde.
            spiller.kons()
            fiende.gen_kons()
            skriv_ut(spiller, fiende)
            if fiende.burning():
                print(fiende.navn() + fiende.ending(), "brenner!")

def generer_vulkan_fiende(spiller):
    tall = randint(1, 10)
    if tall == 1:
        fiende = generer_gnom(spiller, 0, False)
    elif tall <= 5:
        fiende = generer_troll(spiller)
    else:
        fiende = generer_hellhound(spiller)
    return fiende

def generer_hellhound(spiller, sterk=False):
    loot = Loot()
    fiende = Fiende(navn="Helveteshund", race="cerberus", loot=loot, \
    hp=120 + 40 * randint(1, spiller.lvl()) + 400 * int(sterk), \
    a=20 + randint(0, 10 * spiller.lvl()), \
    d=30 + randint(0, 10 * spiller.lvl()) + 120 * int(sterk), \
    kp=50 + randint(0, 3 * spiller.lvl()) + 50 * int(sterk), bonusKp=2, ending="en")
    dynamiskLoot(loot, fiende, spiller)
    skrivHellhound()
    print("\n" + spiller.navn(), "har møtt på en helveteshund!")
    return fiende

def generer_beta(spiller, nr):
    loot = Loot()
    navn = ["Churchill", "Roosevelt"]
    fiende = Fiende(navn[nr - 1], "cerberus", loot, \
    hp=2600 + randint(0, 2) * 100, \
    d=170 + randint(0, 3) * 10, \
    a=180 + randint(0, 3) * 10, \
    kp=190 + randint(0, 3) * 10, bonusKp=5 + randint(0, 1))
    loot.legg_til_item(randint(500, 700), 25)
    skrivHellhound(nr)
    print(spiller.navn(), "har møtt", navn[nr - 1] + "!")
    return fiende

def generer_cerberus(spiller):
    loot = Loot()
    fiende = Fiende("Cerberus", "cerberus", loot, hp=7500, a=150, d=150, kp=350, bonusKp=7)
    dynamiskLoot(loot, fiende, spiller)
    skrivCerberus()
    print("\n" + spiller.navn(), "har møtt på Cerberus!")
    return fiende

def cerberusDialog(spiller):
    return ""

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

    xKp = randint(0, 2 * spiller.lvl())
    d = randint(0, 3 * spiller.lvl())
    item = Item("Flammende hansker", "gloves", xKp=xKp, d=d)
    item.sett_loot_tekst("et par flammende hansker")
    loot.legg_til_item(item, 5)

    hp = randint(0, 4) * 5
    kp = randint(1, 5) * 5
    ekp = int(randint(0, 10 + spiller.lvl()) / 10)
    item = Item("Brennende øyne", "trinket", xHp=hp, xKp=kp, ekstraKp=ekp)
    item.sett_loot_tekst("et par brennende øyne")
    loot.legg_til_item(item, 4)

def bossLoot(loot):
    loot.legg_til_item(500, 50)

def cerberus_kart(qlog):
    skrivVulkan()
    print("""
    Velkommen til forskningslaben Obsidian! Her er stedene du kan dra:
    Vulkanen (v)               Dra til vulkanen og sloss mot helvetes søte biskevisker
    Butikken (k)               Kjøp det du trenger hos "Smolderbrødrenes Smie"
    Forskningslaben (q)        Se om ved forskningslaben utenfor trenger din hjelp""")
    if qlog.hent_qLog()[2].startet() and not qlog.hent_qLog()[2].ferdig():
        print("    Krystallhulen (h)          Dra til krystallhulen og undersøk")
    if qlog.hent_qLog()[3].startet():
        print("    Nord-krystallhulen (h)     Dra til den nordlige krystallhulen")
    if qlog.hent_qLog()[3].startet():
        print("    Sør-krystallhulen (s)      Dra til den sørlige krystallhulen")
    if qlog.hent_qLog()[4].startet():
        print("    Kjernen til vulkanen (c)   Ferd inn mot kjernen av vulkanen og konfronter Cerberus")
    if qlog.hent_qLog()[5].ferdig():
        print("    Ned kjelleren (n)          Besøk hovedkontoret til de Klartenkendes Forening")
    print("    Minnesteinen (l)           Lagre sjelen din i Obsidians lokale minnestein")
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

    #q1
    desk = cerberus_q1(navn)
    ferdigDesk = cerberus_q1_ferdig(navn)
    q = Quest(desk, ferdigDesk, 5, 15, "Forsker Frederikk")
    q.legg_til_reward(xp=3500, gull=200, settTilgjengelig=True, settTilgjengeligIndeks=1)
    q.legg_til_progresjonTekst("Fiender nedkjølt: ")
    q.legg_til_svarTekst("\nEr du klar for å prøve ut formelen?    (ja/nei)\n> ")
    q.legg_til_ekstra_tekst(navn + " lærte seg Nedkjøl (n) med 100% treffsikkerhet!")
    qlog.legg_til_quest(q)

    #q2
    desk = cerberus_q2(navn)
    ferdigDesk = cerberus_q2_ferdig(navn)
    q = Quest(desk, ferdigDesk, 3, 15, "Forsker Frederikk", tilgjengelig=False)
    q.legg_til_reward(xp=3000, gull=400, settTilgjengelig=True, settTilgjengeligIndeks=2)
    q.legg_til_progresjonTekst("Hunder slept tilbake: ")
    q.legg_til_svarTekst("\nVil du hjelpe oss hente tilbake hundene?    (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #q3
    desk = cerberus_q3(navn)
    ferdigDesk = cerberus_q3_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 15, "Forsker Frederikk", tilgjengelig=False)
    q.legg_til_reward(xp=4000, settTilgjengelig=True, settTilgjengeligIndeks=3)
    q.legg_til_progresjonTekst("Hule utforsket: ")
    q.legg_til_svarTekst("\nVil du dra til krystallhulen og utforske?    (ja/nei)\n> ")
    qlog.legg_til_quest(q)


    #q4
    desk = cerberus_q4(navn)
    ferdigDesk = cerberus_q4_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 15, "Forsker Frederikk", tilgjengelig=False)
    q.legg_til_reward(xp=7000, gull=800, settTilgjengelig=True, settTilgjengeligIndeks=4)
    q.legg_til_progresjonTekst("Duppeditt i den nordlige krystallhulen plassert: ")
    q.legg_til_svarTekst("\nKan du plassere duppedingsene?    (ja/nei)\n> ")
    q.legg_til_progresjon(1)
    q.legg_til_progresjonTekstListe("Duppeditt i den sørlige krystallhulen plassert: ", 0)
    qlog.legg_til_quest(q)

    #q5
    desk = cerberus_q5(navn)
    ferdigDesk = cerberus_q5_ferdig(navn)
    q = Quest(desk, ferdigDesk, 1, 15, "Forsker Frederikk", tilgjengelig=False)
    q.legg_til_reward(xp=10000, gull=1000)
    q.legg_til_progresjonTekst("Cerberus bekjempet: ")
    q.legg_til_svarTekst("\nEr du magikeren til å bringe ned den mektige Cerberus?    (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #klartenker-quest
    desk = klartenker_intro(navn)
    ferdigDesk = klartenker_intro_ferdig(navn)
    q = Quest(desk, ferdigDesk, 12500, 20, "Klara Klartenker")
    q.legg_til_reward(xp=10000, gull=5000, kp=50)
    q.legg_til_progresjonTekst("Konsentrajsonspoeng brukt: ")
    q.legg_til_svarTekst("\nØnsker du å søke om å spesialisere deg som Klartenker?    (ja/nei)\n> ")
    qlog.legg_til_quest(q)

    #bq1
    desk = "yo"
    ferdigDesk = "sweet"
    q = Quest(desk, ferdigDesk, 3, 15, "Forsker Frederikk")
    q.legg_til_reward(xp=5000, gull=700)
    q.legg_til_progresjonTekst("Fiender bekjempet: ")
    q.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q)
