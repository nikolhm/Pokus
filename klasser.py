import quests
from random import randint
from prosedyrer import *

class Butikk:
    def __init__(self, navn):
        self._vareliste = []
        self._navn = navn
        self._hadeTekst = "Velkommen tilbake!"

    #Skriver ut varene.
    def skriv_ut_sortiment(self, inv):
        print("    ------------------------------------------------------------")
        print("    Hos '", self._navn, "' har vi følgende varer:", sep="")
        for vare in self._vareliste:
            print("    " + vare.skriv_vare(inv))
        print("\n    Skriv bokstaven til høyre for å kjøpe den valgte varen.", \
            "\n    Skriv 'ferdig' / 'f' for å gå ut, 'selg' / 's' for å selge.", \
            "\n    ------------------------------------------------------------\n")

    def interaksjon(self, inv):
        print("    ------------------------------------------------------------")
        print("    Velkommen til '", self._navn, "'!", sep="")
        print("    ------------------------------------------------------------")
        inn = input("\nVil du kjøpe eller selge? (k/s)         'f' for å gå tilbake\n> ")
        while inn != "f" and inn != "ferdig":
            while inn != "f" and inn != "ferdig" and inn != "k" and inn != "kjøp" and inn != "s" and inn != "selg":
                inn = input(inn + " er ikke en gyldig kommando, skriv 'k', 's' eller 'f'\n> ")
            if inn == "k" or inn == "kjøp":
                while inn != "f" and inn != "ferdig" and inn != "selg" and inn != "s":
                    inn = self.buy(inv)
            if inn == "s" or inn == "selg":
                while inn != "f" and inn != "ferdig" and inn != "k" and inn != "kjøp":
                    if inv.itemListe() != []:
                        try:
                            inn = self.selg(inv)
                        except IndexError:
                            print("Du har ikke så mange ting!")
                    else:
                        input("Du har ingenting å selge. Trykk enter for å gå til sortimentlisten\n> ")
                        inn = "k"
            if inn == "f" or inn == "ferdig":
                print(self._hadeTekst)

    def selg(self, inv):
        print("\n***************************************************************\n////                  Du har følgende ting:                \\\\\\\\")
        print("   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  ")
        inv.skriv_ut_alt()
        print("***************************************************************")
        print("\nDu har", inv.penger(), "gullstykker.")
        print("Skriv tallet ved siden av det du vil selge, 'alt' for å selge alt du ikke bruker,", \
        "\n'k' eller 'kjøp' for å gå til butikken, eller 'f' eller 'ferdig' for å gå tilbake.")
        inn = input("Hva vil du selge?\n> ").lower()

        if inn == "alt":
            svar = input("Skal dette inkludere ting man kan bruke opp?\n> ").lower()
            if svar == "ja" or svar == "j":
                for x in range(len(inv.itemListe())):
                    for item in inv.itemListe():
                        if not item.bruker():
                            inv.selg(inv.itemListe().index(item))
            elif svar == "n" or svar == "nei":
                for x in range(len(inv.itemListe())):
                    for item in inv.itemListe():
                        if not item.bruker() and item.wieldable():
                            inv.selg(inv.itemListe().index(item))
            else:
                return ""
            input("Du solgte alt du ikke bruker! Trykk enter for å fortsette\n> ")
            return ""

        if inn == "k" or inn == "kjøp":
            return "kjøp"

        if inn != "f" and inn != "ferdig":
            try:
                inn = int(inn)
                if inv.itemListe()[inn - 1].bruker():
                    sikker = input("Du bruker denne gjenstanden. Er du sikker på at du vil selge den? (j/n)\n> ")
                    if sikker != "j" and sikker != "ja":
                        return inn
                print("Du solgte", inv.itemListe()[inn - 1].navn().lower(), "for", inv.itemListe()[inn - 1].verdi(), "gullstykker.")
                inv.selg(inn - 1)
            except ValueError:
                print("\nSkriv tallet ved siden av det du vil selge, eller skriv 'f' eller 'ferdig' for å gå tilbake\n> ")
                input("Trykk enter for å gå tilbake\n> ")
        return inn

    #lar karakteren selge og kjøpe ting i butikken.
    def buy(self, inv):
        self.skriv_ut_sortiment(inv)
        print("Du har", inv.penger(), "gullstykker.")
        kommando = input("Hva vil du kjøpe?\n> ")

        if kommando == "i" or kommando == "inventar":
            inv.skriv_inv()
            input("Trykk enter for å gå tilbake til butikken\n> ")
            return ""
        if kommando == "b" or kommando == "bytt":
            kategorier()
            try:
                kategori = int(input("Hvilken kategori vil du bytte innenfor?\n> "))
                if kategori < 8 and kategori > 0:
                    x = inv.skriv_kategori(kategori)
                    if x != 1:
                        indeks = int(input("Hva vil du bytte til? Skriv nummeret til høyre\n> "))
                        item = inv.bytt_til(kategori, indeks)
                        input("Du har byttet til " + item.navn() + ". Trykk enter for å gå tilbake til butikken.\n> ")
                    else:
                        print("Du har ingen ting innenfor den kategorien.")
                        input("Trykk enter for å dra tilbake til butikken.\n> ")
                else:
                    print("Ugyldig kategori")
                    input("Trykk enter for å dra tilbake til butikken.\n> ")
            except ValueError:
                None
            except IndexError:
                print("Ugyldig kategori")
            return ""

        for vare in self._vareliste:
            if vare.kommando() == kommando:
                if inv.penger() >= vare.pris():
                    if inv.check_requirements(vare.item()):
                        inv.bytt(vare.item())
                        inv.penger(-vare.pris())
                        inv.legg_til_item(vare.item())
                        print("Du kjøpte", vare.navn(), "for", vare.pris(), "gullstykker.")
                        print("Du har nå", inv.penger(), "gullstykker igjen.")
                else:
                    print("Du har ikke råd!")
                input("Trykk enter for å dra tilbake til butikken.\n> ")

        return kommando

    #tar inn objekt som parameter
    def legg_til_vare(self, vare):
        self._vareliste.append(vare)

    def legg_til_hadeTekst(self, tekst):
        self._hadeTekst = tekst

class Vare:
    def __init__(self, item, pris, kommando):
        self._item = item
        self._pris = pris
        self._kommando = kommando
        self._buyText = "Hvor mange vil du ha?\n> "

    def pris(self):
        return self._pris

    def kommando(self):
        return self._kommando

    def navn(self):
        return self._item.navn()

    def item(self):
        return self._item

    def type(self):
        return item.type()

    def statliste(self):
        return item.statliste()

    def buyText(self):
        return self._buyText

    def skriv_vare(self, inv):
        stats = finn_stats(self._item)
        if len(stats) == 0:
            return ("{:45s} = {:4}g ({})".format(self._item.navn(), self._pris, self._kommando))
        elif len(stats) == 1:
            return ("{:27s}{:18s} = {:4}g ({})".format(self._item.navn(), stats[0], self._pris, self._kommando))
        elif len(stats) == 2:
            return ("{:27s}{:18s} = {:4}g ({})".format(self._item.navn(), "{}, {}".format(stats[0], stats[1]), self._pris, self._kommando))
        elif len(stats) == 3:
            return ("{:27s}{:18s} = {:4}g ({})".format(self._item.navn(), "{}, {}, {}".format(stats[0], stats[1], stats[2]), self._pris, self._kommando))
        elif len(stats) == 4:
            return ("{:27s}{:18s} = {:4}g ({})".format(self._item.navn(), "{}, {}, {}, {}".format(stats[0], stats[1], stats[2], stats[3]), self._pris, self._kommando))

    def legg_til_buyText(self, tekst):
        self._buyText = tekst

