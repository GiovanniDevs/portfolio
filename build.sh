#!/usr/bin/env bash
# Exit on error
set -o errexit
cd mysite
pip install -r requirements.txt

echo "=== DJANGO_SETTINGS_MODULE: $DJANGO_SETTINGS_MODULE ==="
echo "=== Current directory: $(pwd) ==="
python -c "import django; django.setup(); from django.conf import settings; print('STATIC_ROOT:', settings.STATIC_ROOT); print('STATICFILES_DIRS:', settings.STATICFILES_DIRS); print('INSTALLED_APPS:', settings.INSTALLED_APPS)"

python manage.py collectstatic --no-input --clear -v 2
python manage.py migrate