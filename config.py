import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", "12345"))

    API_HASH = os.environ.get("API_HASH", "48a2eb4ea53bf17eb8679c3ddcd7aec3")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "No")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "No")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "none")
