import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = "19225868"
    API_HASH = "60c8b4510a12fb593dd775409b9f43d2"
    BOT_TOKEN = "5682382680:AAGjG5maWtbBsjWQim6HYJwFdstxZqU4gHQ"
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nI'm A Simple Music Downloader Bot,</b>\n\nJust send me Any Songs name to download it ")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/5f8dce1f31eab05963186.jpg")
    OWNER = os.environ.get("OWNER", "Prabha_sha") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}

