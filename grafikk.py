from random import randint
from colorama import *
from prosedyrer import *
import os
import time
import platform
import sys

init()

def skrivTittel():
    frames = ["""
**********************************************************************************************************************************************

                                                                                                                            ____
                                                                                                                          .'* *.'
                                                                                                                       __/_*_*(_
                                                                                                                      / _______ \\
                                                                                                                     _\_)/___\(_/_
                                                                                                                    / _((\o o/))_ \\
                                                                                                                    \ \())(-)(()/ /
                                                                                                                     ' \(((()))/ '
                                                                                                                    / ' \)).))/ ' \\
                                                                                                                    / _ \ - | - /_  \\
                                                                                                                   (   ( .;''';. .'  )
                                                                                                                   _\\"__ /    )\ __"/_
                                                                                                                     \/  \   ' /  \/
                                                                                                                      .'  '...' ' )
                                                                                                                      / /  |  \ \\
                                                                                                                     / .   .   . \\
                                                                                                                    /   .     .   \\
                                                                                                                   /   /   |   \   \\
                                                                                                                 .'   /    b    '.  '.
                                                                                                             _.-'    /     Db     '-. '-._
                                                                                                         _.-'       |      DDb       '-.  '-.
                                                                                                        (_______mrf/\____.dDDDb.________)____)
**********************************************************************************************************************************************
"""]

    ferdig = """
**********************************************************************************************************************************************

PPPPPPPPPPPPPPPPP         OOOOOOOOO      KKKKKKKKK    KKKKKKK UUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS                       ____
P::::::::::::::::P      OO:::::::::OO    K:::::::K    K:::::K U::::::U     U::::::U  SS:::::::::::::::S                   .'* *.'
P::::::PPPPPP:::::P   OO:::::::::::::OO  K:::::::K    K:::::K U::::::U     U::::::U S:::::SSSSSS::::::S                __/_*_*(_
PP:::::P     P:::::P O:::::::OOO:::::::O K:::::::K   K::::::K UU:::::U     U:::::UU S:::::S     SSSSSSS               / _______ \\
  P::::P     P:::::P O::::::O   O::::::O KK::::::K  K:::::KKK  U:::::U     U:::::U  S:::::S                          _\_)/___\(_/_
  P::::P     P:::::P O:::::O     O:::::O   K:::::K K:::::K     U:::::D     D:::::U  S:::::S                         / _((\o -/))_ \\
  P::::PPPPPP:::::P  O:::::O     O:::::O   K::::::K:::::K      U:::::D     D:::::U   S::::SSSS                      \ \())(-)(()/ /
  P:::::::::::::PP   O:::::O     O:::::O   K:::::::::::K       U:::::D     D:::::U    SS::::::SSSSS                  ' \(((()))/ '
  P::::PPPPPPPPP     O:::::O     O:::::O   K:::::::::::K       U:::::D     D:::::U      SSS::::::::SS               / ' \)).))/ ' \\
  P::::P             O:::::O     O:::::O   K::::::K:::::K      U:::::D     D:::::U         SSSSSS::::S              / _ \ - | - /_  \\
  P::::P             O:::::O     O:::::O   K:::::K K:::::K     U:::::D     D:::::U              S:::::S            (   ( .;''';. .'  )
  P::::P             O::::::O   O::::::O KK::::::K  K:::::KKK  U::::::U   U::::::U               S:::::S           _\\"__ /    )\ __"/_
PP::::::PP           O:::::::OOO:::::::O K:::::::K   K::::::K  U:::::::UUU:::::::U  SSSSSSS     S:::::S              \/  \   ' /  \/
P::::::::P            OO:::::::::::::OO  K:::::::K    K:::::K   UU:::::::::::::UU   S::::::SSSSSS:::::S               .'  '...' ' )
P::::::::P              OO:::::::::OO    K:::::::K    K:::::K     UU:::::::::UU     S:::::::::::::::SS                / /  |  \ \\
PPPPPPPPPP                OOOOOOOOO      KKKKKKKKK    KKKKKKK       UUUUUUUUU        SSSSSSSSSSSSSSS                 / .   .   . \\
                                                                                                                    /   .     .   \\
                                                av                                                                 /   /   |   \   \\
                                                                                                                 .'   /    b    '.  '.
                                      Magic Wand Productions                                                 _.-'    /     Db     '-. '-._
                                                                                                         _.-'       |      DDb       '-.  '-.
                                                                                                        (_______mrf/\____.dDDDb.________)____)
**********************************************************************************************************************************************
    """
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

