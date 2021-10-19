#!/bin/bash

FILE=venv/

if [ ! -d "$FILE" ]; then
    sudo apt-get update
    sudo apt-get install python3.9
    python -m venv venv
fi

source venv/bin/activate &&
pip install -U pip && pip install -r requirements.txt