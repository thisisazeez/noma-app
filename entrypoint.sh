#!/usr/bin/env bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create default superuser if it doesn't exist
echo "Ensuring admin user 'sherif' exists..."
python <<'PY'
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','noma.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username, password, email = "sherif", "superadmin100", "sherif@example.com"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Created superuser: {username}")
else:
    print(f"Superuser '{username}' already exists")
PY

echo "Starting Gunicorn..."
exec gunicorn noma.wsgi:application --bind 0.0.0.0:8000 --workers 3
