from base.settings.settings import *
from base.settings.base_settings import *

AUTH_USER_MODEL = 'practice.User'
INSTALLED_APPS = BASE_INSTALLED_APPS + ['practice.practice']
DATABASE_ROUTERS = ['practice.db_router.DatabaseRouter']
WSGI_APPLICATION = 'practice.wsgi.application'
ALLOWED_APPS = BASE_ALLOWED_APPS + ['practice']