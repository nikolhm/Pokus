from random import randint
from colorama import *
import os
import time
import platform
import sys

init()
gray = Fore.BLACK + Style.BRIGHT
red = Fore.RED + Style.DIM
green = Fore.GREEN + Style.NORMAL
brown = Fore.YELLOW + Style.DIM
white = Fore.WHITE + Style.NORMAL
yellow = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.NORMAL
magenta = Fore.MAGENTA + Style.NORMAL
cyan = Fore.CYAN + Style.NORMAL
reset = Style.RESET_ALL

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def hentFargetGrafikk(tekst, farger):
    return tekst.format(*farger, reset)

def hentGrafikk(path, *farger):
    try:
        with open('rec/grafikk/{}.txt'.format(path)) as g:
            grafikk = g.read()
            if len(farger) > 0:
                return hentFargetGrafikk(grafikk, farger)
            else:
                return grafikk
    except FileNotFoundError:
        print('ASCII art at {} not found'.format(path))

def skrivTittel():
    frames = [hentGrafikk('tittel/tittel_start')]
    ferdig = hentGrafikk('tittel/tittel_slutt')

    # TODO: Erstatt med standardisert fargemetode
    """
    # Farge
    ferdig = list(ferdig)
    f1 = list(frames[0])
    indeks = 0
    while indeks < len(ferdig):
        if (ferdig[indeks] == "P") and (ferdig[indeks + 1] != "r"):
            ferdig.insert(indeks, Fore.RED)
            f1.insert(indeks, Fore.RED)
            indeks += 1

        if ferdig[indeks] == "O":
            ferdig.insert(indeks, Fore.YELLOW)
            f1.insert(indeks, Fore.YELLOW)
            indeks += 1

        if ferdig[indeks] == "K":
            ferdig.insert(indeks, Fore.BLUE)
            f1.insert(indeks, Fore.BLUE)
            indeks += 1

        if (ferdig[indeks] == "U") or (ferdig[indeks] == "D" and (ferdig[indeks - 1] == ":" or ferdig[indeks + 1] == ":")):
            ferdig.insert(indeks, Fore.GREEN)
            f1.insert(indeks, Fore.GREEN)
            indeks += 1

        if ferdig[indeks] == "S":
            ferdig.insert(indeks, Fore.MAGENTA)
            f1.insert(indeks, Fore.MAGENTA)
            indeks += 1

        if ferdig[indeks] == " ":
            ferdig.insert(indeks, Fore.WHITE)
            f1.insert(indeks, Fore.WHITE)
            indeks += 1

        if ferdig[indeks] == "*":
            ferdig.insert(indeks, Fore.WHITE)
            f1.insert(indeks, Fore.WHITE)
            indeks += 1

        indeks += 1

    print(ferdig)

    ferdig = "".join(ferdig)
    frames[0] = "".join(f1)

    ferdig += Style.RESET_ALL
    """
    # Animasjon
    if platform.system() == "Windows":
        ccom = "cls"
    else:
        ccom = "clear"
    os.system(ccom)
    pokusB = list("POKUS:")
    pokusListe = list(frames[0])

    for b in pokusB:
        for x in range(len(ferdig)):
            if ferdig[x] == b:
                if ferdig[x + 1] != "r":
                    pokusListe[x] = b
            if b == "U" and ferdig[x] == "D":
                pokusListe[x] = "D"
        frames.append("".join(pokusListe))
    frames.append(ferdig)

    for f in frames:
        sys.stdout.flush()
        print(f)
        time.sleep(1/12)
        os.system(ccom)
    sys.stdout.flush()
    print(ferdig)

def insertColor(string, styleDict):
    i = 0
    liste = list(string)
    while i < len(liste):
        for characters in styleDict:
            if liste[i] in characters:
                liste.insert(i, styleDict[characters])
                i += 1
        i += 1
    liste.append(Style.RESET_ALL)
    return "".join(liste)

def skriv_ekorn1():
    print(hentGrafikk('ekorn/ekorn1'))

def skriv_ekorn2():
    print(hentGrafikk('ekorn/ekorn2'))

def skriv_ekorn3():
    print(hentGrafikk('ekorn/ekorn3'))

