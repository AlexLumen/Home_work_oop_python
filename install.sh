#!/bin/bash

FILE=venv/

if [ ! -d "$FILE" ]; then
    python -m venv venv
fi

source venv/bin/activate &&
pip install -U pip && pip install -r requirements.txt