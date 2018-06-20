ALLOWED_HOSTS = ['*']

# WSGI_APPLICATION = 'gtfsintegrate.wsgi.application'

SECRET_KEY = '5@ch@sqd_+(4eaj2h60qofszfhuuxk#h#f#ehyb&b+drp@v0&s'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gtfsintegrate_$USER',
        'USER': 'www-data',
        'PASSWORD': '',
        'HOST': 'localhost',  # '127.0.0.1' probably works also
        'PORT': '5432',
    }
}