def skrivGnom():
    clear_screen()
    print(hentGrafikk('gnom/gnom', green))

def skrivTrollmann():
    print(hentGrafikk('trollmann/trollmann'))

def giVassleVink():
    return hentGrafikk('trollmann/trollmann_vink')

def skrivOndTrollmann():
    print(hentGrafikk('trollmann/ond_trollmann'))

def skrivGargouille():
    clear_screen()
    print(hentGrafikk('gargyl/gargyl'))

def skrivGuri():
    clear_screen()
    print(hentGrafikk('gargyl/guri'))

def skrivGravstein():
    clear_screen()
    print(hentGrafikk('gravstein/gravstein'))

def skrivSkjellett():
    clear_screen()
    print(hentGrafikk('skjellett/skjellett'))

def skrivGaute():
    clear_screen()
    print(hentGrafikk('gnom/gaute', green))

def skrivEnhjorning():
    clear_screen()
    print(hentGrafikk('regnbue/enhjorning'))

def skrivFisk():
    clear_screen()
    print(hentGrafikk('regnbue/fisk'))

def skrivSlott():
    clear_screen()
    slott = hentGrafikk('gnom/slott')

    # TODO: Erstatt med standardisert fargemetode
    slott = list(slott)
    t = 0
    while t < len(slott):
        if slott[t] in {"[", "]", "L", "J", "|", "_", "/", "\\"}:
            slott.insert(t, Fore.YELLOW)
            t += 1
        elif slott[t] in {"T", "I", "o", "O", "+", "=", "-", ",", "(", ")", ".", "^", "'"}:
            slott.insert(t, Fore.BLUE)
            t += 1
        elif slott[t] in {"%"}:
            slott.insert(t, Fore.GREEN)
            t += 1
        else:
            slott.insert(t, Style.RESET_ALL)
            t += 1

        t += 1

    print("".join(slott), Style.RESET_ALL)

def skrivStein():
    clear_screen()
    print(hentGrafikk('gargyl/stein', red, [gray, white][randint(0,1)]))

def skrivGargylslott():
    clear_screen()
    print(hentGrafikk('gargyl/slott'))

def skrivFontene():
    clear_screen()
    fontene = hentGrafikk('gargyl/fontene')
    print(insertColor(fontene, {".":blue + Style.BRIGHT, "S+":brown, "=I_\\/~()":gray,}))

def skrivStatue():
    clear_screen()

    statuer = [
        'gargyl/statue/statue1',
        'gargyl/statue/statue2',
        'gargyl/statue/statue3',
        'gargyl/statue/statue4',
        'gargyl/statue/statue5',
        'gargyl/statue/statue6',
        'gargyl/statue/statue7'
    ]

    indeks = randint(0,6)
    farge = [green, blue, yellow, brown, gray, magenta, cyan][randint(0, 6)]
    print(hentGrafikk(statuer[indeks], farge))

def skrivOrm():
    clear_screen()
    print(hentGrafikk('gargyl/orm').format(green, red))

def skrivTroll():
    clear_screen()
    troll = hentGrafikk('troll/troll')

    # TODO: Erstatt med standardisert fargemetode
    farge = randint(0, 5)
    farger = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    f = farger[farge]

    tf = list(troll)
    tf.insert(0, Style.BRIGHT)
    t = 0
    while t < len(tf):
        if (tf[t] in {":", ".", "'", "="}) or ((tf[t] == "/" or tf[t] == "\\") and (tf[t + 1] not in {" ", "_"} and tf[t - 1] not in {"´", " ", "_"})):
            tf.insert(t, f)
            t += 1
        else:
            tf.insert(t, Fore.WHITE)
            t += 1
        t += 1
    troll = "".join(tf)

    print(troll + Style.RESET_ALL)

