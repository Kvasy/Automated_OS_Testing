#Package PreReqs
import os
import platform
import requests
import socket
from datetime import datetime
import subprocess
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import keyboard
from time import sleep
import sys


#Layout custom functions
#STRUCTURAL BASICS:
def line_break():
    print('\n')
def Date_Time_Start():
    current_dateTime = datetime.now()
    print('Date: ', current_dateTime.year, '/', current_dateTime.month, '/', current_dateTime.day)
    print ('Time:', current_dateTime.hour, ':', current_dateTime.minute, ':', current_dateTime.second)
def Date_Time_End():
    current_dateTime = datetime.now()
    print('Date: ', current_dateTime.year, '/', current_dateTime.month, '/', current_dateTime.day)
    print ('Time:', current_dateTime.hour, ':', current_dateTime.minute, ':', current_dateTime.second)

#Send to .txt file
#Still working to figure out how to guarentee this saves to an easy place every time.... maybe a dedicated USB, but will still need different code for Windows/Ubuntu

def log_saver():
    Ubuntu_path = '/home/trenton/Desktop/OS_Test_Report'
    try:
        os.makedir(Ubuntu_path)
    except FileExistsError as exc:
        print('Directory exists. Continuing...')
    with open('OS_Report_Log.txt', 'a') as sys.stdout:
        sys.stdout.write()

#OS BASIC TESTS:
def check_internet_connection():
    request = requests.get('https://www.google.com')
    response = request.status_code
    if response == 200:
        print ('Network Connection Pass')
        print ('Successful ping to: Google.com')
    else:
        print ('Network Failure')
    line_break()
def OS_Info():
    OS_INFO = platform.uname()
    print ('OS: ', OS_INFO[0])
    print ('Release / Kernel: ', OS_INFO[2])
    print ('Version: ', OS_INFO[3])
    print ('CPU Info: ', OS_INFO[5])
    line_break()

def Terminal_Commands():
    os.system('sudo su')
    os.system('trenton-1')
    os.system('sudo apt get update')
    os.system('sudo apt install update')

#Build Out for installation of Ubuntu Packages - SKIP for Windows [Potentially build tool to detect OS later]
def Package_Installation():
    Packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip']
    print (f'{Fore.GREEN}[+] Installation of Ubuntu packages is starting:{Style.RESET_ALL}')
    x=0
    while x < len(Packages):
        print ('Installation of:', Packages[x])
        subprocess.run(['sudo', 'apt','install','-y', Packages[x]])
        if os.error():
            print(f'{Fore.RED}Package: ', Packages[x], 'failed to install.')
            x+=1
        x+=1
        if x > len(Packages):
            break
        print(f'{Fore.GREEN}Success.{Style.RESET_ALL}')

def Pip_Installs():
    Pip_packs = ['colorama','keyboard']
    print (f'{Fore.GREEN}[+] Installation of Pip Packages is starting:{Style.RESET_ALL}')
    x=0
    while x < len(Pip_packs):
        print ('Installation of:', Pip_packs[x])
        subprocess.run(['python3', 'pip','install', Pip_packs[x]])
        if os.error():
            print(f'{Fore.RED}Package: ', Pip_packs[x], 'failed to install.')
            x+=1
        x+=1
        if x > len(Pip_packs):
            break
        print(f'{Fore.GREEN}Success.{Style.RESET_ALL}')

def Sys_Update():
    subprocess.run(['sudo','apt','update','-y'])
    if os.error:
        print(f'{Fore.RED}Error occurred.{Style.RESET_ALL}')
    else:
        print(f'{Fore.GREEN}Update Installed.{Style.RESET_ALL}')

def Package_Cleanup():
    print('Cleaning up...')
    subprocess.run(['sudo', 'apt','autoremove'])
    keyboard.press('enter')
    print (f'{Fore.GREEN}Cleanup complete.{Style.RESET_ALL}')













#MAIN:
def main():
    Date_Time_Start()
    OS_Info()
    check_internet_connection()
    Package_Installation()
    Pip_Installs()
#   Sys_Update()
    Package_Cleanup()
    Date_Time_End()

if __name__ == '__main__':
    main()






