from pyrogram import Client, filters

import yt_dlp
from youtube_search import YoutubeSearch
import requests

import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ABS="❤️ Share 🦈"
APPER="Prabha_sha"
OWNER="🧑‍💻Developer 💁‍♂"
CHANNEL="https://t.me/sindupotha"
B2="https://t.me/share/url?url=%E0%B6%94%E0%B6%BA%E0%B7%8F%E0%B6%A7%E0%B6%AD%E0%B7%8A%20%E0%B6%85%E0%B6%BD%E0%B7%94%E0%B6%AD%E0%B7%8A%20%E0%B6%B4%E0%B6%BB%E0%B6%B1%20%E0%B7%84%E0%B7%90%E0%B6%B8%20%E0%B7%83%E0%B7%92%E0%B6%B1%E0%B7%8A%E0%B6%AF%E0%B7%94%E0%B7%80%E0%B6%9A%E0%B7%8A%E0%B6%B8%20%E0%B6%BD%E0%B7%9A%E0%B7%83%E0%B7%92%E0%B6%BA%E0%B7%99%E0%B6%B1%E0%B7%8A%E0%B6%B8%20Download%20%E0%B6%9A%E0%B6%BB%E0%B6%9C%E0%B6%B1%E0%B7%8A%E0%B6%B1%20%E0%B6%B4%E0%B7%94%E0%B6%BD%E0%B7%94%E0%B7%80%E0%B6%B1%E0%B7%8A%20%E0%B6%B6%E0%B7%9C%E0%B6%A7%E0%B7%8A%20%E0%B6%9A%E0%B7%99%E0%B6%B1%E0%B7%99%E0%B6%9A%E0%B7%8A%20%E0%B6%AD%E0%B6%B8%E0%B6%BA%E0%B7%92%20%E0%B6%B8%E0%B7%9A%20%40SinduPothaBot%20%F0%9F%98%8D%F0%9F%A5%80%E2%99%A5%EF%B8%8F%20%0A%E0%B6%94%E0%B6%BA%E0%B7%8F%E0%B6%A7%20%E0%B6%AD%E0%B7%92%E0%B6%BA%E0%B7%99%E0%B6%B1%E0%B7%8A%E0%B6%B1%E0%B7%99%20Start%20%E0%B6%9A%E0%B6%BB%E0%B6%BD%20%E0%B6%94%E0%B6%BA%E0%B7%8F%E0%B6%A7%20%E0%B6%95%E0%B6%B1%E0%B7%92%20%E0%B7%83%E0%B7%92%E0%B6%82%E0%B6%AF%E0%B7%94%E0%B7%80%E0%B7%99%20%E0%B6%B1%E0%B6%B8%20%E0%B6%91%E0%B7%80%E0%B6%B1%E0%B7%8A%E0%B6%B1%20%E0%B7%80%E0%B7%92%E0%B6%AD%E0%B6%BB%E0%B6%BA%E0%B7%92%20%F0%9F%98%87%0A%0ABot%20By%20%40SinduPotha%20%20%E2%99%A5%EF%B8%8F%E2%98%98%EF%B8%8F%0A"
BUTTON1="🎧 Join Channel 🎶♂"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(BUTTON1, url=CHANNEL)
                 ],[
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/{Config.OWNER}"),
                    InlineKeyboardButton(ABS, url=B2)
            ]
          ]
        ),
        reply_to_message_id=message.id
    )


####Without-CMD # youtube_dl


@Client.on_message(filters.text)
def a(client, message):
    query=message.text
    print(query)
    m = message.reply(
  (f'<i><b>Processing ⦁⦁⦁ 🚀</b></i>'),
  reply_markup=InlineKeyboardMarkup(
             [
            [
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/{Config.OWNER}")
            ]
          ]
        ),
        reply_to_message_id=message.id
    )
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 7000:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return
            performer = f"@SinduPotha" 
            thumb_name = f'thumb{message.id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit(
              ('**එහෙම සිංදුවක් නෑනෙ මහත්තයෝ 🥹 ආයෙමත් Try කරල බලන්න. 😌**'),
              reply_markup=InlineKeyboardMarkup(
             [
            [
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/{Config.OWNER}")
            ]
          ]
        ),
        reply_to_message_id=message.id
    )            
            return
    except Exception as e:
        m.edit(
          ("**එහෙම සිංදුවක් නෑනෙ මහත්තයෝ 🥹 ආයෙමත් Try කරල බලන්න. 😌**"),
            reply_markup=InlineKeyboardMarkup(
             [
            [
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/{Config.OWNER}")
            ]
          ]
        ),
        reply_to_message_id=message.id
    )      
        print(str(e))
        return
    m.edit(
      ('<i><b>Uploading ⦁⦁⦁ 🚀</b></i>'),
    reply_markup=InlineKeyboardMarkup(
             [
            [
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/{Config.OWNER}")
            ]
          ]
        ),
    )
  
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 <b>Title:</b> <i>{title}</i>\n💁‍♂️ <b>Uploaded By:</b> @SinduPothaBot'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep,quote=True, title=title, duration=dur, performer=performer, thumb=thumb_name,
          reply_markup=InlineKeyboardMarkup(
             [
            [
                    InlineKeyboardButton(BUTTON1, url=CHANNEL)
            ]
          ]
        ),
        reply_to_message_id=message.id
    )
        m.delete()
    except Exception as e:
        m.edit(
          ('**An Internal error occured; Contact @Prabha_sha 🤷‍♂️**'),
reply_markup=InlineKeyboardMarkup(
            [
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/{Config.OWNER}")
            ]
        ),
    )          
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
