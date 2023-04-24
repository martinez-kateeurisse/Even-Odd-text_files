#Import colorama
from colorama import Back, Fore, Style 

#Define header design
def even_odd_header():
    print(Fore.MAGENTA, """
                                ──────▄▀▄─────▄▀▄
                                ─────▄█░░▀▀▀▀▀░░█▄ 
                                ─▄▄──█░░░░░░░░░░░█──▄▄
                                █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█"""+ Fore.YELLOW,"""  
                   █▀▀ █ █░░ █▀▀ ▄▄ █░█ ▄▀█ █▄░█ █▀▄ █░░ █ █▄░█ █▀▀
                   █▀░ █ █▄▄ ██▄ ░░ █▀█ █▀█ █░▀█ █▄▀ █▄▄ █ █░▀█ █▄█""")
    print(Fore.WHITE,  "="* 18 + "Extracting Even and Odd integers from a text File" + "="* 18 ,"\n")