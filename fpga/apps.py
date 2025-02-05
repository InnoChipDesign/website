from django.apps import AppConfig


class FpgaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fpga'
    verbose_name = 'Программируемая вентильная матрица'
