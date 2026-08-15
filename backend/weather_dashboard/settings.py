"""
Django settings for weather_dashboard project.

WHY this file matters:
- This is where we load secrets (API key, secret key) from the .env file
  instead of hardcoding them in source code.
- We configure Django REST Framework (DRF) here so our /api/weather/
  endpoint can return JSON.
- We configure django-cors-headers so the React dev server (running on a
  different port, e.g. 5173) is allowed to call this API in development.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load variables from the .env file into os.environ
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# ------------------------------------------------------------------
# SECURITY
# ------------------------------------------------------------------
# Never hardcode the secret key or API keys. Always read them from
# environment variables (which come from the .env file above).
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'unsafe-default-change-me')

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# The OpenWeatherMap API key used by weather/services.py.
# We read it here (in settings) so all apps have one single source of
# truth for configuration, then services.py imports it from settings.
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '')

# ------------------------------------------------------------------
# APPLICATION DEFINITION
# ------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',

    # Local apps
    'weather',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # CorsMiddleware must be placed as high as possible, and before
    # CommonMiddleware, so that CORS headers are added to every response.
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'weather_dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'weather_dashboard.wsgi.application'

# ------------------------------------------------------------------
# DATABASE (SQLite for development)
# ------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weather',
        'USER': 'root',
        'PASSWORD': 'loli123,sara',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
# ------------------------------------------------------------------
# PASSWORD VALIDATION
# ------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------------
# STATIC FILES
# ------------------------------------------------------------------
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------------------------------------------
# DJANGO REST FRAMEWORK
# ------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# ------------------------------------------------------------------
# CORS (allow the React dev server to call this API)
# ------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]
