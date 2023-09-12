try:
    import platform
    import subprocess
    import os
    import psutil
    import keyboard
    #import shutil

    #From_Imports
    from datetime import datetime

except ImportError:
    pass

'''
try:

    #First load all custom modules and functions:
    #from modules.Custom_Modules.log import log_message
    #from modules.reminders import reminders
    #from modules.Ubuntu_Pwr_State import Power_State_Testing

except ImportError:
    pass
'''
#Above is commented out currently in order to figure out what modules break this on other machines

#Add Custom Modules to Functions to prevent load errors on outside machines
import datetime

#Example Usage: 
# log_message('message to be logged') - HAS TIMESTAMP for no timestamp utilize: log_break(message)
def log_message(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{timestamp}] {message}'

    with open ('log.txt', 'a') as log_file:
        log_file.write(log_entry + '\n')

#For usage at start and end to seperate log runs
def log_break(message):
    log_entry = f'{message}'
    with open ('log.txt', 'a') as log_file:
        log_file.write(log_entry + '\n')

#Add back in reminders module - Ubuntu Distros only
def reminders():
    print('DON\'T FORGET THE FOLLOWING:')
    try:
        subprocess.run(['sudo', 'qtcreator'])
        print('Select Tools>Options>Verify that Path shows QT5+.')
    except FileNotFoundError:
        pass
    print('\n')

#Function to format date and time strings
def format_date_time(current_date_time):
    date = f'Date: {current_date_time.year}/{current_date_time.month}/{current_date_time.day}'
    time = f'Time: {current_date_time.hour}:{current_date_time.minute}:{current_date_time.second}'
    return date, time

#DATE_TIME_START
def date_time_start():
    start_time_stamp = "\t\t\t START TIME\n"
    log_message(start_time_stamp)

    current_date_time = datetime.datetime.now()
    date, time = format_date_time(current_date_time)

    log_message(date)
    log_message(time+'\n')

#DATE_TIME_END
def date_time_end():
    end_time_stamp = "\t\t\t END TIME\n"
    log_message(end_time_stamp)

    current_date_time = datetime.datetime.now()
    date, time = format_date_time(current_date_time)

    log_message(date)
    log_message(time+'\n')

#os_info
def os_info():
    #Create Header in LOG
    os_info_header = "\t\t\t OS Information\n"
    log_message(os_info_header)

    #Pull OS Info    
    os_info = platform.uname()
    os = f'OS: {os_info[0]}'
    kernel = f'Release / Kernel: {os_info[2]}'
    version = f'Version: {os_info[3]}'

    log_message(os)
    log_message(kernel)
    log_message(version+'\n')
    return os_info[0]

#Log CPU Information
def log_cpu_info():
    CPU_header = "\t\t\t CPU Information\n"
    log_message(CPU_header)
    #Read CPUINFO file to print name of CPU

    #print CPU Model
    os_info = platform.uname()
    cpu_inf = f'CPU Info: {os_info[5]}'
    log_message(cpu_inf)    

#Windows_DxDIAG

def dxdiag():
    DxDIAG_Header = "\t\t\t DxDIAG\n"
    try:
        result=subprocess.run(['dxdiag',  '/t'], capture_output=True, text=True, check=True)
        log_message(DxDIAG_Header + '\n')
        log_message('DxDiag run successfully. FIle generated \n')
    except subprocess.CalledProcessError as e:
        print(f'Error running command dxdiag: {e}'+ '\n')


#Info_Dumps_linux
def lshw():
    lshw_header = "\t\t\t LSHW\n"
    try:
        result=subprocess.run(['lshw'], capture_output=True, text=True, check=True)
        log_message(result.stdout + '\n')
    except subprocess.CalledProcessError as e:
        print(f'Error running command lshw: {e}'+ '\n')

def lsusb():
    lsusb_header = "\t\t\t LSUSB\n"
    try:
        result=subprocess.run(['lsusb'], capture_output=True, text=True, check=True)
        log_message(result.stdout + '\n')
    except subprocess.CalledProcessError as e:
        print(f'Error running command lsusb: {e}'+ '\n')

def lspci():
    lspci_header = "\t\t\t LSPCI\n"
    try:
        result=subprocess.run(['lspci'], capture_output=True, text=True, check=True)
        log_message(result.stdout + '\n')
    except subprocess.CalledProcessError as e:
        print(f'Error running command lspci: {e}'+ '\n') 

#Combine all above into single function
def linux_info_dumps():
    lshw()
    lsusb()
    lspci()






