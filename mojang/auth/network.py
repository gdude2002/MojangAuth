__author__ = 'Gareth Coles'

import json
import requests

from constants import *
from exceptions import MethodNotAllowedException, NotFoundException, \
    ForbiddenOperationException, IllegalArgumentException, \
    UnsupportedMediaTypeException, UnknownException


def raise_exception(payload):
    """

    :param payload:
    :type payload: dict
    :return:
    """

    if "error" in payload:
        error = payload.get("error")
        error_message = payload.get("errorMessage", "Unknown error")
        cause = payload.get("cause", None)

        if error == "Method Not Allowed":
            raise MethodNotAllowedException(error_message)
        elif error == "Not Found":
            raise NotFoundException(error_message)
        elif error == "ForbiddenOperationException":
            raise ForbiddenOperationException(error_message, cause)
        elif error == "IllegalArgumentException":
            raise IllegalArgumentException(error_message)
        elif error == "Unsupported Media Type":
            raise UnsupportedMediaTypeException(error_message)
        else:
            raise UnknownException(error_message)


def do_authentication(client_token, username, password):
    payload = PAYLOAD_AUTHENTICATE

    payload["clientToken"] = client_token
    payload["username"] = username
    payload["password"] = password

    request = requests.post(
        ROUTE_AUTHENTICATE, headers=HEADERS, data=json.dumps(payload)
    )

    del payload, password

    result = request.json()

    raise_exception(result)
    return result


def do_refresh(client_token, access_token):
    payload = PAYLOAD_REFRESH

    payload["clientToken"] = client_token
    payload["accessToken"] = access_token

    request = requests.post(
        ROUTE_REFRESH, headers=HEADERS, data=json.dumps(payload)
    )

    del payload, access_token

    result = request.json()

    raise_exception(result)
    return result


def do_validate(access_token):
    payload = PAYLOAD_VALIDATE

    payload["accessToken"] = access_token

    request = requests.post(
        ROUTE_VALIDATE, headers=HEADERS, data=json.dumps(payload)
    )

    del payload, access_token

    if request.text:
        return False

    return True


def do_signout(username, password):
    payload = PAYLOAD_SIGNOUT

    payload["username"] = username
    payload["password"] = password

    request = requests.post(
        ROUTE_SIGNOUT, headers=HEADERS, data=json.dumps(payload)
    )

    del payload, password

    if request.text:
        return False

    return True


def do_invalidate(client_token, access_token):
    payload = PAYLOAD_INVALIDATE

    payload["clientToken"] = client_token
    payload["accessToken"] = access_token

    request = requests.post(
        ROUTE_INVALIDATE, headers=HEADERS, data=json.dumps(payload)
    )

    del payload, access_token

    if request.text:
        return False

    return True
