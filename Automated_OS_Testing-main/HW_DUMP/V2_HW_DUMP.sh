#!/bin/bash

#Function to perform Package Update
perform_package_update() {
    echo "Performing Package Update..."
    $PM_CMD update
}

#Function to install lsb-release to get extra system data
install_lsb_release() {
    echo "Attempting Installation of lsb-release..."
    $PM_CMD install lsb-release
}

#Function to construct JSON Output
construct_json_output() {
    echo "Constructing JSON Output file..."
    json="{
        \"SERIAL\": \"$serial\",
        \"DMIDECODE\": \"$dmi\",
        \"CPU\": \"$cpu\",
        \"MEMORY\": \"$mem\",
        \"LSBLK\": \"$blk\",
        \"LSUSB\": \"$usb\",
        \"LSHW\": \"$hw\",
        \"LSPCI\": \"$pci\",
        \"LSDEV\": \"$dev\",
        \"LSMOD\": \"$mod\",
        \"LSB_RELEASE\": \"$release\",
        \"PING\": \"$ping\",
    }"
echo "$json" > "$serial.json"
echo "JSON output saved to: $serial.json"
}

#Ask for user input to prompt for Operating System selection: 
echo "Please select your operating system: "
select os in "Ubuntu" "Red Hat" "CentOS" "OpenSUSE"; do 
    case $os in 
        "Ubuntu" ) PM_CMD='apt'; break;;
        "Red Hat" | "CentOS" ) PM_CMD='yum'; break;;
        "OpenSUSE" ) PM_CMD='zypper'; break;;
    esac
done

echo "Using package manager command: $PM_CMD"

perform_package_update

install_lsb_release

#Run command and store output into a variable
dmi=`dmidecode`
cpu=`lscpu`
mem=`lsmem`
blk=`lsblk`
usb=`lsusb`
hw=`lshw`
pci=`lspci`
dev=`lsdev`
mod=`lsmod`
release=`lsb_release`

#Add a ping function for network testing
ping=`ping www.google.com -c 4 -D`

#Add query for Serial (Still under test, but useful)
serial=`dmidecode | grep -m 1 "Serial Number: "`