def skriv_ekorn1():
    print(""" ,;;:;,
   ;;;;;
  ,:;;:;    ,'=.
  ;:;:;' .=" ,'_\\
  ':;:;,/  ,__:=@
   ';;:;  =./)_
 jgs `"=\_  )_"`
          ``'"`""")

def skriv_ekorn2():
    print("""               _ _
    |\__/|  .~    ~.
    /  o `./      .'
   {o__,   \    {
     / .  . )    \\
     `-` '-' \    }
    .(   _(   )_.'
   '---.~_ _ _|""")

def skriv_ekorn3():
    print("""             __
              \ `-.
     __        )   \\
  .-'  `-._.--'    |
 /               _/
|    ___     __-'. .
|   '   `---<___/|/|
|     _          o  )
|      \   /  ,     |
\  `,   )  \  \-`-._|
 `-/   /---'>_/_\\
 '-`-__`-. '"   "
       "" jb""")

def skrivGnom():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.GREEN + """       ,      ,
      /(.-""-.)\\
  |\  \/      \/  /|
  | \ / =.  .= \ / |
  \( \   o\/o   / )/
   \_, '-/  \-' ,_/
     /   \__/   \\
     \ \__/\__/ /
   ___\ \|--|/ /___
 /`    \      /    `\\
/  jgs  '----'       \\""" + Style.RESET_ALL)

def skrivTrollmann():
    print("""                    ____
                  .'* *.'
               __/_*_*(_
              / _______ \\
             _\_)/___\(_/_
            / _((\o o/))_ \\
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \\
            / _ \ - | - /_  \\
           (   ( .;''';. .'  )
           _\\"__ /    )\ __"/_
             \/  \   ' /  \/
              .'  '...' ' )
              / /  |  \ \\
             / .   .   . \\
            /   .     .   \\
           /   /   |   \   \\
         .'   /    b    '.  '.
     _.-'    /     Db     '-. '-._
 _.-'       |      DDb       '-.  '-.
(_______mrf/\____.dDDDb.________)____)""")

def skrivOndTrollmann():
    print("""
                                           /\\
                     _                    |[]|
                  .'` `'.                 \\||/
                 /    ,-.\                 ||_
                /   /::::\\\\               /|//}
                |  |:::::||              |////}
                |  |:::::||             //'///
                |  |(::::||            //  ||'
                /(()()())|/        _,-//\  ||
               /`((()())))`-,__,-'`* |/  \ ||
             /`  (()((())))        * \   |||
           /`    (()())())|  *    *    |  /||
         |`   *   ()()()())        *   \ | ||
        |          \()()(/      ,.__  * \| ||
        /           `())      /`    `\   | ||
       |                     /        \  / ||
       |    *        *  *    |        | /  ||
       /         /           |        `(   ||
      /   *      .      *    /          )  ||
     |        *   \          |             ||
    /  *          |   *      /             ||
   |\      *  *  /          |              ||
   \/`-._   *   |       *   /              ||
    //   `.    /`           |              ||
   //`.    `. |   *       * \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/       *    *  |              ||
 ||||   ,'` )               /              //
 ||||  /    *   *           /             ||
 `\\\\` /`     *         *   |             //
     |`                *    \            ||
    /     *  *               |           //
  /` *             *      *   \         //
/`     *       jgs     *      |        ||
`-.___,-.      .-.        ___,'        (/""")

