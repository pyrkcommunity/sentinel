#!/bin/bash

cd ~

sudo apt-get update
sudo apt-get -y install python-virtualenv
sudo locale-gen "en_US.UTF-8"

export LC_ALL="en_US.UTF-8" && export LC_CTYPE="en_US.UTF-8"
git clone https://github.com/zocteam/sentinel.git && cd sentinel
virtualenv ./venv
./venv/bin/pip install -r requirements.txt

echo "* * * * * cd $(pwd) && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1" >> /etc/crontab
