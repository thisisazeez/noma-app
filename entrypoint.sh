#!/usr/bin/env bash
set -e

# wait for possible services if you add DB later (currently using sqlite)
echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create admin user 'sherif' with provided password if it doesn't exist.
# NOTE: password is stored in the image logs if you build/run; keep that in mind.
echo "Ensuring admin user 'sherif' exists..."
python - <<'PY'
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','noma.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = "sherif"
password = "super admin #codebase"
email = "sherif@example.com"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Created superuser:", username)
else:
    print("Superuser already exists:", username)
PY

echo "Starting gunicorn..."
gunicorn noma.wsgi:application --bind 0.0.0.0:8000 --workers 3
