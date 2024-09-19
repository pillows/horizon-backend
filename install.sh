#!/bin/sh

python3 -m  venv venv
source venv/bin/activate
pip3 install -r requirements.txt

chmod +x start.sh
./start.sh