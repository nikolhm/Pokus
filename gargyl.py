"""
                *~ Pokus expansion 1.3 ~*
                           av
                   Gaute Svanes Lunde
"""
#Start med å importere alle de nødvendige delfilene.
from klasser import *
from grafikk import *
from quests import *
from prosedyrer import *

#Mainloop:
def gargyl_loop(spiller, inv, klasser, spellbook):
    butikk = Butikk("Skattekammeret")
    garg_butikk(butikk)
    klasser.legg_til_butikk(butikk)

    gargQlog = Questlog()
    garg_quest(gargQlog, spiller)
    klasser.legg_til_questlog(gargQlog)
    qlog = klasser.questlog(2)

    ferdig = False
    if not qlog.hent_quest(0).ferdig():
        ferdig = intro_loop(spiller, inv, klasser, spellbook)

    while not ferdig:
        garg_kart(qlog)

        valg = False
        quest = False
        gaaTilButikk = False
        fangekjeller = False
        utkikk = False
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
                ferdig = slottsgaard_loop(spiller, inv, klasser, spellbook)
                valg = True

            if inn == "a" and qlog.hent_quest(1).startet():
                fangekjeller = True
                valg = True

            if inn == "u" and qlog.hent_quest(2).startet():
                utkikk = True
                valg = True

        while quest:
            #Merk at oppdrag_tilgjengelige() er en funksjon med returverdi.
            inn = qlog.oppdrag_tilgjengelige(spiller.lvl(), "møtehallen").lower()
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

        fiender = 0
        while fangekjeller:

            if not angrip(spiller, generer_statue(spiller), inv, klasser, spellbook):
                fangekjeller = False
                break
            fiender += 1

            if fiender > randint(5, 8):
                print(spiller.navn(), "har nådd bunnen av fangekjelleren, og har funnet en mystisk kiste!")

                if not qlog.hent_quest(1).ferdig():
                    qlog.hent_quest(1).progresser()
                    print(spiller.navn(), "fant noen gamle, uforståelige skrifter i kisten.")

                    #bq1
                    if randint(0, 10) > 7 and qlog.hent_quest(6).progresjon() == 0:
                        qlog.hent_quest(6).progresser()
                        print(spiller.navn(), "fant en levende kosebamse i kisten! Hvem kan det være sin?")

                    input("Trykk enter for å dra tilbake\n> ")
                    fangekjeller = False
                else:
                    loot = Loot()
                    ormLoot(loot)
                    fiende = Fiende("Orm", "dyr", loot, 2300, 150, 130, ending="en")
                    print("\nEn svær orm gjemte seg i kisten!\n" + spiller.navn(), "har møtt en orm!")
                    if angrip(spiller, fiende, inv, klasser, spellbook):
                        print("\n" + spiller.navn(), "fant 350 gullstykker, en stripe konsentrasjonspulver og en trolldrikk i kisten.")
                        item = Item("Trolldrikk", "restoring", hp=300)
                        inv.legg_til_item(item)
                        item = Item("Konsentrasjonspulver", "restoring", kp=200)
                        inv.legg_til_item(item)
                        inv.penger(350)

                        #bq1
                        if randint(0, 10) > 6 and qlog.hent_quest(6).progresjon() == 0:
                            qlog.hent_quest(6).progresser()
                            print(spiller.navn(), "fant en levende kosebamse i kisten! Hvem kan det være sin?")

                        input("Trykk enter for å dra tilbake\n> ")
                    fangekjeller = False
            else:
                print("\n" + spiller.navn(), "går dypere ned i fangekjelleren.")
                input("Trykk enter for å fortsette\n> ")

        while utkikk:
            if not qlog.hent_quest(2).ferdig():
                qlog.hent_quest(2).progresser()
                angrip(spiller, generer_gargyl(spiller), inv, klasser, spellbook)
                utkikk = False
            else:
                tall = randint(1, 10)
                if tall <= 7:
                    fiende = generer_gargyl(spiller)
                else:
                    fiende = generer_statue(spiller)
                if not angrip(spiller, fiende, inv, klasser, spellbook):
                    utikk = False
                    break
                if fiende.race() == "gargyl":
                    qlog.hent_quest(5).progresser()
                if qlog.hent_quest(5).progresjon() == 7 and not qlog.hent_quest(5).ferdig():
                    print("\n\n    * " + spiller.navn(), "har møtt Guri Gargyl! *\n\n")
                    input("Trykk enter for å fortsette\n> ")
                    loot = Loot()
                    guriLoot(loot)
                    fiende = Fiende("Guri Gargyl", "gargyl", loot, 7000, 400, 250, kp=300, bonusKp=7, weapon=70)
                    if angrip(spiller, fiende, inv, klasser, spellbook):
                        qlog.hent_quest(5).progresser_liste(0)
                        utkikk = False

    if ferdig:
        return verdenskart(spiller)

