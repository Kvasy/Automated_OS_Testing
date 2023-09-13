#!/bin/bash

echo "Updating system packages..."
yum update -y

echo "Installing Python-3.10 Requirements"
yum install gcc openssl-devel bzip2-devel libffi-devel -y

echo "Installing Group 'Development Tools'"
yum groupinstall "Development Tools"

cd /
echo "Retrieving Python 3.10 Package"
wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz

echo "Unzipping Python 3.10"
tar -xzf Python 3.10.2.tgz

cd /
cd Python-3.10.2
chmod +x ./configure

echo "Enabling optimizations"
./configure --enable-optimizations

echo "Installing Python 3.10"
make altinstall
cd /

echo "Adding Python 3.10 to PATH"
export PATH="/usr/local/bin:$PATH"

echo "Verifying Python 3.10 Installation"
echo "python3.10 -V"
python3.10 -V
