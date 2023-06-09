import colorama
import os
import subprocess
from colorama import Fore, Style
import keyboard

def Setup_Snapd():
    subprocess.run(['sudo','systemctl','enable', '--now', 'snapd.socket'])
    if os.error:
        print(f'{Fore.RED}Error occurred.{Style.RESET_ALL}')
    else:
        keyboard.press_and_release('enter')
        print(f'{Fore.GREEN}Snapd service started.{Style.RESET_ALL}')

    subprocess.run(['sudo','ln','-s', '/var/lib/snapd/snap', '/snap'])
    if os.error:
        print(f'{Fore.RED}Error occurred.{Style.RESET_ALL}')
    else:
        keyboard.press_and_release('enter')
        print(f'{Fore.GREEN}Snapd service started.{Style.RESET_ALL}')