def intro_loop(spiller, inv, klasser, spellbook):

    print("\n    "+spiller.navn(), """kommer til et mørkt og dystert slott! Store steiner
    ligger strødt rundt omkring. Den nærmeste begynner å bevege på seg, og sakte
    flyr rundt i sirkel, før den suser rett mot""", spiller.navn()+"!\n")

    print(spiller.navn(), "har møtt en stein!")
    fiende = Fiende("Stein", "objekt", Loot(), hp=300, a=130, d=100, weapon=60)
    fiende.return_loot().legg_til_item(50, 100)

    angrip(spiller, fiende, inv, klasser, spellbook)

    return slottsgaard_loop(spiller, inv, klasser, spellbook)

def slottsgaard_loop(spiller, inv, klasser, spellbook):
    qlog = klasser.questlog(2)
    while True:
        intro_kart(qlog)
        inn = input("\nHvor vil du dra?\n> ").lower()

        if inn == "q" and not qlog.hent_quest(0).ferdig():
            qlog.snakk(0, spiller, inv)

        if inn == "q" and qlog.hent_quest(3).startet() and not qlog.hent_quest(4).ferdig():
            qlog.hent_quest(4).sett_tilgjengelig()
            qlog.snakk(4, spiller, inv)
            qlog.hent_quest(4).sett_tilgjengelig(False)
            qlog.hent_quest(3).progresser()
            if qlog.hent_quest(4).ferdig():
                qlog.hent_quest(3).progresser_liste(0)

        if inn == "s":
            while True:
                fiende = Fiende("Stein", "objekt", Loot(), hp=300, a=130, d=100, weapon=60)
                fiende.return_loot().legg_til_item(70, 100)
                print(spiller.navn(), "har møtt en stein!")
<<<<<<< HEAD
=======
                skriv_ut(spiller, fiende)
                skrivStein()
>>>>>>> f1df6d980743099acee79c49f869d11e88410b96

                if not angrip(spiller, fiende, inv, klasser, spellbook):
                    break
                if qlog.hent_quest(0).startet():
                    qlog.hent_quest(0).progresser()
                if qlog.hent_quest(4).startet():
                    qlog.hent_quest(4).progresser()

        if inn == "f":
            return True

        if inn == "t" and qlog.hent_quest(0).ferdig():
            return False

def angrip(spiller, fiende, inv, klasser, spellbook):
    qlog = klasser.questlog(2)
    skriv_ut(spiller, fiende)
    forsteinet = False
    runder = 0
    tur = True
    while True:
        inn = input("\nHva vil du gjøre?\n> ").lower()

        if inn == "f" or inn == "flykt":
            print(spiller.navn(), "drar tilbake til slottsgården.")
            return False

        if forsteinet:
            print("\n" + fiende.navn() + fiende.ending(), "er blitt til stein!")
            if (inn == "kj" or inn == "kjøttifiser") and spiller.kons_igjen() >= 100 and qlog.hent_quest(3).ferdig():
                runder = -4
                forsteinet = False
                tur = False
                spiller.bruk_kons(100)
                print(spiller.navn(), "kastet kjøttifiser!", fiende.navn() + fiende.ending(), "kan nå angripes igjen.")
            else:
                print("Alle angrep er nyttesløse!")
                tur = False
        else:
            tur = kommandoer(inn, spiller, fiende, inv, klasser, spellbook)
            if inn == "kj" or inn == "kjøttifiser" and qlog.hent_quest(3).ferdig():
                print(fiende.navn() + fiende.ending(), "er ikke lenger stein!")

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
            if fiende.race() == "gargyl" and fiende.kp() >= 100 and randint(0, 1) == 1 and runder >= 0:
                print(fiende.navn() + fiende.ending(), "kastet RockNoRoll!")
                print(fiende.navn() + fiende.ending(), "er blitt til stein!")
                fiende.bruk_kons(100)
                forsteinet = True
                runder = 10
            elif fiende.race() != "gargyl" and fiende.kp() >= 50 and randint(0, 2) == 1 \
            and fiende.xHp() - fiende.hp() > 80:
                print(fiende.navn() + fiende.ending(), "kastet restituer!")
                print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(100), "hp!")
                fiende.bruk_kons(50)
            elif fiende.race() == "gargyl" and fiende.kp() >= 40 and randint(0, 10) == 1 \
            and fiende.xHp() - fiende.hp() > 100:
                print(fiende.navn() + fiende.ending(), "kastet restituer!")
                print(fiende.navn() + fiende.ending(), "restorerte", fiende.restorer(100), "hp!")
                fiende.bruk_kons(40)
            else:
                spiller.angrepet(fiende)

            #gir beskjed om karakteren døde
            if spiller.dead():
                write_player_died(spiller, "slottet")
                player_died(spiller, inv, klasser)
                return False

            #skriver ut hp og kp til karakteren og hp til fienden til neste runde.
            else:
                if runder > 0:
                    runder -= 1
                if runder < 0:
                    runder += 1
                if runder == 0:
                    forsteinet = False
                spiller.kons()
                fiende.gen_kons()
                skriv_ut(spiller, fiende)

