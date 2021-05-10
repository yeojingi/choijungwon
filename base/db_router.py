class BaseDatabaseRouter(object):
    ALLOWED_APPS = None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.ALLOWED_APPS:
            return 'default'
        else:
            return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return app_label in self.ALLOWED_APPS
