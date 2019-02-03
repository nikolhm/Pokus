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
    return hentQuest('shroom/banditt/banditt1/start').format(navn=navn)

def banditt_q1_ferdig(navn):
    return hentQuest('shroom/banditt/banditt1/ferdig').format(navn=navn)

def banditt_q2(navn):
    return hentQuest('shroom/banditt/banditt2/start')

def banditt_q2_ferdig(navn):
    return hentQuest('shroom/banditt/banditt2/ferdig')

def banditt_q3(navn):
    return hentQuest('shroom/banditt/banditt3/start').format(navn=navn)

def banditt_q3_ferdig(navn):
    return hentQuest('shroom/banditt/banditt3/ferdig')

def banditt_q4(navn):
    return hentQuest('shroom/banditt/banditt4/start').format(navn=navn)

def banditt_q4_ferdig(navn):
    return hentQuest('shroom/banditt/banditt4/ferdig').format(navn=navn)

def banditt_q5(navn):
    return hentQuest('shroom/banditt/banditt5/start').format(navn=navn)

def banditt_q5_ferdig(navn):
    return hentQuest('shroom/banditt/banditt5/ferdig').format(navn=navn)

def banditt_q6(navn):
    return hentQuest('shroom/banditt/banditt6/start').format(navn=navn)

def banditt_q6_ferdig(navn):
    return hentQuest('shroom/banditt/banditt6/ferdig').format(
         navn=navn,
         red=Fore.RED,
         reset=Style.RESET_ALL
     )

def banditt_dq7(navn):
    return hentQuest('shroom/banditt/duell/duell1/start').format(navn=navn)

def banditt_dq7_ferdig(navn):
    return hentQuest('shroom/banditt/duell/duell1/ferdig').format(navn=navn)

def banditt_dq8(navn):
    return hentQuest('shroom/banditt/duell/duell2/start').format(navn=navn)

def banditt_dq8_ferdig(navn):
    return hentQuest('shroom/banditt/duell/duell2/ferdig')

def banditt_dq9(navn):
    return hentQuest('shroom/banditt/duell/duell3/start').format(navn=navn)

def banditt_dq9_ferdig(navn):
    return hentQuest('shroom/banditt/duell/duell3/ferdig').format(navn=navn)

def banditt_dq10(navn):
    return hentQuest('shroom/banditt/duell/duell4/start').format(navn=navn)

def banditt_dq10_ferdig(navn):
    return hentQuest('shroom/banditt/duell/duell4/ferdig').format(navn=navn)

def banditt_dq11(navn):
    return hentQuest('shroom/banditt/duell/duell5/start').format(navn=navn)

def banditt_dq11_ferdig(navn):
    return hentQuest('shroom/banditt/duell/duell5/ferdig').format(navn=navn)

def banditt_dq12(navn):
    return hentQuest('shroom/banditt/duell/duell6/start').format(navn=navn)

def banditt_dq12_ferdig(navn):
    return hentQuest('shroom/banditt/duell/duell6/ferdig').format(navn=navn)

#Overtrollmann Vassles quests:
def vassle_troll(navn):
    return hentQuest('vassle/troll/start').format(navn=navn)

def vassle_troll_ferdig(navn):
    return hentQuest('vassle/troll/ferdig').format(navn=navn)

def vassle_cerberus(navn):
    return hentQuest('vassle/cerberus/start').format(navn=navn)

def vassle_cerberus_ferdig(navn):
    return hentQuest('vassle/cerberus/ferdig').format(navn=navn)

def vassle_gargyl(navn):
    return hentQuest('vassle/gargyl/start').format(navn=navn)

def vassle_gargyl_ferdig(navn):
    return hentQuest('vassle/gargyl/ferdig').format(navn=navn)

def vassle_shroom(navn):
    return hentQuest('vassle/shroom/start').format(navn=navn)

def vassle_shroom_ferdig(navn):
    return hentQuest('vassle/shroom/ferdig').format(navn=navn)
