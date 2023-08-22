import os
from assets import portscanner
from assets import iplookup
from colorama import Fore, Style


# Functions Class - All ugly, back-end code will be here
class Function:
    def parse_command(cmd):
        # Port Scanner
        if (cmd) == "1":
            portscanner.start()
        # IP Lookup
        elif(cmd == "2"):
            iplookup.start()
        elif(cmd == "3"):
            exit()
        else:
            Menu.main()


    def get_command():
        cmd = input("\n[>] ")
        Function.parse_command(cmd)


# Menu Class - All Menus will be found in here
class Menu:
    def logo():        
        print(Style.BRIGHT + Fore.RED + "  ██████╗ ███████╗ █████╗ ██████╗ ██████╗ ███████╗ ")
        print(Style.BRIGHT + Fore.RED + " ██╔═══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ")
        print(Style.BRIGHT + Fore.RED + " ██║   ██║███████╗███████║██████╔╝██████╔╝█████╗   ")
        print(Style.BRIGHT + Fore.RED + " ██║▄▄ ██║╚════██║██╔══██║██╔══██╗██╔═══╝ ██╔══╝   ")
        print(Style.BRIGHT + Fore.RED + " ╚██████╔╝███████║██║  ██║██║  ██║██║     ███████╗ ")
        print(Style.BRIGHT + Fore.RED + "  ╚══▀▀═╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ ")
        print(Style.BRIGHT + Fore.RED + "                 Qsarpe's Multi-Tool             \n")
        

    def main():
        Menu.logo()
        print("[1] Port Scanner")
        print("[2] IP Search")
        print("[3] Exit")
        Function.get_command()

#Run Main Menu
Menu.main()
