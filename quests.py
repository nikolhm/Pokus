from colorama import *

#Quest relatert til gnomene:
def q1(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Mette Merkelig! Velkommen til borgen! Jeg skulle gjerne vist deg rundt,
    men det er unntakstilstand her på borgen for øyeblikket. Du skjønner det at det har
    kommet et monster til borgen vår som besudler den fine skogen vår og gjør borgen
    til et uhyggelig sted å være. Dette monsteret heter Gaute Gnom den Grusomme, og er
    en gnom av verste sort. Vi har alltid hatt problemer med gnomene i skogen her,
    men etter Gaute Gnoms ankomst har de vært spesielt aggressive! Jeg trenger din hjelp
    til å rydde de brysomme gnomene av veien slik at borgen og skogen vår igjen kan bli
    et harmonisk og magisk sted for alle.

    -- Myrd 10 gnomer.""")
def q1ferdig(navn):
    return "    Takk for hjelpen " + navn + """!
    Dessverre ser det ut til at gnomene fortsetter å herje så lenge
    Gaute Gnom den Grusomme er her. Kanskje Symmetriske Sara har løsningen?\n"""

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
    return "    Glimrende "+navn+"""!
    Ingen skader på kroppen? Så skuffende, det ser ut til at trylleformelen
    er uskadelig og kjedelig. Kanskje hvis jeg modifiserer formelen litt?\n"""

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
    return "    Fantastisk "+navn+"""! Nå kan jeg endelig vise meg offentlig igjen!
    Hva mener du overfladisk? meg?\n"""

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
    return "    Godt jobbet "+navn+"! Nå skal du se hvordan en mester gjør det!\n"

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
    return "    Supert "+navn+"""!
    Med denne teknikken skal man kunne skade gnomen man slåss mot samtidig
    som man helbreder seg selv! Ja, jeg er et geni!\n"""

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
    return "    Hurra! Tusen takk "+navn+"""!
    Nå er endelig monsteret borte! Borgen er trygg igjen, og skogen vil
    snart nok bli et rolig og fint sted å være! Igjen, tusen tusen takk!
    Dine heltedåder har ikke gått umerket hen, Overtrollmann Vassle spurte
    om deg personlig. Dra opp til kontoret hans og hør hva han har å si!
    Kontoret ligger i det øverste spiret her i borgen.\n"""

def bonus_q1(navn):
    return ("    Hei "+navn+"""!
    Mitt navn er Rotete Randi! Jeg har mistet den magiske soppen min! Har du sett
    soppen min? Jeg hadde gitt hatten min for å se min magiske sopp en siste gang!
    """)
def bonus_q1ferdig(navn):
    return """    Har du funnet den? Gi den til meg! Straks!
    Ehh, det var ikke meningen å pushe deg slik, men om du gir den til meg
    skal jeg gi deg hatten min!\n"""

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
    return "    Er det sant? Det finnes faktisk? Dette vil gjøre livet mitt så mye lettere!\n"

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
    Noen her har skremt beboerne fra vettet, de tør ikke bevege seg ut av
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
    Du må finne en måte å avverge gargylenes RockNoRoll-magi. Snakk
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

#Spesialiseringsquests
def smertedreper_intro(navn):
    return """    Hei {}!
    Si meg, hva vet du om smertedrepernes vakre kunst? Ingenting?
    La meg gi deg en kort introduksjon: Vi i Foreningen for Smertedrepere har som
    filosofi at det å ta skade slett ikke er en svakhet, men en lærdom, en lekse,
    kunnskap man kan ta med seg videre i livet! Men for å lære noe som helst av smerten
    må man tåle den først. Derfor spesialiserer vi oss innen kunsten å tåle så mye
    skade som mulig!

    Vi i Foreningen for Smertedrepere rekrutterer nye medlemmer, men vi har strenge
    medlemmskrav. Alle som søker, må ha mistet minst 25000 helsepoeng fra fiender!

    -- Mist 25000 helsepoeng fra fiender.""".format(navn)
def smertedreper_intro_ferdig(navn):
    return "    Utmerket {}! Du finner vårt kontor opp trappen fra hovedhallen. Ser deg der!\n".format(navn)

def klartenker_intro(navn):
    return """    Hei {}!
    Har du hørt om klartenkere før? Klartenkere er oss som er helt klar i hodet,
    spesielt etter en god stripe konsentrasjonspulver! Vi konsentrerer oss om
    konsentrasjon, og mener det er essensen av suksess i enhver kamp. Konsentrason
    er det som gjør oss magikere til magikere, og uten den ligger vi tynt an!

    Vi i de Klartenkendes Forening rekrutterer nye medlemmer, men for å søke om
    å bli medlem krever vi at du har brukt minst 12500 konsentrasjonspoeng!

    -- Bruk 12500 konsentrasjonspoeng.""".format(navn)
def klartenker_intro_ferdig(navn):
    return "    Flott! Du finner vårt hovedkontor der borte. Snakkes der!\n"

def muskelbunt_intro(navn):
    return """    Hei {}!
    Hvilket forhold har du til muskelbunter? Vi er ikke så skumle som vi høres
    ut, men definitivt så farlige som vi høres ut! Vi i Muskelbunters Felles-
    forening mener at trylletriks er hendig å ha opp ermet, men til syvende og
    sist er det vanlige angrep som avgjør en kamp.

    Vi i de Muskelbunters Forening rekrutterer nye medlemmer, men for å søke om
    å bli medlem krever vi at du har tatt minst 75000 helsepoeng fra fiender!

    -- Ta 75000 helsepoeng fra fiender.""".format(navn)
def muskelbunt_intro_ferdig(navn):
    return """    Utmerket {}! Du finner vårt kontor i nabodimensjonen vår. Det er en portal
    ved utedoen som tar deg rett dit. Ser deg der!\n""".format(navn)

#Troll:
def troll_q1(navn):
    return "    Hei, " + navn + """!
    Det er uhyre mange troll rundt i dette området. Ettersom tiden har gått
    har vi blitt vant til det, men de har blitt mer og mer uredde i det siste.
    De har til og med gått så nærme som å pisse på bålet gjennom pipa. Vet du
    hvor mye ammoniak det der lukter!? Uansett skjønner vi at for å sette litt
    brems på selvsikkerheten deres, bør vi true dem litt. De begynner å nærme
    seg området rundt hytta. La dem kjenne at de må holde seg unna tilholdsstedet
    vårt, fordi vi er farlige. De kommer ikke til å le når 25 av dem blir utryddet
    utenfor og ikke kommer seg hjem.

    -- Myrd 25 troll."""
def troll_q1_ferdig(navn):
    return "    Tusen takk, " + navn + """!
    Det er så fint å kjenne en magiker som ikke bøyer til slike ubrukelige ting
    som "moral og etikk". Det er oss eller dem. De angriper oss og da må vi beskytte
    oss selv: Det er så enkelt. Jeg lurer på hvorfor de gjør det i det første uansett...
    """

def troll_q2(navn):
    return "    Hei, " + navn + """!
    Jeg hørte du hjalp Rolf med å ta ned noen voldsomme troll nær hytta. Jeg har
    ansvaret her for å forske på trollene og finne ut hvordan de funker. På grunn
    av innsikten min i både fysiologien til troll og psykologien, så brukes jeg
    ofte som strategisk troll-ekspert. Vi skjønner nå at en faksjon av trollene
    har bygd seg en hule ikke langt herifra, som de bruker til å sende soldater
    til området rundt hytta. Som en ekspert vet jeg at grunnen til dette er trollenes
    overtroiske og paranoide tenkning. De tror at magi er overordnet alle levende
    skapnigner, bortsett fra lederen deres. Trollkongen har blitt sagt å ha magiske
    evner. Vi er ikke så sikre på det, det kan hende det bare er et rykte.

    Vi trenger noen til å gå ned til hulen for å stoppe disse fanatiske trollene.
    For å gjøre dette vil jeg gi deg noen ladninger med svart pulver. Du må sette
    dem i riktige posisjoner rundt i hulen, slik at eksplosjonen ødelegger basen
    deres. Vær forsiktig! Hver gang troll setter opp en hule, er det alltid en beta
    som kommer med. Betaene er troll direkte under Kongen. De er store, kraftige, men
    verst for deg: de har ekstremt god luktesans. Hvis betaen oppdager deg, må
    du forberede deg på at troll kommer til å bli kastet mot deg. Du kan vente deg
    minst 3 troll per gang du må gjennom. Det er enda verre om betaen finner deg.
    Han er ikke en fiende å ta lett på. Hvis du er heldig, får du satt alle 5 ladninger
    på plass før du blir oppdaget."""
def troll_q2_ferdig(navn):
    return "    Vakkert arbeid, " + navn + """!
    Det er nok ikke lenge før de setter opp en ny operasjonsbase, gitt at de ikke
    kommer til å gi opp før lederen deres er ute av spill. Det er slik de fungerer.
    Uten lederen så har de ikke et mål i livet. Det er litt som maur. De er avhengige
    av Dronningen. Kongen har ekstremt mye makt over trollene hans. Vi har prøvd å
    finne ham veldig lenge, men trollene vet å holde ham så gjemt som mulig...\n"""

def troll_q3(navn):
    return "    Hei, pssst! " + navn + """!
    Det er meg! Zip! Ikke vær lurt av forkledningen min. Jeg må late som jeg er en
    gammel trollmann for å komme inn i badstua. Trollmennene her er sjåvinistiske
    relikker med foreldete verdier. Hvis jeg ikke later som jeg er mann, blir jeg
    bare ignorert. "Lag meg en sandwich, heks!" "Jeg har lyst til å dyppe staven
    min i det der, hvis du skjønner hva jeg mener!" De er absolutt motbydelige!

    Likevel må jeg finne ut hva de vet om trollene. Jeg har overhørt noe prat om
    å dra ned til den gamle minen å rydde ut noen av de sterkere trollene. Disse
    gamle fjertene snakker om å gjøre det, men de bare snakker og snakker og gjør
    niks. Kan du gå ned i minen og drepe en beta? Jeg tror det kan være mulig at
    du kan finne informasjon om hvor Trollkongen gjemmer seg. Trollkongen sender
    alltid ut ordre gjennom betaene og de har ikke så god hukommelse.

    -- Dra ned i minen og drep en beta."""
def troll_q3_ferdig(navn):
    return "    Hei, " + navn + """!
    Så du fant et skriv på trollet? Det er veldig vanskelig å lese trollsk, men
    jeg kan tyde hovedpunktene, med manglende nøyaktighet. Det står noe i duren
    av... *spyr* Å nei! For helvete! Hva er galt med dem?! Trollene skriver
    alt i form av vemmeligheter. Det er helt frastøtende! Likeve *blæææh* ser
    jeg at trollet fikk ordre om å *surt oppstøt* til Helvetesgapet. Det må være
    der Trollkongen befinner seg. Jeg har hørt at ingen av gamlingene tør å gå
    ned dit. Det er visst for farlig med faren for steinras... For noen pyser!
    """

def troll_q4(navn):
    return "    Hei, " + navn + """!
    Nå som vi vet hvor trollkongen er kan vi ta ham ned. Du må likevel være
    forsiktig. Jeg har hørt at han har veldig sterk magi. Du vet aldri hva han
    har opp ermet...
    """
def troll_q4_ferdig(navn):
    return """    Kjempebra {}! Nå kan jeg endelig ta av meg dette skjegget og dra hjem!
    Dra tilbake til borgen og rapporter om vår suksess til Vassle!""".format(navn)

def troll_bq1(navn):
    return """    Har du noen gang hørt Rock&Troll-musikk?! Det er det beste jeg noen gang har hørt!
    Trozzy Ozbourne, "The Trolling Stones", "Stone Zeppelin", "(Huldra's) Kiss", "Boomerang Rapido",
    Troll Dylan, Elvis Trollsley... Jeg klarer meg ikke en eneste dag uten å ha hørt på dem! Likevel
    fikk jeg litt problemer når jeg dro ut i skogen med en "venninne" og noe viagrooma-rot, hvis du
    skjønner hva jeg mener! Jeg tok med "Trolling Stones"-albumet mitt og må ha mistet det! Det er
    ekstremt vanskelig å få tak i de albumene! Trollene må ha funnet det innen nå. Jeg skjønner kanskje
    at de kommer til å nyte det også, men jeg er helt avhengig av "Trolling Stones". Jeg må ha det tilbake!\n"""
def troll_bq1_ferdig(navn):
    return "    Har du funnet albumet mitt?! Vær så snill, gi det tilbake! Jeg gjør hva som helst!\n"

#Shroom:
def shroom_q1(navn):
    return "    Hei " + navn + """!
    Virkelig godt å se deg igjen, vi har havnet i en heller uheldig situasjon
    her. Vassle sendte oss for å undersøke den magiske ubalansen i skogen
    her, da vi brått ble angrepet av en gjeng banditter. De virket helt fra
    seg av sinne, og sa at våre magiske eksperimenter hadde gått over streken!
    Som regel pleier bare en eller to banditter vise seg i disse traktene om
    gangen, men nå var det mange av dem! Vi har ikke klart å fokusere på
    oppgaven vår i det hele tatt, siden vi stadig må flykte fra bandittene!
    Vi har hørt rykter om at bandittene er en del av en organisert kriminal-
    bande som holder til dypere inn i skogen. Kan du, som den modigste av
    oss, dra til bandittenes leir og finne ut hvorfor de jakter oss sånn?

    En av våre stakkers torturerte rotter sa man burde gå VENSTRE HØYRE
    VENSTRE i skogen, men er usikker på hvordan stedsansen til torturerte
    rotter fungerer...

    -- Finn bandittenes hovedleir og stopp angrepene."""
def shroom_q1_ferdig(navn):
    return """    Trenger vi ikke bekymre oss lengre for banditt-angrep? Fantastisk!
    Da kan vi fokusere på oppgaven fremover, og jeg tror Strategiske Synne har
    et spesielt oppdrag til deg """ + navn + ".\n"

def shroom_q2(navn):
    return "    Akk " + navn + """.
    Det går ulykkens vei for meg. Jeg er en middelmådig magiker som aldri har
    fått til noe særlig av det jeg prøver på her i livet. Men så en dag ble
    jeg spurt om å ta ansvaret for mat og utstyr på en topp-hemmelig ekspedisjon
    utsendt hit av Overtrollmann Vassle selv! Tenk så Lykkelig jeg ble! Og Tenk
    og hvor knust jeg ble da jeg fant ut at de skøyerske gnomene har stjålet
    mesteparten av det. Vi har levd på bark og mose de siste dagene, og min
    popularitet her i leiren er stadig synkende. Kan du gjøre meg og resten
    av leiren en stor tjeneste og finne de stjålne forsyningene?

    -- Finn 13 stålne forsyninger."""
def shroom_q2_ferdig(navn):
    return "    Endelig kan vi spise litt skikkelig mat igjen! Mange mange takk " + navn + """!
    Kanskje de andre vil se meg i et annet lys nå.\n"""

def shroom_q3(navn):
    return "    Hei " + navn + """!
    Er ikke denne skogen fantastisk? Trær må være det mest spennende i verden,
    og i denne delen av skogen har jeg funnet mange flere sorter enn vanlig.
    Ikke nok med det, men det virker som om de er levende! Det er også grunnen
    til at jeg trenger hjelp fra deg. Til vanlig katalogiserer jeg alle nye
    tresorter jeg finner selv, men til tross for min ekstraordinære egenskap
    til å teleportere meg dit jeg vil, duger jeg ikke når det kommer til kamp.
    Kan du gi meg 'tamme' eksemplarer av noen av de fascinerende tresortene
    som pryder denne kanten av skogen?

    -- Oppdag et knippe forskjellige tresorter."""
def shroom_q3_ferdig(navn):
    return "    Eik, bøk, tre, fire, sort, guffs- Hei " + navn + """!
    Humm, disse notatene sier lite om trærenes indre komposisjon og
    under-suverene overlevelseskraft, men de duger! Tenk så interessant,
    kraftige X-verdier i barkens nedre hjørneparti splittes HVERT sekund
    for å gjøre plass til et stadig ekspanderende volum, forårsaket av
    både indre og ytre dragningskraft påkalt av monopolare bio-felt
    fremdrevet av saktegående motstandsprosesser...

    *Kjedelige Kjell durer på om trær. Du sniker deg unna*\n"""

def shroom_q4(navn):
    return "    Akk " + navn + """.
    Det var stor jubel i leiren da du returnerte de stjålne forsyningene, men
    selv med dem kommer vi ikke til å holde lenge. Det vi trenger er noen til
    å lage mat for oss, en som kan bruke ressursene rundt oss til noe matnyttig.
    En som Kent Kokk! Vi trenger Kent Kokk! Hvis du noen gang møter på Kent Kokk
    på dine reiser, kunne du bedt ham komme hit?

    -- Finn Kent Kokk og be ham lage mat for ekspedisjonen."""
def shroom_q4_ferdig(navn):
    return "    Strålende " + navn + """, virkelig strålende!
    Med Kent Kokk på laget, kan vi holde ut her så lenge som er krevd av oss!
    Jeg ser frem til deilige delikatesser de neste dagene. Har hørt noen rykter
    om at han har fått en ny interesse for steiner, vet du noe om det?\n"""

def shroom_q5(navn):
    return "    " + navn + """!
    Vi ble sendt her for å utforske en magisk ubalanse lokalisert her i utkanten
    av vår egen skog. Som du helt sikkert har merket, er ikke alt som det skal
    her. Trær og andre ting i skogen har fått en egen vilje og er blitt aggresive,
    i tillegg til at folk her har startet å oppføre seg merkelig. For ikke snakke
    om alt styret med bandittene! Vi har mye å takke deg for, men vårt arbeid
    er knapt i gang. Som du har observert, har lignende magiske ubalanser oppstått
    andre steder også. Fra din beskrivelse virker det som om en magiker står bak
    disse grufulle gjerningene. At andre enn oss magikere har evne til å utføre
    magi er farlig og ikke noe vi kan ta lett på. Jeg har sendt fire magikere i
    forskjellige retninger, og en er enda ikke tilbake. Kan du dra opp bakken
    og lete etter henne?

    -- Let i området opp bakken etter Pàn Tú."""
def shroom_q5_ferdig(navn):
    return "    Du må være " + navn + """! Mitt navn er Pàn Tú.
    Jeg har hørt mye om deg, men nå er ikke tiden for hyggelige introduksjoner.
    Jeg har lokalisert Shroomsenes tilholdsted og tilegnet meg svært verdifull
    informasjon. Zip sier jeg kan stole på deg, så her er den: Shroomsene er
    splittet i to leirer. Den ene er fanatisk opptatt av selvdyrkelse, mens
    den andre ser ut til å være mulig å kommunisere med. Jeg har allerede noen
    kontakter innad i den leiren, men på grunn av min... menneskelighet, sliter
    jeg med å få ut informasjon ubemerket.

    Hør her """ + navn + """, dette er svært viktig.
    Det finnes noen ondskapsfulle sjeler innen våre egne rekker, som konspirerer
    med fienden og gjør livene våre sure. Rapporter tilbake til Strategiske Synne,
    men ikke nevn spionasjen eller de to leirene. Snakk med Zip, og bare Zip, når
    du er klar for å gjøre noe virkelig godt her i verden.

    Vi snakkes. Hold et åpent sinn """ + navn + ".\n"

def shroom_q6(navn):
    return """    Shrooms?
    Jeg har aldri hørt om noe slikt før, men om forvokste sopper nå
    besitter magiske evner, er situasjonen blitt verre enn først antatt. Vi må
    tenke strategisk her og ikke gjøre noe forhastet. Målet vårt er å utgjevne
    den magiske ubalansen, som helt sikkert er opphavet til disse 'shroomsene'
    og alle de andre levende skapningene i skogen som ikke burde være levende.
    Men om vi leter direkte etter kilden vil shroomsene oppdage målet vårt med
    en gang, og de virker som en fiende vi ikke bør undervurdere. Derfor trenger
    vi en distraksjon. Jeg sender et team med gode magikere opp bakken og dypere
    inn i skogen for å slåss direkte mot shroomsene. Med denne taktikken slår vi
    to fluer i en smekk, vi får distraksjonen vi trenger, og vi reduserer trusselen
    for en shroom-invasjon. Jeg trenger at du, som har støtt på disse shroomsene
    før, er med i feltet og leder ann kampen mot udyrene!

    Og en ting til """ + navn + """. Jeg burde kanskje ha advart deg før, men vi er ikke
    helt sikre på hvor lojaliteten til Pàn Tú ligger. Ta alt hun sier med en klype
    salt!

    -- Drep 20 shrooms."""
def shroom_q6_ferdig(navn):
    return "    Strålende " + navn + """.
    Kampene fortsetter, men jeg har en viktigere oppgave til deg.\n"""

def shroom_q7(navn):
    return "    Hei der " + navn + """!
    Dine magiske krefter har økt betraktelig siden sist, men det er alltid
    rom for forbedring! Er du kjent med formelen Opphold? Den forvirrer
    fienden i to runder, og gir deg tid til å ta tilbake overtaket i en
    ellers nedgående kamp. Men, jeg har funnet en metode å gjøre formelen
    enda mer effektiv på, uten at det krever noe mer konsentrasjon fra deg!
    Spesielt her ute på ekspedisjonen er det viktig at alle er på sitt beste,
    men som alltid har jeg mine prinsipper: Ingen skal lære noe de ikke kan
    kontrollere, slik som det neket Gale Gizly. Opphold fiender 7 ganger, så
    skal jeg lære deg hvordan formelen blir enda kraftigere!

    -- Opphold fiender med formelen Opphold 7 ganger."""
def shroom_q7_ferdig(navn):
    return "    Flott " + navn + """!
    Det er viktig at alle er på sitt ypperste i disse tider. Her er
    hemmeligheten til å utføre god og effektiv magi...\n"""

def shroom_q8(navn):
    return "    Hei igjen " + navn + """!
    Det var rett av deg å komme til meg med denne informasjonen. Strategiske
    Synne bryr seg mest om å utslette shroomsene, men om vi kan kommunisere
    med noen av dem, kan vi kanskje finne ut hva som egentlig har skjedd her.
    Dette er informasjon av uvurderlig verdi som er verdt tapene det kan
    medføre om vi ikke fokuserer på å raskt utslette fienden. Finn Pàn Tú
    og møt kontakten hennes, koste hva det koste vil. Vi trenger å vite hva
    som har skjedd her! Og husk, hold et åpent sinn.

    -- Møt kontakten til Pàn Tú."""
def shroom_q8_ferdig(navn):
    return """    Så de er ikke den Barmhjertiges barn altså. Det forklarer en del!
    Pàn Tú har forduftet sier du? Kanskje jeg burde dra ut i skogen og... lete
    etter henne. Ja. Definitivt! Hold et åpent sinn """ + navn + "!\n"

def shroom_q9(navn):
    return "    " + navn + """! Det er krise!
    Det viser seg at Pàn Tú er en forræder! Hun har brutt all kontakt med oss,
    og hun var sist sett flyktende innover i shroom-terretorium sammen med en
    annen skikkelse! Ikke nok med det, men Zip har også sporløst forsvunnet!
    Zip er en nøkkelbrikke i denne ekspedisjonen, og om Zip er blitt bortført
    er det svært alvorlig. Om Zip også er en forræder ligger vi tynt an! Fort,
    dra opp bakken og inn til fronten og finn Zap! Om noen vet noe mer om Zip,
    må det være Zap.

    -- Finn Zap ved fronten og finn ut hva som har skjedd med Zip."""
def shroom_q9_ferdig(navn):
    return """    Er Zip også en forræder?! Da ligger vi taktisk svært dårlig an!
    Stakkars Zap, Zip og Zap har alltid vært en enhet i seg selv!\n"""

def shroom_q10(navn):
    return "    Tiden er inne " + navn + """, for å gjøre slutt på dette.
    Vi har en dårlig taktisk posisjon i forhold til fienden, og vi er mange
    ganger undertallige. Vårt eneste håp er å kutte av kilden deres til magi.
    Det vil utgjevne den magiske ubalansen her, som var det vi kom for å gjøre,
    så får de resterende shroomsene leve ut sine liv i dette hjørnet av skogen.
    Såfremt shroomsene i seg selv ikke besitter evnen til å skape flere magiske
    kreasjoner, burde det ikke være nødvendig å drepe dem alle. I tillegg har
    vi ikke ressurser nok til en slik operasjon.

    Heldigvis har vi klart å uthente informasjon mens fiendens fokus var ved
    kampene med fronten. Det viser seg at kilden til deres magi kommer fra et
    lite tjern, som er senteret av shroom-terretoriumet. Det er en smal sak å
    forurense tjernet med en standard Kast Hvitløk-formel som alle magikere kan,
    men å komme bort til det blir utfordringen! Vi har bestemt å sende deg inn
    alene slik at du kan snike deg ubemerket dit, samtidig som vi sender alle
    våre magikere til fronten for å avlede oppmerksomheten. Men pass på, De har
    helt sikkert utstasjonert vakter ved tjernet, som vil ha en stadig påfylling
    av magiske krefter!

    -- Forurens tjernet i midten av shroom-terretoriumet."""
def shroom_q10_ferdig(navn):
    return "    Hurra! Du " + navn + """, må være den dyktigste magikeren vi har!
    Rapporter tilbake til Overtrollmann Vassle så han får høre om seieren vår!\n"""

def shroom_bq1(navn):
    return """    Salig er du, som får oppleve nærværet deres!
    Men det er ikke nok, vi må ha mer. MER! Javisst, våre overordnede er ikke
    fornøyd med vår innsats. Vi må vise mer dedikasjon! MER! Vi trenger noe
    håndfast vi kan bruke til å tilbe dem på, et totem eller noe slikt!
    Har du sett noe slikt rundt omkring?
    """
def shroom_bq1_ferdig(navn):
    return """    Fantastisk! Dommedagen er snart på oss, og det er viktig å vise soppen
    hvilken side vi egentlig står på! Bli med meg """ + navn + ", i et kjapt blodoffer!\n"

def shroom_bq2(navn):
    return """    Pàn Tú er en forræder!
    Jeg har blitt satt til oppgaven å administrere en gransking innad i
    ekspedisjonen, og se etter eventuelle beskjeder noen kan ha hatt fra
    Pàn Tú eller hennes sammensvorne. Alle bevis er helt sikkert revet opp
    og kastet i skogen, men om du finner noen biter av lapper eller andre
    hint, kom rett til meg med det!\n"""
def shroom_bq2_tekst():
    return """    Alle korrespondanser ser ut til å omhandle 'den Barmhjertige'.
    Motivene er uklare, men det virker ikke som om de er direkte i liga med
    shroomsene. Dette er høyst merkverdig og svært alvorlig, og en sak jeg skal
    ta opp med Overtrollmann Vassle. Ikke snakk om dette til noen, og helst glem
    alt som har skjedd!\n"""

def shroom_bq3(navn):
    return """    Hei igjen {}!
    Det har skjedd igjen! Den stakkers magiske sussesoppen min har forsvunnet!
    Har du sett ham? Vi var bare ute og trente med vennene hans, så plutselig
    forsvant han! Det er klart slike sopper gjør som de vil, og de må adlydes,
    ADLYDES! OG TILbes men tenk en slik liten stakkerslig nussesussesopp alene
    i den store fæle skogen! Noen må finne ham! Jeg er sikker på at om du finner
    ham, vil han bli så glad at han kan låne deg kreftene sine en gang i blandt!
    Slike sussesopper som ham har sterke KRAFTIGE USTOPPELIGE krefter som kan
    komme til god nytte i en kamp!\n""".format(navn)
def shroom_bq3_tekst():
    return """    Du har nå muligheten til å tilkalle den magiske soppen i kamp!
    For å gjøre det, skriv 'tilkall sopp' eller bare 'ts'. Soppen vil ikke
    adlyde deg om du er utenfor denne delen av skogen, og vil ikke komme om
    du allerede har en alliert ved din side i kamp. Skriv 's' i kamp for å
    se detaljer.\n"""

def kjellprat():
    return """"    ...Trevirksomhets invirkning på utenforstående faktorer aldri vil gjøre
    opp for skadeområdet innenfor et omfang på en slik biokultur, dessuten har
    bark-områdene et eget beskyttende lag spesielt for slike metalliske
    gjenstander, laget nettopp av de øvre grenpartiene på slike typer, noe som
    også har innvirkning og ringvirkning på trærnes røtter...\n"""

#Shroom: Banditter
def banditt_q1(navn):
    return "    Hei! Hva heter du? " + navn + """ ja, nettopp!
    Om du vil diskutere vår angrepsstrategi mot magikerne, må du snakke med
    Bjarte Banditt. Ellers har jeg et business-forslag som kan være svært gunstig
    for oss begge, og du ser ut som en som kan hjelpe meg!

    For ikke lenge siden stjelte jeg fire svært verdifulle lommeur. Men det er
    lite med ære blandt banditter, og noen har robbet dem fra meg mens jeg sov!
    Kan du banke opp noen banditter og se om du finner de for meg? Jeg har
    masse gullstykker jeg kan gi deg tilbake!

    -- Finn fire lommeur."""
def banditt_q1_ferdig(navn):
    return "    MOHAHA! *ond latter*\n" +\
    "    Tusen takk " + navn + """! Tenker de tenker seg om to ganger neste gang de lømmlene bestemmer
    seg for å ikke invitere meg med på lommeur-jakt!\n"""

def banditt_q2(navn):
    return """    Hei du!
    Du ser ut som en kapabel banditt som er godt kjent med sverdfekternes
    eldgamle kampkunster. Kan du vise meg dine triks? Du skjønner det at
    Fagre Frida, den vakreste, smarteste, mest fantastiske personen som noen
    gang har vandret på denne jord, kun er interessert i dem som kan imponere
    med sverdbruken sin. Dessverre er dette en av mine svakere sider! Om jeg
    bare hadde vært like god til å svinge et sverd som jeg er til å knivstikke,
    lyge og bedra... Akk! Men, om jeg kan henge meg på deg en stund, observere
    dine triks og finesser, kanskje jeg da kan bli bedre?

    -- Kast Utforsk 6 ganger."""
def banditt_q2_ferdig(navn):
    return """\n    Neeeeeei, Fagre Frida!! Du din lømmel! Bare ikke ta sverdet mitt når jeg
    dør! Din snik, jeg skal kv- aaaaargh *Ussle Ulv dør på dramatisk vis*\n"""

def banditt_q3(navn):
    return "    Hei " + navn + """!
    Har du hørt om soppen? Den magiske soppen som bor her iblandt oss? De passer
    på oss når vi går oss vill, og holder oss trygge under deres hatt. De vet
    alt, og kjenner alle! De er i luften, i bakken, blandt åndene og blandt
    oss levende! Dra, min disippel, til soppstedet utenfor leiren her, og hør
    selv at de snakker direkte til deg!

    -- Dra til soppstedet og hør hva de magiske soppene har å si."""
def banditt_q3_ferdig(navn):
    return "    Deres vilje er vår lov! Vi må adlyde straks! Dra ut og finn disse trærne!\n"

def banditt_q4(navn):
    return "    Jaså " + navn + """, ikke helt forberedt?
    Enhver god banditt burde være mentalt tre steg foran byttet. Avledning,
    overraskelse og illusjoner, dette er mine spesialiteter! Vil du lære å
    finpusse din egen smidighet, forvirre fiendens sinn og stikke av med de
    saftigste byttene? Jeg kan vise deg hvordan man senker konsentrasjonen
    til fienden, se og lær!

    Skriv 'di' eller 'distraher' for å kaste Distraher på fienden!

    -- Distraher fiender 9 ganger."""
def banditt_q4_ferdig(navn):
    return "    Utmerket " + navn + """!
    med slike ferdigheter vil du nok raskt øke din fryktinngytenhet!\n"""

def banditt_q5(navn):
    return "    " + navn + """!
    For et strålende talent! Slik teknikk! Og så tiltrekkende hender!
    Jeg kunne ikke unngå å legge merke til hvor effektivt du slo ned den
    knivstikkende slasken Ussle Ulf. Si meg, er du interessert i å gjøre
    meg en tjeneste? Det har seg nemlig slik at eksen min, Onde Olga, har
    blitt særdeles hovmoden i det siste. Hun pleide å være tolererbar, men
    i det siste har hun blitt umotståel- ehm, utålelig! Hun burde virkelig
    bli jekket ned et par hakk, til felles gode for alle her i leiren. Hun
    pleier å henge ved duellringen, kanskje du kan offentlig bekjemper henne
    med dine fantastiske evner i ringen? Så kan vi se nærmere på dine evner
    privat etterpå.

    -- Bekjemp Onde Olga i duellringen."""
def banditt_q5_ferdig(navn):
    return "    For en lykkedag! Tusen takk " + navn + """!
    Onde Olga har startet å vise interesse for meg igjen! Jeg bare vet
    at vi kommer til å utrette virkelig grufulle ting sammen! Ekte
    kjærlighet er absolutt en sjelden vare, husk på det """ + navn + """.
    Vi to fikk aldri en sjanse sammen, men jeg er sikker på at den rette for
    deg er der ute et sted.\n"""

def banditt_q6(navn):
    return "    Hvem er du? Du ser ut som en " + navn + ". Yup, definitivt " + navn + """.
    Uansett hvem du er, her er vi alle felles banditter, og i disse harde tidene må
    vi banditter stå sammen mot de ondskapsfulle magikerne! De har alltid vært en
    pest og en plage, stanset våre robberier og jaget oss vekk til denne skogen.
    Men de har aldri direkte angrepet oss før, ikke slik som nå. Vi er ikke helt
    sikre på hva de har gjort, men denne ellers medgjørlige skogen har i det siste
    blitt... levende. På et vis. I tillegg har våre medbanditter oppført seg særdeles
    merkverdig i det siste. Jeg er sikker på at dette er Kjedelige Kjell sitt verk!
    Han er allerede notorisk for sin evne til å kjede folk til døde, men han er og
    gal etter alt som har med trær og natur å gjøre. Om bare han hadde vært
    'ordnet', kunne vi gått tilbake til vår vanlige tilværelse. Kan du ordne saken?
    Kutt av ham fingeren til bevis!

    -- Kutt av fingeren til Kjedelige Kjell og vis den til Bjarte Banditt."""
def banditt_q6_ferdig(navn):
    return "    Er dette den ekte fingeren til Kjedelige Kjell? Fantastisk " + navn + """!
    Dette må jo bety at deres utspekulerte planer om å gjøre skogen levende har
    kommet til en stopp. Utmerket! Angrep fra skogen vil opphøre, folk vil
    returnere til normalen, de hersens sopp-fanatikerne vil åpne øynene, kanskje
    til og med det store treet over oss som plutselig dukket opp vil trekke
    seg tilbak- """ + Fore.RED + "Hei " + navn + """. Vi har ventet på deg. Disse fjolsene er snart under
    vår kontroll, de vil ikke forstyrre dere lengre. Dette neket tar vi med
    oss. Vi vil sees igjen """ + navn + ". " + Style.RESET_ALL + """Huff da, jeg ble litt svimmel. Uansett, alt
    vil bli bra fremover, tusen takk! Jeg tror jeg skal ta meg en tur ut i
    skogen for å feire, jeg fikk plutselig veldig lyst på sopp...\n"""

def banditt_dq7(navn):
    return "    Hei " + navn + """!
    Mitt navn er Onde Olga, og jeg er den som styrer duellringen her.
    Du ser ut som en kapabel banditt, har du lyst til å teste deg? Heder
    og ære finner du nok ikke her, men du får muligheten til å vinne en
    fin slump gullstykker! Hvis du vinner da selvfølgelig, skulle du dø
    eller flykte før motstanderen er beseiret, mister du pengene som er
    krevd for deltakelse. Det koster 500 per kamp; desto verre odds, desto
    større vinnerlønn til deg.

    Siden du er ny her, starter du nederst på rangstigen. Om du takker ja,
    vil du bli satt opp mot Patetiske Patrick. Jeg har ingen tips å gi mot
    ham."""
def banditt_dq7_ferdig(navn):
    return "    Gratulerer med seieren " + navn + """! Nå skal det sies at Patetiske Patrick
    aldri har vunnet en eneste kamp før, så det sier ingenting om en
    spjæling som deg...\n"""

def banditt_dq8(navn):
    return "    Hei igjen " + navn + """.
    Denne gang settes du opp mot Store Sture. Han er en stor kar som tåler en
    støyt, så hold et øye med dine egne helsepoeng mens du hakker løs!"""
def banditt_dq8_ferdig(navn):
    return """    Store Sture har stamina, men ikke stort med angrepspotensiale. Du
    får vente til en senere anledning med å vise om du virkelig duger til noe.\n"""

def banditt_dq9(navn):
    return "    Nok en gang trekkes du mot duellringens vold og hete " + navn + """!
    Din neste motstander er en litt tøffere utfordring. Smidige Sandra har lært
    seg noen smidige triks, hun kan sette deg ut av spill og gjemme seg selv i
    mørket mens hun slikker sine sår. Ta fra henne konsentrasjonen slik at hun
    ikke kan gjemme seg noe sted! Om du trenger hjelp til det, snakk med Taktiske
    Tore."""
def banditt_dq9_ferdig(navn):
    return """    Hun kan være en skikkelig utfordring for de fleste, men klarte ikke
    å beseire deg """ + navn + ". Jeg får disiplinere henne selv i natt.\n"

def banditt_dq10(navn):
    return "    Denne gangen skal du nok få deg en utfordring " + navn + """!
    Kraftige Kari er sterkere enn folk flest, men sikter dårlig med slagene sine.
    Selv om hun er kraftig nok til å slå deg ut med noen få slag, så tåler hun ikke
    så mye selv. Noen godt plasserte angrep burde gjøre susen, og om du i tillegg
    klarer å oppholde henne så hun ikke kan angripe deg, er duellen over på null
    komma niks."""
def banditt_dq10_ferdig(navn):
    return "    Du begynner å komme deg " + navn + """, det må være jeg som har god påvirkning
    på deg. Nå har du bare en duellant igjen før duell-mester tittelen går til deg!\n"""

def banditt_dq11(navn):
    return "    Du er tilbake for en siste kamp " + navn + """!
    Dette er øyeblikket vi har ventet på, og din siste duellant er:
    Teite Tim! Og han er langt fra like inkapabel som mange av dine
    tidligere duellanter. Teite Tim har mangt et triks opp i ermet,
    bruk det du har lært så langt og gi meg en seier og en ny
    duell-mester!"""
def banditt_dq11_ferdig(navn):
    return "    Gratulerer " + navn + """!
    Den nye duell-mesteren er DEG! Og det hele er min fortjeneste! Godt jobbet
    Onde Olga! Jeg er virkelig av de snedigste, lureste og beste bandittene i
    denne leiren! Ser deg rundt om kring """ + navn + ", jeg skal feire meg selv!\n"

def banditt_dq12(navn):
    return """    HVA?!?!?
    Ønsker du å duellere meg? Hvordan våger du! Jeg som har reist deg fra sølen
    og oppdratt deg som min egen! Jeg har lært deg å duellere slik proffene
    gjør det, bedre enn proffene gjør det! Og nå snur du ryggen mot meg?

    Om det er slik vil ha det; Ta dine siste steg """ + navn + "!"
def banditt_dq12_ferdig(navn):
    return """    D- du har beseiret meg! Hvordan er det mulig?
    Hvem har sendt deg """ + navn + """?

    Fagre Frida altså. Hun er ikke så dum som hun ser ut,
    kanskje jeg burde gi henne en ny sjanse\n"""

#Overtrollmann Vassles quests:
def vassle_troll(navn):
    return "    Hei " + navn + """!
    Det har oppstått en ubalanse i magien på flere steder i verden.
    Dette er ikke bra! Om vi magikere ikke kan kontrollere magien, vil
    andre skapninger kunne dra nytte av den og. Om det skjer er alt håp
    ute! Vi må kvele magien i disse skapningene før de blir kraftige nok
    til å utslette menneskeheten, og dessuten finne ut hvorfor de har
    fått magiske evner i utgangspunktet.

    Jeg har sendt ut ... til fjellhytta for å utforske ubalansen som har
    oppstått i fjellkjeden der. Området er kjent for å være en typisk
    samleplass for troll. Kan du hjelpe ... i å finne og rette opp
    ubalansen der?

    -- Hjelp ... å finne og rette opp ubalansen med fjellhytta."""
def vassle_troll_ferdig(navn):
    return "    Du har vært en uvurderlig hjelp " + navn + """!
    Dette du sier er rart... stuff stuff stuff"""

def vassle_cerberus(navn):
    return "    Hei " + navn + """!
    Det har oppstått en ubalanse i magien på flere steder i verden.
    Dette er ikke bra! Om vi magikere ikke kan kontrollere magien, vil
    andre skapninger kunne dra nytte av den og. Om det skjer er alt håp
    ute! Vi må kvele magien i disse skapningene før de blir kraftige nok
    til å utslette menneskeheten, og dessuten finne ut hvorfor de har
    fått magiske evner i utgangspunktet.

    Jeg har sendt ut ... til vulkanen for å utforske ubalansen som har
    oppstått der. Det har blitt sett svære hunder med opptil flere hoder
    i den regionen før, så vær klar! Kan du hjelpe ... i å finne og rette
    opp ubalansen der?

    -- Hjelp ... å finne og rette opp ubalansen med vulkanen."""
def vassle_cerberus_ferdig(navn):
    return "    Du har vært en uvurderlig hjelp " + navn + """!
    Dette du sier er rart... stuff stuff stuff"""

def vassle_gargyl(navn):
    return "    Hei " + navn + """!
    Det har oppstått en ubalanse i magien på flere steder i verden.
    Dette er ikke bra! Om vi magikere ikke kan kontrollere magien, vil
    andre skapninger kunne dra nytte av den og. Om det skjer er alt håp
    ute! Vi må kvele magien i disse skapningene før de blir kraftige nok
    til å utslette menneskeheten, og dessuten finne ut hvorfor de har
    fått magiske evner i utgangspunktet.

    Jeg har sendt ut Zap til slottet i enden av skogen her for å utforske
    ubalansen som har oppstått der. Vi er ikke helt sikker på hva som
    er senter for ubalansen, men vi har hørt merkelige rapporter om
    livløse objekter komme til live og skade beboerne av slottet der.
    Dessuten har all kontakt blitt brutt for noen dager siden. Kan du
    hjelpe Zap i å finne og rette opp ubalansen med slottet?

    -- Hjelp Zap å finne og rette opp ubalansen med slottet."""
def vassle_gargyl_ferdig(navn):
    return "    Tusen takk " + navn + """!
    Med dette problemet løst, har vi en mindre ting å tenke på. Likevel
    er det urovekkende å høre at det kanskje er en mystisk magiker som står
    bak det hele. Hva kan motivet være? Noe sier meg at disse problemene
    ikke vil ta en slutt før vi får stoppet denne magikeren. Men det må
    vi ta senere, for vi har flere problemer! En stor ubalanse har oppstått
    midt inne i skogen her, og det truer magi-borgen!\n"""

def vassle_shroom(navn):
    return "    Hei " + navn + """!
    Det har hendt noe svært mystisk. Et nytt utbrudd av ubalanse
    innen magien hendte i skogen her mens du var borte. Vi trodde
    først det var noen av Gaute Gnom den Grusommes mest trofaste
    følgere som hadde funnet en måte å tilnærme seg magi på, og
    sendte en liten gruppe for å undersøke saken. Vi har ikke sett
    dem siden, men det kom nettopp en budskapsrotte med beskjeden
    "skogen lever". Vi har prøvd å sende rotter tilbake, men ingen
    har overlevd turen, og nå streiker de igjen grunnet 'for høy
    yrkesrisiko'. Alt håp henger på dine skuldre """ + navn + """! Finn ut
    hva som har skjedd med ekspedisjonen, og rett opp ubalansen!

    -- Finn ekspedisjonen og rett den magiske ubalansen i skogen."""
def vassle_shroom_ferdig(navn):
    return "    Du er en helt " + navn + """!
    Denne magikeren, 'den Barmhjertige' er en pest og en plage og må
    stanses omgåelig! Vær forsiktig med den informasjonen du tilegner
    deg fra hans agenter, jeg tror vi har å gjøre med en magiker jeg
    kjente en gang for lenge siden, og han er en manipulerende løgner
    som benytter alle midler for å oppnå sine egne syke drømmer! Lukk
    sinnet for hans galne ambisjoner før de går til hodet på deg og.\n"""