def generer_statue(spiller):
    loot = Loot()
    fiende = Fiende(navn="Statue", race="objekt", loot=loot, \
    hp=60 + 20 * randint(1, spiller.lvl()), \
    a=20 + randint(0, 10 * spiller.lvl()), \
    d=30 + randint(0, 10 * spiller.lvl()), \
    kp=50 + randint(0, 3 * spiller.lvl()), bonusKp=2, ending="en")
    dynamiskLoot(loot, fiende, spiller)
    print("\n" + spiller.navn(), "har møtt på en levende statue!")
    return fiende

def generer_gargyl(spiller):
    loot = Loot()
    hp = 1000 + randint(0, spiller.lvl()) * 25
    a = 180 + randint(spiller.lvl() - 10, spiller.lvl() + 10)
    d = 120 + 2 * spiller.lvl()
    kp = 130 + 5 * round(spiller.lvl() / 4) + randint(-10, 10)
    bkp = randint(4, 6)
    w = randint(65, 75)
    fiende = Fiende("Gargyl", "gargyl", loot, hp, a, d, kp=kp, bonusKp=bkp, weapon=w, ending="en")
    gargylLoot(loot, fiende, spiller)
    skrivGargouille()
    print("\n" + spiller.navn(), "har møtt på en gargyl!")
    return fiende

def dynamiskLoot(loot, fiende, spiller):
    tall = round(10 + fiende.xp() / 10)
    loot.legg_til_item(tall, 60)

    kpkp = int(randint(1, spiller.lvl()) /10) *25 + 100
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 10)

    tdhp = randint(1, spiller.lvl()) * 5 + 175
    item = Item("Trolldrikk", "restoring", hp=tdhp)
    loot.legg_til_item(item, 15)

    a = randint(0, 4 * spiller.lvl())
    xKp = randint(0, 3 * spiller.lvl())
    item = Item("Stiv stav", "weapon", a=a, xKp=xKp)
    loot.legg_til_item(item, 5)

    a = randint(40, 40 + 5 * spiller.lvl())
    item = Item("Sverd'I'stein", "weapon", a=a, blade=True)
    item.sett_loot_tekst("et sverd")
    loot.legg_til_item(item, 6)

    xHp = randint(0, 2 * spiller.lvl())
    d = int(randint(0, 4 * spiller.lvl()) /10) *10
    item = Item("Rusten rustning", "robe", xHp=xHp, d=d)
    loot.legg_til_item(item, 4)

def ormLoot(loot):
    item = Item("Ormeskinn:Pannebånd", "hat", xHp=70, d=60)
    loot.legg_til_item(item, 20)

    item = Item("Ormeskinn:Sko", "shoes", xHp=20, xKp=30, a=10)
    loot.legg_til_item(item, 20)

    item = Item("Ormeskinn:Truse", "robe", xKp=100)
    loot.legg_til_item(item, 20)

    item = Item("Ormeskinn:Hansker", "gloves", a=10, xHp=10, xKp=10)
    loot.legg_til_item(item, 20)

    item = Item("Ormetann", "weapon", a=135, xHp=15, blade=True)
    loot.legg_til_item(item, 20)

