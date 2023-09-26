REPORT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
REPORT_STANDART_DATE_FORMAT = "%d-%m-%Y"
RATE_DATE_FORMAT = "%YYYY-MM-DD"


def convert_date_for_json(date):
    return date.strftime(REPORT_DATETIME_FORMAT)


def convert_date_for_html(date):
    return date.strftime(REPORT_STANDART_DATE_FORMAT)
