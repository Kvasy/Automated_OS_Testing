from datetime import datetime
import subprocess
import platform
import psutil
import ping3


class install_python:
    def __init__(self, pkg_mgr_cmd):
        self.subprocess = subprocess
        self.pkg_mgr_cmd = pkg_mgr_cmd
    
    def update(self, pkg_mgr_cmd):
        self.subprocess.run(['sudo', pkg_mgr_cmd, 'update'])
        
    def python310(self, pkg_mgr_cmd):
        self.subprocess.run(['sudo', pkg_mgr_cmd, 'install', 'python3.10'])
        
    def python310_centos(self, pkg_mgr_cmd):
        self.subprocess.run([])
        self.subprocess.run(['sudo', 'chmod', '+x', 'CentOS7_Python3-10.sh'])
        self.subprocess.run(['./CentOS7_Python3-10.sh'])
        

#Not yet implemented
    def update_windows(self):
        self.subprocess.run(['INSERT_FUNC_TO_DL_PYTHON_HERE'])
        

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
   
    def install_packages(self,pkg_manager_cmd, packages):
        '''
        Install Packages using the specified package manager command.
        '''
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
       
    def ubuntu_package_installation(self):
        '''
        Install packages on Ubuntu
        '''       
        try:
            pkg_manager_cmd = self.subprocess.check_output(['which', 'apt']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'apt-get\' not found. Please ensure it is installed.')
        packages = ['python3-pip', 'qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'snapd', 'mesa-libGLU-devel.x86_64']
        self.install_packages(pkg_manager_cmd, packages)
        

    def rhel_package_installation(self):
        '''
        Install packages on Red Hat Enterprise Linux
        ''' 
        try:
            pkg_manager_cmd = self.subprocess.check_output(['which', 'yum']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'yum\' not found. Please ensure it is installed.')
        packages = ['python3-pip', 'qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'snapd', 'mesa-libGLU-devel.x86_64']
        self.install_packages(pkg_manager_cmd, packages)


    def centos_package_installation(self):
        '''
        Install packages on CentOS
        ''' 
        
        #Check Package Manager
        try:
            pkg_manager_cmd = subprocess.check_output(['which', 'yum']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'yum\' not found. Please ensure it is installed.')
        
        packages = ['python3-pip', 'openssl-devel', 'qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'snapd', 'mesa-libGLU-devel.x86_64']
        self.install_packages(pkg_manager_cmd,packages)
        

    def opensuse_package_installation(self):
        '''
        Install Packages on OpenSUSE
        '''
        try:
            pkg_manager_cmd = self.subprocess.check_output(['which', 'zypper']).decode().strip()
        except FileNotFoundError:
            raise Exception('Package Manager \'zypper\' not found. Please ensure it is installed.')

        packages = ['python3-pip', 'qtcreator','ethtool', 'ipmitool', 'qtbase5-dev', 'qt5-qmake', 'cmake', 'snapd', 'mesa-libGLU-devel.x86_64']
        self.install_packages(pkg_manager_cmd, packages)
        
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
            import psutil
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
            if response_time is not None or 0 or 0.0:
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