def gargylLoot(loot, fiende, spiller):
    tall = round(30 + fiende.xp() / 10)
    loot.legg_til_item(tall, 60)

    kpkp = int(randint(1, spiller.lvl()) /10) *25 + 100
    item = Item("Konsentrasjonspulver", "restoring", kp=kpkp)
    item.sett_loot_tekst("en stripe konsentrasjonspulver")
    loot.legg_til_item(item, 10)

    tdhp = randint(1, spiller.lvl()) * 5 + 175
    item = Item("Trolldrikk", "restoring", hp=tdhp)
    loot.legg_til_item(item, 15)

    hp = randint(0, 4) * 10
    kp = randint(1, 5) * 10
    ekp = randint(1, 4)
    item = Item("Stein", "trinket", xHp=hp, kp=kp, ekstraKp=ekp)
    loot.legg_til_item(item, 5)

def guriLoot(loot):
    loot.legg_til_item(2000, 25)

    item = Item("Steinsko", "shoes", xHp=-30, d=100, lvl=18)
    item.sett_loot_tekst("et par sko av stein")
    loot.legg_til_item(item, 25)

    item = Item("Stein-hatt", "hat", xHp=-30, d=125, lvl=18)
    loot.legg_til_item(item, 25)

    item = Item("Krystallkule", "trinket", xHp=125, lvl=18)
    loot.legg_til_item(item, 25)

def garg_kart(qlog):
    print("""
    Velkommen til slottet! Her er stedene du kan dra:
    Slottsgården (s)           Dra til slottsgården
    Butikken (k)               Se hva Tina har tilgjengelig i 'Skattekammeret'
    Møtehallen (q)             Diskuter angrepsstrategi i møtehallen""")
    if qlog.hent_qLog()[1].startet():
        print("    Fangekjelleren (a)         Dra til fangekjelleren og finn skjulte skatter!")
    if qlog.hent_qLog()[2].startet():
        print("    Utkikkstårnet (u)          Bekjemp gargyler i de øvre delene av slottet!")
    print("    Ut i verden (f)            Viser deg kart over alle stedene du kan dra\n")

def intro_kart(qlog):
    print("""
    Du står i slottsgården! Her er stedene du kan dra:
    Slottsporten (s)           Rydd bort steiner foran slottsporten""")
    if not qlog.hent_quest(0).ferdig():
        print("    Fontenen (q)               Snakk med Zap")
    if qlog.hent_quest(3).startet() and not qlog.hent_quest(4).ferdig():
        print("    Fontenen (q)               Snakk med Kent Kokk")
    if qlog.hent_quest(0).ferdig():
        print("    Slottet (t)                Dra til slottet")
    print("    Verdenskart (f)            Se på verdenskartet")

def garg_butikk(butikk):
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

def garg_q1(navn):
    return "    " + navn + """!
    Du kommer i grevens tid! Overtrollmann Vassle sendte meg for å undersøke de
    underlige magiske aktivitetene som omringet slottet her, og jeg forventet
    å finne et par forskrudde magikere forsøke å tilfredstille sine forskrudde
    fantasier ved å påkalle en hornet demon eller noe slikt. Det vanlige altså.
    Men med en gang jeg kom i nærheten av slottet her, ble jeg bombandert av
    sinte steiner. Ja, steiner! Som var sinte! Hvordan er dette mulig? Det
    er noe galt her som ikke er rett """ + navn + """! For å komme til bunns i dette, må
    vi komme oss inn på slottet. Klar en vei for steiner, så vi har fri passasje!

    -- Klar en fri vei til slottet ved å "rydde" bort steiner. 7 burde holde."""
def garg_q1_ferdig(navn):
    return "    Fort! Vi må kjappe oss inn! Håper beboerne her er like hele!\n"

def garg_q2(navn):
    return "    Hei " + navn + """!
    Noen her har skremt beboerne fra vettet, de tørr ikke bevege seg ut av
    møtehallen her. Det påstås at det finnes skapninger på slottet her som
    kan manipulere og skape liv til steiner og metall, og til og med gjøre
    seg selv om til ugjennomtrengbar stein! Hvis det er disse skapningene
    som har skapt ubalansen Overtrollmann Vassle snakket om, må dette
    undersøkes! Såvidt jeg har forstått fra beboerne her, finnes det en
    slu orm i fangekjelleren som av sikkerhetsgrunner loggfører all aktivitet
    på slottet. Naturligvis. Alle slott har jo en loggfører. Finn loggene til
    ormen i fangekjelleren!

    -- Finn loggene til ormen i fangekjelleren."""
