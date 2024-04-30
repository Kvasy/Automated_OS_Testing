#!/bin/bash

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
