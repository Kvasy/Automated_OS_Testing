#!/bin/bash
yum update -y
yum install gcc openssl-devel bzip2-devel libffi-devel -y
yum groupinstall "Development Tools"

cd /
wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz
tar -xzf Python 3.10.2.tgz
cd /
cd Python-3.10.2
chmod +x ./configure
./configure --enable-optimizations
make altinstall
python3.10 -V
