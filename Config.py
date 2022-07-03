import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "12429107"))
    API_HASH = os.environ.get("API_HASH", "2c1096dfd767dfdfab961bb2fffe6be3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "R125R")
    SUPPORT = os.environ.get("SUPPORT", "R125R")
    CHANNEL = os.environ.get("CHANNEL", "QQQLO")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
