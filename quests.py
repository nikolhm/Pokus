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
    return hentQuest('cerberus/cerberus1/start').format(navn=navn)

def cerberus_q1_ferdig(navn):
    return hentQuest('cerberus/cerberus1/ferdig').format(navn=navn)

def cerberus_q2(navn):
    return hentQuest('cerberus/cerberus2/start').format(navn=navn)

def cerberus_q2_ferdig(navn):
    return hentQuest('cerberus/cerberus2/ferdig').format(navn=navn)

def cerberus_q3(navn):
    return hentQuest('cerberus/cerberus3/start').format(navn=navn)

def cerberus_q3_ferdig(navn):
    return hentQuest('cerberus/cerberus3/ferdig').format(navn=navn)

def cerberus_q4(navn):
    return hentQuest('cerberus/cerberus4/start').format(navn=navn)

def cerberus_q4_ferdig(navn):
    return hentQuest('cerberus/cerberus4/ferdig').format(navn=navn)

def cerberus_q5(navn):
    return hentQuest('cerberus/cerberus5/start').format(navn=navn)

def cerberus_q5_ferdig(navn):
    return hentQuest('cerberus/cerberus5/ferdig')

def cerberus_bq1(navn):
    return hentQuest('cerberus/bonus/bonus1/start').format(navn=navn)

def cerberus_bq1_ferdig(navn):
    return hentQuest('cerberus/bonus/bonus1/ferdig')

#Spesialiseringsquests
def smertedreper_intro(navn):
    return hentQuest('spesialisering/smertedreper/start').format(navn=navn)

def smertedreper_intro_ferdig(navn):
    return hentQuest('spesialisering/smertedreper/ferdig').format(navn=navn)

def klartenker_intro(navn):
    return hentQuest('spesialisering/klartenker/start').format(navn=navn)

def klartenker_intro_ferdig(navn):
    return hentQuest('spesialisering/klartenker/ferdig')

def muskelbunt_intro(navn):
    return hentQuest('spesialisering/muskelbunt/start').format(navn=navn)

def muskelbunt_intro_ferdig(navn):
    return hentQuest('spesialisering/muskelbunt/ferdig').format(navn=navn)

#Shroom:
def shroom_q1(navn):
    return hentQuest('shroom/shroom1/start').format(navn=navn)

def shroom_q1_ferdig(navn):
    return hentQuest('shroom/shroom1/ferdig').format(navn=navn)

def shroom_q2(navn):
    return hentQuest('shroom/shroom2/start').format(navn=navn)

def shroom_q2_ferdig(navn):
    return hentQuest('shroom/shroom2/ferdig').format(navn=navn)

def shroom_q3(navn):
    return hentQuest('shroom/shroom3/start').format(navn=navn)

def shroom_q3_ferdig(navn):
    return hentQuest('shroom/shroom3/ferdig').format(navn=navn)

def shroom_q4(navn):
    return hentQuest('shroom/shroom4/start').format(navn=navn)

def shroom_q4_ferdig(navn):
    return hentQuest('shroom/shroom4/ferdig').format(navn=navn)

def shroom_q5(navn):
    return hentQuest('shroom/shroom5/start').format(navn=navn)

def shroom_q5_ferdig(navn):
    return hentQuest('shroom/shroom5/ferdig').format(navn=navn)

def shroom_q6(navn):
    return hentQuest('shroom/shroom6/start').format(navn=navn)

def shroom_q6_ferdig(navn):
    return hentQuest('shroom/shroom6/ferdig').format(navn=navn)

def shroom_q7(navn):
    return hentQuest('shroom/shroom7/start').format(navn=navn)

def shroom_q7_ferdig(navn):
    return hentQuest('shroom/shroom7/ferdig').format(navn=navn)

def shroom_q8(navn):
    return hentQuest('shroom/shroom8/start').format(navn=navn)

def shroom_q8_ferdig(navn):
    return hentQuest('shroom/shroom8/ferdig').format(navn=navn)

def shroom_q9(navn):
    return hentQuest('shroom/shroom9/start').format(navn=navn)

def shroom_q9_ferdig(navn):
    return hentQuest('shroom/shroom9/ferdig')

def shroom_q10(navn):
    return hentQuest('shroom/shroom10/start').format(navn=navn)

def shroom_q10_ferdig(navn):
    return hentQuest('shroom/shroom10/ferdig').format(navn=navn)

def shroom_bq1(navn):
    return hentQuest('shroom/bonus/bonus1/start')

def shroom_bq1_ferdig(navn):
    return hentQuest('shroom/bonus/bonus1/ferdig').format(navn=navn)

def shroom_bq2(navn):
    return hentQuest('shroom/bonus/bonus2/start')

def shroom_bq2_tekst():
    return hentQuest('shroom/bonus/bonus2/ferdig')

def shroom_bq3(navn):
    return hentQuest('shroom/bonus/bonus3/start').format(navn=navn)

def shroom_bq3_tekst():
    return hentQuest('shroom/bonus/bonus3/ferdig')

def kjellprat():
    return hentQuest('shroom/bonus/kjellprat')

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
