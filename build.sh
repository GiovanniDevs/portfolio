#!/usr/bin/env bash
# Exit on error
set -o errexit

cd mysite

# Install Python dependencies
pip install -r requirements.txt

# Remove old collected static files to prevent stale references
rm -rf static/

# Collect static files (CSS, JS, images) into one folder
# WhiteNoise serves them from there
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate