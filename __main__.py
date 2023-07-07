#First load all custom modules and functions:

from modules.Custom_Modules.line_break import line_break
from modules.Custom_Modules.log import log_message
#from modules.Pip_Installs import Pip_Installs
#from modules.OS_Selection import OS_Info
#from modules.Ubuntu_CPU_Info import CPU_Info
#from modules.Memory_Info import Memory_Info
#from modules.Networking import Network_Chk
#from modules.Ubuntu_Pkg_Install import Package_Installation
#from modules.Setup_Snapd import Setup_Snapd
from modules.Reminders import Reminders
from modules.Ubuntu_Pwr_State import Power_State_Testing

#MAIN:
#Imports
import platform
import subprocess
import os
import psutil
import subprocess
import requests
import keyboard


#From_Imports
from datetime import datetime

#DATE_TIME_START
def Date_Time_Start():
        #TIME_START
        START_TIME_STAMP = "\t\t\t START TIME\n"
        log_message(START_TIME_STAMP)

        current_dateTime = datetime.now()
        date = 'Date: ' + str(current_dateTime.year) + '/' + str(current_dateTime.month) + '/' + str(current_dateTime.day)
        time = 'Time: ' + str(current_dateTime.hour) + ':' + str(current_dateTime.minute) + ':' + str(current_dateTime.second)
        log_message(date)
        log_message(time+'\n')

#DATE_TIME_END
def Date_Time_End():
        #TIME_END
        
        END_TIME_STAMP = "\t\t\t END TIME\n"
        log_message(END_TIME_STAMP)

        current_dateTime = datetime.now()
        date = 'Date: ' + str(current_dateTime.year) + '/' + str(current_dateTime.month) + '/' + str(current_dateTime.day)
        time = 'Time: ' + str(current_dateTime.hour) + ':' + str(current_dateTime.minute) + ':' + str(current_dateTime.second)
        log_message(date)
        log_message(time+'\n')

#OS_INFO
def OS_Info():
        #Create Header in LOG
        OS_INFO_header = "\t\t\t OS Information\n"
        log_message(OS_INFO_header)

        #Pull OS Info    
        OS_INFO = platform.uname()
        os = 'OS: '+ str(OS_INFO[0])
        kernel = 'Release / Kernel: '+ str(OS_INFO[2])
        version = 'Version: '+ str(OS_INFO[3])
        line_break()

        if OS_INFO[0] == 'Windows':
                log_message(os)
                log_message(kernel)
                log_message(version+'\n')
                return 'Windows'
        elif OS_INFO[0] == 'Ubuntu':
                log_message(os)
                log_message(kernel)
                log_message(version+'\n')
                return 'Ubuntu'
        elif OS_INFO[0] == 'OpenSUSE':
                log_message(os)
                log_message(kernel)
                log_message(version+'\n')
                return 'OpenSUSE'
        elif OS_INFO[0] == 'Red Hat':
                log_message(os)
                log_message(kernel)
                log_message(version+'\n')
                return 'Red Hat'

#PIP_INSTALLS
def Pip_Installs():
        #Add header to PIP Package Installation
        PIP_Header = "\t\t\t PIP Package Information\n"
        log_message(PIP_Header)

        #Run func to install Pip packs automatically
        Pip_packs = ['keyboard', 'psutil']
        print ('[+] Installation of Prerequisite Pip Packages is starting.')
        log_pip = '[+] Installation of Prerequisite Pip Packages is starting.'
        log_message(log_pip)
        x=0
        while x < len(Pip_packs):
                try:
                        print ('Installation of:', Pip_packs[x])
                        pack_being_installed = 'Installation of: ' + str(Pip_packs[x])
                        log_message(pack_being_installed)
                        subprocess.run(['pip','install', Pip_packs[x]])
        #Need to investigate why failed installs still report success

                        print('Success')
                        install_success = 'Success.'
                        log_message(install_success+'\n')

        #If OS Error print FAILURE and indicate which package was unsuccessful
                except os.error():
                        print('Package: ', Pip_packs[x], 'failed to install.')
                        fail_install = 'Package: ' + str(Pip_packs[x]) + ' failed to install.'
                        log_message(fail_install+'\n')
                        x+=1
                x+=1
                if x > len(Pip_packs):
                        break
        
#CPU_INFO
#Get CPU Info (Linux Only Var)
def CPU_Info():
        CPU_header = "\t\t\t CPU Information\n"
        log_message(CPU_header)
        #Read CPUINFO file to print name of CPU

        #print CPU Model
        OS_INFO = platform.uname()
        cpu_inf = 'CPU Info: ' + str(OS_INFO[5])
        

