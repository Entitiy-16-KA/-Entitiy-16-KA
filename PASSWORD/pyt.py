import os
import subprocess
from colorama import Fore, Style, init


print(Fore.YELLOW + "Yapan: Entitiy 16 KA" + Style.RESET_ALL)
print(Fore.YELLOW + "@Entitiy_16_KA" + Style.RESET_ALL)
print(" ")


Şifre = input(Fore.BLUE + "Şifrenizi girin:  " + Style.RESET_ALL)


if Şifre == "565728!@":
    dosya = r"Pit\pitbuks.mp4"

    subprocess.run([dosya], shell=True)