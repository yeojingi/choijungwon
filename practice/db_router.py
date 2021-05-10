from base.db_router import BaseDatabaseRouter
from practice import settings


class DatabaseRouter(BaseDatabaseRouter):
    ALLOWED_APPS = settings.ALLOWED_APPS
