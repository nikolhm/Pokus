"""
                *~ Troll- expansion ~*

"""
#Start med å importere alle de nødvendige delfilene.
from klasser import *
from grafikk import *
from quests import *
from prosedyrer import *

"""
Litt generelt: xHp, xKp og xProgresjon betyr total mengde (max) av det man kan
ha av noe. For alle mulige argumenter som kan brukes ved opprettelsen av
de forskjellige objektene, se __init__-metode i klasser.py. Det skal
generelt ikke være nødvendig å forandre på implementasjonen innenfor klassene.
Skulle det likevel være ønskelig, ta kontakt med meg (Gaute) på facebook
eller evt. på gaute.svanes@gmail.com. Noen unntak kan gjelde Spellbook-klassen
og skriv_inv-metoden i Inventory-klassen som muligens må utvides avhengig
av innholdet i expansionen. Ta uansett kontakt med meg om det skulle være
tilfellet. Item-klassen er en mye brukt klasse, og brukes mest til loot,
reward i quest og som vare i butikken. Alle items må ha en kategori oppgitt
i konstruktøren. Dette må være en av følgende:

restoring       restorerer hp eller kp eller begge.
damaging        gjør skade på fienden (f.eks tryllepulver)
weapon          våpen. Merk at både sverd og stav er i samme kategori. Er det et
                sverd, sett blade=True som argument
hat             Hatter/luer
gloves          hansker
robe            sett med klær/klær generelt
shoes           sko
beard           falskt skjegg
trinket         ting (kan være hva som helst) som gir stats
various         ting som ikke gir stats.

For å få denne test-expansionen til å fungere, ta vekk #-tegnet foran
spiller.sett_sted_tilgjengelig(0)

Er det noen spørsmål, ikke nøl med å spørre meg :)

- Gaute Svanes Lunde
"""

"""
    Start med å lage en Main-loop. Denne skal kalles fra pokus.py, og kjører
    hele denne delen. Det skal være mulig å kalle denne loopen flere ganger, altså
    at man kan "komme tilbake" til dette stedet på et senere tidspunkt, uten at
    noe har forandret seg. For at det skal fungere, må questlog og butikk lages
    utenfor denne filen, og lages dermed i pokus.py.

    La oss si at vår helt og hovedkarakter har kommet til et magisk sted fylt med
    regnbuer og onde enhjørninger.

    Merk at det aldri brukes æøå i variabelnavn eller prosedyre/funksjon/metode-navn.
    Main-loopen skal ta inn spiller, inventory, klasser og spellbook, slik at de kan
    brukes senere.
"""

