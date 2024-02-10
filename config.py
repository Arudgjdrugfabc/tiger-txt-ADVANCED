import os

API_ID = API_ID = 26724120

API_HASH = os.environ.get("API_HASH", "2370ac15ee55f834bc025baa8daa948f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6885831766:AAHqymvA1JeU7fiew58zGQlr8PVKWwzDQIA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1297798209))

LOG = -1002036169570

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6826891165").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