def skrivGargouille():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(""" ,                                                               ,
 \\'.                                                           .'/
  ),\                                                         /,(
 /__\\'.                                                     .'/__\\
 \  `'.'-.__                                           __.-'.'`  /
  `)   `'-. \                                         / .-'`   ('
  /   _.--'\ '.          ,               ,          .' /'--._   \\
  |-'`      '. '-.__    / \             / \    __.-' .'      `'-|
  \         _.`'-.,_'-.|/\ \    _,_    / /\|.-'_,.-'`._         /
   `\    .-'       /'-.|| \ |.-"   "-.| / ||.-'\       '-.    /`
     )-'`        .'   :||  / -.\\\\ //.- \  ||:   '.        `'-(
    /          .'    / \\\\_ |  /o`^'o\  | _// \    '.          \\
    \       .-'    .'   `--|  `"/ \"`  |--`   '.    '-.       /
     `)  _.'     .'    .--.; |\__"__/| ;.--.    '.     '._  ('
     /_.'     .-'  _.-'     \\\\ \/^\/ //     `-._  '-.     '._\\
     \     .'`_.--'          \\\\     //          `--._`'.     /
      '-._' /`            _   \\\\-.-//   _            `\ '_.-'
          `<     _,..--''`|    \`"`/    |`''--..,_     >`
           _\  ``--..__   \     `'`     /   __..--``  /_
          /  '-.__     ``'-;    / \    ;-'``     __.-'  \\
         |    _   ``''--..  \\'-' | '-'/  ..--''``   _    |
         \     '-.       /   |/--|--\|   \       .-'     /
          '-._    '-._  /    |---|---|    \  _.-'    _.-'
              `'-._   '/ / / /---|---\ \ \ \\'   _.-'`
                   '-./ / / / \`---`/ \ \ \ \.-'
                       `)` `  /'---'\  ` `(`
                      /`     |       |     `\\
                     /  /  | |  jgs  | |  \  \\
                 .--'  /   | '.     .' |   \  '--.
                /_____/|  / \._\   /_./ \  |\_____\\
               (/      (/'     \) (/     `\)      \)""")

def skrivGuri():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""    		 ,	           ,
                / \               / \\
              .//\ \             / /\\\\.
              |/vv\ \    _,_    / /vv\|
              ||   \ |.-"   "-.| /   ||
              || x  / -.\\\\ //.- \  x ||
              \\\\__  |  /o`^'o\  |  __//
               `----|  `"/ \\"`  |----`
                    ; |\__"__/| ;
                    \\\\  \/^\/  //
                     \\\\       //
                      \\\\/\./\//
                       \_` `_/
                         `"`""")

