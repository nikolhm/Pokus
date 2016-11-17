

def skrivRegnbue():
    bue = """               ,aaaaaa.
            ,aaabbbbbbaaa.
         ,aaabbbccccccbbbaaa.
       ,aabbbcccddddddcccbbbaa.
     ,aabbcccddd'    'dddcccbbaa.
   ,aabbccddd'          'dddccbbaa.
  ,abbccdd'                'ddccbba.
 ,abccdd'                    'ddccba.
,abcdd'                        'ddcba.
abccd'                          'dccba"""

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
