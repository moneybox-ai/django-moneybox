REPORT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def convert_date(date):
    return date.strftime(REPORT_DATETIME_FORMAT)
