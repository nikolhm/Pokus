from grafikk import *

#Verdenskart.
def verdenskart(spiller):
    while True:
        print("""
        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
                    ~   VERDENSKART   ~
                                                """)
        if spiller.kart()[1]:
            print("    Magi-borgen (Gnomer)                    (1)")
        if spiller.kart()[2]:
            print("    Slottet (Gargyler)                      (2)")

        #test-eksempel
        if spiller.kart()[0]:
            print("    Eksempel-expansion                      (0)")
        print("    ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

        inn = input("Hvor vil du dra? (Skriv nummeret til høyre)\n> ")
        if inn == "0" and spiller.kart()[0]:
            return "test"
        if inn == "1" and spiller.kart()[1]:
            return "gnom"
        if inn == "2" and spiller.kart()[2]:
            return "gargyl"

#Skriver ut hvilke kommandoer man kan gjøre i angrepsmodus.
def hjelp():
    print("""
    Her er kommandoene du kan bruke:
    ---------------------------------------------------------------------------
    angrip (eller a)             angriper fienden
    tryllepulver (eller t)       kaster tryllepulver på fienden
    trolldrikk (eller d)         drikker en trolldrikk, gir deg 150 helsepoeng
    konsentrasjonspulver (kp)    Sniffer en stripe konsentrasjonspulver, gir 100 kp
    spesialangrep (eller s)      gir deg hvilke angrep du kan bruke
    erfaringspoeng (eller xp)    gir deg hvor langt igjen du har til neste nivå
    total xp                     gir deg din totale sum av erfaringspoeng
    egenskaper (eller e)         gir deg hvilke egenskaper du har
    inventar (eller i)           gir deg hvor mange av hver ting du har
    bytt (eller b)               gir deg mulighet til å bytte stav eller hatt
    oppdrag (eller q)            gir deg hvilke oppdrag du er på
    flykt (eller f)              tar deg tilbake til borgen
    hjelp (eller h)              gir deg denne listen med kommandoer
    ---------------------------------------------------------------------------
    """)

#Skriver ut de viktigste kommandoene.
def mini_hjelp():
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

def kommandoer(inn, spiller, fiende, inv, klasser, spellbook, tur=True):
    qlog = klasser.questlog(1)
    #gir xp
    if inn == "xp" or inn == "erfaringspoeng":
        spiller.xp()

    #gir total xp
    elif inn == "total xp":
        spiller.total_xp()

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

    #viser stats
    elif inn == "e" or inn == "egenskaper":
        spiller.stats()

    #viser tilgjengelige spesialangrep
    elif inn == "s" or inn == "formler":
        spellbook.skriv_spellbook()

    #angriper fienden på vanlig måte
    elif inn == "a" or inn == "angrip":
        if not fiende.untouchable():
            weapon = inv.har_type("weapon")
            if weapon and weapon.blade():
                skade = fiende.angrepet(spiller.a(), inv.hent_weaponA())
                if spellbook.utforsk():
                    print(spiller.navn(), "fikk", spiller.restorer(skade), "liv!")
            else:
                fiende.angrepet(spiller.a())
        else:
            print("Angrep er nyttesløst i fiendens nåværende form.")
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

    elif inn == "kj" or inn == "kjøttifiser":
        tur = spellbook.meatify(fiende)

    #kaster utforsk. Krever lvl 17
    elif inn == "u" or inn == "utforsk":
        tur = spellbook.brukUtforsk()

    #gir liste over kommandoer.
    elif inn == "h" or inn == "hjelp":
        hjelp()

    #Intet spill er komplett uten en juksekode. Dessuten særdeles
    #brukbart for å teste programmet. Dreper en fiende på første forsøk.
    elif inn == "j" or inn == "juks":
        fiende.angrepet(10042)

    #Juksekode nr. 2: gir 10000 xp.
    elif inn == "j2" or inn == "juks2":
        spiller.gi_xp(10000)

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
    totalStats = 0
    for s in statliste:
        if s != 0:
            totalStats += 1
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