def skrivStortTroll():
    clear_screen()
    troll = hentGrafikk('troll/troll_stor')

    # TODO: Erstatt med standardisert fargemetode
    farge = randint(0, 5)
    farger = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    f = farger[farge]

    tf = list(troll)
    tf.insert(0, Style.BRIGHT)
    t = 0
    while t < len(tf):
        if (tf[t] in {":", ".", "'", "=", "%"}) or ((tf[t] in {"/", "\\", "|"}) and (tf[t + 1] not in {" ", "_", "\\"} and tf[t - 1] not in {"´", " ", "_", "/"})):
            tf.insert(t, f)
            t += 1
        else:
            tf.insert(t, Fore.WHITE)
            t += 1
        t += 1
    troll = "".join(tf)

    print(troll + Style.RESET_ALL)

def skrivTrollBoss():
    clear_screen()
    boss = hentGrafikk('troll/troll_boss')

    f = Fore.RED

    tf = list(boss)
    tf.insert(0, Style.BRIGHT)
    t = 0
    while t < len(tf):
        if (tf[t] in {":", ".", "'", "=", "%"}) or ((tf[t] in {"/", "\\", "|"}) and (tf[t + 1] not in {" ", "_", "\\"} and tf[t - 1] not in {"´", " ", "_", "/"})):
            tf.insert(t, f)
            t += 1
        else:
            tf.insert(t, Fore.WHITE)
            t += 1
        t += 1
    boss = "".join(tf)

    print(boss + Style.RESET_ALL)

def skrivBirdman():
    clear_screen()
    print(hentGrafikk('random/birdman'))

def skrivHytte():
    clear_screen()
    hytte = hentGrafikk('troll/hytte')

    hytte = list(hytte)
    t = 0
    while t < len(hytte):
        if hytte[t] in {"%", "/", "\\", "~", ",", ";", "*", "#", "^", "`"}:
            hytte.insert(t, Fore.GREEN)
            t += 1
        elif hytte[t] in {"_", "-", "=", "[", "]", "|"}:
            hytte.insert(t, Fore.YELLOW)
            t += 1
        else:
            hytte.insert(t, Style.RESET_ALL)
            t += 1

        t += 1

    print("".join(hytte), Style.RESET_ALL)


def skrivRegnbue():
    clear_screen()
    bue = hentGrafikk('regnbue/regnbue')

    # TODO: Erstatt med standardisert fargemetode
    bue = list(bue)
    indeks = 0
    while indeks < len(bue):
        if bue[indeks] == "a":
            bue.insert(indeks, Fore.RED)
            indeks += 1

        if bue[indeks] == "b":
            bue.insert(indeks, Fore.GREEN)
            indeks += 1

        if bue[indeks] == "c":
            bue.insert(indeks, Fore.BLUE)
            indeks += 1

        if bue[indeks] == "d":
            bue.insert(indeks, Fore.YELLOW)
            indeks += 1

        indeks += 1

    bue = "".join(bue)

    print(bue)

    print(Style.RESET_ALL)

def skrivVulkan():
    clear_screen()
    vulkan = hentGrafikk('vulkan/vulkan')

    vulkan = list(vulkan)
    indeks = 0
    while indeks < len(vulkan):
        if vulkan[indeks].lower() in {"v", "o"}:
            vulkan.insert(indeks, Fore.RED)
            indeks += 1

        if vulkan[indeks] in {"/", "\\"}:
            vulkan.insert(indeks, Fore.WHITE)
            indeks += 1

        indeks += 1

    vulkan = "".join(vulkan)

    print(vulkan)

    print(Style.RESET_ALL)

def skrivBanditt():
    clear_screen()
    print(hentGrafikk('shroom/banditt/banditt'))

def skrivRotte():
    clear_screen()
    print(hentGrafikk('rotte/rotte'))

def skrivShroom():
    return hentGrafikk('shroom/shroom', red, brown, yellow)

def skrivSkjegghattShroom():
    print(hentGrafikk('shroom/shroom_skjegghatt', red, brown, yellow, green))

