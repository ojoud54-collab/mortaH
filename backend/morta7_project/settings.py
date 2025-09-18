import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'changeme')
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'
INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rest_framework',
    'apps.accounts','apps.orders',
]
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware']
ROOT_URLCONF = 'morta7_project.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':[ 'django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'morta7_project.wsgi.application'
AUTH_USER_MODEL = 'accounts.User'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework_simplejwt.authentication.JWTAuthentication',)}
# --- Render deployment additions ---
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '.onrender.com,localhost').split(',')
# --- end Render additions ---