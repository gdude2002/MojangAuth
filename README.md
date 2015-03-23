MojangAuth
==========

This is a Python library for interacting with [Mojang's Authentication API](http://wiki.vg/Authentication).
It's intended to be used for webapps and the like, but any Python project could use it.

Note that while Mojang has said that this [should be used for custom logins](https://twitter.com/KrisJelbring/status/453573406341206016),
they also stated that [credentials should never be collected from users](https://twitter.com/KrisJelbring/status/461390585086361600).
Be responsible and use at your own discretion.

Usage
=====

* Install as usual [from PyPi](https://pypi.python.org/pypi/MojangAuth) or `setup.py install`.

`mojang.auth.Account` can be used as follows.

```python
client_token = "My client secret"

account = Account(client_token)

# Authenticate using the user's username and password.

account.authenticate("username_or_email", "password")

print("{}: {}".format(account.username, account.uuid))

# Refresh the user's access token to make sure it's still valid.
# If this raises an exception, their token is no longer valid.

try:
    account.refresh()
except Exception:
    print("Account's token is no longer valid.")
    exit()

# Validate that this is the session they logged into most recently.
# Use `refresh` to check validity - This is for servers to check that the
# user didn't log in since this token was obtained.

if account.validate():
    print("This is the user's most recent session.")
    
    # Sign out all of the user's logged-in sessions everywhere.
    # Don't use this if you just want to make your token invalid.

    account.signout()
else:
    print("The user has logged in elsewhere since obtaining this session.")
    
    # Invalidate this login session.

    account.invalidate()

```
