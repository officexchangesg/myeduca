# class AuthRouter:
#     route_app_labels = {'auth', 'contenttypes'}
#
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'postgres'
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'postgres'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#             obj1._meta.app_label in self.route_app_labels or
#             obj2._meta.app_label in self.route_app_labels
#         ):
#            return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'postgres'
#         return None
class ShopDbRouter:
    db2use = 'postgres'
    def db_for_read(self, model, **hints):
        return self.db2use
    def db_for_write(self, model, **hints):
        return self.db2use
    def allow_relation(self, obj1, obj2, **hints):
        return self.db2use
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return self.db2use