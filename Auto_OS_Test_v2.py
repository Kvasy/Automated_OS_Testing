import platform
import subprocess
import sys
import venv
import os
from Test_Classes import LogMessageFunc, DateTimeHandler, OSPackageInstallations, LinuxInfo, cpu_mem_netwk, install_python


def install_python_ubuntu():
    try:
        subprocess.run(['sudo', 'apt', 'update'])
        subprocess.run(['sudo', 'apt', 'install', 'python3.10'])
    except subprocess.CalledProcessError as e:
        logger.log_message(f'Error install Python3.10 on Ubuntu...{e}')





def check_and_update_python():
    os_name = platform.system()

    if os_name == 'Linux':
        dist_name = platform.linux_distribution()[0].lower()
        if dist_name == 'linux':
            update('apt')
            update.python310('apt')
        elif dist_name == 'centos':
            update('yum')
            update.python310_centos()
        elif dist_name == 'redhat':
            update('yum')
            update.python310('yum')
        elif dist_name == 'open suse':
            update('zypper')
            update.python310('zypper')
            
    elif os_name == 'Windows':
        update.update_windows()


    #Check current version
    subprocess.run(['sudo', 'apt', 'update'])
    current_version = platform.python_version()
    logger.log_message('Current Python Version:' + str(current_version))
    
    #Define Latest Version here: I am thinking 3.7 should be the most specified as it will enable f-strings, but not push EoL OS too far.
    latest_version = "3.10.0"
    
    #Compare Version
    if current_version != latest_version:
        logger.log_message('Attempting Python Update...')
        subprocess.run(['apt', 'install', 'python3.10'])





#CONSTANTS:
LOG_FILE = 'log.txt'
logger = LogMessageFunc(LOG_FILE)
date_time_handler = DateTimeHandler()
linux_info = LinuxInfo(logger)
ospkginstaller = OSPackageInstallations(logger)
Gen_HW = cpu_mem_netwk(logger)
update = install_python()
break_lines = '----------------------------------------------------------------------------------------------'
#pip_packs = ['certifi', 'keyboard', 'psutil', 'ping3']

#Install Packages from requirements.txt
def install_required_packages():
    logger.log_message('Installing Required Packages...')
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

#Verify latest Python >= 3.10


        
def create_and_activate_venv():
    venv_dir = os.path.expanduser('~/AUTO_OS_TEST/.venv')
    os.makedirs(venv_dir, exist_ok=True)
    logger.log_message('Making virtual environment...')
    venv.create(venv_dir, with_pip=True)
        
    #Activate VENV
    activate_script = os.path.join(venv_dir, 'bin', 'activate')
    logger.log_message('Activating Virtual Environment...')
    subprocess.run(['source', activate_script], shell=True)

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
def pip_installs(packs):
    #Add header to PIP Package Installation
    pip_header = "\t\t\t PIP Package Information\n"
    logger.log_message(pip_header)

    #Define the required Packages
    

    #Check and Install Packages
    logger.log_message('[+] Checking & Installation of Prerequisite Pip Packages is starting.')
    
    python_executable = sys.executable
    
    for package in packs:
        try:
            subprocess.run([python_executable, '-m', 'pip', 'install', '--upgrade', 'pip'], capture_output=True, text=True)
            #Run PIP CMD show to check if a package is already installed
            result = subprocess.run([python_executable, 'pip', 'show', package], capture_output=True, text=True)

            #Package is already Installed
            if result.returncode == 0:
                logger.log_message(f'Package {package} is already installed. Skipping Installation')
                try:
                    subprocess.run([python_executable,'-m', 'pip', 'install', '--upgrade', package])
                except subprocess.CalledProcessError as e:
                    logger.log_message(f'An error has occurred during upgrade. Error: {e}')
            
            #package is not installed
            else:
                logger.log_message(f'Installing Package: {package}')
                try:
                    subprocess.run([python_executable,'-m', 'pip', 'install', package])
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

def install_pip():
    #Check if PIP is installed
    python_executable = sys.executable
    try:
        subprocess.run([python_executable, '-m', 'pip', '--version'], check=True)
        logger.log_message('PIP is already installed. Proceeding...')
    except subprocess.CalledProcessError:
        #If pip is NOT installed, install it
        try:
            logger.log_message('PIP is not installed. Installing...')
            subprocess.run(['sudo', 'apt', 'install' ,'python3-pip'], check=True)
            logger.log_message('PIP installed successfully.')
        except subprocess.CalledProcessError as e:
            logger.log_message(f'Error installing PIP: {e}')
            raise

def install_venv():
    subprocess.run(['sudo', 'apt', 'install', 'python3.10-venv'])


#MAIN FUNCTION
def main():
    logger.log_break(break_lines)
    #Pip installs to be replaced with requirements.txt
    #pip_installs(pip_packs)
    date_time_handler.date_time_start(logger)
    os_info()
    operating_system = os_input()
    os_chooser(operating_system)
    date_time_handler.date_time_end(logger)
    logger.log_break(break_lines)

#MAIN
if __name__ == '__main__':
    check_and_update_python()
    install_venv()
    create_and_activate_venv()
    install_pip()
    install_required_packages()
    main()
