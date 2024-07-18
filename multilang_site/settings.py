# -*- coding: utf-8 -*-
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
import environ
import dj_database_url
from dotenv import load_dotenv

# Définir le répertoire de base
BASE_DIR = Path(__file__).resolve().parent.parent

# Charger les variables d'environnement à partir du fichier .env
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Initialisation des variables d'environnement
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Accéder à la variable d'environnement
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", 'default-secret-key')
DEBUG = env.bool('DJANGO_DEBUG', default=False)

# Utilisez DEBUG basé sur la présence de 'RENDER' dans les variables d'environnement
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'multilang_site.urls'

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

WSGI_APPLICATION = 'multilang_site.wsgi.application'

# Configuration de la base de données

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Utilisez le moteur approprié pour votre base de données
        'NAME': BASE_DIR / "db.sqlite3",         # Le nom de la base de données ou le chemin vers le fichier de base de données
    }
}


DATABASES["default"] = dj_database_url.parse("postgresql://dbmultilangsite_user:GTCHsrBwrIZQzSUoZ7FiqR6A7yotMGxD@dpg-cq1rn7bv2p9s73d6tpsg-a.frankfurt-postgres.render.com/dbmultilangsite")

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('Français')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static')
]

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
