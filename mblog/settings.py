"""
Django settings for mblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&p@m#kioe0&v_wcepbw2q+nl8(3*38(&0o!8$-g)qb8kj)_#tv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.auth.middleware',
    'essay',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mblog.urls'

WSGI_APPLICATION = 'mblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

MYSQL_HOST = 'w.rdc.sae.sina.com.cn'
MYSQL_PORT = '3307'
MYSQL_USER = '3415on4nal'
MYSQL_PASS = 'mzi11x0wlmyzz1x2iyhlyh312xxkwmk52mly5iwl'
MYSQL_DB   = 'app_xxxxx'

# MYSQL_HOST = 'localhost'
# MYSQL_PORT = '5432'
# MYSQL_USER = 'jiangnan'
# MYSQL_PASS = '123456'
# MYSQL_DB   = 'django'

# from sae._restful_mysql import monkey
# monkey.patch()

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = ('essay/static')


TEMPLATE_CONTEXT_PROCESSORS = ['django.contrib.auth.context_processors.auth', 'essay.templatetags.context_processor.globals_var']