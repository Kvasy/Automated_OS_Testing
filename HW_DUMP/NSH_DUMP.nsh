echo off
echo "starting scan"

smbiosview >> log_dump.txt
memmap >> log_dump.txt
pci >> log_dump.txt

echo "Done"