class Questlog:
    def __init__(self):
        self._quests = []

    def legg_til_quest(self, quest):
        self._quests.append(quest)

    def hent_qLog(self):
        return self._quests

    def hent_quest(self, indeks):
        return self._quests[indeks]

    #Skriver ut hvilke oppdrag man har tilgjengelige. Skriver ut dem man ikke enda kan gjøre
    #for å vise hvilken lvl som trengs for hvert enkelt. De uten noe nivå angitt kan ikke
    #startes, kun fullføres, og inkluderer å finne ting fra fienden tilfeldig. De
    #oppdragene man har fullført blir skjult.
    def oppdrag_tilgjengelige(self, lvl, sted):
        print("\n    Velkommen til", sted + "! Følgende personer ønsker å snakke med deg:")
        i = 0
        while i < len(self._quests):
            if not self._quests[i].ferdig() and self._quests[i].tilgjengelig() and not self._quests[i].bonus():
                print("    {:36} ({})".format("{} (nivå {})".format(self._quests[i].navn(), self._quests[i].lvl()), i+1))
            elif not self._quests[i].ferdig() and self._quests[i].tilgjengelig() and self._quests[i].bonus():
                print("    {:36} ({})".format(self._quests[i].navn(), i+1))
            i += 1

        #Sjekker om det er minst ett oppdrag tilgjengelig.
        ikkeFerdig = 0
        for q in self._quests:
            if q.ferdig() == False:
                ikkeFerdig += 1
        if ikkeFerdig == 0:
            print("Kjedelige Kjell vil diskutere tresorter. Du sniker deg unna.")
            return "f"
        else:
            print("\nDitt nåværende nivå er", lvl)
            return input("Skriv tallet til høyre for å høre hva de har å si. Skriv 'f' eller 'ferdig' for å gå ut\n> ")

    def snakk(self, indeks, spiller, inv):
        if indeks + 1 <= len(self._quests):
            if not self._quests[indeks].ferdig() and spiller.lvl() >= self._quests[indeks].lvl() \
            and self._quests[indeks].tilgjengelig() and not self._quests[indeks].bonus():
                if not self._quests[indeks].startet():
                    print(self._quests[indeks].deskripsjon())
                    svar = self._quests[indeks].svar()
                    if svar == "j" or svar == "ja":
                        self._quests[indeks].start()
                elif self._quests[indeks].startet() and not self._quests[indeks].sjekk_ferdig():
                    print(self._quests[indeks].deskripsjon())
                    for progresjon in self._quests[indeks].skriv_ut_progresjon():
                        print("   ", progresjon)
                    input("\nTrykk enter for å gå tilbake\n> ")
                elif self._quests[indeks].sjekk_ferdig():
                    self._quests[indeks].sett_ferdig()
                    print()
                    print(self._quests[indeks].ferdig_desk())
                    self._quests[indeks].reward(inv, spiller, self)
                    input("\nTrykk enter for å gå tilbake\n> ")

            elif not self._quests[indeks].ferdig() and spiller.lvl() >= self._quests[indeks].lvl() \
            and self._quests[indeks].tilgjengelig() and self._quests[indeks].bonus():
                if self._quests[indeks].sjekk_ferdig():
                    print(self._quests[indeks].deskripsjon())
                    print(self._quests[indeks].ferdig_desk())
                    svar = self._quests[indeks].svar()
                    if svar == "j" or svar == "ja":
                        self._quests[indeks].reward(inv, spiller, self)
                        self._quests[indeks].sett_ferdig()
                    input("\nTrykk enter for å gå tilbake\n> ")
                else:
                    print(self._quests[indeks].deskripsjon())
                    for progresjon in self._quests[indeks].skriv_ut_progresjon():
                        print("   ", progresjon)
                    input("\nTrykk enter for å gå tilbake\n> ")

            elif self._quests[indeks].lvl() > spiller.lvl() and self._quests[indeks].tilgjengelig():
                print("\nDu er ikke på høyt nok nivå til å snakke med",self._quests[indeks].navn())
                input("Trykk enter for å gå tilbake\n> ")

    def tell_startet(self):
        startet = 0
        for q in self._quests:
            if q.startet() and not q.ferdig():
                startet += 1
        return startet

    def skriv_ut(self, spiller):
        for q in self._quests:
            if q.startet() and not q.ferdig():
                print("\n" + q.navn(), "sitt oppdrag:")
                for progresjon in q.skriv_ut_progresjon():
                    print(progresjon)

