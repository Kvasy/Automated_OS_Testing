#Package PreReqs
import os
import subprocess




import pkg_resources
import platform
import requests
import socket
from datetime import datetime

import keyboard
from time import sleep
import sys
import psutil

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


