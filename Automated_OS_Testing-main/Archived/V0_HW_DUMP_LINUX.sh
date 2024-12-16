#!/bin/bash

#Check for Package Management command:
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

if command_exists apt; then
    #Ubuntu and Debain based systems
    PM_CMD='apt'
elif command_exists yum; then
    #Red Hat based Systems (Including CentOS)
    PM_CMD='yum'
elif command_exists dnf; then
    #Red Hat based Systems (Including Fedora)
    PM_CMD='dnf'
elif command_exists zypper; then
    #OPEN SUSE
    PM_CMD='zypper'
elif command_exists pacman; then
    #Red Hat based Systems (Including CentOS)
    PM_CMD='pacman'
else
    echo "Error: Unsupported distribution or package manager not found.'
    exit 1
fi

echo "Using package manager command: $PM_CMD"

#Perform Package Update
update="$PM_CMD update"
$update

#Install lsb-release to get extra system data
inst_lsb_rel="$PM_CMD install lsb-release"
$inst_lsb_rel

#Run command and store output into a variable
dmi="$(dmidecode)"
cpu="$(lscpu)"
mem="$(lsmem)"
blk="$(lsblk)"
usb="$(lsusb)"
hw="$(lshw)"
pci="$(lspci)"
dev="$(lsdev)"
mod="$(lsmod)"
release="$(lsb_release)"

#Add a ping function for network testing
ping="$(ping www.google.com -c 4 -D)"

#Add query for Serial (Still under test, but useful)
serial="$(dmidecode | grep -m 1 "Serial Number: ")"

dmi_serial="$(dmidecode | grep Serial Number)"

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

echo "$json" > $serial.json