def garg_q2_ferdig(navn):
    return "    Strålende " + navn + """!
    Dette skal ta meg rundt 3 sekunder å oversette! Snakk med meg om litt,
    så skal jeg ha en plan for hvordan vi skal gå videre. Forresten, om du
    skulle være på jakt etter skatter, tror jeg at hvis du drar ned til
    fangekjelleren igjen kan du sikkert finne noe av verdi. Jeg kan ikke
    garantere at loggfører-ormen er villig til å la deg stikke av med det
    da... Meeen så har jeg også hørt at ormeskinn gir usedvanlig bra
    defensivbonus.\n"""

def garg_q3(navn):
    return "    OK " + navn + """!
    Jeg har nå oversatt loggen fra skriftlig ormtunge. Det viser seg at
    rett før den magiske ubalansen her oppsto, kom det en kraftig magiker
    på besøk. Etter besøket, begynte steiner og statuer å komme til live
    i og rundt slottet. Det ser  ut til at ubalansen har sitt episenter i
    utkikkstårnet her på slottet. Kan du dra opp og utforske? Og husk, om
    du møter noe uvanlig, løp vekk og rapporter til meg!

    -- Utforsk utkikkstårnet."""
def garg_q3_ferdig(navn):
    return "    Gargyler? Som blir til stein? Her må noe gjøres " + navn + "!\n"

def garg_q4(navn):
    return "    " + navn + """!
    Du må finne en måte å avvergen gargylenes RockNoRoll-magi. Snakk
    med Kent Kokk, han pleier å kunne koke opp ganske gode steinsupper
    til kvelds, når det ikke er annet å spise i nærheten. Altså, ikke at
    man koker suppe på steinene, men spiser steinene. Ganske godt med
    litt ekstra salt! Kanskje du kan overtale Kent Kokk til å lære deg
    hans hemmelige trylleformel som gjør steiner spiselige? Jeg skal sende
    bud på ham, gå og møt ham i slottsgården!

    -- Hør med Kent Kokk om han kan hjelpe."""
def garg_q4_ferdig(navn):
    return """    'Kjøttifiser' sier du? Jaja, det får vel duge! Jeg skal studere
    loggene ytterligere, og koke opp en slagplan!\n"""

def garg_q5(navn):
    return "    Hei " + navn + """!
    Steinsupper ja! Det var alltid en klassiker i gode gamle dager. Dessverre
    er det ganske lenge siden jeg har gjort noe slikt nå, så jeg husker ikke
    nøyaktig hva det var jeg gjorde... Det er kanskje best om jeg repeterer
    litt for meg selv før jeg lærer det videre, men til det trenger jeg steiner,
    og her virker alle steinene noe... motvillige? Kan du gjøre dem mer
    medgjørlige og samle inn 10 stykk?

    -- Finn 10 steiner."""
def garg_q5_ferdig(navn):
    return "    Strålende " + navn + """!
    Med disse skal jeg kunne lære deg en trygg og brukbar trylleformel for
    å gjøre stein om til kjøtt! Husk at du kun kan bruke den når fienden
    består av stein! Etter at du har kastet formelen, skal fienden også ha
    problem med å bli til stein igjen i iallefall noen få runder etterpå.\n"""

def garg_q6(navn):
    return "    Hei " + navn + """!
    Det ser ut til at det er gargylene som skaper trøbbel og ubalanse her.
    Dermed må vi eliminere dem! Jeg har en teori om at det er en sjefsgargyl
    som leder alle de andre. Om vi bare utsletter denne sjefsgargylen, vil
    problemet løse seg selv, og vi kan rapportere gode nyheter til Vassle.
    Denne sjefsgargylen går under navnet Guri Gargyl, og holder seg for seg
    selv. Vi må prøve å lure henne frem! Hvis du setter i gang med å slakte
    andre gargyler, burde hun før eller siden dukke opp.

    -- Eliminer Guri Gargyl."""
def garg_q6_ferdig(navn):
    return "    Fantastisk! Strålende! Godt jobbet " + navn + """!
    Dra tilbake til Magi-borgen og rapporter suksessen vår til Overtrollmann
    Vassle!\n"""

def garg_bq1(navn):
    return "    Hei " + navn + """!
    Jeg har klart å havne på feil side med slottets loggfører, og som straff
    for stygg ordbruk har den ormen tatt kosebamsen min! Kosebamsen min
    er den eneste som virkelig forstår meg! Hva snakker du om, selvfølgelig
    kan den snakke. Om du noen gang finner skattekisten til loggføreren,
    kan du se om du finner kosebamsen min der? Det kan være den har vandret
    avgårde, men før eller siden kommer den til å være i kisten!
    """