#Mainloop:
def troll_loop(spiller, inv, klasser, spellbook):
    """Questlog blir laget utenfor loopen, og lagres i klasser-objektet.
    For å enkelt kunne referere til dette, lagrer vi vårt Questlog-objekt
    som en variabel:"""
    qlog = klasser.questlog(2)

    """Vi begynner med en valgløkke. Her bestemmes alle stedene karakteren kan
    gå, og består gjerne av et sted man får quest, en butikk, og diverse
    kamp-instanser som kan være quest-relatert eller frie. Brukeren får opp
    et kart over hvor man kan dra, som vi lager i en egen prosedyre."""

    ferdig = False
    while not ferdig:
        """kartet tar inn qlog som parameter, slik at det kan forandre seg
        basert på hvilke quest man har gjort."""
        trollKart(qlog)

        """Her deklereres alle variablene som blir brukt i hovedløkken. variablene
        bestemmer hvilken løkke den skal gå inn i etterpå."""
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

            """Skal kun gå i denne løkken hvis man har startet, men ikke er ferdig med,
            quest nummer 2. Merk opptelling begynner med 0."""
            if inn == "c" and qlog.hent_quest(1).startet() and not qlog.hent_quest(1).ferdig():
                cave = True
                valg = True

            if inn == "h" and qlog.hent_quest(2).startet():
                helvete = True
                valg = True

        """Questlog-klassen sin oppdrag_tilgjengelige-metode viser lvl og stedet
        man er, samt returnerer brukerens input. Snakk-metoden brukes for å
        starte, sjekke progresjon eller fullføre et quest, avhengig av progresjon.
        Det kan brukes seperat for spesielle quest, men i dette tilfellet
        samles alle som gir quest på et sted (utenfor stallen). Vil man ha det,
        kan løkken nedenfor kopieres."""
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

        "Om butikken er ferdig oppsatt med varer, trengs ikke mer enn å kalle interaksjon-metoden."
        while gaaTilButikk:
            klasser.butikk(1).interaksjon(inv)
            gaaTilButikk = False

        """Dette er instansen med fri kamp, som her går undet navnet 'regnbue'.
        Her vil man alltid møte en ny fiende helt til man drar vekk. I dette
        tilfellet veksler fienden man møter med å være en fisk og en enhjørning.
        Enhjørningen er et eksempel på dynamisk generering av fiende, mens
        fisken er statisk. Det vil si at enhjørningen kan variere i hvor god den
        er, og skalerer med spillerens nivå, mens fisken alltid har samme stats.
        Fiendene genereres her i egne løkker.

        Jeg har her valgt å sette angrepsinstansen i en egen prosedyre (angrip)
        slik at den kan brukes på hvilken som helst fiende. Angrip-prosedyren
        returnerer her True hvis fienden er overvunnet, eller False hvis man
        løper vekk eller dør."""
        while fjell:
            fiende = generer_troll(spiller)

            skriv_ut(spiller, fiende)
            fjell = angrip(spiller, fiende, inv, klasser, spellbook)

            "progresserer første questet hvis det er aktivt."
            if fjell and qlog.hent_quest(0).startet():
                qlog.hent_quest(0).progresser()

        #Denne løkken lagrer spillet.
        while lagre:
            minnestein(spiller, inv, klasser)
            lagre = False

        "Quest nummer 2 er satt i en egen instans, og har tre progresjoner som følges."
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
            "progresserer her den første av de ekstra progresjonene som ble lagt til."
            #qlog.hent_quest(1).progresser_liste(0)

            #Fiende 3
            skrivTrollBoss()
            print(spiller.navn(), "har møtt en enormt troll!")
            fiende = Fiende("Enormt troll", "troll", Loot(), 1000, 200, 200, kp=150)
            fiende.return_loot().legg_til_item(500, 100)
            skriv_ut(spiller, fiende)
            if angrip(spiller, fiende, inv, klasser, spellbook):
                qlog.hent_quest(1).progresser()
                print("\n*Du klarte det! Nå har du svaret!*\n")
            cave = False

        "Quest nummer 3 skal slå en boss, og er satt i egen instans."
        while helvete:
            loot = Loot()
            item = Item("Overpowered ting", "trinket", a=200, d=200, ekstraKp=10)
            loot.legg_til_item(item, 50)
            loot.legg_til_item(3000, 50)
            fiende = Fiende("Smart troll", "troll", loot, 2500, 300, 250, kp=100, bonusKp=5, weapon=60)

            print("        " + spiller.navn(), """har møtt sisteboss! Han forklarer alt,
        korrupsjonen av trollene osv. Han snakker så lenge at det
        burde egentlig blitt lagt til en egen prosedyre.\n""")
            skriv_ut(spiller, fiende)
            if angrip(spiller, fiende, inv, klasser, spellbook):
                qlog.hent_quest(2).progresser()

            helvete = False

    """Man havner i her når brukeren vil se verdenskartet. Da går man ut av
    hovedløkken, og går til løkken i pokus.py. """
    if ferdig:
        return verdenskart(spiller)


"""
                                Angrepsløkken:

    Denne løkken gir brukeren mulighet til å utføre alle kommandoer som er
    implementert i spillet. De ligger lett tilgjengelig i kommandoer()-funksjonen
    i prosedyrer.py. kommandoer() avgjør om brukeren har brukt sin tur eller ikke,
    og utfører de kommandoene brukeren ønsker, med unntak av flykt-funksjonen som
    må implementeres seperat.

    Etter kommandoer(), gjenstår det å se om fienden er død. I så fall, får
    spilleren xp og loot. Hvis ikke fienden er død, sjekkes det om spilleren
    har brukt opp sin tur. Om det er tilfellet, får fienden angripe.
    I dette tilfellet kan fienden enten angripe vanlig, eller bruke kp
    for å restorere seg selv. Etter fienden har angrepet, sjekkes det om
    spilleren er død. Om det er tilfellet, skrives dødstekst, og inventory
    og eventuelle quests resettes automatisk med spiller-klassen sin
    player_died()-metode.

    Om ingen er død, får begge tilbake litt kp, og informasjon om spiller og
    fiende skrives ut.
"""
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