class Quest:
    def __init__(self, desk, ferdigDesk, xProgresjon, lvl, navn, tilgjengelig=True, bonus=False, resetIfDead=False):
        self._deskripsjon = desk
        self._ferdigDesk = ferdigDesk
        self._progresjon = 0
        self._xProgresjon = xProgresjon
        self._lvl = lvl
        self._startet = False
        self._ferdig = False
        self._resetIfDead = resetIfDead
        self._reward = []
        self._tilgjengelig = tilgjengelig
        self._bonus = bonus
        self._giverNavn = navn
        self._ekstraTekst = ""
        self._svarTekst = "Vil du hjelpe meg?\n> "
        self._progresjonTekst = "Progresjon: "
        self._xProgresjonListe = []
        self._progresjonListe = []
        self._progresjonTekstListe = []

    def navn(self):
        return self._giverNavn

    def deskripsjon(self):
        return self._deskripsjon

    def ferdig_desk(self):
        return self._ferdigDesk

    def progresjon(self):
        return self._progresjon

    def xProgresjon(self):
        return self._xProgresjon

    def lvl(self):
        return self._lvl

    def startet(self):
        return self._startet

    def ferdig(self):
        return self._ferdig

    def bonus(self):
        return self._bonus

    def reset_if_dead(self):
        return self._resetIfDead

    def tilgjengelig(self):
        return self._tilgjengelig

    def svar(self):
        return input(self._svarTekst).lower()

    def skriv_ut_progresjon(self):
        if self._xProgresjonListe == []:
            return [str(self._progresjonTekst + str(self._progresjon) + "/" + str(self._xProgresjon))]

        else:
            i = 0
            liste = [str(self._progresjonTekst + str(self._progresjon) + "/" + str(self._xProgresjon))]
            while i<len(self._xProgresjonListe):
                liste.append(str(self._progresjonTekstListe[i] + str(self._progresjonListe[i]) + "/" + str(self._xProgresjonListe[i])))
                i += 1
            return liste

    def start(self):
        self._startet = True

    def sett_tilgjengelig(self, tilgjengelig=True):
        self._tilgjengelig = tilgjengelig

    def progresser(self, antall=1):
        self._progresjon += antall
        if self._progresjon > self._xProgresjon:
            self._progresjon = self._xProgresjon

    def sjekk_ferdig(self):
        if self._xProgresjonListe == []:
            if self._progresjon == self._xProgresjon:
                return True
            else:
                return False

        #Multiple quest objectives
        else:
            completed = 0
            i = 0
            while i<len(self._xProgresjonListe):
                if self._progresjonListe[i] == self._xProgresjonListe[i]:
                    completed += 1
                i += 1
            if completed == len(self._xProgresjonListe) and self._progresjon == self._xProgresjon:
                return True
            else:
                return False

    def sett_ferdig(self):
        self._ferdig = True

    def legg_til_progresjonTekst(self, tekst):
        self._progresjonTekst = tekst

    def legg_til_svarTekst(self, tekst):
        self._svarTekst = tekst

    def legg_til_reward(self, xp=0, gull=0, hp=0, kp=0, ekstraKp=0, a=0, \
    d=0, item=None, settTilgjengelig=False, settTilgjengeligIndeks=0):
        self._reward = [xp, gull, hp, kp, ekstraKp, a, d, item, settTilgjengelig, settTilgjengeligIndeks]

    def legg_til_ekstra_tekst(self, tekst):
        self._ekstraTekst = tekst

    def legg_til_progresjon(self, xProgresjon):
        self._xProgresjonListe.append(xProgresjon)
        self._progresjonListe.append(0)
        self._progresjonTekstListe.append("Progresjon: ")

    def legg_til_progresjonTekstListe(self, tekst, indeks):
        self._progresjonTekstListe[indeks] = tekst

    def progresser_liste(self, indeks):
        self._progresjonListe[indeks] += 1
        if self._progresjonListe[indeks] > self._xProgresjonListe[indeks]:
            self._progresjonListe[indeks] = self._xProgresjonListe[indeks]

    def reward(self, inv, spiller, qlog):
        print("Gratulerer!",spiller.navn(), "fullførte", self._giverNavn, "sitt oppdrag!\n")

        if self._ekstraTekst != "":
            print(self._ekstraTekst)

        #xp
        if self._reward[0] != 0:
            print(spiller.navn(), "får", self._reward[0], "erfaringspoeng!")
            spiller.gi_xp(self._reward[0])

        #gull
        if self._reward[1] != 0:
            print(spiller.navn(), "får", self._reward[1], "gullstykker!")
            inv.penger(self._reward[1])

        #hp
        if self._reward[2] != 0:
            print(spiller.navn(), "får", self._reward[2], "ekstra helsepoeng!")
            spiller.hev_hp(self._reward[2])

        #kp
        if self._reward[3] != 0:
            print(spiller.navn(), "får", self._reward[3], "ekstra konsentrasjonspoeng!")
            spiller.hev_kp(self._reward[3])

        #ekstra kp
        if self._reward[4] != 0:
            print(spiller.navn(), "får", self._reward[4], "ekstra konsentrasjonspoeng per runde!")
            spiller.hev_ekstraKp(self._reward[4])

        #a
        if self._reward[5] != 0:
            print(spiller.navn(), "får", self._reward[5], "ekstra angrepspoeng!")
            spiller.hev_a(self._reward[5])

        #a
        if self._reward[6] != 0:
            print(spiller.navn(), "får", self._reward[6], "ekstra defensivspoeng!")
            spiller.hev_d(self._reward[6])

        #item
        if self._reward[7]:
            item = self._reward[7]
            print(self._giverNavn + "s", item.navn().lower(), "gir deg følgende fordeler:")
            statliste = finn_stats(item)
            print(" ".join(statliste))

            gammelItem = inv.har_type(item.type())
            if gammelItem:
                statliste = finn_stats(gammelItem)
                print("\n" + spiller.navn() + "s nåværende", gammelItem.navn().lower(), "gir deg følgende fordeler:")
                print(" ".join(statliste))

            inn = input("\nVil du bruke den? (ja/nei)\n> ").lower()
            while inn != "ja" and inn != "nei" and inn != "j" and inn != "n":
                inn = input(inn + " er ikke en gyldig kommando. Skriv 'ja' eller 'nei'\n> ")
            if inn == "ja" or inn == "j":
                inv.legg_til_item(item, bruk=True)
            else:
                inv.legg_til_item(item)

        #sett tilgjengelig annet quest
        if self._reward[8]:
            quest = qlog.hent_quest(self._reward[9]).sett_tilgjengelig()

    def reset_progresjon(self):
        self._progresjon = 0

    def reset_progresjonListe(self, indeks):
        self._progresjonListe[indeks] = 0

