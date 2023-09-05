from django.conf import settings


class Utils:
    @staticmethod
    def convert_date(date):
        return date.strftime(settings.DATE_FORMAT)
