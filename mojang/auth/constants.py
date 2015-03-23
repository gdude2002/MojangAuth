__author__ = 'Gareth Coles'

# Base URL

BASE_URL = "https://authserver.mojang.com"

# Custom headers

HEADERS = {
    "Content-Type": "application/json"
}

# Routes

ROUTE_AUTHENTICATE = BASE_URL + "/authenticate"
ROUTE_REFRESH = BASE_URL + "/refresh"
ROUTE_VALIDATE = BASE_URL + "/validate"
ROUTE_SIGNOUT = BASE_URL + "/signout"
ROUTE_INVALIDATE = BASE_URL + "/invalidate"

# Payloads (these are here in case the base payloads can have any other
# constant parameters in the future)

PAYLOAD_AUTHENTICATE = {
    "agent": {  # Pretend to be Minecraft so we can get usernames, etc
        "name": "Minecraft",
        "version": 1
    },

    "username": None,
    "password": None,
    "clientToken": None
}

PAYLOAD_REFRESH = {
    "accessToken": None,
    "clientToken": None
}

PAYLOAD_VALIDATE = {
    "accessToken": None
}

PAYLOAD_SIGNOUT = {
    "username": None,
    "password": None
}

PAYLOAD_INVALIDATE = {
    "accessToken": None,
    "clientToken": None
}