class Spiller:
    #Oppretter alle variablene som trengs i klassen i konstruktøren.
    def __init__(self, navn):
        #hp = helsepoeng, kp xHp = max hp, kp = konsentrasjonspoeng (mana/energy)
        #a = angrep, d = defensiv, xp = erfaringspoeng (experience points), xXp = total xp
        self._navn = navn
        self._xHp = 100
        self._hp = 100
        self._kp = 60
        self._xKp = 60
        self._ekstraKp = 11
        self._a = 10
        self._d = 10
        self._xXp = 0
        self._xp = 0
        self._spesialisering = None
        self._sted = "tutorial"
        self._fuglelukt = False

        #Lager en liste som holder styr på hvor mye xp som trengs for neste lvl (nivå)
        #Listen begynner med 80 og øker med et tall som øker med et tall som øker med gjennomsnittlig 9.
        #Setter etterpå max lvl lik 70
        self._xpListe = [int(80 * x + (80 * (x - 1) / 10) * (x * x / 5 + x / 1.5)) for x in range(1, 71)]
        self._xpListe[69] = 100000000
        self._lvl = 1

        #Kart
        self._kartListe = [False for x in range(10)]

    #Denne metoden gir total a fra spilleren og brukes til å angripe fienden.
    def a(self):
        return self._a

    #Brukes når spilleren blir angrepet av fienden. a hentes fra fienden, og
    #brukeren kan på det meste blokkere en verdi av 1/4 av sin d.
    def angrepet(self, fiende):
        skade = randint(0, fiende.a())
        if fiende.weapon_dmg():
            skade = round(randint(0, fiende.a()) / 10) + fiende.weapon_dmg()
        skade -= int(randint(0, self._d) / 4)
        if skade <= 0:
            print(fiende.navn() + fiende.ending() + " bommet!")
        else:
            print(self._navn, "mistet", skade, "liv!")
            self._hp -= skade

    #både "du" og karakterens navn blir brukt i spillet.
    def navn(self):
        return self._navn

    #Returnerer lvl
    def lvl(self):
        return self._lvl

    #setter eller returnerer spesialiseringen
    def spesialisering(self, spesialisering=None):
        if spesialisering:
            self._spesialisering = spesialisering
        return self._spesialisering

    #gir brukeren informasjon om hvilke stats de har, samt lvl og xp til neste lvl.
    def stats(self):
        print(self._navn,"har følgende egenskaper:")
        print("Angrepspoeng:        ", self._a)
        print("Defensivpoeng:       ", self._d)
        print("Helsepoeng:           ", self._hp, "/", self._xHp, sep="")
        print("Konsentrasjonspoeng:  ", self._kp, "/", self._xKp, sep="")
        print("KP per runde:        ", self._ekstraKp)
        print("Erfaringspoeng:       ", self._xp, "/", self._xpListe[self._lvl - 1], sep="")
        print("Nivå:                ", self._lvl)

    #Etter hver runde i angrepsmodus regenererer karakteren et visst antall kp.
    #dette antallet kan også økes etter fullføring av bestemte quest.
    #Grunnøkningen er satt til 11 så det skal være vits i å ha f.eks en hatt som gir
    #+2 kp, ettersom alle spesialangrepene bare krever et rundt tall av kp.
    def kons(self):
        self._kp += self._ekstraKp
        if self._kp > self._xKp:
            self._kp = self._xKp

    #returnerer nåværende kp
    def kons_igjen(self):
        return self._kp

    #bruker kp. Brukes når karakteren utfører et spesialangrep
    def bruk_kons(self, k):
        self._kp -= k

    #restorerer opptil en gitt mengde hp
    def restorer(self, hp):
        self._hp += hp
        if self._hp > self._xHp:
            x = hp - (self._hp - self._xHp)
            self._hp = self._xHp
            return x
        else:
            return hp

    #restorerer opptil en gitt mengde kp
    def restorer_kp(self, kp):
        self._kp += kp
        if self._kp > self._xKp:
            x = kp - (self._kp - self._xKp)
            self._kp = self._xKp
            return x
        else:
            return kp

    #gir xp og setter mulighet for lvl up
    def gi_xp(self, xp):
        self._xp += xp
        self._xXp += xp

        #Del 1/2: lvl-up
        #Verdien til det første elementet i _xpListe er mengden xp som trengs for å
        #komme til lvl 2.
        while self._xp >= self._xpListe[self._lvl - 1]:
            self._xp -= self._xpListe[self._lvl - 1]
            self._lvl += 1
            print(self._navn, "har gått opp et nivå!", self._navn,"er nå nivå", self._lvl)

            #Dette skjer hver gang man når en ny lvl; max hp økes med 10+5*lvl,
            #kp økes med 10, a med 10 og d med 5.
            self._xHp += 10 + self._lvl * 5
            self._hp += 10 + self._lvl * 5

            self._xKp += 10
            self._kp += 10

            self._a += 10
            self._d += 5

            #Når man når lvl 3, 5 og 10 lærer karakteren et nytt spesialangrep.
            if self._lvl == 3:
                print(self._navn, "har lært et nytt trylletriks! Du kan nå bruke restituer! (r)")
            if self._lvl == 5:
                print(self._navn, "har lært et nytt trylletriks! Du kan nå bruke vind! (v)")
            if self._lvl == 10:
                print(self._navn, "har lært et nytt trylletriks! Du kan nå bruke super restorasjon! (sr)")
            if self._lvl == 17:
                print(self._navn, "har lært et nytt trylletriks! Du kan nå bruke utforsk! (u)")

        #Skulle man miste xp, kan man potensielt miste en lvl.
        while self._xp < 0:
            self._xp += self._xpListe[self._lvl - 2]

            self._xHp -= 10 + self._lvl * 5
            self._hp -= 10 + self._lvl * 5

            self._xKp -= 10
            self._kp -= 10

            self._a -= 10
            self._d -= 5

            self._lvl -= 1

    #angir om karakteren er død eller ikke.
    def dead(self):
        if self._hp <= 0:
            return True
        else:
            return False

    #Fjerner ting i inventory og setter starterstatsene til å være lavere enn vanlig.
    def die(self, inv):
        inv.reset()
        self._hp = int(self._xHp/3)
        self._kp = int(self._xKp/4)
        self._fuglelukt = True

    #egen metode for å skrive ut nåværende nivå og hvor mye xp som trengs for neste lvl.
    def xp(self):
        print(self._navn, "er på nivå", self._lvl)
        print(self._navn, " har ", self._xp, "/", self._xpListe[self._lvl - 1], " erfaringspoeng.", sep="")

    #returnerer total xp (xXp)
    def total_xp(self):
        return self._xXp

    #Skriver ut karakterens hp/xHp og kp/xKp. Dette skjer hver runde så brukeren
    #alltid er oppdatert på hvor mange hp og kp som gjenstår. Dette er det nærmeste
    #jeg kommer en "health bar" / "energy bar" med terminal-grafikk.
    def skriv_ut(self):
        print(self._navn, " HP: ", self._hp, "/", self._xHp, ", KP: ", self._kp, "/", self._xKp, sep="")

    #Hever max hp
    def hev_hp(self, hp):
        self._xHp += hp
        self._hp += hp

    #Hever max kp
    def hev_kp(self, kp):
        self._xKp += kp
        self._kp += kp

    #Hever a
    def hev_a(self, a):
        self._a += a

    #Hever d
    def hev_d(self, d):
        self._d += d

    #Hever antall ekstra kp man får hver runde.
    def hev_ekstraKp(self, kp):
        self._ekstraKp += kp

    #bytter statsene en item gir. Tar minus de gamle statsene, gitt i gListe, og
    #plusser på de nye statsene, gitt i nListe.
    def bytt_stats(self, gListe, nListe):
        self._a   -= gListe[0]
        self._xKp -= gListe[1]
        self._kp  -= gListe[1]
        self._xHp -= gListe[2]
        self._hp  -= gListe[2]
        self._d   -= gListe[3]
        self._ekstraKp -= gListe[4]
        self._a   += nListe[0]
        self._xKp += nListe[1]
        self._kp  += nListe[1]
        self._xHp += nListe[2]
        self._hp  += nListe[2]
        self._d   += nListe[3]
        self._ekstraKp += nListe[4]

    def fuglelukt(self):
        return self._fuglelukt

    def kart(self):
        return self._kartListe

    def sett_sted_tilgjengelig(self, indeks):
        self._kartListe[indeks] = True

    def hentSted(self):
        return self._sted

    def byttSted(self, plass):
        self._sted = plass

class Loot:
    def __init__(self):
        self._loot = []
        self._droprates = []
        self._totalDroprate = 0

    def legg_til_item(self, item, droprate):
        self._loot.append(item)
        self._droprates.append(self._totalDroprate + droprate)
        self._totalDroprate += droprate

    def hent_loot(self):
        tall = randint(1, self._totalDroprate)
        for x in range(len(self._droprates)):
            if tall <= self._droprates[x]:
                return self._loot[x]

