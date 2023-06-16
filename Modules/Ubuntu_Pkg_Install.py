#Build Out for installation of Ubuntu Packages - SKIP for Windows [Potentially build tool to detect OS later]

import subprocess
import os
from colorama import Fore, Style

def Package_Installation():
    Packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
    print (f'{Fore.GREEN}[+] Installation of Ubuntu packages is starting:{Style.RESET_ALL}')
    x=0
    while x < len(Packages):
        print ('Installation of:', Packages[x])
        subprocess.run(['sudo', 'apt','install','-y', Packages[x]])
        if os.error():
            print(f'{Fore.RED}Package: ', Packages[x], f'failed to install.{Style.RESET_ALL}')
            x+=1
        x+=1
        if x > len(Packages):
            break
        print(f'{Fore.GREEN}Success.{Style.RESET_ALL}')
