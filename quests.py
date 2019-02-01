from colorama import *

def hentQuest(path):
     try:
          with open('rec/quests/{}.txt'.format(path)) as f:
               return f.read()
     except FileNotFoundError:
          print('Fant ikke quest under stien {}'.format(path))

#Quest relatert til gnomene:
def q1(navn):
    return hentQuest('gnom/gnom1/start').format(navn=navn)

def q1ferdig(navn):
    return hentQuest('gnom/gnom1/ferdig').format(navn=navn)

def q2(navn):
    return hentQuest('gnom/gnom2/start').format(navn=navn)

def q2ferdig(navn):
    return hentQuest('gnom/gnom2/ferdig').format(navn=navn)

def q3(navn):
    return hentQuest('gnom/gnom3/start').format(navn=navn)

def q3ferdig(navn):
    return hentQuest('gnom/gnom3/ferdig').format(navn=navn)

def q4(navn):
    return hentQuest('gnom/gnom4/start').format(navn=navn)

def q4ferdig(navn):
    return hentQuest('gnom/gnom4/ferdig').format(navn=navn)

def q5(navn):
    return hentQuest('gnom/gnom5/start').format(navn=navn)

def q5ferdig(navn):
    return hentQuest('gnom/gnom5/ferdig').format(navn=navn)

def q6(navn):
    return hentQuest('gnom/gnom6/start').format(navn=navn)

def q6ferdig(navn):
    return hentQuest('gnom/gnom6/ferdig').format(navn=navn)

def bonus_q1(navn):
    return hentQuest('gnom/bonus/bonus1/start').format(navn=navn)

def bonus_q1ferdig(navn):
    return hentQuest('gnom/bonus/bonus1/ferdig')

def bonus_q2(navn):
    return hentQuest('gnom/bonus/bonus2/start').format(navn=navn)

def bonus_q2ferdig(navn):
    return hentQuest('gnom/bonus/bonus2/ferdig')

#Gargyl:
def garg_q1(navn):
    return hentQuest('gargyl/gargyl1/start').format(navn=navn)

def garg_q1_ferdig(navn):
    return hentQuest('gargyl/gargyl1/ferdig')

def garg_q2(navn):
    return hentQuest('gargyl/gargyl2/start').format(navn=navn)

def garg_q2_ferdig(navn):
    return hentQuest('gargyl/gargyl2/ferdig').format(navn=navn)

def garg_q3(navn):
    return hentQuest('gargyl/gargyl3/start').format(navn=navn)

def garg_q3_ferdig(navn):
    return hentQuest('gargyl/gargyl3/ferdig').format(navn=navn)

def garg_q4(navn):
    return hentQuest('gargyl/gargyl4/start').format(navn=navn)

def garg_q4_ferdig(navn):
    return hentQuest('gargyl/gargyl4/ferdig')

def garg_q5(navn):
    return hentQuest('gargyl/gargyl5/start').format(navn=navn)

def garg_q5_ferdig(navn):
    return hentQuest('gargyl/gargyl5/ferdig').format(navn=navn)

def garg_q6(navn):
    return hentQuest('gargyl/gargyl6/start').format(navn=navn)

def garg_q6_ferdig(navn):
    return hentQuest('gargyl/gargyl6/ferdig').format(navn=navn)

def garg_bq1(navn):
    return hentQuest('gargyl/bonus/bonus1/start').format(navn=navn)

def garg_bq1_ferdig(navn):
    return hentQuest('gargyl/bonus/bonus1/ferdig')

#Troll:
def troll_q1(navn):
    return hentQuest('troll/troll1/start').format(navn=navn)

def troll_q1_ferdig(navn):
    return hentQuest('troll/troll1/ferdig').format(navn=navn)

def troll_q2(navn):
    return hentQuest('troll/troll2/start').format(navn=navn)

def troll_q2_ferdig(navn):
    return hentQuest('troll/troll2/ferdig').format(navn=navn)

def troll_q3(navn):
    return hentQuest('troll/troll3/start').format(navn=navn)

def troll_q3_ferdig(navn):
    return hentQuest('troll/troll3/ferdig').format(navn=navn)

def troll_q4(navn):
    return hentQuest('troll/troll4/start').format(navn=navn)

