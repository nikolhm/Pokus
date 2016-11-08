#Quest relatert til gnomene:
def q1(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Mette Merkelig! Velkommen til borgen! Jeg skulle gjerne vist deg rundt,
    men det er unntakstilstand her på borgen for øyeblikket. Du skjønner det at det har
    kommet et monster til borgen vår som besudler den fine skogen vår og gjør borgen
    til et uhyggelig sted å være. Dette monsteret heter Gaute Gnom den Grusomme, og er
    en gnom av værste sort. Vi har alltid hatt problemer med gnomene i skogen her,
    men etter Gaute Gnoms ankomst har de vært spesielt aggressive! Jeg trenger din hjelp
    til å rydde de brysomme gnomene av veien slik at borgen og skogen vår igjen kan bli
    et harmonisk og magisk sted for alle.

    -- Myrd 10 gnomer.""")
def q1ferdig(navn):
    return "Takk for hjelpen " + navn + "! Dessverre ser det ut til at gnomene fortsetter å herje så lenge Gaute Gnom den Grusomme er her. Kanskje Symmetriske Sara har løsningen?\n"

def q2(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Gale Gizly! Jeg er spesielt interessert i magi som helbreder kroppen!
    Tenk så fascinerende, alt man trenger er å konsentrere seg litt, så ordner
    magien resten. Likevel er det mange her som er redd for å bruke slik magi. "unaturlig"
    kaller de det. Som om vi driver med noe naturlig som helst her. Uansett, jeg trenger
    en forsøkskanin for å se hvilke konsekvenser det har på kroppen. Kan du restorere
    totalt 300 helsepoeng på deg selv, og så komme tilbake hit så jeg kan undersøke?

    -- Restorer 300 helsepoeng på deg selv.""")
def q2ferdig(navn):
    return "Glimrende "+navn+"! Ingen skader på kroppen? Så skuffende, det ser ut til at trylleformelen er uskadelig og kjedelig. Kanskje hvis jeg modifiserer formelen litt?\n"

def q3(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Fine Fredrikke! Jeg skulle bare ut i skogen for å la resten av verden
    nyte synet av mitt ytre, da de fordømte gnomene kom ut fra ingensteds og stjal
    vesken min! Hva skal jeg gjøre? Alle mine magiske sminkesaker lå i den vesken!
    Hva vil skje med mitt ytre? Jeg kommer til å bli like stygg som deg!
    Kan du vær så snill hjelpe meg å få tilbake sminkesakene? Gnomene har nok åpnet
    vesken og fordelt innholdet, så det kan bli vanskelig å finne alt.

    -- Finn 6 sminkeartikler.""")
def q3ferdig(navn):
    return "Fantastisk "+navn+"! Nå kan jeg endelig vise meg offentlig igjen! Hva mener du overfladisk? meg?\n"

def q4(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Magiske Mikkel! Jeg liker å få ting til å fly! Dytte ting med et
    vindpust! Det er rett og slett trollbindende å stirre på naturens vakre krefter
    bli manipulert av mennesker. Har du erfaring med trylleformelen "vind"? Jeg kan
    lære deg hvordan å maksimere potensialet til trylleformelen! Men først må du bevise
    at du behersker trylleformelen godt nok. Her om dagen var det en idiot som blåste
    av spiret på et av tårnene i borgen med en ukontrollert trylleformel!

    -- Kast "vind" 5 ganger""")
def q4ferdig(navn):
    return "Godt jobbet "+navn+"! Nå skal du se hvordan en mester gjør det!\n"

def q5(navn):
    return ("    Hei igjen "+navn+"""!
    Gale Gizly er back in business, og denne gangen har jeg funnet svaret! Med litt
    eksperimentering og bare noen få tårnspir i svinn har jeg økt min forståelse
    for magiens verden, da spesielt med tanke på helbredende magi. Det viser
    seg at når du helbreder deg selv, tar du energi fra naturen rundt deg.
    Jeg har funnet en metode som gjør at du kan spesifisere hvor du vil hente
    energien fra, noe som kan være nyttig når du slåss mot gnomene. Jeg er
    ganske sikker på at denne formelen ikke vil drepe deg, alt du trenger å
    gjøre er å kaste "super restituer" tre ganger, så er du klar for å lære
    hemmeligheten bak energi-konsentrering.

    -- Kast "super restituer" tre ganger.""")
def q5ferdig(navn):
    return "Supert "+navn+"! Med denne teknikken skal man kunne skade gnomen man slåss mot samtidig som man helbreder seg selv! Ja, jeg er et geni!\n"

def q6(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Symmetriske Sara! Disse gnomene har herjet i skogene rundt borgen vår
    lenge nok, men uansett hvor mange vi kverter dukker det stadig opp fler! Det
    er helt sikkert på grunn av Gaute Gnom den Grusomme, og nå har vi endelig
    funnet ut hvor han klekker sine grusomme planer fra! Det viser seg at Gaute
    holder til i en hule dypt inne i skogen, godt beskyttet av sine beste Gnomevakter.
    Er du helten vi trenger? Er du modig nok til å vandre gjennom skogen til den
    skjulte hulen til Gaute Gnom den Grusomme? Om du er det, vær på vakt!
    Gaute er en gnom utenom det vanlige, et beist større og styggere enn noe annet!

    -- Bekjemp Gaute Gnom den Grusomme""")
def q6ferdig(navn):
    return "Hurra! Tusen takk "+navn+"! Nå er endelig monsteret borte! Borgen er trygg igjen, og skogen vil snart nok bli et rolig og fint sted å være! Igjen, tusen tusen takk!\n"

def bonus_q1(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Rotete Randi! Jeg har mistet den magiske soppen min! Har du sett
    soppen min? Jeg hadde gitt hatten min for å se min magiske sopp en siste gang!
    """)
def bonus_q1ferdig(navn):
    return "Har du funnet den? Gi den til meg! Straks!\nEhh, det var ikke meningen å "+\
    "pushe deg slik, men om du gir den til meg skal jeg gi deg hatten min!\n"

def bonus_q2(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Mirakuløse Marte! Jeg har tatt på meg oppdraget å lære nybegynnerne på borgen
    litt skikkelig magi, men en stor del av tiden går til å rette oppgavene de skriver.
    Det tar lang tid og er kjedelig, og i det siste har noen fjols begynt å skrive
    unødvendig lange oppgaver. "Valgfritt emne", pøh! Det er jeg som må sitte og se gjennom
    det hele, mens de langer ut om ting de synes er interessante. Rotete sammensetning er
    det og! Om jeg bare hadde hatt en magisk trylleformel som på magisk vis bare rettet
    alle oppgavene for meg! Har du hørt om noe slikt?
    """)
def bonus_q2ferdig(navn):
    return "Er det sant? Det finnes faktisk? Dette vil gjøre livet mitt så mye lettere!\n"

#Flere quest (coming soon)