class Fiende:
    #Samme prinsipp i konstruktøren som spiller-klassen, men færre variabler og
    #flere parametre. Merk at _xp-variabelen angir hvor mye karakteren får av xp
    #for å drepe fienden. Fienden har ingen lvl som referansepunkt, kun hp, a og d.
    def __init__(self, navn, race, loot, hp, a, d, kp=0, bonusKp=0, weapon=0, ending=""):
        self._navn = navn
        self._race = race
        self._xHp = hp
        self._hp = hp
        self._a = a
        self._d = d
        self._xKp = kp
        self._kp = kp
        self._bonusKp = bonusKp
        self._weaponDmg = weapon
        self._xp = round((self._xHp + self._a + self._d + self._kp + self._bonusKp * 10) / 1.2)
        self._ending = ending
        self._loot = loot

        #skill-relaterte variabler
        self._untouchable = False
        self._untouchableCD = 0

    def navn(self):
        return self._navn

    def ending(self):
        return self._ending

    def weapon_dmg(self):
        return self._weaponDmg

    def return_loot(self):
        return self._loot

    def race(self):
        return self._race

    def hp(self):
        return self._hp

    def xHp(self):
        return self._xHp

    #returnerer fiendens a. Brukes når fienden skal angripe.
    def a(self, a=0):
        self._a += a
        return self._a

    #returnerer fiendens kp. Brukes til spells
    def kp(self, kp=0):
        self._kp += kp
        return self._kp

    def d(self, d=0):
        self._d += d
        return self._d

    def bonusKp(self, bKp=0):
        self._bonusKp += bKp
        return self._bonusKp

    #returnerer fiendens xp. Brukes når fienden er død.
    def xp(self):
        return self._xp

    #returnerer untouchable.
    def untouchable(self):
        return self._untouchable

    #returnerer aktiveringstiden eller cooldown til untouchable
    def untouchableCD(self):
        return self._untouchableCD

    #Tar inn True og cooldown når untouchable skal aktiveres eller deaktiveres.
    def set_untouchable(self, u, uCD):
        self._untouchable = u
        self._untouchableCD = uCD

    #Tar imot skade gjort av spilleren som parameter. Parameteret er altså max
    #skade som kan bli gjort, men hvor mye som faktisk blir gjort avhenger av randint
    #og fiendens d.
    def angrepet(self, a=0, sverdA=0):
        skade = randint(0, a)
        if sverdA:
            skade = round(randint(0, a) / 10) + sverdA
        skade -= int(randint(0, self._d) / 4)
        if skade <= 0:
            print("Du bommet!")
            return 0
        else:
            if skade > self._hp:
                skade = self._hp
            print(self._navn, "mistet", skade, "liv!")
            self._hp -= skade
            return skade

    #Skriver ut hvor mye skade fienden tar.
    def mist_liv(self, skade):
        if self._hp < skade:
            skade = self._hp
        print(self._navn, "mistet", skade, "liv.")
        self._hp -= skade
        return skade

    def restorer(self, hp):
        self._hp += hp
        if self._hp > self._xHp:
            x = hp - (self._hp - self._xHp)
            self._hp = self._xHp
            return x
        else:
            return hp

    #Angir om fienden er død.
    def dead(self):
        if self._hp <= 0:
            return True
        else:
            return False

    #Skriver ut fiendens stats. Gjøres hver runde samtidig som karakterens stats skrives ut.
    def skriv_ut(self):
        if self._xKp == 0:
            print(self._navn, " HP: ", self._hp, "/", self._xHp, sep="")
        else:
            print(self._navn, " HP: ", self._hp, "/", self._xHp, ", KP: ", self._kp, "/", self._xKp, sep="")

    #bruker en gitt mengde kp.
    def bruk_kons(self, mengde):
        self._kp -= mengde

    #genererer kp etter hver runde. Oppdaterer også cooldown for untouchable.
    def gen_kons(self):
        self._kp += 5 + self._bonusKp
        if self._kp > self._xKp:
            self._kp = self._xKp

        if self._untouchableCD > 0:
            self._untouchableCD -= 1
        elif self._untouchableCD < 0:
            self._untouchableCD += 1
        elif self._untouchableCD == 0:
            self._untouchable = False

    def loot(self, spiller, inv):
        item = self._loot.hent_loot()
        try:
            tekst = spiller.navn() + " fant " + item.loot_tekst() + " på " + self._navn + self._ending
            if item.wieldable():
                tekst += "! Den gir deg følgende fordeler:"
                for _ in finn_stats(item):
                    tekst += " " + _ + ","
            print(tekst.strip(",") + ".")

            if item.wieldable():
                gammelItem = inv.har_type(item.type())
                if gammelItem:
                    tekst = "Din nåværende " + gammelItem.navn().lower() + " gir deg følgende fordeler:"
                    for _ in finn_stats(gammelItem):
                        tekst += " " + _ + ","
                    print(tekst.strip(",") + ".")

                inn = input("Vil du bruke den? (ja/nei)\n> ").lower()
                while inn != "ja" and inn != "nei" and inn != "j" and inn != "n":
                    inn = input(inn + " er ikke en gyldig kommando. Skriv 'ja' eller 'nei'\n> ")
                if inn == "ja" or inn == "j":
                    inv.legg_til_item(item, bruk=True)
                else:
                    inv.legg_til_item(item)
            else:
                inv.legg_til_item(item)

        except AttributeError:
            print(spiller.navn(), "fant", item, "gullstykker på", self._navn + self._ending + "!")
            inv.penger(item)