#RUN FOR CPU_INFO
        try:
                with open('/proc/cpuinfo', 'r') as f:
                        file_info = f.readlines()
                        cpuinfo = [x.strip().split(':')[1] for x in file_info if 'model name' in x]
                for index, item in enumerate(cpuinfo):
                        print('[+] Processor ' + str(index) + ' : ' + item)
                        cpu = '[+] Processor ' + str(index) + ' : ' + str(item)
                        log_message(cpu)
        except:
                if FileNotFoundError:
                        print(FileNotFoundError)
                        pass



        # This code will print the number of CPU cores present
        #print("[+] Number of Physical cores :", psutil.cpu_count(logical=False))
        phys_cores = "[+] Number of Physical cores : " + str(psutil.cpu_count(logical=False))
        #print("[+] Number of Total cores :", psutil.cpu_count(logical=True))
        total_cores = "[+] Number of Total cores : " + str(psutil.cpu_count(logical=True))
        line_break()
        
        # This will print the maximum, minimum and current CPU frequency
        cpu_frequency = psutil.cpu_freq()
        print(f"[+] Max Frequency : {cpu_frequency.max:.2f}Mhz")
        cpu_max_freq = f"[+] Max Frequency : + {cpu_frequency.max:.2f}Mhz"
        print(f"[+] Min Frequency : {cpu_frequency.min:.2f}Mhz")
        cpu_min_freq = f"[+] Min Frequency : {cpu_frequency.min:.2f}Mhz"
        line_break()

        log_message(cpu_inf)
        log_message(phys_cores)
        log_message(total_cores)
        log_message(cpu_max_freq)
        log_message(cpu_min_freq+'\n')

#Memory_Info
def Memory_Info():
    #Func. to convert Bytes to GB
    def bytes_to_GB(bytes):
        gb = bytes/(1024*1024*1024)
        gb = round(gb, 2)
        return gb
    
    #This will print the primary memory details
    memory_header = "\t\t\t Memory Information\n"
    log_message(memory_header)

    virtual_memory = psutil.virtual_memory()
    print("[+] Total Memory present :", bytes_to_GB(virtual_memory.total), "Gb")
    total_mem = "[+] Total Memory present :" +str(bytes_to_GB(virtual_memory.total))+ " Gb"
    log_message(total_mem+'\n')
    

#PACKAGE_INSTALLATION
#Build Out for installation of Ubuntu Packages - SKIP for Windows [Potentially build tool to detect OS later]
def Package_Installation():

    def check():
        OS_INFO = platform.uname()
        if (OS_INFO[0]) != 'Windows':
            return False

    
    if check() == True:
        log_message('OS is Windows...Skipping Ubuntu Packages.')
    
    elif check() == False:
        Packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
        print ('[+] Installation of Ubuntu packages is starting')
        x=0
        while x < len(Packages):
                print ('Installation of:', Packages[x])
                try:
                        subprocess.run(['sudo', 'apt','install','-y', Packages[x]])
                        print('Success')
                except FileNotFoundError:
                        pass
                if os.error():
                        print('Package: ', Packages[x], 'failed to install.')
                        x+=1
                x+=1
                if x > len(Packages):
                        break
                
#Network Testing
def Network_Chk():
        #Create Network Header
        network_header = ("\t\t\t Network Information\n")
        log_message(network_header)

        # gathering all network interfaces (virtual and physical) from the system
        if_addrs = psutil.net_if_addrs()
        # printing the information of each network interfaces
        # needs further debugging
        for interface_name, interface_addresses in if_addrs.items():
                for address in interface_addresses:
                        print(f"Interface :", interface_name)
                        interface=f"Interface :"+ str(interface_name)
                        log_message(interface)
                if str(address.family) == 'AddressFamily.AF_INET':
                        print(f"[+] IP Address: ", address.address)
                        ip="[+] IP Address: " + address.address
                        log_message(ip)
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                        print(f"[+] MAC Address: ", address.address)
                        mac="[+] MAC Address: " + address.address
                        log_message(mac+'\n')
                line_break()

        #if error
        if ConnectionError():
                print ('Network Failure')
                log_message('Connection Error')
        else:
                request = requests.get('https://www.google.com')
                response = request.status_code
                if response == 200:
                        print(response)
                        log_message(response)
                        print ('Network Connection Pass')
                        print ('Successful ping to: Google.com')
                        log_message('NETWORK PASSED\n')
                elif response!= 200:
                        print ('Network Failure')
                        log_message(response)
                        log_message('NETWORK FAILED\n')
                line_break()

#Setup_SNAPD
def Setup_Snapd():
        try:
                subprocess.run(['sudo','systemctl','enable', '--now', 'snapd.socket'])
        except FileNotFoundError:
                pass        
        if os.error:
                print('Error occurred.')
        else:
                keyboard.press_and_release('enter')
                print('Snapd service started.')
        try:
                subprocess.run(['sudo','ln','-s', '/var/lib/snapd/snap', '/snap'])
        except FileNotFoundError:
                pass
        if os.error:
                print('Error occurred')
        else:
                keyboard.press_and_release('enter')
                print('Snapd service started')

def main():
        Date_Time_Start()
        Pip_Installs()
        OS_Info()
        CPU_Info()
        Memory_Info()
        Network_Chk()
        Package_Installation()
        Setup_Snapd()
        Reminders()
        #Sys_Update()
        #Package_Cleanup()
        #Burn_Linux()
        Power_State_Testing()
        Date_Time_End()

#MAIN
if __name__ == '__main__':
    main()
