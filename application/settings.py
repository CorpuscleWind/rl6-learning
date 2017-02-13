import os

from config import SafeConfigParser

config = SafeConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLATFORM_CONFIG_NAME = "local.conf"

production_config = os.path.join('/etc', 'rl', PLATFORM_CONFIG_NAME)
development_config = os.path.join(BASE_DIR, 'conf', PLATFORM_CONFIG_NAME)

config_path = production_config if os.path.exists(production_config) else development_config
config.read(config_path)

SECRET_KEY = 'tuu)0lx#ticu6f%^o91+%==xgw@vpc5x9zyq58^8wttj&^91n+'
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'feedback',
    'learning'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'application.urls'

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

WSGI_APPLICATION = 'application.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'ENGINE', 'django.db.backends.mysql'),
        'NAME': config.get('database', 'NAME'),
        'USER': config.get('database', 'USER'),
        'PASSWORD': config.get('database', 'PASSWORD'),
        'HOST': config.get('database', 'HOST', '127.0.0.1'),
        'PORT': config.getint('database', 'PORT', 3306),
        'OPTIONS': {'charset': 'utf8'},
        'TEST_CHARSET': 'utf8',
    }
}

AUTH_PASSWORD_VALIDATORS = []
AUTH_USER_MODEL = 'core.User'

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = 'collected_static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'), )

MEDIA_ROOT = config.get('common', 'media', os.path.join(BASE_DIR, 'media'))

MEDIA_URL = '/media/'