def troll_q4_ferdig(navn):
    return hentQuest('troll/troll4/ferdig').format(navn=navn)

def troll_bq1(navn):
    return hentQuest('troll/bonus/bonus1/start')

def troll_bq1_ferdig(navn):
    return hentQuest('troll/bonus/bonus1/ferdig')

#Cerberus
def cerberus_q1(navn):
    return "    Hei, " + navn + """!
    Velkommen til Obsidian Forskningslab. Jeg er Dr. Frederikk.
    Vi er her for å undersøke opphavet til de voldelige hundene som har dukket opp
    i området. Alt vi har fått vite gjennom rykter er at hundene blir ledet av en
    trehodet hund, som vi har valgt å kalle "Cerberus". Selv om denne informasjonen
    ikke er helt solid, så har vi kunnet bekrefte at hundene blir ledet telepatisk
    av et ukjent vesen. Ellers har vi ikke gjort mye fremgang, untatt i forhold til
    forsvar mot disse hundene.

    Du har kanskje lagt merke til at de er immune mot ild og varme. De setter ofte
    fyr på seg selv for å øke angrepsstyrke og å skremme bort fiender. Det er vanskelig
    å kjempe mot en fiende som brenner. Derfor har vi utviklet en formel for å slukke
    flammene. Vi har valgt å kalle formelen for "Nedkjøl". Den krever litt øvelse for
    å mestre, men fra det jeg har hørt fra gode gamle Vassle, er du et naturtalent.
    Jeg tror du bare trenger å øve på å kaste formelen fem ganger før du kan bruke det
    uten problemer.

    -- Slukk ilden til 5 helveteshunder."""
def cerberus_q1_ferdig(navn):
    return "    Utrolig, " + navn + """!
    Vassle sa du var en flink magiker, men det var en vits når jeg sa at du kunne
    mestre det på fem ganger! Mesteparten av forskerne her brukte måneder på å treffe
    med 75% treffsikkerhet!\n"""

def cerberus_q2(navn):
    return "    Greit, " + navn + """!
    Nå som du har lært deg å forsvare deg mot disse nye og uforutsigbare fiendene
    har vi et oppdrag for deg. Grunnet de telepatiske evnene til "Cerberus" har
    tre helveteshunder flyktet forskningslaben. Vi har merket at lederen er meget
    intellegent og kan se alt som undersåttene kan se.

    De hundene var del av et klassifisert forskningsprosjekt, som har som mål å
    spore de telepatiske signalene fra undersåttene tilbake til "Cerberus".
    Vi var på kanten av en stor oppdagelse når de slapp ut bakdøra. Vi trenger
    de bikkjene! Gå rundt vulkanen og finn forskningseksemplarene. De burde ha
    en Obsidian-logo brent inn i hofta.

    -- Finn 3 helveteshunder med en Obsidian-logo på hofta"""
def cerberus_q2_ferdig(navn):
    return "    Strålende arbeid" + navn + """!
    Endelig kan vi spore de signalene tilbake! Vi trenger litt kalibrering og vi
    må tweeke litt på algoritmene, men vi er på grensen av et massivt gjennombrudd!
    """

def cerberus_q3(navn):
    return "    Eureka, " + navn + """!!!
    Vi har funnet "Cerberus"!!! Signalene leder tilbake til en krystallhule ikke
    langt herifra. Den første gruppen med speidere vi sendte har ikke rapportert
    tilbake. Når vi sendte gruppe #2 fant de de forbrente likene til gruppe #1.

    Dette er vår sjanse til å undersøke og tilpasse kreftene til "Cerberus".
    Gå inn i den hulen og hent meg "Cerberus"!

    -- Underforsk krystallhulen."""
def cerberus_q3_ferdig(navn):
    return """    Hæææ!!!
    Var ikke "Cerberus" i hulen!? Er du sikker på at den ikke slapp unna, du
    inkompetente nek! Jeg skal passe på at Vassle aldri kaller på dine tjenester
    igjen! Her har jeg gjort min banebrytene forskning og vært på forkanten av
    menneskeheten, mens du bare har gått rundt og slått ut noen søte små valper,
    så kan du ikke engang finne meg et ordentlig eksemplar!? Fjern deg frå synet mitt!

    Å! Så du fant noe annet i hulen... En krystall... Denne er interressant...

    Kjempebra arbeid, """ + navn + """! Jeg skjønner hvorfor Vassle har så gode ting å si
    om deg! Det er så godt å være rundt kompetente profesjonelle! Jeg tror jeg kan
    lære nok om denne krystallen for å finne plasseringen til "Cerberus"!
    """

