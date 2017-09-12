#!/bin/bash
#browse to https://www.tensorflow.org/install/install_linux#InstallingVirtualenv
#use python 2.7 commands
sudo apt-get install python-pip python-dev python-virtualenv # for Python 2.7
#create virtual env directory
#assume we want to install virtual environment in user's home directory
cd
mkdir tensorflow-pip-install
#create virtual environment:
virtualenv --system-site-packages tensorflow-pip-install # for Python 2.7
#activate virtual environment:
source ~/tensorflow-pip-install/bin/activate
# ensure latest pip
easy_install -U pip
#install tensorflow with gpu support:
pip install --upgrade tensorflow-gpu  # for Python 2.7 and GPU
pip install jupyter
