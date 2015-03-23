__author__ = 'Gareth Coles'

from network import do_authentication, do_refresh, do_invalidate, do_signout, \
    do_validate


class Account(object):
    __client_token = ""
    __access_token = ""

    __username = ""
    __uuid = ""
    __legacy = False
    __logged_in = False
    __profiles = []

    @property
    def legacy(self):
        return self.__legacy

    @property
    def logged_in(self):
        return self.__logged_in

    @property
    def profiles(self):
        return self.__profiles

    @property
    def username(self):
        return self.__username

    @property
    def uuid(self):
        return self.__uuid

    def __init__(self, client_token):
        self.__client_token = client_token

    def authenticate(self, username, password):
        data = do_authentication(self.__client_token, username, password)
        del username, password

        self.__profiles = data["availableProfiles"]
        self.__access_token = data["accessToken"]

        profile = data["selectedProfile"]

        self.__uuid = profile["id"]
        self.__username = profile["name"]
        self.__legacy = profile["legacy"]

        self.__logged_in = True

    def refresh(self):
        data = do_refresh(self.__client_token, self.__access_token)

        self.__access_token = data["accessToken"]

        profile = data["selectedProfile"]

        self.__uuid = profile["id"]
        self.__username = profile["name"]

    def validate(self):
        return do_validate(self.__access_token)

    def signout(self, username, password):
        data = do_signout(username, password)
        del username, password

        self.__logged_in = not data
        return data

    def invalidate(self):
        data = do_invalidate(self.__client_token, self.__access_token)

        self.__logged_in = not data
        return data