def cerberus_q4(navn):
    return "    " + navn + """!!! Min favorittmagiker!
    Jeg har jobbet hardt og enestående bra på å finne en måte å bruke krystallen
    til å lokalisere "Cerberus". Det hadde tatt årevis for alle som ikke har mitt
    geni, men jeg har funnet en strategi!

    1) Først innså jeg at det var noe rart som skjedde når jeg plasserte andre
    krystaller i nærheten av den store krystallen. De hadde endret farge i komplett
    synkronitet. På den måten kunne jeg se at de alle var forbundet. Fra dette begynte
    forskningen min på den utrolige Keezzller-Bong-effekten som krystallene stråler.
    De er forbundet i en type bethorgatansk vis. Konfigurasjonen er helt absurd,
    men fascinerende! Jeg husker jeg drømte om slike beta-dismaliserte Krack-Baller
    svingninger når jeg ikke ble invitert til Senile Sverres bursdagfest i tredjeåret
    på magikerskolen... på en krogo-partisan måte finnes det ingen forbindelse mellom...
    og ingen elsker pseudo-euretiske kvaliteter like mye som meg!... IKKE SOV, HØR
    PÅ GENIET MITT!!!

    2) Det andre jeg innså var at jeg kunne bruke minoritetsladningsbærerdiffusjonskoeffisientmålingsapparaturer
    til å måle disse diminutive forskjellene i mellom avstanden må krystallene når
    de plasseres lenger vekk fra hverandre. Det krevde en del arbeid, men det førte
    til min nye oppfinnelse! Det er en enkel minoritetsladningsbærerdiffusjonskoeffisientmålingsapparatur
    som sammler og sammenligner enorme mengder atomære data i samtid ved hjelp
    eksperimentell kvantesammenfiltring. Ikke noe fancy eller utstående, men det
    får jobben gjort!

    Kort sagt så trenger jeg at du plasserer to av mine nettopp navngitte
    frederikk-krystallkvantesammenfiltringsminoritetsladningsbærerdiffusjonskoeffisientmålingsapparaturer
    helt på insiden av to forskjellig krystallhuler på motsatte sider av vulkanen.
    Den tredje plasserer jeg her i laboratoriet. På den måten kan vi triangulere
    posisjonen til "Cerberus" og få oss et ordentlig forskningsprosjekt.

    -- Plasser 2 minoritetsladningsbærer-hvadetnåvarigjen."""
def cerberus_q4_ferdig(navn):
    return "    " + navn + """!!! Du er tilbake!
    Dataene strømmer inn! Nå som frederikk-krystallkvantesammenfiltringsminoritetsladningsbærerdiffusjonskoeffisientmålingsapparaturene
    er satt inn i riktige posisjoner får vi så klart perfekte og dynamisk live
    informasjon om "Cerberus" sine koordinater! Jeg gjør aldri feil.
    """

def cerberus_q5(navn):
    return "    Nå, " + navn + """, skal alt det harde arbeidet mitt bære resultater!
    Vi har konstant kunnskap om hvor vi kan finne Cerberus, men alle skvadronene
    jeg har sendt til å fange den har endt opp fritert. Jeg tviler på at du kan
    få til dette, så uerfaren som du er, men jeg har ikke flere bønder, så vel vel.

    Jeg sender deg med en skvadron til å fange "Cerberus", men du får ta ned monsteret
    selv. Skvadronene har dannet en jævla fagforening. De gidder ikke "å bli behandlet
    som prøvekaniner". Likevel gjør ikke du noe så tåpelig, så gå dø eller vinn!
    Helst vinn, så klart, men da må jeg betale deg...

    -- Fang Cerberus."""
def cerberus_q5_ferdig(navn):
    return "    Takk. Du er ferdig. Ta pengene dine og dra til Vassle med historier om geniet mitt.\n"