class Spellbook:
    def __init__(self, klasser, spiller, inv):
        self._klasser = klasser
        self._spiller = spiller
        self._inv = inv

        self._utforsk = False
        self._utforskRunder = 0

    def skriv_spellbook(self):
        print("Her er følgende angrep du kan bruke:")
        print("angrep (eller a)         angriper vanlig")
        print("tryllepulver (eller t)   kaster tryllepulver på fienden (100 skade)")
        if self._spiller.lvl() >= 3:
            print("restituer (eller r)      gir deg 40 helsepoeng\n\
                         Krever 50 konsentrasjonspoeng, tryllestav og nivå gir ekstra effekt.")
        if self._spiller.lvl() >= 5:
            print("vind (eller v)           tryller frem et kraftig vindkast (150+ skade)\n\
                         krever tryllestav og 100 konsentrasjonspoeng")
        if self._spiller.lvl() >= 10:
            print("super restituer (sr)     gir deg 220 helsepoeng\n\
                         Krever 100 konsentrasjonspoeng, tryllestav og nivå gir ekstra effekt.")
        if self._spiller.lvl() >= 17:
            print("utforsk (u)              de neste 5 vanlige angrepene stjeler liv.\n\
                         Krever 195 konsentrasjonspoeng.")

        gnomeqlog = self._klasser.questlog(1)
        gargyllog = self._klasser.questlog(4)
        #Disse spesialangrepet krever å ha fullført et bestemt quest.
        if gnomeqlog.hent_quest(4).ferdig():
            print("konsentrer energi (ke)   stjeler 300 helsepoeng\n\
                         Krever 150 konsentrasjonspoeng, tryllestav gir ekstra effekt.")
        if gargyllog.hent_quest(4).ferdig():
            print("kjøttifiser (kj)         gjør forsteinede fiender om til kjøtt\n\
                         Krever 100 konsentrasjonspoeng.")

    def tryllepulver(self, fiende):
        harPulver = None
        for o in self._inv.itemListe():
            if o.navn() == "Tryllepulver":
                harPulver = o
        if harPulver:
            self._inv.bruk_item(harPulver)
            print(self._spiller.navn(), "kastet tryllepulver!")
            if not fiende.untouchable():
                fiende.mist_liv(100)
            else:
                fiende.mist_liv(0)
            return False
        else:
            print("Du har ikke mer tryllepulver igjen!")
            return True

    def konsentrasjonspulver(self):
        tempListe = []
        for o in self._inv.itemListe():
            if o.navn() == "Konsentrasjonspulver":
                tempListe.append(o)
        if tempListe != []:
            print("Dine mengder med konsentrasjonspulver gir følgende virkning:")
            for d in tempListe:
                print("{:7} {:>4}kp".format(str(int(tempListe.index(d) + 1)) + ".", d.kp()))
            indeks = input("Hvilken vil du sniffe? (skriv nummeret)\n> ")
            try:
                kp = self._spiller.restorer_kp(tempListe[int(indeks) - 1].kp())
                self._inv.bruk_item(tempListe[int(indeks) - 1])
                print(self._spiller.navn(), "sniffet en stripe konsentrasjonspulver!")
                print(self._spiller.navn(), "restorerte", kp, "konsentrasjonspoeng.")
                return False
            except ValueError:
                print("Du må skrive et tall!")
                return True
            except IndexError:
                print("Du har ikke så mange striper konsentrasjonspulver!")
                return True
        else:
            print("Du har ikke mer konsentrasjonspulver!")
        return True

    def trolldrikk(self):
        tempListe = []
        for o in self._inv.itemListe():
            if o.navn() == "Trolldrikk":
                tempListe.append(o)
        if tempListe != []:
            print("Du har følgende trolldrikker:")
            for d in tempListe:
                print("{:7} {:>4}hp".format(str(int(tempListe.index(d) + 1)) + ".", d.hp()))
            indeks = input("Hvilken vil du drikke? (skriv nummeret)\n> ")
            try:
                hp = self._spiller.restorer(tempListe[int(indeks) - 1].hp())
                self._inv.bruk_item(tempListe[int(indeks) - 1])
                print(self._spiller.navn(), "drakk en flaske trolldrikk!")
                print(self._spiller.navn(), "restorerte", hp, "helsepoeng.")
                return False
            except ValueError:
                print("Du må skrive et tall!")
                return True
            except IndexError:
                print("Du har ikke så mange trolldrikker!")
                return True
        else:
            print("Du har ikke flere flasker med trolldrikke!")
            return True

    def restituer(self):
        if self._spiller.lvl() >= 3 and self._spiller.kons_igjen() >= 50:
            self._spiller.bruk_kons(50)
            r = self._spiller.restorer(40 + self._spiller.lvl() * 4 + self._inv.hent_weaponKp())
            print("Du kastet Restituer!")
            print(self._spiller.navn(), "restorerte", r, "helsepoeng")
            qlog = self._klasser.questlog(1)

            #oppdaterer quest-variabel om quest er aktivt.
            if qlog.hent_quest(1).startet() and not qlog.hent_quest(1).ferdig():
                qlog.hent_quest(1).progresser(r)

            return False

        #ikke nok kp
        elif self._spiller.lvl() >= 3:
            print("Du har ikke nok konsentrasjonspoeng!")
        return True

    def vind(self, fiende):
        if self._spiller.lvl() >= 5 and self._spiller.kons_igjen() >= 100 and self._inv.har_type("weapon"):
            if not self._inv.har_type("weapon").blade():
                self._spiller.bruk_kons(100)

                #etter fullførelse av quest tar dette angrepet 150 ekstra liv.
                qlog = self._klasser.questlog(1)
                print(self._spiller.navn(), "kastet Vindkast!")
                if fiende.untouchable():
                    fiende.mist_liv(0)
                else:
                    if qlog.hent_quest(3).ferdig():
                        fiende.mist_liv(round(self._inv.hent_weaponA() * 1.5) + 300)
                    else:
                        fiende.mist_liv(round(self._inv.hent_weaponA() * 1.5) + 150)

                #oppdaterer quest-variabel
                if qlog.hent_quest(3).startet() and not qlog.hent_quest(3).ferdig():
                    qlog.hent_quest(3).progresser()
                return False

            else:
                print("Du trenger en tryllestav!")

        #man trenger en tryllestav for å bruke dette angrepet.
        elif self._spiller.lvl() >= 5 and not self._inv.har_type("weapon"):
            print("Du trenger en tryllestav!")

        #ikke nok kp
        elif self._spiller.lvl() >= 5 and self._spiller.kons_igjen() < 100:
            print("Du har ikke nok konsentrasjonspoeng!")

        return True

    def super_restituer(self):
        if self._spiller.lvl() >= 10 and self._spiller.kons_igjen() >= 100 and self._inv.har_type("weapon"):
            if not self._inv.har_type("weapon").blade():
                self._spiller.bruk_kons(100)
                r = self._spiller.restorer(140 + self._spiller.lvl() * 8 + self._inv.hent_weaponKp())
                print("Du kastet super restituer!")
                print(self._spiller.navn(), "restituerte", r, "helsepoeng.")

                #oppdaterer quest-variabel
                qlog = self._klasser.questlog(1)
                if qlog.hent_quest(1).startet() and not qlog.hent_quest(1).ferdig():
                    qlog.hent_quest(1).progresser(r)
                if qlog.hent_quest(4).startet() and not qlog.hent_quest(4).ferdig():
                    qlog.hent_quest(4).progresser()
                return False

            else:
                print("Du trenger en tryllestav!")

        #krever tryllestav
        elif self._spiller.lvl() >= 10 and not self._inv.har_type("weapon"):
            print("Du trenger en tryllestav!")

        #Ikke nok kp
        elif self._spiller.lvl() >= 10 and self._spiller.kons_igjen() < 100:
            print("Du har ikke nok konsentrasjonspoeng!")
        return True

    def konsentrer_energi(self, fiende):
        qlog = self._klasser.questlog(1)
        if qlog.hent_quest(4).ferdig():
            if self._spiller.kons_igjen() >= 150:
                self._spiller.bruk_kons(150)
                print(self._spiller.navn(), "kastet Konsentrer Energi!")
                if fiende.untouchable():
                    skadeGjort = fiende.mist_liv(0)
                else:
                    skadeGjort = fiende.mist_liv(300 + self._inv.hent_weaponA() + self._inv.hent_weaponKp())
                print(self._spiller.navn(), "fikk", self._spiller.restorer(skadeGjort), "liv.")
                return False
            else:
                print("Du har ikke nok konsentrasjonspoeng!")
                return True
        return True

    def meatify(self, fiende):
        qlog = self._klasser.questlog(4)
        if qlog.hent_quest(4).ferdig():
            if self._spiller.kons_igjen() >= 100 and fiende.race() == "gargyl":
                self._spiller.bruk_kons(100)
                print(self._spiller.navn(), "kastet Kjøttifiser!")
                if fiende.untouchable():
                    print(fiende.navn() + fiende.ending(), "er tvunget tilbake til sin kjøttlige form!")
                    fiende.set_untouchable(False, -2)
                else:
                    print(fiende.navn() + fiende.ending(), "vil være i sin kjøttlige form en stund til!")
                    fiende.set_untouchable(False, -6)
                return False

            elif self._spiller.kons_igjen() >= 100 and fiende.navn() == "Stein":
                self._spiller.bruk_kons(100)
                print(self._spiller.navn(), "kastet Kjøttifiser!")
                print("Du gjorde steinen om til en velsmakende kjøttbolle.")
                fiende.mist_liv(1000000)
                print(self._spiller.navn(), "fikk", self._spiller.restorer(300), "liv.")
                return False

            elif self._spiller.kons_igjen() >= 100:
                print("Denne fienden er ikke forsteinet.")
            else:
                print("Du har ikke nok konsentrasjonspoeng!")
        return True

    def brukUtforsk(self):
        if self._spiller.lvl() >= 17 and self._spiller.kons_igjen() >= 195 and self._inv.har_type("weapon"):
            if self._inv.har_type("weapon").blade():
                self._spiller.bruk_kons(195)
                print(self._spiller.navn(), "kastet Utforsk!")
                self._utforsk = True
                self._utforskRunder = 5
                return False
            else:
                print("Du trenger et sverd!")
        elif self._spiller.lvl() >= 17 and self._spiller.kons_igjen() >= 195:
            print("Du trenger et sverd!")
        elif self._spiller.lvl() >= 17:
            print("Du har ikke nok konsentrasjonspoeng!")
        return True

    def utforsk(self):
        utforsk = False
        if self._utforsk:
            self._utforskRunder -= 1
            utforsk = True
        if self._utforskRunder == 0:
            self._utforsk = False
        return utforsk

