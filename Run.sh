#!/bin/bash
#Error code: || { echo ""; exit 1; }
# CURRENTLY UNTESTED #
#########################################################################################################################################################
#                                                                       VARIABLES                                                                       #
#########################################################################################################################################################
usr=${SUDO_USER:-$(whoami)}

#########################################################################################################################################################

#Establish super user rights
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root (use sudo)." >&2
    exit 1
fi
#########################################################################################################################################################
#                                                                       FUNCTIONS                                                                       #
#########################################################################################################################################################
#Create a quick function to simplify error exiting.
#This will almost certainly get used in many scripts...
error_exit() {
    echo "$1" >&2
    exit 1
}

# Function to check and install Python 3.12
install_python3_12() {
    if ! python3 --version 2>/dev/null | grep -q "^Python 3.12."; then
        echo "Python 3.12 not detected. Installing..."
        apt update -y || { echo "Failed to update apt. Check your network connection."; exit 1; }
        apt install -y software-properties-common || { echo "Failed to install required tools."; exit 1; }
        add-apt-repository -y ppa:deadsnakes/ppa || { echo "Failed to add Python PPA."; exit 1; }
        apt update -y || { echo "Failed to update apt after adding PPA."; exit 1; }
        apt install -y python3.12 python3.12-distutils || { echo "Python 3.12 installation failed."; exit 1; }
        echo "Setting Python 3.12 as default for python3."
        update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
        update-alternatives --set python3 /usr/bin/python3.12
    else
        echo "Python 3.12 is already installed and set as default."
    fi
}

#Download APT packages
install_apt_packs() {
    apt-get update -y || { echo "Failed to perform apt update. Do you have Network?"; exit 1; }
    apt-get install -y python3.12 || { echo "Failed to install python3.12."; exit 1; }
    apt-get install -y ipmitool || { echo "Failed to install ipmitool."; exit 1; }
    apt-get install -y net-tools || { echo "Failed to install net-tools."; exit 1; }
}

#Install python dependencies
install_py_deps() {
    python3 -m pip install psutil || { echo "Failed to install psutil."; exit 1; }
    python3 -m pip install ping3 || { echo "Failed to install ping3."; exit 1; }
    python3 -m pip install platform || { echo "Failed to install platform Python package."; exit 1; }
    python3 -m pip install colorama || { echo "Failed to install colorama Python package."; exit 1; }
}


#########################################################################################################################################################
#/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|#
#########################################################################################################################################################
#                                                                          SCRIPT                                                                       #
#########################################################################################################################################################
# Install Python 3.12 if not already present
install_python3_12

#Download and install apt_packs
install_apt_packs

#Install Python Dependencies
install_py_deps

#Copy over files to OS system Desktop
mkdir -p /home/$usr/Desktop/Auto_OS_Test || { echo "Failed to create Desktop directory."; exit 1; }
cp -av ./Automated_OS_Testing-main/ /home/$usr/Desktop/Auto_OS_Test || { echo "Failed to copy files to Desktop Directory 'Auto_OS_Test'."; exit 1; }

#Switch to AUTO_OS Desktop folder
cd /home/$usr/Desktop/Auto_OS_Test || { echo "Failed to navigate into Desktop OS Test Directory."; exit 1; }

#Create HW Dump
chmod +x ./HW_DUMP/V2_HW_DUMP.sh || { echo "Failed to make HW Dump executable."; exit 1; }
bash ./HW_DUMP/V2_HW_DUMP.sh || { echo "Failed to execute HW DUMP. Ensure the V2_HW_DUMP.sh script exists and is executable."; exit 1; }



#Launch main OS Test
su $usr
python3 /home/$usr/Desktop/Auto_OS_Test/Automated_OS_Testing-main/Auto_OS_Test_v2.py || { echo "The script crashed or failed out... :("; exit 1; }

echo "Testing Completed. Please review logs for any missing information."
#########################################################################################################################################################
#/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|/|\/|\|#
#########################################################################################################################################################
