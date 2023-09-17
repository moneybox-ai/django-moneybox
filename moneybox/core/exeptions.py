class RateNotExist(Exception):
    def __init__(self, message='Wrong Data input or this rate doesn`t exist'):
        self.message = message
        super().__init__(self.message)
