import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = "2192067"
    API_HASH = "d2e0ba99f1b9cdb632b43633edb76f11"
    BOT_TOKEN = "5851948681:AAGCEfMnl5LTxI4dctfsOZOJdzJsg2PZzw0"
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nI'm A Simple Music Downloader Bot,</b>\n\nJust send me Any Songs name to download it ")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/5f8dce1f31eab05963186.jpg")
    OWNER = os.environ.get("OWNER", "Prabha_sha") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}