def garg_bq1_ferdig(navn):
    return "    Bamse!!! Gi meg bamse!\n"

def garg_quest(qlog, spiller):
    navn = spiller.navn()

    #q1
    desk1 = garg_q1(navn)
    ferdigDesk1 = garg_q1_ferdig(navn)
    q1 = Quest(desk1, ferdigDesk1, 7, 15, "Zap")
    q1.legg_til_reward(xp=2000, gull=200)
    q1.legg_til_progresjonTekst("Steiner ryddet: ")
    q1.legg_til_svarTekst("\nKan jeg regne med din hjelp?     (ja/nei)\n> ")
    qlog.legg_til_quest(q1)

    #q2
    desk2 = garg_q2(navn)
    ferdigDesk2 = garg_q2_ferdig(navn)
    q2 = Quest(desk2, ferdigDesk2, 1, 15, "Zap")
    q2.legg_til_reward(xp=6000, gull=500, settTilgjengelig=True, settTilgjengeligIndeks=2)
    q2.legg_til_progresjonTekst("Logg funnet: ")
    q2.legg_til_svarTekst("\nVil du hjelpe?    (ja/nei)\n> ")
    qlog.legg_til_quest(q2)

    #q3
    desk3 = garg_q3(navn)
    ferdigDesk3 = garg_q3_ferdig(navn)
    q3 = Quest(desk3, ferdigDesk3, 1, 15, "Zap", tilgjengelig=False)
    q3.legg_til_reward(xp=6000, gull=500, settTilgjengelig=True, settTilgjengeligIndeks=3)
    q3.legg_til_progresjonTekst("Utkikkstårn utforsket: ")
    q3.legg_til_svarTekst("\nVil du hjelpe?    (ja/nei)\n> ")
    qlog.legg_til_quest(q3)

    #q4
    desk4 = garg_q4(navn)
    ferdigDesk4 = garg_q4_ferdig(navn)
    q4 = Quest(desk4, ferdigDesk4, 1, 15, "Zap", tilgjengelig=False)
    q4.legg_til_reward(xp=5000, gull=2000, settTilgjengelig=True, settTilgjengeligIndeks=5)
    q4.legg_til_progresjonTekst("Kent Kokk snakket med: ")
    q4.legg_til_progresjon(1)
    q4.legg_til_progresjonTekstListe("Trylleformel lært: ", 0)
    q4.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q4)

    #q5
    desk5 = garg_q5(navn)
    ferdigDesk5 = garg_q5_ferdig(navn)
    q5 = Quest(desk5, ferdigDesk5, 10, 16, "Kent Kokk", tilgjengelig=False, resetIfDead=True)
    q5.legg_til_reward(xp=5000, gull=2000)
    q5.legg_til_progresjonTekst("Steiner samlet inn: ")
    q5.legg_til_ekstra_tekst("Du har lært et nytt trylletriks, 'kjøttifiser' ('kj')!")
    q5.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q5)

    #q6
    desk6 = garg_q6(navn)
    ferdigDesk6 = garg_q6_ferdig(navn)
    q6 = Quest(desk6, ferdigDesk6, 7, 17, "Zap", tilgjengelig=False)
    q6.legg_til_reward(xp=5000, gull=2000)
    q6.legg_til_progresjonTekst("Gargyler tillintetgjort: ")
    q6.legg_til_progresjon(1)
    q6.legg_til_progresjonTekstListe("Guri Gargyl slaktet: ", 0)
    q6.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q6)

    #bq1
    deskBq1 = garg_bq1(navn)
    ferdigDeskBq1 = garg_bq1_ferdig(navn)
    bq1 = Quest(deskBq1, ferdigDeskBq1, 1, 1, "Besynderlige Berit", bonus=True, resetIfDead=True)
    item = Item("Berits skjegg", "beard", kp=50, ekstraKp=5)
    bq1.legg_til_reward(xp=10000, item=item)
    bq1.legg_til_ekstra_tekst("Dette betyr så mye for oss! Her, ta det magiske skjegget mitt!.\n")
    bq1.legg_til_progresjonTekst("Kosebamse funnet: ")
    bq1.legg_til_svarTekst("Vil du gi kosebamsen til Besynderlige Berit?   (ja/nei)\n> ")
    qlog.legg_til_quest(bq1)
