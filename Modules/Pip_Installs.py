import subprocess
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

def Pip_Installs():
    Pip_packs = ['colorama','keyboard', 'psutil', 'pkg_resources']
    print ('[+] Installation of Prerequisite Pip Packages is starting.')
    x=0
    while x < len(Pip_packs):
        print ('Installation of:', Pip_packs[x])
        subprocess.run(['pip','install', Pip_packs[x]])
        if os.error():
            print('Package: ', Pip_packs[x], 'failed to install.')
            x+=1
        x+=1
        if x > len(Pip_packs):
            break
        import colorama
        print(f'{Fore.GREEN}Success.{Style.RESET_ALL}')