#RUN FOR log_cpu_info
    try:
        with open('/proc/cpuinfo', 'r') as f:
            file_info = f.readlines()
            cpuinfo = [x.strip().split(':')[1] for x in file_info if 'model name' in x]
        for index, item in enumerate(cpuinfo):
            cpu = f'[+] Processor {index} : {item}'
            log_message(cpu)
    except FileNotFoundError:
        pass

    # This code will print the number of Total CPU cores present
    phys_cores = "[+] Number of Physical cores : " + str(psutil.cpu_count(logical=False))
    total_cores = "[+] Number of Total cores : " + str(psutil.cpu_count(logical=True))
    cpu_frequency = psutil.cpu_freq()
    cpu_max_freq = f"[+] Max Frequency : + {cpu_frequency.max:.2f}Mhz"

    #Log Results
    log_message(phys_cores)
    log_message(total_cores)
    log_message(cpu_max_freq + '\n')

#log_memory_information
def log_memory_info():
    #Func. to convert Bytes to GB
    def bytes_to_GB(bytes):
        gb = bytes / (1024 * 1024 * 1024)
        gb = round(gb, 2)
        return gb

    memory_header = "\t\t\t Memory Information\n"
    log_message(memory_header)

    #This will print the primary memory details
    virtual_memory = psutil.virtual_memory()
    total_mem = f"[+] Total Memory present : {bytes_to_GB(virtual_memory.total)} Gb"
    log_message(total_mem + '\n')

#PIP_INSTALLS
def pip_installs():
    #Add header to PIP Package Installation
    pip_header = "\t\t\t PIP Package Information\n"
    log_message(pip_header)

    #Define the required Packages
    pip_packs = ['keyboard', 'psutil', 'ping3']

    #Check and Install Packages
    log_message('[+] Checking & Installation of Prerequisite Pip Packages is starting.')
    for package in pip_packs:
        try:
            #Run PIP CMD show to check if a package is already installed
            result=subprocess.run(['pip', 'show', package], capture_output=True, text=True)

            #Package is already Installed
            if result.returncode == 0:
                log_message(f'Package {package} is already installed. Skipping Installation')
            
            #package is not installed
            else:
                log_message(f'Installing Package: {package}')
                try:
                    subprocess.run(['pip', 'install', package])
                except:
                    pass

        #Error occurred during Pip show command OR installation
        except subprocess.CalledProcessError as e:
            log_message(f'Failed to check or install package: {package}. Error: {e}')
    log_break('')
    
#PACKAGE_INSTALLATION
#Build Out for installation of Ubuntu Packages - SKIP for Windows [Potentially build tool to detect OS later]
def ubuntu_package_installation():
    packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
    
    #Check Package Manager
    try:
        pkg_manager_cmd = subprocess.check_output(['which', 'apt-get']).decode().strip()
    except FileNotFoundError:
         raise Exception('Package Manager \'apt-get\' not found. Please ensure it is installed.')

    #Install Packages with Flags for Exceptions
    for package in packages:
        try:
            subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
            log_message(f'{package} installed.')
        except FileNotFoundError:
            pass
        except subprocess.CalledProcessError:
            log_message(f'{package} failed to install.')
        except Exception as e:
            log_message(f'An error occurred while installing {package}: {str(e)}')
    log_message('Packages installed.\n')   

def rhel_package_installation():
    packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
    
    #Check Package Manager
    try:
        pkg_manager_cmd = subprocess.check_output(['which', 'yum']).decode().strip()
    except FileNotFoundError:
         raise Exception('Package Manager \'yum\' not found. Please ensure it is installed.')

    #Install Packages with Flags for Exceptions
    for package in packages:
        try:
            subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
            log_message(f'{package} installed.')
        except FileNotFoundError:
            pass
        except subprocess.CalledProcessError:
            log_message(f'{package} failed to install.')
        except Exception as e:
            log_message(f'An error occurred while installing {package}: {str(e)}')
    log_message('Packages installed.\n')

def centos_package_installation():
    packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
    
    #Check Package Manager
    try:
        pkg_manager_cmd = subprocess.check_output(['which', 'yum']).decode().strip()
    except FileNotFoundError:
         raise Exception('Package Manager \'yum\' not found. Please ensure it is installed.')

    #Install Packages with Flags for Exceptions
    for package in packages:
        try:
            subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
            log_message(f'{package} installed.')
        except FileNotFoundError:
            pass
        except subprocess.CalledProcessError:
            log_message(f'{package} failed to install.')
        except Exception as e:
            log_message(f'An error occurred while installing {package}: {str(e)}')
    log_message('Packages installed.\n')

def opensuse_package_installation():
    packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
    
    #Check Package Manager
    try:
        pkg_manager_cmd = subprocess.check_output(['which', 'zypper']).decode().strip()
    except FileNotFoundError:
         raise Exception('Package Manager \'zypper\' not found. Please ensure it is installed.')

    #Install Packages with Flags for Exceptions
    for package in packages:
        try:
            subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
            log_message(f'{package} installed.')
        except FileNotFoundError:
            pass
        except subprocess.CalledProcessError:
            log_message(f'{package} failed to install.')
        except Exception as e:
            log_message(f'An error occurred while installing {package}: {str(e)}')
    log_message('Packages installed.\n')

