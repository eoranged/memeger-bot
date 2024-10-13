from os import environ

from dotenv import load_dotenv

load_dotenv()

# Pyrogram (mtproto)
CLIENT_VERSION = environ.get("TG_CLIENT_VERSION", "unknown 1.0.0")
API_ID = environ.get("TG_CLIENT_API_ID", None)
API_HASH = environ.get("TG_CLIENT_API_HASH", None)
# tg bot
BOT_TOKEN = environ.get("TG_BOT_TOKEN", None)
