__author__ = 'Gareth Coles'


class MojangApiException(Exception):
    def __init__(self, message):
        self.message = message


class MethodNotAllowedException(MojangApiException):
    message = "The method specified in the request is not allowed for the " \
              "resource identified by the request URI"


class NotFoundException(MojangApiException):
    message = "The server has not found anything matching the request URI"


class ForbiddenOperationException(MojangApiException):
    message = ""

    def __init__(self, message, cause=None):
        super(ForbiddenOperationException, self).__init__(message)

        self.cause = cause


class IllegalArgumentException(MojangApiException):
    pass


class UnsupportedMediaTypeException(MojangApiException):
    pass


class UnknownException(MojangApiException):
    pass