'''

#BURN INSTALLATION
def Windows_Burn_Installation():
    software_path =
    subprocess.run([software_path])
    result = subprocess.run([software_path], capture_output=True)
    if result.returncode == 0:
            pass
    else:
            log_message('PassMark Failed to Install - Please Install Manually.', result.returncode)

'''

#Network Testing
def network_chk():
    #Setup Sub-Functions
    def ping_google():
        import ping3
        response_time = ping3.ping('google.com')

        if response_time is not None:
            response_time = round(response_time, 5)
            log_message('Ping Successful to Google.com. Response time: ' + str(response_time) + '\n')
        else:
            log_message('Ping failed to Google.com.\n')

    #Create Network Header
    network_header = ("\t\t\t Network Information\n")
    log_message(network_header)

    # gathering all network interfaces (virtual and physical) from the system
    if_addrs = psutil.net_if_addrs()

    #Print each interface name
    for interface_name, interface_addresses in if_addrs.items():
        interface=f'Interface : {interface_name}'
        log_message(interface)

        #Print IP
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                ip=f'[+] IP Address: {address.address}'
                log_message(ip + '\n')
    
    #Run Ping Command
    ping_google()

'''
#CopyxTest
def copy_x_test():
    def file_gen(file_path, size_in_bytes):
        chunk_size = 1024 * 1024 #1MB chunk size for efficient writing

        with open(file_path, 'wb') as file:
            bytes_written=0

            while bytes_written < size_in_bytes:
                chunk = b'\0' *min(chunk_size, size_in_bytes - bytes_written)
                file.write(chunk)
                bytes_written += len(chunk)

        log_message(f'File Generated: {file_path}')

    #Generates a 1GB file within the main directory of C:\  
    file_gen('C:\\log_test.log', 1024 * 1024 * 1024)

    #Calcs MD5_Hash
    def calc_md5(file_path):
        import hashlib
        hash_md5 = hashlib.md5()
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    og_hash = calc_md5('C:\\log_test.log')
    source = 'C:\\log_test.log'
    dest = ''
    new_dest = 'C:\\copyxtest\\log_test.log'

    def copy_source_to_ext(source, dest):
        shutil.copy2(source, dest)

    def copy_ext_to_source(dest, new_dest):
        shutil.copy2(dest, new_dest)

    old = calc_md5(source)
    new = calc_md5(new_dest)

    def compare_hash(old, new):
        if old == new:
            return log_message('Pass_1')
        else:
            print('TBD')
'''
            
#Setup_SNAPD
def setup_snapd():
    try:
        subprocess.run(['sudo','systemctl','enable', '--now', 'snapd.socket'])
    except FileNotFoundError:
        pass        
    if os.error:
        print('Error occurred.')
    else:
        keyboard.press('enter')
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

#Ubuntu:
def os_chooser(operating_system):
    def ubuntu_test():
        log_cpu_info()
        log_memory_info()
        network_chk()
        ubuntu_package_installation()
        setup_snapd()
        linux_info_dumps()
        reminders()
        #Sys_Update()
        #Package_Cleanup()
        #Burn_Linux()
        #Power_State_Testing()
        date_time_end()

    def windows_test():
        log_cpu_info()
        log_memory_info()
        network_chk()
        dxdiag()
        date_time_end()
    
    def rhel_test():
        log_cpu_info()
        log_memory_info()
        network_chk()
        rhel_package_installation()
        setup_snapd()
        linux_info_dumps()
        reminders()
        #Sys_Update()
        #Package_Cleanup()
        #Burn_Linux()
        #Power_State_Testing()
        date_time_end()

    def open_suse_test():
        log_cpu_info()
        log_memory_info()
        network_chk()
        opensuse_package_installation()
        setup_snapd()
        linux_info_dumps()
        reminders()
        #Sys_Update()
        #Package_Cleanup()
        #Burn_Linux()
        #Power_State_Testing()
        date_time_end()

    def centos_test():
        log_cpu_info()
        log_memory_info()
        network_chk()
        centos_package_installation()
        setup_snapd()
        linux_info_dumps()
        reminders()
        #Sys_Update()
        #Package_Cleanup()
        #Burn_Linux()
        #Power_State_Testing()
        date_time_end()

    if operating_system == 'Linux':
        ubuntu_test()

    elif operating_system== 'Windows':
        windows_test()

    elif operating_system == 'CentOS':
        centos_test()

    elif operating_system == 'Red Hat Enterprise Linux':
        rhel_test()

    elif operating_system == 'OpenSUSE Leap':
        open_suse_test()

def main():
    log_break('----------------------------------------------------------------------------------------------')
    date_time_start()
    pip_installs()
    #Define functions PER OS:
    operating_system = os_info()
    os_chooser(operating_system)
    log_break('----------------------------------------------------------------------------------------------')

#MAIN
if __name__ == '__main__':
    main()