#Package PreReqs
import os
import subprocess

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


import pkg_resources
import platform
import requests
import socket
from datetime import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import keyboard
from time import sleep
import sys
import psutil


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
    print("\n\t\t\t Network Information\n")

    # gathering all network interfaces (virtual and physical) from the system
    if_addrs = psutil.net_if_addrs()
    # printing the information of eah network interfaces
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"Interface :", interface_name)
            if str(address.family) == 'AddressFamily.AF_INET':
                print("[+] IP Address :", address.address)
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print("[+] MAC Address :", address.address)
            line_break()

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

#Build Out for installation of Ubuntu Packages - SKIP for Windows [Potentially build tool to detect OS later]
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

#Currently investigating how to hold kernel
def Sys_Update():
    subprocess.run(['sudo','apt','upgrade'])
    if os.error:
        print(f'{Fore.RED}Error occurred.{Style.RESET_ALL}')
    else:
        keyboard.press_and_release('enter')
        print(f'{Fore.GREEN}Update Installed.{Style.RESET_ALL}')


#Currently malfunctioning for unknown reasons. Makes you manually press Y/n
def Package_Cleanup():
    print('Cleaning up...')
    subprocess.run(['sudo', 'apt','autoremove'])
    keyboard.press_and_release('enter')
    print (f'{Fore.GREEN}Cleanup complete.{Style.RESET_ALL}')

#Get CPU Info (Linux Only Var)
def CPU_Info():
    #Read CPUINFO file to print name of CPU
    try:
        with open('/proc/cpuinfo', 'r') as f:
            file_info = f.readlines()
        cpuinfo = [x.strip().split(':')[1] for x in file_info if 'model name' in x]
        for index, item in enumerate(cpuinfo):
            print('[+] Processor ' + str(index) + ' : ' + item)
    except:
        if FileNotFoundError:
            print(FileNotFoundError)
            pass
    
    # This code will print the number of CPU cores present
    print("[+] Number of Physical cores :", psutil.cpu_count(logical=False))
    print("[+] Number of Total cores :", psutil.cpu_count(logical=True))
    line_break()
    
    # This will print the maximum, minimum and current CPU frequency
    cpu_frequency = psutil.cpu_freq()
    print(f"[+] Max Frequency : {cpu_frequency.max:.2f}Mhz")
    print(f"[+] Min Frequency : {cpu_frequency.min:.2f}Mhz")
    line_break()

def Memory_Info():
    #Func. to convert Bytes to GB
    def bytes_to_GB(bytes):
        gb = bytes/(1024*1024*1024)
        gb = round(gb, 2)
        return gb
    #This will print the primary memory details
    print("\n\t\t\t Memory Information\n")

    virtual_memory = psutil.virtual_memory()
    print("[+] Total Memory present :", bytes_to_GB(virtual_memory.total), "Gb")
    line_break()

def Burn_Linux():
    program_path = os.getcwd()
    print(program_path)

def Power_State_Testing():
    import subprocess
    import time

    def test_system_sleep():
        # Put the system to sleep
        subprocess.run(['systemctl', 'suspend'])
        
        # Wait for a few seconds to allow the system to enter sleep mode
        time.sleep(5)

        # Check if the system is awake
        result = subprocess.run(['systemctl', 'is-system-running'], capture_output=True, text=True)
        output = result.stdout.strip()
        if output == 'running':
            print("System wake-up successful!")
        else:
            print("System failed to wake up.")

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

def Reminders():
    print('DON\'T FORGET THE FOLLOWING:')
    subprocess.run(['sudo', 'qtcreator'])
    print('Select Tools>Options>Verify that Path shows QT5+.')
    line_break()

#MAIN:
def main():
        Date_Time_Start()
        Pip_Installs()
        OS_Info()
        CPU_Info()
        Memory_Info()
        check_internet_connection()
        Package_Installation()
        Setup_Snapd()
        Reminders()
#        Sys_Update()
#        Package_Cleanup()
#        Burn_Linux()
        Power_State_Testing()
        Date_Time_End()

#MAIN
if __name__ == '__main__':
    main()






