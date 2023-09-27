from rest_framework.exceptions import APIException


class RateNotExist(Exception):
    def __init__(self, message="Wrong Data input or this rate doesn`t exist"):
        self.message = message
        super().__init__(self.message)


class ReportAPIException(APIException):
    def __init__(self, detail, status_code=None):
        super().__init__(detail)
        self.status_code = status_code
