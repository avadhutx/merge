import os


class Config(object):
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    API_ID = int(os.getenv("API_ID", ""))
    OWNER = int(os.environ.get("OWNER", "589641907"))
    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "yashoswalyo")
    PASSWORD = os.getenv("PASSWORD", "mergebot")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    FLAG = int(
        os.getenv("FLAG", 1)
    )  # Dont Change this(unfinished feature!!) or else bot will stop working
    LOGCHANNEL = (
        os.getenv("LOGCHANNEL") or None
    )  # Add channel id with -100 /\or/\ channel user name without @
