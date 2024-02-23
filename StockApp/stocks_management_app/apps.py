from django.apps import AppConfig

class StocksManagementAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stocks_management_app'
    
    # def ready(self):
    #     from . import signals

