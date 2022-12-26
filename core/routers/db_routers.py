class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}  # what application's access it has like

    # we want to keep users , sessions, admin into users_db

    def db_for_read(self, model, **hints):  # allow database to read
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):  # allowing relationships on databases
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None


class PracticeRouter:
    route_app_labels = {'practice_db'}  # what access it has like

    def db_for_read(self, model, **hints):  # allow database to read
        if model._meta.app_label in self.route_app_labels:
            return 'practice_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'practice_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'practice_db'
        return None


class Aqua:
    route_app_labels = {'aqua'}  # what access it has like  app_name

    def db_for_read(self, model, **hints):  # allow database to read
        if model._meta.app_label in self.route_app_labels:
            return 'aqua_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'aqua_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'aqua_db'
        return None
