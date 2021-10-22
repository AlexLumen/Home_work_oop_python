#!/bin/bash

FILE=venv/

if [ ! -d "$FILE" ]; then
    PATH=${PATH}:/usr/local/bin
    #python -m venv venv
fi

source venv/bin/activate &&
pip install -U pip && pip install -r requirements.txt