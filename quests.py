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

#Troll:
def troll_q1(navn):
    return "    Hei, " + navn + """!
    Det er uhyre mange troll rundt i dette området. Ettersom tiden har gått
    har vi blitt vant til det, men de har blitt mer og mer uredde i det siste.
    De har til og med gått så nærme som å pisse på bålet gjennom pipa. Vet du
    hvor mye ammoniak det der lukter!? Uansett, skjønner vi at for å sette litt
    brems på selvsikkerheten deres, bør vi true dem litt. Jeg tenker et lite
    folkemord bør gjøre dem litt redde. Gå ut og drep 25 troll. Menn, kvinner
    og barn. Det er ikke så vanskelig. Man ser ikke forskjell på dem uansett!

    -- Myrd 25 troll uten nåde."""
def troll_q1_ferdig(navn):
    return "    Tusen takk, " + navn + """!
    Det er så fint å kjenne en magiker som ikke bøyer til slike ubrukelige ting
    som "moral og etikk". Det er oss eller dem. De angriper oss uansett om de er
    kvinner eller barn og da må vi beskytte oss selv. Jeg lurer på hvorfor de gjør
    det i det første uansett...
    """

def troll_q2(navn):
    return "    Hei, pssst! " + navn + """!
    Det er meg! Zip! Ikke vær lurt av forkledningen min. Jeg må late som jeg er en
    gammel trollmann for å komme inn i badstua. Trollmennene her er sjåvinistiske
    relikker med foreldete verdier. Hvis jeg ikke later som jeg er mann, blir jeg
    bare ignorert. "Lag meg en sandwich, heks!" "Jeg har lyst til å dyppe staven
    min i det der, hvis du skjønner hva jeg mener!" De er absolutt motbydelige!

    Likevel må jeg finne ut hva de vet om trollene. Jeg har overhørt noe prat om
    å dra ned til den gamle minen å rydde ut noen av de sterkere trollene. Disse
    gamle fjertene snakker om å gjøre det, men de bare snakker og snakker og gjør
    niks. Kan du gå ned i minen og drepe et digert troll? Jeg tror du kan finne
    noen informasjon om lederen av trollene. Vi vet overraskende lite om ham...

    -- Dra ned i minen og drep et digert troll."""
def troll_q2_ferdig(navn):
    return "    Hei, " + navn + """!
    Så du fant et skriv på trollet? Det er veldig vanskelig å lese trollsk, men
    jeg kan tyde hovedpunktene, med manglende nøyaktighet. Det står noe i duren
    av... *spyr* Å nei! For helvete! Hva er galt med dem?! Trollene skriver
    alt i form av vemmeligheter. Det er helt frastøtende! Likeve *blæææh* ser
    jeg at trollet fikk ordre om å *surt oppstøt* til Helvetesgapet. Det må være
    der Trollkongen befinner seg. Jeg har hørt at ingen av gamlingene tør å gå
    ned dit. Det er visst, for farlig med faren for steinras... For noen pyser!
    """

def troll_q3(navn):
    return "    Hei, " + navn + """!
    Nå som vi vet hvor trollkongen er kan vi ta ham ned. Du må likevel være
    forsiktig. Jeg har hørt at han har veldig sterk magi. Du vet aldri hva han
    har opp ermet...
    """

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
    return ""

def shroom_bq1(navn):
    return """    Salig er du, som får oppleve nærværet deres!
    Men det er ikke nok, vi må ha mer. MER! Javisst, våre overordnede er ikke
    fornøyd med vår innsats. Vi må vise mer dedikasjon! MER! Vi trenger noe
    håndfast vi kan bruke til å tilbe dem på, et totem eller noe slikt!
    Har du sett noe slikt rundt omkring?
    """
def shroom_bq1_ferdig(navn):
    return """    Fantastisk! Dommedagen er snart på oss, og det er viktig å vise soppen
    hvilken side vi egentlig står på! Bli med meg, """ + navn + " i et kjapt blodoffer!\n"

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
    return """Hei du!
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
    pleier å henge med duellringen, kanskje du kan offentlig bekjemper henne
    med dine fantastiske evner i ringen? Så kan vi se nærmere på dine evner
    privat etterpå.

    -- Bekjemp Onde Olga i duellringen."""
def banditt_q5_ferdig(navn):
    return ""

def banditt_q6(navn):
    return "    Hvem er du? Du ser ut som en " + navn + ". Yup, definitivt " + navn + """".
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
    return ""

def banditt_dq7(navn):
    return "Duellring 1"
def banditt_dq7_ferdig(navn):
    return "Nice!"

def banditt_dq8(navn):
    return "Duellring 2"
def banditt_dq8_ferdig(navn):
    return "Nice!"

#Overtrollmann Vassles quests:
def vassle_troll(navn):
    return "    Hei " + navn + """!
    Det har oppstått en ubalanse i magien på flere steder i verden.
    Dette er ikke bra! Om vi magikere ikke kan kontrollere magien, vil
    andre skapninger kunne dra nytte av den og. Om det skjer er alt håp
    ute! Vi må kvele magien i disse skapningene før de blir kraftige nok
    til å utslette menneskeheten, og dessuten finne ut hvorfor de har
    fått magiske evner i det første.

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
    fått magiske evner i det første.

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
    fått magiske evner i det første.

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
    er urovekkende å høre at det kanskje er en mystisk magiker som står
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
    yrkesrisiko'. Alt håp henger på dine skuldre """ + navn + """! Finn
    ut hva som har skjedd med ekspedisjonen, og rett opp i ubalansen!

    -- Finn ekspedisjonen og rett den magiske ubalansen i skogen."""
def vassle_shroom_ferdig(navn):
    return "    Du er en helt " + navn + """!
    Denne magikeren er en pest og en plage og må stanses omgåelig!\n"""