class Inventory:
    def __init__(self, spiller, klasser):
        self._spiller = spiller
        self._klasser = klasser
        self._penger = 100

        #Item-lister
        self._items = []
        self._weapons = []
        self._hats = []
        self._gloves = []
        self._robes = []
        self._shoes = []
        self._beards = []
        self._trinkets = []
        self._restoring = []
        self._damaging = []
        self._various = []
        self._categoryList = [self._weapons, self._hats, self._gloves, self._robes\
        , self._shoes, self._beards, self._trinkets, self._various, self._restoring, self._damaging]
        self._wieldable = [self._categoryList[x] for x in range(7)]

    def penger(self, antall=0):
        self._penger += antall
        return self._penger

    def itemListe(self):
        return self._items

    def legg_til_item(self, item, bruk=False):
        if bruk:
            self.bytt(item)
            item.bruker(True)

        self._items.append(item)

        if item.type() == "restoring":
            self._restoring.append(item)
        if item.type() == "damaging":
            self._damaging.append(item)
        if item.type() == "weapon":
            self._weapons.append(item)
        if item.type() == "hat":
            self._hats.append(item)
        if item.type() == "gloves":
            self._gloves.append(item)
        if item.type() == "robe":
            self._robes.append(item)
        if item.type() == "shoes":
            self._shoes.append(item)
        if item.type() == "beard":
            self._beards.append(item)
        if item.type() == "trinket":
            self._trinkets.append(item)
        if item.type() == "various":
            self._various.append(item)

    def bruk_item(self, item):
        if self.check_requirements(item):
            for x in self._items:
                if x == item:
                    self._items.pop(self._items.index(item))
            for category in self._categoryList:
                for i in category:
                    if i == item:
                        category.pop(category.index(item))

    def bytt(self, item):
        if self.check_requirements(item):
            #Lager tom statliste
            gammelStatliste = [0 for x in range(len(item.statliste()))]

            #Finner gamle stats
            for objekt in self._items:
                if objekt.type() == item.type() and objekt.bruker():
                    gammelStatliste = objekt.statliste()
                    objekt.ikke_bruk()

            #Bytter stats
            self._spiller.bytt_stats(gammelStatliste, item.statliste())
            item.bruker(True)

    def bytt_til(self, kategori, i):
        item = self._categoryList[kategori - 1][i - 1]
        if item.bruker():
            item = Item("ingenting", item.type())
        self.bytt(item)

        return item

    def check_requirements(self, item):
        ok = True
        lvl = False
        spes = False
        tekst = item.navn() + " krever "

        if item.lvl() and item.lvl() > self._spiller.lvl():
            print(self._spiller.navn(), "er ikke på høyt nok nivå for å bruke", item.navn() + "!")
            ok = False
            lvl = True
        if item.spesialisering() and self._spiller.spesialisering() != item.spesialisering():
            print(self._spiller.navn(), "har ikke riktig spesialisering for å bruke", item.navn() + "!")
            ok = False
            spes = True

        if not ok:
            if lvl and not spes:
                tekst += "nivå " + str(item.lvl()) + "."
            elif not lvl and spes:
                tekst += "spesialiseringen " + item.spesialisering() + "."
            elif lvl and spes:
                tekst += "nivå " + str(item.lvl()) + ", og spesialiseringen " + item.spesialisering() + "."
            print(tekst)

        return ok

    def har_type(self, typeObjekt):
        for item in self._items:
            if item.type() == typeObjekt:
                if item.bruker():
                    return item
        return None

    def hent_statliste(self, typeObjekt):
        liste = [0, 0, 0, 0, 0, 0, 0, 0]
        for item in self._items:
            if item.type() == typeObjekt:
                if item.bruker():
                    liste = item.statliste()
        return liste

    def selg(self, i):
        itemInQuestion = self._items[i]
        self._penger += self._items.pop(i).verdi()
        if itemInQuestion.bruker():
            self._spiller.bytt_stats(itemInQuestion.statliste(), [0 for x in range(8)])
        for category in self._categoryList:
            for item in category:
                if itemInQuestion == item:
                    category.pop(category.index(item))

    def skriv_kategori(self, kategori):
        x = self.skriv_ut_alt(self._categoryList[kategori - 1])
        return x

    def hent_weaponA(self):
        for weapon in self._weapons:
            if weapon.bruker():
                return weapon.statliste()[0]
        return 0

    def hent_weaponKp(self):
        for weapon in self._weapons:
            if weapon.bruker():
                return weapon.statliste()[3]
        return 0

    def skriv_ut_alt(self, itemListe="default"):
        if itemListe == "default":
            itemListe = self._items
        if len(itemListe) == 0:
            return 1
        else:
            x = 0
            for item in itemListe:
                x += 1

                statliste = finn_stats(item)

                if len(statliste) == 0:
                    if item.bruker():
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn() + " **bruker**", "{} ".format(""), item.verdi(), x))
                    else:
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn(), "{} ".format(""), item.verdi(), x))
                elif len(statliste) == 1:
                    if item.bruker():
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn() + " **bruker**", "{} {}".format("", statliste[0]), item.verdi(), x))
                    else:
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn(), "{} {}".format("", statliste[0]), item.verdi(), x))
                elif len(statliste) == 2:
                    if item.bruker():
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn() + " **bruker**", "{} {}, {}".format("", statliste[0], statliste[1]), item.verdi(), x))
                    else:
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn(), "{} {}, {}".format("", statliste[0], statliste[1]), item.verdi(), x))
                elif len(statliste) == 3:
                    if item.bruker():
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn() + " **bruker**", "{} {}, {}, {}".format("", statliste[0], statliste[1], statliste[2]), item.verdi(), x))
                    else:
                        print("{:28s}{:25} {:>4}g ({})".format(item.navn(), "{} {}, {}, {}".format("", statliste[0], statliste[1], statliste[2]), item.verdi(), x))
                elif len(statliste) == 4:
                    if item.bruker():
                        print("{:28s}{:30} {:>4}g ({})".format(item.navn() + " **bruker**", "{} {}, {}, {}, {}".format("", statliste[0], statliste[1], statliste[2], statliste[3]), item.verdi(), x))
                    else:
                        print("{:28s}{:30} {:>4}g ({})".format(item.navn(), "{} {}, {}, {}, {}".format("", statliste[0], statliste[1], statliste[2], statliste[3]), item.verdi(), x))
            return 0

    def skriv_inv(self):
        kp = 0
        td = 0
        tp = 0
        for x in self._items:
            if x.navn() == "Konsentrasjonspulver":
                kp += 1
            if x.navn() == "Trolldrikk":
                td += 1
            if x.navn() == "Tryllepulver":
                tp += 1

        print("Du har", self._penger, "gullstykker.")
        if tp != 0:
            print("Du har", tp, "håndfuller med tryllepulver.")
        if td != 0:
            print("Du har", td, "flasker med trolldrikke.")
        if kp != 0:
            print("Du har", kp, "striper med konsentrasjonspulver.")
        if len(self._weapons) == 1:
            print("Du har et våpen.")
        elif self._weapons != []:
            print("Du har", len(self._weapons), "våpen. ('b' for å bytte)")
        if len(self._hats) == 1:
            print("Du har en hatt")
        elif self._hats != []:
            print("Du har", len(self._hats), "hatter. ('b' for å bytte)")
        if len(self._gloves) == 1:
            print("Du har et par med hansker.")
        elif self._gloves != []:
            print("Du har", len(self._gloves), "par hansker. ('b' for å bytte)")
        if len(self._robes) == 1:
            print("Du har et sett med klær.")
        elif self._robes != []:
            print("Du har", len(self._robes), "sett med klær. ('b' for å bytte)")
        if len(self._shoes) == 1:
            print("Du har et par sko.")
        elif self._shoes != []:
            print("Du har", len(self._shoes), "par sko. ('b' for å bytte)")
        if len(self._beards) == 1:
            print("Du har et falskt skjegg.")
        elif self._beards != []:
            print("Du har", len(self._beards), "stk falske skjegg. ('b' for å bytte)")
        if len(self._trinkets) == 1:
            print("Du har en duppedings.")
        elif self._trinkets != []:
            print("Du har", len(self._trinkets), "duppedingser. ('b' for å bytte)")

        for ting in self._various:
            print("Du har en", ting.navn())

        #Gnom
        qListeGnom = self._klasser.questlog(1).hent_qLog()
        if not qListeGnom[2].ferdig() and qListeGnom[2].progresjon() != 0:
            print("Du har", qListeGnom[2].progresjon(), "sminkeartikler.")
        if not qListeGnom[6].ferdig() and qListeGnom[6].progresjon() != 0:
            print("Du har en magisk sopp.")
        if not qListeGnom[7].ferdig() and qListeGnom[7].progresjon() != 0:
            print("Du har en magisk trylleformel for å rette oppgaver.")

        #Gargyl
        qListeGargyl = self._klasser.questlog(4).hent_qLog()
        if not qListeGargyl[4].ferdig() and qListeGargyl[4].progresjon() != 0:
            print("Du har", qListeGargyl[4].progresjon(), "steiner.")
        if not qListeGargyl[6].ferdig() and qListeGargyl[6].progresjon() != 0:
            print("Du har en levende kosebamse.")

    #Resetter inventory til å inneholde ingenting
    def reset(self):
        for x in range(len(self._items)):
            self.selg(0)
        self._penger = 3