def skrivGravstein():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""                                          __.....__
                                        .'         ':,
                                       /  __  _  __  \\\\
                                       | |_)) || |_))||
                                       | | \\\\ || |   ||
                                       |             ||   _,
                                       |             ||.-(_{}
                                       |             |/    `
                                       |        ,_ (\;|/)
                                     \\\\|       {}_)-,||`
                                     \\\\;/,,;;;;;;;,\\\\|//,
                                    .;;;;;;;;;;;;;;;;,
                                   \,;;;;;;;;;;;;;;;;,//
                                  \\\\;;;;;;;;;;;;;;;;,//
                                 ,\\';;;;;;;;;;;;;;;;'
                                jgs;;;;;;;;;;;'''`""")

def skrivSkjellett():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""                 .-"```"-.
                /         \\
                |  _   _  |
                | (_\ /_) |
                (_   A   _)
                 | _____ |
                 \`"\"\"\"\"`/
                  '-.-.-'
                   _:=:_
            .-\"\"\"\"`_'='_`"\"\"\"-.
           (`,-- -`\   /`- --,`)
           / //`-_--| |--_-`\\\\ \\
          / /(_-_  _| |_  _-_)\ \\
         / / (_- __ \ / __ -_) \ \\
        / /  (_ -_ - ^ - _- _)  \ \\
       / /   (_-  _ /=\ _ - _)   \ \\
      / /     (_ -.':=:'. -_)     \ \\
     (`;`     (_-'  :=:  '-_)     `;`)
      \\\\.   jgs __  :=:  __       .//
       \\\\\    .'  `':=:'`  '.    ///
        \\\\\  |  .--. = .--.  |  ///
         \\\\\ |  (  / = \  )  | ///
          \\\\` \ _`' \=/ '`_ / `//
          ;`)  ( ;_/`v`\_; )  (`;
          |||\ | |       | | /|||
          |\\\\  | |       | |  //|
               | |       | |
               | |       | |
               | |       | |
               | |       | |
               | |       | |
              (._)       (_.)
               ||,       ,||
               ||:       :||
               ||:       :||
               ||:       :||
               ||:       :||
               ||'       '||
              ///)       (\\\\\\
            .///`         `\\\\\.
           `//`             `\\\\`""")

def skrivGaute():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.GREEN + """           ,           ,
          /(  .-\"\"\""-. )\\
      |\  \/           \/  /|
      | \ /     \  /    \ / |
      \( \      o\/o     / )/
       \_,    '-/  \-'   ,_/
         /     / __ \     \\
         \     \/  \/     /
       ___\     /--\\     /___
     /`    \            /    `\\
    /       '\\\\\\\\\\/////'       \\
   /         '\\\\\\\\////'         \\
  /            '\\\\//'            \\
 /       |  lgs  \/   nhm  |      \\""" + Style.RESET_ALL)



def skrivEnhjorning():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""                  <<<<>>>>>>           .----------------------------.
               _>><<<<>>>>>>>>>       /               _____________)
      \|/      \<<<<<  < >>>>>>>>>   /            _______________)
-------*--===<=<<           <<<<<<<>/         _______________)
      /|\     << @    _/      <<<<</       _____________)
             <  \    /  \      >>>/      ________)  ____
                 |  |   |       </      ______)____((- \\\\\\\\
                 o_|   /        /      ______)         \  \\\\\\\\    \\\\\\\\\\\\\\
                      |  ._    (      ______)           \  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                      | /       `----------'    /       /     \\\\\\\\\\\\\\     \\\\
              .______/\/     /                 /       /          \\\\\\
             / __.____/    _/         ________(       /\\
            / / / ________/`---------'         \     /  \_
           / /  \ \                             \   \ \_  \\
          ( <    \ \                             >  /    \ \\
           \/      \\\\_                          / /       > )
                    \_|                        / /       / /
                                             _//       _//
                                            /_|       /_|""")

def skrivFisk():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""                          .
                          A       ;
                |   ,--,-/ \---,-/|  ,
               _|\,'. /|      /|   `/|-.
           \`.'    /|      ,            `;.
          ,'\   A     A         A   A _ /| `.;
        ,/  _              A       _  / _   /|  ;
       /\  / \   ,  ,           A  /    /     `/|
      /_| | _ \         ,     ,             ,/  \\
     // | |/ `.\  ,-      ,       ,   ,/ ,/      \/
     / @| |@  / /'   \  \      ,              >  /|    ,--.
    |\_/   \_/ /      |  |           ,  ,/        \  ./' __:..
    |  __ __  |       |  | .--.  ,         >  >   |-'   /     `
  ,/| /  '  \ |       |  |     \      ,           |    /
 /  |<--.__,->|       |  | .    `.        >  >    /   (
/_,' \\\\  ^  /  \     /  /   `.    >--            /^\   |
      \\\\___/    \   /  /      \__'     \   \   \/   \  |
       `.   |/          ,  ,                  /`\    \  )
         \  '  |/    ,       V    \          /        `-\\
          `|/  '  V      V           \    \.'            \_
           '`-.       V       V        \./'\\
               `|/-.      \ /   \ /,---`\\
                /   `._____V_____V'
                           '     '""")

def skrivSlott():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    slott = """                      ___                                                    ___
                      T)))                       __,___,_                    T)))
                      |                          TT  )   )                   |
                     /T\                         ||  )   )                  /T\\
                    / L \                        ||-^--^-'                 / L \\
                   / [O] \                       ||                       / [O] \\
                  /   T   \                  _.+'||'+._                  /   T   \\
                 |____|____|             _.+'____/\____'+._             |____|____|
                   [_]|[_]              [_]_____[||]_____[_]              [_]|[_]
                  .[_]|[_].             [_]_____[||]_____[_]             .[_]|[_].
          ._._._._|IIIIIII|._._._._.___.====================.___._._._._.|IIIIIII|_._._._.
         /|\._./\|/   L   \|/._._.\|[_] \/   \II/[]\II/   \/ [_]|/._._.\|/   L   \|/\._./|\\
        []TTTTTTT[]==[O]==[]TTTTTTTT[_] /\_._.II_[]_II._._/\ [_]TTTTTTTT[]==[O]==[]TTTTTTT[]
        []|._._.|[]   T   []._./\._.[_]/  [__]/  ||  \[__]  \[_]._./\._.[]   T   []|._._.|[]
        []IIIIIII[]IIIIIII[]IIIIIIII[_]===[__]\._||_./[__]===[_]IIIIIIII[]IIIIIII[]IIIIIII[]
       /|--------[]-------[]--------[_]---[__]-+=II=+-[__]---[_]--------[]-------[]--------|\\
      /|| _/T\_  ||\\\\_I_//||  _/T\_ [_]    \_\_/T\/T\_/_/    [_] _/T\_  ||\\\\_I_//||  _/T\_ ||\\
      ||| |_O_| ,/|=/_|_\=|\, |_O_| [_]    |_L_LT||TJ_J_|    [_] |_O_| ,/|=/_|_\=|\, |_O_| |||
      ||| |_O_| |||___|___||| |_O_| [_]____[]/|||/\|||\[]    [_] |_O_| |||___|___||| |_O_| |||
      [_]\IIIII/[_]\IIIII/[_]\IIIII/[_]IIII[]\==/%%\==/[]IIII[_]\IIIII/[_]\IIIII/[_]\IIIII/[_]
      [_].\_I_/.[_].\_I_/.[_].\_I_/.[_]\II/[].\_\%%/_/.[]\II/[_].\_I_/.[_].\_I_/.[_].\_I_/.[_]
      L_J./   \.L_J./   \.L_J./   \.L_JI  I[]./      \.[]I  IL_J./   \.L_J./   \.L_J./   \.L_J
      L_J|     |L_J|     |L_J|     |L_J|  |[]|        |[]|  |L_J|     |L_J|     |L_J|     |L_J
      L_J|_____|L_J|_____|L_J|_____|L_J|__|[]|        |[]|__|L_J|_____|L_J|_____|L_J|_____|L_J"""

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
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""                   ooo OOO OOO ooo
               oOO                 OOo
           oOO                         OOo
        oOO                               OOo
      oOO                                   OOo
    oOO                                       OOo
   oOO                                         OOo
  oOO         __                  ___           OOo
 oOO          \ \_____      _____/ /             OOo
 oOO           \______\    /______/              OOo
 oOO                                             OOo
 oOO                                             OOo
 oOO                                             OOo
  oOO               ___________                 OOo
   oOO            /             \              OOo
    oOO         /                 \           OOo;;;;
      oOO                                   OOo;;;;;;;;;
        oO                                OOo;;;;;;;;;;;;;
           oOO                         OOo;;;;;;;;;;;;;;;;;;;;
               oOO                 OOo;;;;;;;;;;;;;;;;;;;;;;;;;;
                   ooo OOO OOO ooo;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;nhm""")

def skrivGargylslott():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""                                 /\\
                                 ||
                                 ||
                                 ||
                                 ||
                                /  \\
                                |--|
                                |  |
                               /    \\
                            ,-v|::::|    ,`^,
                        v.   )/:::::|_  `)v(
                     ,-'),\  |:::::/ ^\   ||
                      )(||   |:::::"\/"  | |                   ||
                     | |||   )`----'||   | |                 __\\\\
                  __ | || \  |._____||   | |   |            (  )(
                  || | || | | v v v|'`|  | |   |             )(| |
                  )( | |I |(^)v v v|,.| .' |  / \\           | | |
                  ||/  |I | )|v v v|I | |  |  | |           _| | |
              ||  ||mmm|   \||v v v|I '||  |  | |          |  \\| |
              ||  ||/v,+--'|||v(^)v|I  || ^|  | |           || | |
              ||  | \ |^ ^^`'`vv||v|vvv|| ^'.|  |           /| | |
              | \ |-| |^ ^^/  \\v||/^ ^^|/\^^||  |          .'| | |
              |  || | |    |  |v|||^ ^^|  \^|   |          | '.|.'
              |  \+-\ |^ ^^|__| |||    |   \|   |          |  | |
              |--|   \|^ ^,+  |+--+^ ^ |    Y _ | _        |  | |
              |  |   \|,-.:|  ||  |^ ^ |    | |  |   _   |   | |
              |   \  \|; `;|  \/--+    | | /--.-._|_  ||  |   | |
              |   |   \/ ( |   |  |^ ^d| |/| /|   | `-,-- |   | |,
              |   |   \ \ \|   |  | ^|8||o |o |  /|  /|   |   | '.
   -hrr-      |   |  _,\--.|   |   | `"||| || | o | o |  |    '. |
              |\,-|-' _|--.|   |   |^ ^| | || | | | | | o|    ||  |
             /| |,|,-'   \ |._ |   |^^^|/O\/^\|/^\|/^\|/ |    ||  .
       _.Y._/ |   |       \|  `|   |  ^|_ / O Y O | O\/ |   ,'||  |
     ,'     `\|   |    |   Y   |`--|  |   |---|.__|  /  |_,'  |   |
  ,-,         )   |   -+-  |   |   | /^\  |   |   |  /  |    ,.   |
 (  \       /\|       ,|.  |   |   |/   \/^\ /\  /\ /\\\\ |   | _'  |
  \  \ \\\\/\//\    _,-_/  `.|   |    | o | o Y  \/  \//\|    ' [  /|
   ) /\,-       ,:--'::-.  `.  |    |,-.|__ | o| o /\\\\\|   |   |/||
  (  \   \/\/\,( ...:::::`-. `.     ( . |. ),-.|,- \\\\//\   |  //||
   `--`-.___  /\-,----,._   `-.`.   /\  `-' `._| .//\\\\\/ _|.,'/||
            `--//// //|  `-._  `-\  | \_    |   _/\\\\\///\    /|||
              //// //|,: \\\\ \\\\--._\ |_| `---|__/  //\\\\/\\\\   / ||
             `-'`'//_|,   \\\\ \\\\ \\\\ /v\/\,      `.//_|| | | /|
                 (_)       \\\\ \\\\ \\\\-._   \/ \;.,.    `-^',' |
                           (_)) \(_)  `---.__  ` \/\/\  (
                              `-'            `---._  /   \\
                                                   `(     )""")

def skrivStatue():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    statuer = ["""              {}
             .--.
            /.--.\\
            |====|
            |`::`|
        .-;`\..../`;-.
       /  |...::...|  \\
      |   /'''::'''\   |
      ;--'\   ::   /\--;
      <__>,>._::_.<,<__>
      |  |/   ^^   \|  |
      \::/|        |\::/
      |||\|        |/|||
      ''' |___/\___| '''
           \_ || _/
           <_ >< _>
           |  ||  |
           |  ||  |
          _\.:||:./_
    jgs  /____/\____\\""",
    """   ,   A           {}
  / \, | ,        .--.
 |    =|= >      /.--.\\
  \ /` | `       |====|
   `   |         |`::`|
       |     .-;`\..../`;-.
      /\\\\/  /  |...::...|  \\
      |:'\ |   /'''::'''\   |
       \ /\;-,/\   ::   /\--;
       |\ <` >  >._::_.<,<__>
       | `""`  /   ^^   \|  |
       |       |        |\::/
       |       |        |/|||
       |       |___/\___| '''
       |        \_ || _/
       |        <_ >< _>
       |        |  ||  |
       |        |  ||  |
       |       _\.:||:./_
       | jgs  /____/\____\\""",
       """        {}
       .--.
      /.--.\\
      |====|
      |`::`|
  .-;`\..../`;_.-^-._
 /  |...::..|`   :   `|
|   /'''::''|   .:.   |
;--'\   ::  |..:::::..|
<__> >._::_.| ':::::' |
|  |/   ^^  |   ':'   |
\::/|       \    :    /
|||\|        \   :   /
''' |___/\___|`-.:.-`
     \_ || _/    `
     <_ >< _>
     |  ||  |
     |  ||  |
    _\.:||:./_
jgs/____/\____\\""",
         """      /\\
      ||
      ||
      ||
      ||           {}
      ||          .--.
      ||         /.--.\\
      ||         |====|
      ||         |`::`|
     _||_    .-;`\..../`;-.
      /\\\\   /  |...::...|  \\
      |:'\ |   /'''::'''\   |
       \ /\;-,/\   ::   /\--;
        \ <` >  >._::_.<,<__>
         `""`  /   ^^   \|  |
               |        |\::/
               |        |/|||
               |___/\___| '''
                \_ || _/
                <_ >< _>
                |  ||  |
                |  ||  |
               _\.:||:./_
         jgs  /____/\____\\""",
         """   ,   A           {}
  / \, | ,        .--.
 |    =|= >      /.--.\\
  \ /` | `       |====|
   `   |         |`::`|
       |     .-;`\..../`;_.-^-._
      /\\\\/  /  |...::..|`   :   `|
      |:'\ |   /'''::''|   .:.   |
       \ /\;-,/\   ::  |..:::::..|
       |\ <` >  >._::_.| ':::::' |
       | `""`  /   ^^  |   ':'   |
       |       |       \    :    /
       |       |        \   :   /
       |       |___/\___|`-.:.-`
       |        \_ || _/    `
       |        <_ >< _>
       |        |  ||  |
       |        |  ||  |
       |       _\.:||:./_
       | jgs  /____/\____\\""",
       """      /\\
      ||
      ||
      ||
      ||           {}
      ||          .--.
      ||         /.--.\\
      ||         |====|
      ||         |`::`|
     _||_    .-;`\..../`;_.-^-._
      /\\\\   /  |...::..|`   :   `|
      |:'\ |   /'''::''|   .:.   |
       \ /\;-,/\   ::  |..:::::..|
        \ <` >  >._::_.| ':::::' |
         `""`  /   ^^  |   ':'   |
               |       \    :    /
               |        \   :   /
               |___/\___|`-.:.-`
                \_ || _/    `
                <_ >< _>
                |  ||  |
                |  ||  |
               _\.:||:./_
         jgs  /____/\____\\""",
         """                   {}
                  .--.
                 /.--.\\
                 |====|
                 |`::`|
             .-;`\..../`;_.-^-._
      /\\\\   /  |...::..|`   :   `|
      |:'\ |   /'''::''|   .:.   |
     @|\ /\;-,/\   ::  |..:::::..|
     `||\ <` >  >._::_.| ':::::' |
      || `""`  /   ^^  |   ':'   |
      ||       |       \    :    /
      ||       |        \   :   /
      ||       |___/\___|`-.:.-`
      ||        \_ || _/    `
      ||        <_ >< _>
      ||        |  ||  |
      ||        |  ||  |
      ||       _\.:||:./_
      \/ jgs  /____/\____\\"""]

    indeks = randint(0,6)
    print(statuer[indeks])

def skrivTroll():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    troll = """           .:\:/:.
         .:\:\:/:/:.
        :.:\:\:/:/:.:
       :=.' -   - '.=:
       '=(\ 9   9 /)='
          (  (_)  )
          /`-vvv-´\\
         /         \\
        / /|,,,,,|\ \\
       /_//  /^\  \\\\_\\
       WW(  (   )  )WW
        __\,,\ /,,/__
   jgs (______Y______)"""

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
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    troll = """                       %%|%%
                 .\%%%%%%|%%%%%%/.
               .:\:\%%%%%|%%%%%/:/:.
              .:\:\:\%%%%|%%%%/:/:/:.
              :.:\:\:\%%%|%%%/:/:/:.:
             :=.' -             - '.=:
            '=(\     @       @     /)='
                \       /_\       /
                 \     [___]     /
            __    \_____________/   __
          /`-vv                   vv-  \\
         /                              \\
        /   /|,,,                 ,,,|\  \\
       /_  //  /                  \  \\\\_\\
       WW(  (  ____________________  )  )WW
        __\,,\                      /,,/__
   jgs (______Y                      ______)"""

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
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    boss = """                       %%|%%
                 .\%%%%%%|%%%%%%/.
               .:\:\%%%%%|%%%%%/:/:.
              .:\:\:\%%%%|%%%%/:/:/:.
              :.:\:\:\%%%|%%%/:/:/:.:
             :=.' -             - '.=:
            '=(\     _       _    /)='
                \       /_\       /
                 \     /___\\     /
            __    \_____________/   __
          /`-vv                   vv-  \\
         /                              \\
        /   /|,,,                 ,,,|\  \\
       /_  //  /                  \  \\\\_\\
       WW(  (  ____________________  )  )WW
        __\,,\                      /,,/__
   jgs (______Y                      ______)"""

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
    print("""    ,_
     \`(  ;".____
     )\~\/  6\___\\
    ( (\ \   /--`
     ) )\ `-' `\\
      ( )|}:{|\ \\
       ( |___|(( \\
         |   | )(~)
         ||^|| ( )
         (| |)   (
         || ||
      ,=`~| |~`=,jgs""")

def skrivHytte():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    hytte = """                                            /\\
/\                                         /%%\  /\\
%%\\            ,                          /%%%%\/%%\\
%%%\\          ,~,                /\\       /%%%%/%%%%\\    ,   /\\
%%%\\         ,~~~,   /\\         /%%\\  /\\ /%%%%%//\\%%\/\\ ,~, /%%\\
%%%%\\  /\\   ,~~~~~, /%%\\   /\\   /%%\\ /%%\\%/\\%/\\/%%\\%/%%\\~~~/%%%%\\
%%%%\\ /%%\\ /\\~~~~~~/%%%%\\ /%%\\ /%%%%\\/%%\\/%%\\%%\\%%%/%(%%\\~~/%%%%\\
%%%%%\\/%%\\/%%\\~/\\~~/%%%%\\/%%%%/%%%%%%\\%%/%%%%\\%%\\%%/)%%%\\~/%%%%%%\\
%/\\%%/%%%%\\%%%/%%\\/%%%%%%\\%%/\\/%%/\\%%\%%/\\%%%\\%%\\%%(%%%%%/%%%%%%%%\\
/%%\\/%%%%%%\\/\\/%%\\/%%%%%%\\%/%%\\%/%%\\%%\\/%%\\_______[_]________%%%%%%\\
%%%%/%%%%%%/%%\%%/%%%%%%%%\/%%\%/%%\%%/%%%%\ _-       _-  _- \%%%%%\\
%%%/%%%%%%%/%%\%%/%%/\%%%%/%%%%\%%%%\/%%%%%%\______-__________\***,*
lc/%%%%%%%/%%%%\/%%/%%\%%%/%%%%\%%%%\/%%%%%%\__===______====_]   ,~,  _-
**/%%%%%%/%%%%%%,%%/%%\%%/%%%%%%\%%%/%%%%%%%%\_|_|______|  |_]  ,~~~,
 /%%%%%%%/%%%%%,~,/%%%%\/%%%%%%%%\%/%%%%%%%%%%\_________|- |_] ,~~~~~,
 /%%%%%%/%%%%%,~~~,%%%%\/%%%%%%%%\%/%%%%%%%%%%\___#__#__|__|_],~~~~~~~,
/%%%%%#%/#%%%,~~~~~,%%%/%%%%%%%%%%/%%%%%%%%%%%%\\***\/***/  \\*  ,~~;~~,
*******\/***,~~~~~~~,**/%%%%%%%%%/%%%%%%%%%%%%%%\\   _-            |
 -_          ,~~;~~,   **********/%%%%%%%%%%%%%%\       ^^      ~***~
      ^^        |   ,    _-     /%%%%%%%%%%%%#%%#\        _-
            _-    ,`|`,         ************\/**   _-          _-
  _-               \ /           _-         _-   ~~
                  ~***~"""

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
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    bue = """               ,aaaaaa.                             ,aaaaaa.                              ,aaaaaa.                               ,aaaaaa.
            ,aaabbbbbbaaa.                        ,aaabbbbbbaaa.                        ,aaabbbbbbaaa.                        ,aaabbbbbbaaa.
         ,aaabbbccccccbbbaaa.                  ,aaabbbccccccbbbaaa.                  ,aaabbbccccccbbbaaa.                  ,aaabbbccccccbbbaaa.
       ,aabbbcccddddddcccbbbaa.              ,aabbbcccddddddcccbbbaa.              ,aabbbcccddddddcccbbbaa.              ,aabbbcccddddddcccbbbaa.
     ,aabbcccddd'    'dddcccbbaa.          ,aabbcccddd'    'dddcccbbaa.          ,aabbcccddd'    'dddcccbbaa.          ,aabbcccddd'    'dddcccbbaa.
   ,aabbccddd'          'dddccbbaa.      ,aabbccddd'          'dddccbbaa.      ,aabbccddd'          'dddccbbaa.      ,aabbccddd'          'dddccbbaa.
  ,abbccdd'                'ddccbba.    ,abbccdd'                'ddccbba.    ,abbccdd'                'ddccbba.    ,abbccdd'                'ddccbba.
 ,abccdd'                    'ddccba.  ,abccdd'                    'ddccba.  ,abccdd'                    'ddccba.  ,abccdd'                    'ddccba.
,abcdd'                        'ddcba.,abcdd'                        'ddcba.,abcdd'                        'ddcba.,abcdd'                        'ddcba.
abccd'                          'dccbaabccd'                          'dccbaabccd'                          'dccbaabccd'                          'dccba"""

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
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    vulkan = """                      ooO
                     ooOOOo
                   oOOOOOOoooo
                 ooOOOooo  oooo
                /vvv\\
               /V V V\\
              /V  V  V\\
             /     V   \\
            /      VV   \\
           /        VVV   \\
         /        VVVV     \\
        /         VVVVVVV   \\
       /            VVVVVVVVVVVVV"""

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
    print("""                _
    	       / \\
    	    __|   |__
           / <|   |> \\
           '-._____.-'
            ,| O_o |,
             \\\\###//
              .| |.
          ,############\\
         /  #########,  \\
        /_<'#########'./_\\
       '_7_ ######### _o_7
        (  \\[o-o-o-o]/  )
         \\|l#########l|/
            ####_####
           /    |    \\
  	   |    |    |
           |_  _|_  _|
           |\\\\//|\\\\//|
           \\//\\\\|//\\\\/
         ___\\\\// \\\\//___
        (((___X\\ /X___))) """)

def skrivRotte():
    print(""" _  _  .-'   '-.
(.)(.)/         \\
 /66            ;   jgs
o_\\\\-mm-......-mm`~~~~~~~~~~~~~""")
