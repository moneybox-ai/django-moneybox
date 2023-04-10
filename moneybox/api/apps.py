from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig


from moneybox.settings import RUN_TYPE

from api.tasks import update_currency


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        if RUN_TYPE == "WEB":
            import api.signals
        else:
            scheduler = BackgroundScheduler()
            scheduler.add_job(update_currency, "interval", minutes=1)
            scheduler.start()
