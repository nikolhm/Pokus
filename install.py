import platform
import os
import sys

def install(package):
    print("""Colorama er ikke installert. Du trenger Colorama for å spille Pokus med farger.
For å spille må du installere Colorama og starte spillet på nytt.""")
    if input("Vil du installere colorama nå?\n> ").lower() in {"ja", "j"}:
        osys = platform.system()
        if osys == "Linux" or osys == "Darwin":
            os.system("pip3 install --user colorama")
            os.system("clear")
        else:
            os.system("pip install --user colorama")
            os.system("cls")
    sys.exit("Du må starte spillet på nytt nå.")
