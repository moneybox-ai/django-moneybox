REPORT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
REPORT_STANDART_DATE_FORMAT = "%d-%m-%Y"
RATE_DATE_FORMAT = "%YYYY-MM-DD"


def convert_date_to_datetime_format(date):
    return date.strftime(REPORT_DATETIME_FORMAT)


def convert_date_to_standart_format(date):
    return date.strftime(REPORT_STANDART_DATE_FORMAT)
