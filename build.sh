#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

echo "Make migrations..."
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

echo "Collect static files..."
python3 manage.py collectstatic --no-input --clear
