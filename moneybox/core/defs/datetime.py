REPORT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
RATE_DATE_FORMAT = "%YYYY-MM-DD"


def convert_date(date):
    return date.strftime(REPORT_DATETIME_FORMAT)
