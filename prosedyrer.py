from grafikk import *
from os import listdir, system
import platform, sys
if platform.system() == "Windows":
    from uuid import UUID
    import knownpaths

#Verdenskart.
def verdenskart(spiller):
    while True:
        clear_screen()
        print("""
    ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
                ~   VERDENSKART   ~
                                                """)
        if spiller.kart()[1]:
            print("    Magi-borgen (Gnomer)                    (1)")
        if spiller.kart()[2]:
            print("    Fjellhytta (Troll)                      (2)")
        if spiller.kart()[3]:
            print("    Vulkanen (Cerberus)                     (3)")
        if spiller.kart()[4]:
            print("    Slottet (Gargyler)                      (4)")
        if spiller.kart()[5]:
            print("    Skogen (Shrooms)                        (5)")

        #test-eksempel
        if spiller.kart()[0]:
            print("    Eksempel-expansion                      (0)")
        print("    ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("    -   Skriv 'exit' for å avslutte spillet.  -")

        inn = input("\nHvor vil du dra? (Skriv nummeret til høyre)\n> ").lower()
        if inn == "0" and spiller.kart()[0]:
            return "test"
        if inn == "1" and spiller.kart()[1]:
            return "gnom"
        if inn == "2" and spiller.kart()[2]:
            return "troll"
        if inn == "3" and spiller.kart()[3]:
            return "cerberus"
        if inn == "4" and spiller.kart()[4]:
            return "gargyl"
        if inn == "5" and spiller.kart()[5]:
            return "shroom"
        if inn in {"exit", "avslutt"} and \
        input("Progresjon blir ikke lagret når du avslutter. Vil du avslutte likevel?   (Progresjon kan lagres ved minnesteiner)\n> ").lower() in {"ja", "j", "yes"}:
            sys.exit("\nVelkommen tilbake til Pokus!")

#Skriver ut hvilke kommandoer man kan gjøre i angrepsmodus.
def hjelp():
    print("""
    Her er kommandoene du kan bruke:
    ---------------------------------------------------------------------------
    angrip (eller a)             angriper fienden
    tryllepulver (eller t)       kaster tryllepulver på fienden
    trolldrikk (eller d)         drikker en trolldrikk, gir deg helsepoeng
    konsentrasjonspulver (kp)    Sniffer en stripe konsentrasjonspulver, gir kp
    spesialangrep (eller s)      gir deg hvilke angrep du kan bruke
    erfaringspoeng (eller xp)    gir deg hvor langt igjen du har til neste nivå
    total xp                     gir deg din totale sum av erfaringspoeng
    egenskaper (eller e)         gir deg hvilke egenskaper du har
    inventar (eller i)           gir deg hvor mange av hver ting du har
    bytt (eller b)               gir deg mulighet til å bytte stav eller hatt
    oppdrag (eller q)            gir deg hvilke oppdrag du er på
    flykt (eller f)              tar deg tilbake til borgen
    poeng (eller p)              viser deg din moral
    hjelp (eller h)              gir deg denne listen med kommandoer
    ---------------------------------------------------------------------------
    """)

#Skriver ut de viktigste kommandoene.
def mini_hjelp():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
    Her er kommandoer du kan bruke:
    ---------------------------------------------------------------------------
    angrip (eller a)             angriper fienden
    tryllepulver (eller t)       kaster tryllepulver på fienden
    trolldrikk (eller d)         drikker en trolldrikk, gir deg 150 helsepoeng
    flykt (eller f)              tar deg tilbake til borgen
    hjelp (eller h)              gir deg en fullstendig liste over kommandoer
    ---------------------------------------------------------------------------
    """)

def kategorier():
    print("""    ~ - - - - - - - - - - - - - - - - - ~
    Våpen                              (1)
    Hatter                             (2)
    Hansker                            (3)
    Klær                               (4)
    Sko                                (5)
    Skjegg                             (6)
    Duppedingser                       (7)
    ~ - - - - - - - - - - - - - - - - - ~""")

#Tar spiller og fiende som parametre. Skriver ut stats hver runde.
def skriv_ut(s, f):
    s.skriv_ut()
    f.skriv_ut()

def pause():
    input("Trykk enter for å fortsette\n> ")

def kommandoer(inn, spiller, fiende, inv, klasser, spellbook, tur=True, allierte=[], fiender=[]):
    kp = spiller.kp()
    fHp = fiende.hp()

    if not fiender:
        fiender.append(fiende)
    #gir xp
    if inn == "xp" or inn == "erfaringspoeng":
        spiller.xp()

    #gir total xp
    elif inn == "total xp":
        print(spiller.navn(), "har totalt fått", spiller.total_xp(), "erfaringspoeng.")

    #viser Questlog
    elif inn == "q" or inn == "oppdrag":
        q = 0
        for qlogs in klasser.alle_questlogger():
            q += qlogs.tell_startet()
        if q == 0:
            print(spiller.navn(), "har ingen påbegynte oppdrag.")
        else:
            print(spiller.navn(), "har", q, "påbegynt(e) oppdrag:")
            for qlogs in klasser.alle_questlogger():
                qlogs.skriv_ut(spiller)

    #viser inventory
    elif inn == "i" or inn == "inventar":
        inv.skriv_inv()

    #bytter stav eller hatt
    elif inn == "b" or inn == "bytt":
        kategorier()
        try:
            kategori = int(input("Hvilken kategori vil du bytte innenfor?\n> "))
            if kategori < 8 and kategori > 0:
                x = inv.skriv_kategori(kategori)
                if x != 1:
                    indeks = int(input("Hva vil du bytte til? Skriv nummeret til høyre\n> "))
                    item = inv.bytt_til(kategori, indeks)
                    if item:
                        input("Du har byttet til " + item.navn() + ". Trykk enter for å fortsette.\n> ")
                else:
                    print("Du har ingen ting innenfor den kategorien.")
                    input("Trykk enter for å fortsette.\n> ")
            else:
                print("Ugyldig kategori")
                input("Trykk enter for å fortsette.\n> ")
        except ValueError:
            None
        except IndexError:
            print("Ugyldig kategori")

    #swap
    if inn == "swap" or inn == "sw":
        inv.swap()

    #viser stats
    elif inn == "e" or inn == "egenskaper":
        spiller.stats()

    #viser godhets- og ondhetspoeng
    elif inn == "p" or inn == "poeng":
        spiller.good_evil_points()

    #viser tilgjengelige spesialangrep
    elif inn == "s" or inn == "formler":
        spellbook.skriv_spellbook()

    #angriper fienden på vanlig måte
    elif inn == "a" or inn == "angrip":
        if not fiende.untouchable():
            weapon = inv.har_type("weapon")
            if weapon and weapon.blade():
                skade = fiende.angrepet(spiller.a(), round(inv.hent_weaponA() * \
                (1 + (0.15 * int(spiller.spesialisering() == "Muskelbunt")))))
                if spellbook.utforsk():
                    print(spiller.navn(), "fikk", spiller.restorer(skade), "liv!")
            else:
                fiende.angrepet(spiller.a())
        else:
            print("Angrep er nyttesløst i fiendens nåværende form.")
        #burning
        if fiende.burning():
            print(spiller.navn(), "mistet", spiller.mist_liv(randint(30, 70)), "liv fra flammene under angrepet.")
        tur = False

    #angriper fienden med tryllepulver.
    elif inn == "t" or inn == "tryllepulver":
        tur = spellbook.tryllepulver(fiende)

    #drikker en flaske trolldrikk.
    elif inn == "d" or inn == "trolldrikk":
        tur = spellbook.trolldrikk()

    elif inn == "kp" or inn == "konsentrasjonspulver":
        tur = spellbook.konsentrasjonspulver()

    #bruker vanlig restituer. Krever lvl 3
    elif inn == "r" or inn == "restituer":
        tur = spellbook.restituer()

    #angriper fienden med vind. Krever lvl 5
    elif inn == "v" or inn == "vind":
        tur = spellbook.vind(fiende)

    #kaster super restituer. Krever lvl 10
    elif inn == "sr" or inn == "super restituer":
        tur = spellbook.super_restituer()

    #kaster konsentrer energi. Krever fullførelse av quest.
    elif inn == "ke" or inn == "konsentrer energi":
        tur = spellbook.konsentrer_energi(fiende)

    #kaster Nedkjøl. Krever fullførelse av quest.
    elif inn == "n" or inn == "nedkjøl":
        tur = spellbook.freeze(fiende)

    #kaster kjøttifiser. Krever utførelse av quest.
    elif inn == "kj" or inn == "kjøttifiser":
        tur = spellbook.meatify(fiende)

    #kaster Utforsk. Krever lvl 17.
    elif inn == "u" or inn == "utforsk":
        tur = spellbook.brukUtforsk()

    #kaster Opphold. Krever lvl 20.
    elif inn == "o" or inn == "opphold":
        tur = spellbook.brukOpphold(fiende)

    #kaster Distraher. Krever fullførelse av quest.
    elif inn == "di" or inn == "distraher":
        tur = spellbook.distraher(fiende)

    #kaster Solidifiser. Krever spesialisering Smertedreper.
    elif inn == "so" or inn == "solidifiser":
        tur = spellbook.brukSolidifiser()

    #kaster Tankeboble. Krever spesialisering Klartenker.
    elif inn == "ta" or inn == "tankeboble":
        tur = spellbook.brukTankeboble()

    #kaster Forsterk. Krever spesialisering Muskelbunt.
    elif inn == "fo" or inn == "forsterk":
        tur = spellbook.brukForsterk()

    #kaster Lys. Krever formel kjøpt og 10 gp.
    elif inn == "l" or inn == "lys":
        tur = spellbook.bruk_lys()

    #kaser Korrupsjon. Krever formel kjøpt og 10 op.
    elif inn == "ko" or inn == "korrupsjon":
        tur = spellbook.korrupsjon(fiende)

    #gir liste over kommandoer.
    elif inn == "h" or inn == "hjelp":
        hjelp()

    #spilleren gjør ingenting.
    elif inn == "ingenting":
        print(spiller.navn(), "gjør ingenting.")
        tur = False

    #resetter spellbook om man flykter fra en kamp.
    elif inn == "f" or inn == "flykt":
        spellbook.reset()

    elif inn in {"juks", "j2", "j3", "j4", "juks2", "juks3", "juks4", "j"}:
        print("Juksemaker!", spiller.navn(), "mistet", spiller.mist_liv(10), "liv!")

    #Intet spill er komplett uten en juksekode. Dessuten særdeles
    #brukbart for å teste programmet. Dreper en fiende på første forsøk.
    """elif inn == "j" or inn == "juks":
        fiende.angrepet(100042)

    #Juksekode nr. 2: når ønsket lvl.
    elif inn == "j2" or inn == "juks2":
        liste = [int(80*x+(80*(x-1)/10)*(x*x/5+x/1.5)) for x in range(1, 71)]
        try:
            lvl = int(input("Hvilken lvl vil du til?\n> "))
            spiller.gi_xp(sum(liste[0:lvl - 1]) -spiller.total_xp())
        except ValueError:
            print("Du må skrive et tall!")

    #Juksekode nr. 3: Får ønsket antall gullstykker.
    elif inn == "j3" or inn == "juks3":
        try:
            inv.penger(int(input("Hvor mange gullstykker vil du ha?\n> ")))
        except ValueError:
            print("Du må skrive et tall!")

    #Juksekode nr. 4: Restorerer liv og kp til fullt.
    elif inn == "j4" or inn == "juks4":
        spiller.restorer(100000)
        spiller.restorer_kp(10000)"""

    #aktiverer Lys
    if not tur and spellbook.lys():
        gp = spiller.good_points()
        ep = spiller.evil_points()
        mengde = round((((gp + 0.01) / (gp + ep + 0.001)) * gp * 100) / 5)
        print(spiller.navn(), "restorerte", spiller.restorer(mengde), "liv fra lyset!")
        for a in allierte:
            if a:
                print(a.navn(), "restorerte", a.restorer(mengde), "liv fra", spiller.navn() + "s lys!")

    #akiverer korrupsjon
    if not tur and fiende.bleeding() > 0:
        fiende.korrupt()

    #aktiverer burning
    if not tur and spiller.burning()[0]:
        print(spiller.navn(), "mistet", spiller.mist_liv(randint(\
        spiller.burning()[1] - round(spiller.burning()[1] / 20), \
        spiller.burning()[1] + round(spiller.burning()[1] / 20))), "liv fra flammene.")

    #progresserer solidifiser, forsterk og tankeboble
    if not tur:
        spellbook.solidifiserCD(fiende, fiender)
        spellbook.forsterkCD(fiende, fiender)
        spellbook.tankeboble()

    #progresserer klartenker-quest. Avgjør hvor mye kp som er brukt.
    if klasser.questlog(3).hent_quest(5).startet() and kp - spiller.kp() > 0:
        klasser.questlog(3).hent_quest(5).progresser(kp - spiller.kp())

    #progresserer muskelbunt-quest. Avgjør hvor mye hp som er tatt fra fienden.
    if klasser.questlog(2).hent_quest(4).startet():
        klasser.questlog(2).hent_quest(4).progresser(fHp - fiende.hp())

    return tur

def player_died(spiller, inv, klasser):
    spiller.die(inv)
    qlogListe = klasser.alle_questlogger()
    for log in qlogListe:
        qListe = log.hent_qLog()
        for q in qListe:
            if q.reset_if_dead():
                q.reset_progresjon()

def write_player_died(spiller, sted):
    skrivGravstein()
    print("\n\n                                     DØD")
    print("\n\n    **************************************************************************")
    input("    Trykk enter for å fortsette\n    > ")
    print("\n    **************************************************************************")
    print("    ", spiller.navn(), " døde! Alt håp er ute, og ", spiller.navn(), """ etterlates
    naken og forslått på bakken, klar til å bli sakte fortært av allverdens kryp.
    For en trist slutt!

    MEN!
    Kanskje smiler lykken til """, spiller.navn(), """ likevel? Tilfeldigvis går en
    krokete nekromant forbi de råtne benrestene til """, spiller.navn(), """, hvorpå
    nekromanten får den strålende idéen å blande dette prakteksemplaret av
    menneskebenrester med de nærliggende fuglerestene.\n""", sep="")
    input("    Trykk enter for å fortsette\n    > ")
    print("    Benrestene til ", spiller.navn(), """ kokes sakte i en kjele gjemt langt ned i
    en mørk hule et sted resten av verden forlengst har glemt. En særegen
    odor av fugleekskrement blandet med råttent menneskekjøtt, enhjørningsblod
    og en touch av kanel fyller hulen. Dette ellers livløse stedet, tidligere
    kun bebodd av vandøde troll som ble avvist under det årlige meningsløse
    paringsrituale for vandøde skapninger like ved, begynner plutselig å koke
    av liv samtidig som innholdet i kjelen koker over. Nekromanten, som regner
    seg selv som død og sympatiserer med skapningene som bor i denne delen av landet,
    setter i et hjerteskjærende ul, tett etterfulgt av en livlig, lenge glemt, folkevise.
    """, spiller.navn(), """ har gjennoppstått fra de døde! En noe skuffet nekromant
    bemerker seg at denne personen ikke er halvt fugl, til tross for en
    bemerkelsesverdig lukt av fjær og noe gulere øyne. """, spiller.navn(), """, forvirret
    og redd, ser seg om i hulen og lurer på hvordan man kan komme seg tilbake til
    """, sted, """, men nekromanten er blitt rasende av sitt eget nederlag og bestemmer seg
    for å drepe """, spiller.navn(), """.

    """, spiller.navn(), """ dør igjen.""", sep="")
    input("\n    Trykk enter for å fortsette\n    > ")
    print("""
    MEN!
    Universets tilfeldigheter ville ha det til at en vandrende magiker finner
    liket til """, spiller.navn(), """! Denne magikeren har spesialisert seg
    i restorerende magi, og har lenge hatt lyst til å prøve ut sin magi
    på døde mennesker, noe som har gitt Gizly tilnavnet "Gale".

    Mistenksom på fuglelukten som utstår fra """, spiller.navn(), """, bestemmer
    Gale Gizly seg for å stille """, spiller.navn(), """ et viktig spørsmål,
    et spørsmål som vil for all tid bestemme om , """, spiller.navn(), """ skal
    leve eller forbli død. Gale Gizly trenger gjennom dødens barrierre, og spør:

                       ***Hva er det største i livet?***
    """, sep="")
    input("    Hva er svaret?\n    > ")
    print("""\n    Godt fornøyd med svaret, vekker Gale Gizly""", spiller.navn(), """tilbake
    til livet!

    En noe fortumlet""", spiller.navn(), """våkner opp forslått, men trygg og
    med noenlunde stabil mental helse opp i""", sted + ".\n")
    input("    Trykk enter for å fortsette\n    > ")

def finn_stats(item):
    statliste = item.statliste()
    totalStats = sum([int(bool(s)) for s in statliste])

    i1 = 0
    i2 = 0
    listestats = [0 for z in range(totalStats)]
    listetekst = ["" for z in range(totalStats)]
    listestatTekst = item.statlisteTekst()
    while i1 < len(statliste):
        if statliste[i1] != 0:
            listetekst[i2] = listestatTekst[i1]
            listestats[i2] = statliste[i1]
            i2 += 1
        i1 += 1
    returnListe = ["" for z in range(totalStats)]
    i = 0
    while i < len(listetekst):
        returnListe[i] = listetekst[i] + ":" + str(listestats[i])
        i += 1
    return returnListe

#Prosedyrer og funksjoner knyttet til lagring og lasting av filer:

if platform.system() == "Windows":
    docFolder = knownpaths.get_path(UUID('{FDD39AD0-238F-46AF-ADB4-6C85480369C7}'))
else:
    docFolder = ""
    if "Save" not in listdir():
        os.system("mkdir Save")

def minnestein(spiller, inv, klasser):
    pris = 100
    sPris = 500
    if spiller.lvl() >= 10:
        pris = 300
        sPris = 2000
    if spiller.lvl() >= 20:
        pris = 500
        sPris = 8000
    if spiller.lvl() >= 30:
        pris = 2000
        sPris = 20000
    if spiller.lvl() >= 40:
        pris = 4500
        sPris = 35000

    print("""                     *** MINNESTEIN ***

    Du er ved en minnestein! Her kan du bevare sjelen din, og
    hente den ut igjen ved et senere tidspunkt. Å bevare sjelen
    kommer ikke uten en pris. For å bevare din sjel, krever
    minnesteinen et offer på""", pris, "gullstykker.\n")
    inn = ""
    while inn not in {"j", "ja", "n", "nei"}:
        inn = input("Ønsker du å bevare sjelen din?    (ja/nei)\n> ").lower()
    if inn == "j" or inn == "ja":
        if inv.penger() >= pris:
            inv.penger(-pris)
            lagre(spiller, inv, klasser)
            input("\nBevaring av sjelen er vellykket! Trykk enter for å fortsette\n> ")
        else:
            print("\n    Du har ikke nok gullstykker til å bevare sjelen din.")
            print("    Minnesteinen kan likevel godta et offer i form av", sPris, "erfaringspoeng.")
            inn = ""
            while inn not in {"j", "ja", "n", "nei"}:
                inn = input("\nØnsker du å bevare sjelen din for denne prisen?    (ja/nei)\n> ").lower()
            if (inn == "j" or inn == "ja") and spiller.total_xp() >= sPris:
                spiller.gi_xp(-sPris)
                lagre(spiller, inv, klasser)
                input("\nBevaring av sjelen er vellykket! Trykk enter for å fortsette\n> ")
            elif inn == "j" or inn == "ja":
                print("\n    Du har ikke nok erfaringspoeng å ofre til minnesteinen.")
                print("    Er du sikker på at ditt eventyr er verdt å lagre?")
                print("    Kom tilbake når du har noe verdifult å ofre til minnesteinen,")
                print("    som f.eks. livet ditt. Ikke verdt noe nå iallefall.")
                input("\nTrykk enter for å dra tilbake\n> ")
    return

def load_screen():
    osys = platform.system()
    inn = ""
    print("""    *********************************************************

    Velkommen til Pokus! Her er dine valg:

    Start et nytt spill                                  (1)
    Last tidligere spill                                 (2)
    Avslutt programmet                                   (3)

    *********************************************************""")
    while inn != "1" and inn != "2" and inn != "3":
        inn = input("Hva vil du gjøre?\n> ")
    if inn == "1":
        clear_screen()
        return False
    elif inn == "2":
        if osys == "Windows":
            if "pokus_saves" not in listdir(docFolder):
                os.system("mkdir " + docFolder + "\\pokus_saves")
            filer = listdir(docFolder + "\\pokus_saves")
        else:
            if "Save" not in listdir():
                os.system("mkdir Save")
            filer = listdir("Save")
        if filer == []:
            print("Du har ingen lagrede filer!")
            input("\nTrykk enter for å fortsette\n> ")
            return load_screen()
        else:
            clear_screen()
            print("""    *********************************************
            Her er spillene du kan laste:
    - - - - - - - - - - - - - - - - - - - - - - -""")
            i = 1
            for fil in filer:
                print("{:4}{:40}({})".format("", fil[0:len(fil)-4], i))
                i += 1
            print("    - - - - - - - - - - - - - - - - - - - - - - -")
            print("    Skriv tallet til høyre for å laste spillet.")
            print("    Skriv 0 for å gå tilbake.")
            print("    *********************************************")
            inn = input("Hvilket spill vil du laste?\n> ")
            while inn != "0":
                try:
                    if osys == "Windows":
                        return docFolder + "\\pokus_saves\\" + filer[int(inn) -1]
                    else:
                        return "Save/" + filer[int(inn) -1]
                except ValueError:
                    print("\nDu må skrive et tall!\n")
                except IndexError:
                    print("\nDu har ikke så mange filer!\n")
                inn = input("Hvilket spill vil du laste?\n> ")
            return load_screen()
    elif inn == "3":
        sys.exit("\nVelkommen tilbake!")

def lagre(spiller, inv, klasser, nr=0):
    osys = platform.system()
    if osys == "Windows":
        filnavn = docFolder + "\\pokus_saves\\" + spiller.navn() + ".sav"
        if nr:
            filnavn = docFolder + "\\pokus_saves\\" + spiller.navn() + "(" + str(nr) + ")" ".sav"
    else:
        filnavn = "Save/" + spiller.navn() + ".sav"
        if nr:
            filnavn = "Save/" + spiller.navn() + "(" + str(nr) + ")" ".sav"

    try:
        fil = open(filnavn)
        fil.close()
        if spiller.first_save():
            fil = open("012bsd13ryvjbkuj54ub7.sav")
            fil.close()
        lagre(spiller, inv, klasser, nr +1)
        return
    except FileNotFoundError:
        try:
            dekrypt(filnavn)
        except FileNotFoundError:
            pass
        spiller.first_save(True)
        with open(filnavn, "w") as fil:
            fil.write("")

        lagreListe = ["Spiller\n"]

        spillerinf = spiller.lagre_stats(inv)
        kartListe = spillerinf.pop()
        tekst = ""
        for x in range(len(spillerinf)):
            tekst += str(spillerinf[x]) + ","
        lagreListe.append(tekst.strip(",") + "\n")
        tekst = ""
        for x in range(len(kartListe)):
            tekst += str(int(kartListe[x])) + ","
        lagreListe.append(tekst.strip(",") + "\n")

        lagreListe.append("Inventory\n")
        lagreListe.append(str(inv.penger()) + "\n")
        itemListe = inv.itemListe()
        for item in itemListe:
            infListe = [item.navn(), item.type()]
            for stat in item.statliste():
                infListe.append(str(stat))
            infListe.append(str(int(item.bruker())))
            infListe.append(item.spesialisering())
            infListe.append(str(item.lvl()))
            infListe.append(str(int(item.blade())))
            tekst = ""
            for inf in infListe:
                tekst += inf + ","
            lagreListe.append(tekst.strip(",") + "\n")

        lagreListe.append("Questlog\n")
        for qlog in klasser.alle_questlogger():
            for q in qlog.hent_qLog():
                if q.startet() or q.progresjon() or q.ferdig():
                    tekst = str(klasser.alle_questlogger().index(qlog)) + ","
                    tekst += str(qlog.hent_qLog().index(q)) + ","
                    tekst += str(int(q.startet())) + ","
                    tekst += str(int(q.ferdig())) + ","
                    tekst += str(q.progresjon())
                    for progresjon in q.progresjon_liste():
                        tekst += "," + str(progresjon)
                    lagreListe.append(tekst + "\n")

        with open(filnavn, "a") as fil:
            for linje in lagreListe:
                fil.write(linje)

    krypt(filnavn)

def last_navn(filnavn):
    dekrypt(filnavn)
    with open(filnavn) as fil:
        linje = fil.readline()
        return fil.readline().strip().split(",")[:2]

def last_fil(spiller, inv, klasser, filnavn):
    with open(filnavn) as fil:
        linje = fil.readline()
        linje = fil.readline().strip()
        spillerInf = linje.split(",")
        spillerInf.pop(0)
        spillerInf.pop(0)
        linje = fil.readline().strip()
        kartliste = linje.split(",")
        i = 0
        while i < len(kartliste):
            kartliste[i] = bool(int(kartliste[i]))
            i += 1
        spiller.last_stats(spillerInf, kartliste)

        linje = fil.readline()
        inv.penger(int(fil.readline().strip()) - 100)
        linje = fil.readline().strip()
        while linje != "Questlog":
            itemInf = linje.split(",")
            inv.last_inn(itemInf)
            linje = fil.readline().strip()

        linje = fil.readline().strip()
        while linje != "":
            questInf = linje.split(",")
            qlog = klasser.questlog(int(questInf[0]))
            q = qlog.hent_quest(int(questInf[1]))
            q.start((bool(int(questInf[2]))))
            q.sett_ferdig(bool(int(questInf[3])))
            if q.ferdig():
                if q.hent_sett_tilgjengelig_reward()[0]:
                    try:
                        for x in q.hent_sett_tilgjengelig_reward()[1]:
                            qlog.hent_quest(x).sett_tilgjengelig()
                    except TypeError:
                        qlog.hent_quest(q.hent_sett_tilgjengelig_reward()[1]).sett_tilgjengelig()
            q.progresser(int(questInf[4]))
            if q.progresjon_liste():
                for x in range(5, 5 + len(q.progresjon_liste())):
                    q.progresser_liste(x - 5, int(questInf[x]))
            linje = fil.readline().strip()
    krypt(filnavn)

def krypt(filnavn):
    ingetingAaSeHer = "hunGunIcorN"
    skalSkrive =  []
    tekst = ""
    with open(filnavn) as fil:
        for linje in fil:
            bokstaver = list(linje.strip())
            for x in range(len(bokstaver)):
                bokstaver[x] = chr(ord(bokstaver[x]) + ord(ingetingAaSeHer[x % len(ingetingAaSeHer)]))


            skalSkrive.append("".join(bokstaver))
    for linje in skalSkrive:
        tekst += linje + "\n"

    with open(filnavn, "w", encoding="UTF-8") as fil:
        fil.write(tekst)

def dekrypt(filnavn):
    ingentingInteressant = "hunGunIcorN"
    skalSkrive =  []
    tekst = ""
    with open(filnavn, encoding="UTF-8") as fil:
        for linje in fil:
            bokstaver = list(linje.strip("\n"))
            for x in range(len(bokstaver)):
                bokstaver[x] = chr(ord(bokstaver[x]) - ord(ingentingInteressant[x % len(ingentingInteressant)]))
            skalSkrive.append("".join(bokstaver))
    for linje in skalSkrive:
        tekst += linje + "\n"

    with open(filnavn, "w") as fil:
        fil.write(tekst)

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