def cerberus_bq1(navn):
    return "    Hei, " + navn + """!
    Du lurer kanskje hva en marinbiolog gjør her ute på et sted uten vann. Det lurer
    jeg også på... Herr Overtrollmann Vassle har valgt å sette den fremste eksperten
    hans på akvatiske mikro-organismer på et sted hvor vann fordamper nesten umiddelbart.

    Det gir ikke så mye mening for meg, men jeg tror jeg har akkurat det jeg trenger
    for å overbevise Hans Ærede Overtrollmann Vassle om å bli overført til et annet
    sted. Hvilket som helst annet sted!

    Jeg oppdaget at den grønne, slimete og elastiske gørra som troll dekker seg
    med faktisk er alger! De lever i symbiose med trollene! Det er den største
    oppdagelsen i  livet mitt! Ikke spør hvordan jeg fant det ut...

    Jeg utførte min egen forskning på egen tid i hemmelighet fra Frederikk. Jeg
    hadde konkrete og repliserbare bevis! Så kom trollene... De snek seg inn i
    laboratoriet, fordi de ser på alle typer undersøkelse eller forskning på dem
    som farlig og unaturlig. Nå har de stjålet arbeidet mitt, som jeg trenger for
    å komme meg ut herifra! De har nok spredt sidene rundt vulkanen. Vær så snill,
    hjelp meg finne livsverket mitt!

     -- Finn 5 seksjoner av forskningsmateriale.\n"""
def cerberus_bq1_ferdig(navn):
    return "    Du fant det! Jeg trodde jeg måtte starte fra bunnen av!\n"

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
    return """    Flott! Du finner vårt hovedkontor ned kjelleren fra forskningslaben.
    Der driver vi litt... forskning på si. Vi produserer iallefall helt kanon konsentrasjonspulver!
    Snakkes der!\n"""

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

    Jeg har sendt ut Zip til fjellhytta for å utforske ubalansen som har
    oppstått i fjellkjeden der. Området er kjent for å være en typisk
    samleplass for troll. Kan du hjelpe Zip i å finne og rette opp
    ubalansen der?

    -- Hjelp Zip å finne og rette opp ubalansen med fjellhytta."""
def vassle_troll_ferdig(navn):
    return "    Du har vært en uvurderlig hjelp " + navn + """!
    Dette du sier om en magiker som støtter trollene er urovekkende,
    men vi har dessverre ikke tid til å undersøke dette nå. En ny krise
    har oppstått, denne gangen mye nærmere oss! En stor ubalanse har
    oppstått midt inne i skogen her, og det truer magi-borgen!\n"""

def vassle_cerberus(navn):
    return "    Hei " + navn + """!
    Det har oppstått en ubalanse i magien på flere steder i verden.
    Dette er ikke bra! Om vi magikere ikke kan kontrollere magien, vil
    andre skapninger kunne dra nytte av den og. Om det skjer er alt håp
    ute! Vi må kvele magien i disse skapningene før de blir kraftige nok
    til å utslette menneskeheten, og dessuten finne ut hvorfor de har
    fått magiske evner i utgangspunktet.

    Jeg har sendt ut Forsker Frederikk til vulkanen for å utforske ubalansen
    som har oppstått der. Stedet pleide å være fullt av troll, men Dr. Frederikk
    har rapportert om at svære brennende hunder har blitt mer og mer dominerende
    der i det siste. I tillegg virker de koordinerte, noe som ikke er vanlig
    oppførsel for slike hunder. Kan du hjelpe Forsker Frederikk i å finne og
    rette opp ubalansen der?

    -- Hjelp Forsker Frederikk å finne og rette opp ubalansen med vulkanen."""
def vassle_cerberus_ferdig(navn):
    return "    Tusen takk for at du har holdt ut Forsker Frederikk så langt " + navn + """!
    Dette med telepati er virkelig spennende saker, om vi kan både stoppe Cerberus
    og helveteshundene fra å benytte seg av det, og få kontroll på den selv, er
    dette et stort skritt i vår kamp for overlevelse! Likevel er det høyst
    urovekkende å høre om denne magikeren. Men det får vi ta siden, det har
    oppstått en ny ubalanse, og denne gangen truer det magi-borgen direkte!\n"""

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
