import pyzipper
import pyfiglet
from colorama import Fore, Style, init
import os
# Colorama initialize
init(autoreset=True)
os.system("clear")
def show_logo():
    logo = pyfiglet.figlet_format("ZIP CRACK")
    print(Fore.CYAN + logo)
    print(Fore.YELLOW + "Author: Your Team Name\n" + Style.RESET_ALL)

# প্রথমে লোগো দেখাও
show_logo()

# Zip file path input
z = input("Enter zip File Path: ")
pw = input("Enter zip File password list path: ")

found = False

with pyzipper.AESZipFile(z) as zip_file:
    with open(pw, "r", errors="ignore") as file:
        for password in file:
            password = password.strip()
            try:
                zip_file.pwd = password.encode("utf-8")
                zip_file.extractall()
                show_logo()
                print(Fore.GREEN + pyfiglet.figlet_format("PASSWORD FOUND"))
                print(Fore.CYAN + "✅ Password: " + Fore.YELLOW + password)
                found = True
                break
            except:
                print(Fore.RED + "❌ Wrong password: " + password)

if not found:
    print(Fore.RED + "\n❌ No correct password found in the list.")

input(Fore.MAGENTA + "\nPress Enter to exit...")