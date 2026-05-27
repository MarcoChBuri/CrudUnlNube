#!/bin/bash
# 1. Collect static files so WhiteNoise doesn't crash (HTTP 500)
python manage.py collectstatic --noinput

# 2. Run database migrations to prevent missing tables (HTTP 500)
python manage.py migrate

# 3. Start Gunicorn bound to 0.0.0.0:8000 (CRITICAL)
gunicorn --bind=0.0.0.0:8000 --timeout 600 core.wsgi
