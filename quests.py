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

#Gargyl:
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

def troll_q1(navn):
    return "    Hei " + navn + """!
    Det er uhyre mange troll rundt i dette området. Ettersom tiden har gått
    har vi blitt vant til det, men de har blitt mer og mer uredde i det siste.
    De har til og med gått så nærme som å pisse på bålet gjennom pipa. Vet du
    hvor mye ammoniak det der lukter!? Uansett, skjønner vi at for å sette litt
    brems på selvsikkerheten deres, bør vi true dem litt. Jeg tenker et lite
    folkemord bør gjøre dem litt redde. Gå ut og drep 25 troll. Menn, kvinner
    og barn. Det er ikke så vanskelig. Man ser ikke forskjell på dem uansett!

    -- Myrd 25 troll uten nåde."""

def troll_q1_ferdig(navn):
    return "    Tusen takk " + navn + """!
    Det er så fint å kjenne en magiker som ikke bøyer til slike ubrukelige ting
    som "moral og etikk". Det er oss eller dem. De angriper oss uansett om de er
    kvinner eller barn og da må vi beskytte oss selv. Jeg lurer på hvorfor de gjør
    det i det første uansett...
    """

#Flere quest (coming soon)