"""Her genereres en fiende, tilfeldig skalert etter spillerens nivå.
I dette tilfellet, om spilleren er i lvl 20, kan fienden maksimalt ta 220 liv."""
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

"""
                                    Loot:

    Loot lages ved å opprette et nytt Loot-objekt, deretter fylle det opp med
    items gjennom .legg_til_item()-metoden. Den tar et item-objekt og et tall
    som parametre, der tallet representerer sannsynligheten for å få denne tingen.
    Om alle tallene i Loot-objektetes legg_til_item()-metode tilsammen blir tallet
    100, vil det utrykke prosent. Om summen av alle tallene er 143, og en item har
    sannsynlighet på 32, er det en 32/143-sjanse for å få tingen.

    Penger kan legges til ved å putte et tall der item-objektet skulle vært.

    I denne prosedyren, skaleres tingene i forhold til lvl til spilleren.
    I statsiskLoot-prosedyren under, har tingene faste stats.
"""
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

"Her er kartet til Troll-expansionen. Noen steder avhenger av quest for å vises."
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

"""Her settes en butikk opp. Alt som trengs er å opprete Item-objekter, og legge
de til i butikken gjennom Butikk-klassens .legg_til_vare()-metode."""
def trollButikk(butikk):
    butikk.legg_til_hadeTekst("\nVelkommen tilbake! Og pass deg for troll!\n")

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

"""
                                    Quest:

    I denne prosedyren fylles Questlog-objektet opp med quests. Siden dette bare
    er en test, er beskrivelsene korte, og lagt direkte til her, men der quest-beskrivelsen
    og avslutningsbeskrivelsen er lengre, kan de puttes til egne prosedyrer og legges
    i quests.py-filen.

    Ved opprettelse av Quest-objekter, er følgende argumenter
    nødvendige: Deskripsjon, ferdig-deksripsjon (/slutttekst/takketekst), total
    progresjon som trengs (som f.eks. finn 20 ting, drep 12 dyr osv.), lvl for å starte
    questet, og navnet til den som gir questet. Belønning blir lagt til med en egen metode.
    For total oversikt over hvilke argumenter man kan gi ved opprettelse av Quest-objekt
    og ved legg_til_reward()-metoden, se i klasser.py-filen.
"""
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
    ferdigDesk2 = "Takk igjen " + navn + "!"
    q2 = Quest(desk2, ferdigDesk2, 1, 16, "Zip")
    item = Item("Trollskjegg", "beard", xKp=80, ekstraKp=20)
    q2.legg_til_reward(xp=1000, gull=2500, item=item, settTilgjengelig=True, settTilgjengeligIndeks=2)
    q2.legg_til_ekstra_tekst("Her kommer ekstra tekst. Noe som involverer skjegget som blir gitt i reward kanskje?")
    """
    q2.legg_til_progresjonTekst("Stor fiende 1 bekjempet: ")
    q2.legg_til_progresjon(1)
    q2.legg_til_progresjonTekstListe("Stor fiende 2 bekjempet: ", 0)
    q2.legg_til_progresjon(1)
    """
    q2.legg_til_progresjonTekst("Digert troll drept: ")
    q2.legg_til_svarTekst("\nVil legge ut på et eventyr for å finne svaret?    (ja/nei)\n> ")
    qlog.legg_til_quest(q2)

    #q3
    "Dette questet er utilgjengelig intill fullførelse av det forige questet."
    desk3 = "    Hei " + navn + "!\n    Dette er siste quest! Progresser ved å drepe hovedbossen!"
    ferdigDesk3 = "Takk " + navn + "! Du dette var skikkelig bra kodet!"
    q3 = Quest(desk3, ferdigDesk3, 1, 16, "Questholder 2", tilgjengelig=False)
    q3.legg_til_reward(xp=5000, gull=2000)
    q3.legg_til_progresjonTekst("Boss bekjempet: ")
    q3.legg_til_svarTekst("\nVil du hjelpe oss?    (ja/nei)\n> ")
    qlog.legg_til_quest(q3)