class Item:
    def __init__(self, navn, typeObjekt, a=0, d=0, hp=0, kp=0, xHp=0, xKp=0, \
    ekstraKp=0, dmg=0, bruk=False, spesialisering=None, lvl=0, blade=False):
        self._navn = navn
        self._type = typeObjekt
        self._blade = blade
        self._a = a
        self._d = d
        self._hp = hp
        self._xHp = xHp
        self._kp = kp
        self._xKp = xKp
        self._ekstraKp = ekstraKp
        self._dmg = dmg
        self._statliste = [self._a, self._xKp, self._xHp, self._d, self._ekstraKp, self._dmg, self._hp, self._kp]
        self._statlisteTekst = ["a", "kp", "hp", "d", "ekstra kp", "skade", "+hp", "+kp"]
        self._bruker = bruk
        self._wieldable = False
        self._spesialisering = spesialisering
        self._lvl = lvl
        self._verdi = ( a + d + xHp + xKp + ekstraKp * 30 + int(hp/10) + int(kp/5) + int(dmg*0.05) ) * 8
        self._lootTekst = "en " + self._navn.lower()
        if self._type == "weapon" or self._type == "hat" or self._type == "gloves" \
        or self._type == "robe" or self._type == "shoes" or self._type == "beard" or self._type == "trinket":
            self._wieldable = True

    def navn(self):
        return self._navn

    def type(self):
        return self._type

    def wieldable(self):
        return self._wieldable

    def blade(self):
        return self._blade

    def spesialisering(self):
        return self._spesialisering

    def lvl(self):
        return self._lvl

    def statliste(self):
        return self._statliste

    def statlisteTekst(self):
        return self._statlisteTekst

    def hp(self):
        return self._hp

    def kp(self):
        return self._kp

    def verdi(self):
        return self._verdi

    def loot_tekst(self):
        return self._lootTekst

    def bruker(self, skalBruke=False):
        if skalBruke:
            self._bruker = True
        return self._bruker

    def ikke_bruk(self):
        self._bruker = False

    def sett_verdi(self, verdi):
        self._verdi = verdi

    def sett_loot_tekst(self, tekst):
        self._lootTekst = tekst

class Klasser:
    def __init__(self):
        self._butikker = []
        self._questlogs = []

    def butikk(self, indeks):
        return self._butikker[indeks]

    def alle_butikker(self):
        return self._butikker

    def questlog(self, indeks):
        return self._questlogs[indeks]

    def alle_questlogger(self):
        return self._questlogs

    def legg_til_butikk(self, butikk):
        self._butikker.append(butikk)

    def legg_til_questlog(self, qlog):
        self._questlogs.append(qlog)
