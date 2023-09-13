from datetime import datetime
import platform
import subprocess
import sys
try:
    import psutil
    import ping3
except ImportError:
    pass



#Adding Classes to attempt simplification
class LogMessageFunc:
    def __init__(self, log_file):
        self.log_file = log_file

    def log_message(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'[{timestamp}] {message}'

        with open (self.log_file, 'a') as log_file:
            log_file.write(log_entry + '\n')

    def log_break(self, message):
        log_entry = f'{message}'
        with open (self.log_file, 'a') as log_file:
            log_file.write(log_entry + '\n')

class DateTimeHandler:
    def __init__(self):
        pass

    def format_date_time(self, current_date_time):
        date = f'Date: {current_date_time.year}/{current_date_time.month}/{current_date_time.day}'
        time = f'Time: {current_date_time.hour}:{current_date_time.minute}:{current_date_time.second}'
        return date, time

    def date_time_start(self, logger):
        start_time_stamp = "\t\t\t START TIME\n"
        logger.log_message(start_time_stamp)

        current_date_time = datetime.now()
        date, time = self.format_date_time(current_date_time)

        logger.log_message(date)
        logger.log_message(time+'\n')

    def date_time_end(self, logger):
        end_time_stamp = "\t\t\t END TIME\n"
        logger.log_message(end_time_stamp)

        current_date_time = datetime.now()
        date, time = self.format_date_time(current_date_time)

        logger.log_message(date)
        logger.log_message(time+'\n')

class LinuxInfo:
    def __init__(self, logger):
        self.logger = logger

    #Info_Dumps_linux
    def lshw(self):
        lshw_header = "\t\t\t LSHW\n"
        try:
            result=subprocess.run(['lshw'], capture_output=True, text=True, check=True)
            self.logger.log_message(result.stdout + '\n')
        except subprocess.CalledProcessError as e:
            self.logger.log_message(f'Error running command lshw: {e}'+ '\n')

    def lsusb(self):
        lsusb_header = "\t\t\t LSUSB\n"
        try:
            result=subprocess.run(['lsusb'], capture_output=True, text=True, check=True)
            self.logger.log_message(result.stdout + '\n')
        except subprocess.CalledProcessError as e:
            self.logger.log_message(f'Error running command lsusb: {e}'+ '\n')

    def lspci(self):
        lspci_header = "\t\t\t LSPCI\n"
        try:
            result=subprocess.run(['lspci'], capture_output=True, text=True, check=True)
            self.logger.log_message(result.stdout + '\n')
        except subprocess.CalledProcessError as e:
            self.logger.log_message(f'Error running command lspci: {e}'+ '\n') 

    def linux_cpu_scan(self):
        #RUN FOR log_cpu_info
        try:
            with open('/proc/cpuinfo', 'r') as f:
                file_info = f.readlines()
                cpuinfo = [x.strip().split(':')[1] for x in file_info if 'model name' in x]
            for index, item in enumerate(cpuinfo):
                cpu = f'[+] Processor {index} : {item}'
                self.logger.log_message(cpu)
        except FileNotFoundError:
            pass

        # This code will print the number of Total CPU cores present
        phys_cores = "[+] Number of Physical cores : " + str(psutil.cpu_count(logical=False))
        total_cores = "[+] Number of Total cores : " + str(psutil.cpu_count(logical=True))
        cpu_frequency = psutil.cpu_freq()
        cpu_max_freq = f"[+] Max Frequency : + {cpu_frequency.max:.2f}Mhz"

        #Log Results
        self.logger.log_message(phys_cores)
        self.logger.log_message(total_cores)
        self.logger.log_message(cpu_max_freq + '\n')


    #Combine all above into single function
    def linux_info_dumps(self):
        self.lshw()
        self.lsusb()
        self.lspci()
        self.linux_cpu_scan()

class OSPackageInstallations:
    def __init__(self, logger):
        self.logger = logger
        self.subprocess = subprocess

    #PACKAGE_INSTALLATION
    #Build Out for installation of Ubuntu Packages - SKIP for Windows [Potentially build tool to detect OS later]
    def ubuntu_package_installation(self):
        packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
        
        #Check Package Manager
        try:
            pkg_manager_cmd = self.subprocess.check_output(['which', 'apt-get']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'apt-get\' not found. Please ensure it is installed.')

        #Install Packages with Flags for Exceptions
        for package in packages:
            try:
                self.subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
                self.logger.log_message(f'{package} installed.')
            except FileNotFoundError:
                self.logger.log_message(f'{package} failed to install. FileNotFoundError')
            except self.subprocess.CalledProcessError as e:
                self.logger.log_message(f'{package} failed to install. Error {e}')
            except Exception as e:
                self.logger.log_message(f'An error occurred while installing {package}: {str(e)}')
        self.logger.log_message('Packages installed.\n')   

    def rhel_package_installation(self):
        packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
        
        #Check Package Manager
        try:
            pkg_manager_cmd = self.subprocess.check_output(['which', 'yum']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'yum\' not found. Please ensure it is installed.')

        #Install Packages with Flags for Exceptions
        for package in packages:
            try:
                self.subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
                self.logger.log_message(f'{package} installed.')
            except FileNotFoundError:
                self.logger.log_message(f'{package} failed to install. FileNotFoundError')
            except self.subprocess.CalledProcessError as e:
                self.logger.log_message(f'{package} failed to install. Error {e}')
            except Exception as e:
                self.logger.log_message(f'An error occurred while installing {package}: {str(e)}')
        self.logger.log_message('Packages installed.\n')  

    def centos_package_installation(self):
        packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
        
        #Check Package Manager
        try:
            pkg_manager_cmd = subprocess.check_output(['which', 'yum']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'yum\' not found. Please ensure it is installed.')
        #Install Packages with Flags for Exceptions
        for package in packages:
            try:
                self.subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
                self.logger.log_message(f'{package} installed.')
            except FileNotFoundError:
                self.logger.log_message(f'{package} failed to install. FileNotFoundError')
            except self.subprocess.CalledProcessError as e:
                self.logger.log_message(f'{package} failed to install. Error {e}')
            except Exception as e:
                self.logger.log_message(f'An error occurred while installing {package}: {str(e)}')
        self.logger.log_message('Packages installed.\n')  

    def opensuse_package_installation(self):
        packages = ['qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'python3-pip', 'snapd', 'mesa-libGLU-devel.x86_64']
        
        #Check Package Manager
        try:
            pkg_manager_cmd = self.subprocess.check_output(['which', 'zypper']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'zypper\' not found. Please ensure it is installed.')

        #Install Packages with Flags for Exceptions
        for package in packages:
            try:
                self.subprocess.run(['sudo', pkg_manager_cmd, 'install', '-y', package], check=True)
                self.logger.log_message(f'{package} installed.')
            except FileNotFoundError:
                self.logger.log_message(f'{package} failed to install. FileNotFoundError')
            except self.subprocess.CalledProcessError as e:
                self.logger.log_message(f'{package} failed to install. Error {e}')
            except Exception as e:
                self.logger.log_message(f'An error occurred while installing {package}: {str(e)}')
        self.logger.log_message('Packages installed.\n')

class cpu_mem_netwk:
    def __init__(self, logger):
        self.logger = logger
        self.subprocess = subprocess

    #Log CPU Information
    def log_cpu_info(self):
        CPU_header = "\t\t\t CPU Information\n"
        self.logger.log_message(CPU_header)
        #Read CPUINFO file to print name of CPU

        #print CPU Model
        os_info = platform.uname()
        cpu_inf = f'CPU Info: {os_info[5]}'
        self.logger.log_message(cpu_inf)    


    #log_memory_information
    def log_memory_info(self):
        #Func. to convert Bytes to GB
        def bytes_to_GB(bytes):
            gb = bytes / (1024 * 1024 * 1024)
            gb = round(gb, 2)
            return gb

        memory_header = "\t\t\t Memory Information\n"
        self.logger.log_message(memory_header)

        #This will print the primary memory details
        virtual_memory = psutil.virtual_memory()
        total_mem = f"[+] Total Memory present : {bytes_to_GB(virtual_memory.total)} Gb"
        self.logger.log_message(total_mem + '\n')

    #Network Testing
    def network_chk(self):
        #Setup Sub-Functions
        def ping_google(self):
            response_time = ping3.ping('google.com')
            if ModuleNotFoundError:
                pass
            if response_time is not None:
                response_time = round(response_time, 5)
                self.logger.log_message('Ping Successful to Google.com. Response time: ' + str(response_time) + '\n')
            else:
                self.logger.log_message('Ping failed to Google.com.\n')

        #Create Network Header
        network_header = ("\t\t\t Network Information\n")
        self.logger.log_message(network_header)

        # gathering all network interfaces (virtual and physical) from the system
        if_addrs = psutil.net_if_addrs()

        #Print each interface name
        for interface_name, interface_addresses in if_addrs.items():
            interface=f'Interface : {interface_name}'
            self.logger.log_message(interface)

            #Print IP
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    ip=f'[+] IP Address: {address.address}'
                    self.logger.log_message(ip + '\n')
        
        #Run Ping Command
        ping_google(self)

    def gen_hw_dump(self):
        self.log_cpu_info()
        self.log_memory_info()
        self.network_chk()

#CONSTANTS:
LOG_FILE = 'log.txt'
logger = LogMessageFunc(LOG_FILE)
date_time_handler = DateTimeHandler()
linux_info = LinuxInfo(logger)
ospkginstaller = OSPackageInstallations(logger)
Gen_HW = cpu_mem_netwk(logger)
break_lines = '----------------------------------------------------------------------------------------------'

#os_info
def os_info():
    #Create Header in LOG
    os_info_header = "\t\t\t OS Information\n"
    logger.log_message(os_info_header)

    #Pull OS Info    
    os_info = platform.uname()
    os = f'OS: {os_info[0]}'
    kernel = f'Release / Kernel: {os_info[2]}'
    version = f'Version: {os_info[3]}'

    logger.log_message(os)
    logger.log_message(kernel)
    logger.log_message(version+'\n')
    return os_info[0]

def os_input():
    os_options = {
        1: 'Ubuntu',
        2: 'Windows',
        3: 'CentOS',
        4: 'Red Hat Enterprise Linux',
        5: 'OpenSUSE Leap'
    }

    while True:
        try:
            user_input = int(input(
                'Which OS is currently under Test?:\n'
                '1. Ubuntu\n'
                '2. Windows\n'
                '3. CentOS\n'
                '4. Red Hat Enterprise Linux\n'
                '5. OpenSUSE Leap\n'
                'Please select a number 1-5 and press \'Enter\': '
            ))
            if user_input in os_options:
                selected_os = os_options[user_input]
                logger.log_message(f'OS: {selected_os}\n')
                return selected_os
            else:
                print('Invalid input! Please enter a number between 1 and 5.: ')
        except ValueError:
            print('Invalid input! Please enter a number between 1 and 5.: ')

#Windows_DxDIAG
def dxdiag():
    DxDIAG_Header = "\t\t\t DxDIAG\n"
    try:
        result=subprocess.run(['dxdiag',  '/t'], capture_output=True, text=True, check=True)
        logger.log_message(DxDIAG_Header)
        logger.log_message('DxDiag run successfully. File generated \n')        
    except subprocess.CalledProcessError as e:
        print(f'Error running command dxdiag: {e}'+ '\n')

#PIP_INSTALLS
def pip_installs():
    #Add header to PIP Package Installation
    pip_header = "\t\t\t PIP Package Information\n"
    logger.log_message(pip_header)

    #Define the required Packages
    pip_packs = ['keyboard', 'psutil', 'ping3']

    #Check and Install Packages
    logger.log_message('[+] Checking & Installation of Prerequisite Pip Packages is starting.')
    
    python_executable = sys.executable
    
    for package in pip_packs:
        try:
            #Run PIP CMD show to check if a package is already installed
            result = subprocess.run([python_executable, 'pip', 'show', package], capture_output=True, text=True)

            #Package is already Installed
            if result.returncode == 0:
                logger.log_message(f'Package {package} is already installed. Skipping Installation')
                try:
                    subprocess.run([python_executable,'-m', 'pip', 'install', '--upgrade', '--user', package])
                except subprocess.CalledProcessError as e:
                    logger.log_message(f'An error has occurred during upgrade. Error: {e}')
            
            #package is not installed
            else:
                logger.log_message(f'Installing Package: {package}')
                try:
                    subprocess.run([python_executable,'-m', 'pip', 'install', '--user', package])
                except:
                    pass

        #Error occurred during Pip show command OR installation
        except subprocess.CalledProcessError as e:
            logger.log_message(f'Failed to check or install package: {package}. Error: {e}')
    logger.log_break('')

#Ubuntu:
def os_chooser(operating_system):
    def ubuntu_test():
        Gen_HW.gen_hw_dump()
        ospkginstaller.ubuntu_package_installation()
        linux_info.linux_info_dumps()     

    def windows_test():
        Gen_HW.gen_hw_dump()
        dxdiag()       
    
    def rhel_test():
        Gen_HW.gen_hw_dump()
        ospkginstaller.rhel_package_installation()
        linux_info.linux_info_dumps()       

    def open_suse_test():
        Gen_HW.gen_hw_dump()
        ospkginstaller.opensuse_package_installation()
        linux_info.linux_info_dumps()       

    def centos_test():
        Gen_HW.gen_hw_dump()
        ospkginstaller.centos_package_installation()
        linux_info.linux_info_dumps()

    if operating_system == 'Ubuntu':
        ubuntu_test()
    elif operating_system == 'Windows':
        windows_test()
    elif operating_system == 'CentOS':
        centos_test()
    elif operating_system == 'Red Hat Enterprise Linux':
        rhel_test()
    elif operating_system == 'OpenSUSE Leap':
        open_suse_test()

#MAIN FUNCTION
def main():
    logger.log_break(break_lines)
    pip_installs()
    date_time_handler.date_time_start(logger)
    os_info()
    operating_system = os_input()
    os_chooser(operating_system)
    date_time_handler.date_time_end(logger)
    logger.log_break(break_lines)

#MAIN
if __name__ == '__main__':
    main()