def skrivSopp(art):
    clear_screen()
    dim = Style.DIM
    red2 = Fore.RED

    sopper = [
        ('shroom/sopp/sopp1', (Fore.YELLOW + dim, reset + red2, reset)),
        ('shroom/sopp/sopp2', (brown, red2, green, reset)),
        ('shroom/sopp/sopp3', (brown, red2, green, reset)),
        ('shroom/sopp/sopp4', (yellow, red2, reset)),
        ('shroom/sopp/sopp5', (green, reset)),
        ('shroom/sopp/sopp6', (brown, red2, green, reset)),
        ('shroom/sopp/sopp7', (brown, red2, green, reset)),
        ('shroom/sopp/sopp8', ()),
        ('shroom/sopp/sopp9', ())
    ]

    if art == "liten":
        soppvalg = 0
    elif art == "tre":
        soppvalg = 7
    elif art == "familie":
        soppvalg = 8
    else:
        soppvalg = randint(0, 6)

    grafikk = hentGrafikk(sopper[soppvalg][0])
    if len(sopper[soppvalg][1]) > 0:
        fargetGrafikk = grafikk.format(*sopper[soppvalg][1])
    else:
        fargetGrafikk = grafikk

    if soppvalg == 4:
        print(insertColor(fargetGrafikk, {"oO":red2, ".,;:'`":brown}))
    elif soppvalg == 7:
        print(insertColor(fargetGrafikk, {"o78":red2, "\"_.,;:'`":brown}))
    elif soppvalg == 8:
        print(insertColor(fargetGrafikk, {"oO":red2, "\"(_.,;:'`":brown}))
    else:
        print(fargetGrafikk)


def skrivTre(kvist=False):
    clear_screen()
    g = Fore.GREEN
    b = Fore.YELLOW + Style.DIM

    trees = [
        ('shroom/tre/tre1', ()),
        ('shroom/tre/tre2', ()),
        ('shroom/tre/tre3', ()),
        ('shroom/tre/tre4', (b, reset)),
        ('shroom/tre/tre5', ()),
        ('shroom/tre/tre6', ()),
        ('shroom/tre/tre7', (b, reset)),
    ]

    treIndex = randint(0, 6)
    treet = trees[treIndex]
    if len(treet[1]) > 0:
        fargetTre = hentGrafikk(treet[0]).format(*treet[1])
    else:
        fargetTre = hentGrafikk(treet[0])

    if treIndex in set(range(3)):
        print(insertColor(fargetTre, {"cpd&%()@O":g, "|/\\_-":b}))
    elif treIndex == 4:
        print(insertColor(fargetTre, {"#cpd&%()@O":g, "\{\}|/\\_-":b}))
    elif treIndex == 5:
        print(insertColor(fargetTre, {"*cpd&%@O":g, ",()|/\\_-":b}))
    else:
        print(fargetTre)

def skrivMoseStein():
    clear_screen()
    stein = """
               #\\##\\#
             #  #O##O###
            #*#  #\\##\\###
            ##*#  #\\##\\##
           . ##*#  #o##\\#
        . ._. ._*#  #\\#
     .. . ..._--_. ._ ._-- ._"""
    print(insertColor(stein, {"#*":green, ".\\":gray, "O":red}))

def skrivGuffsliffsaff():
    clear_screen()

    red2 = Fore.RED + Style.DIM

    tre = hentGrafikk('shroom/tre/guffsliffslaff')
    print(insertColor(tre, {",oO.": red2, "\\/|\{\}~-_": brown}))

def skrivHodeskalle():
    clear_screen()
    print(hentGrafikk('shroom/hodeskalle'))

def skrivLeir():
    clear_screen()
    print(hentGrafikk('shroom/leir', brown, reset))

def skrivBandittLeir():
    clear_screen()
    print(hentGrafikk('shroom/banditt/bandittleir_tre'))

def skrivBaal():
    clear_screen()
    print(hentGrafikk('shroom/baal'))

def skrivTekanne():
    clear_screen()
    print(hentGrafikk('shroom/tekanne'))

def skrivSkilt():
    clear_screen()
    print(hentGrafikk('shroom/banditt/bandittleir_skilt'))

def skrivHellhound(nr=0):
    farger = [red, Fore.GREEN + Style.BRIGHT, Fore.CYAN + Style.BRIGHT]
    clear_screen()
    print(hentGrafikk('vulkan/hellhound', farger[nr]))

def skrivCerberus():
    clear_screen()
    red2 = Fore.RED
    print(hentGrafikk('vulkan/cerberus', red2))
