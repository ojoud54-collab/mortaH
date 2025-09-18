#!/usr/bin/env bash
set -e
echo "Installing Python dependencies..."
pip install -r backend/requirements.txt
echo "Running migrations..."
python backend/manage.py migrate --noinput
echo "Collecting static files..."
python backend/manage.py collectstatic --noinput
echo "Build step finished."