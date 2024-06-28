#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

#REMAKE BY NOBITA XD AND TRYTOLIVEALONE



import asyncio
import os
import time
from urllib.request import urlretrieve

import requests as r
import wget
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from config import SUDO_USERS
from .help import *


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(
    filters.command(["vid", "video"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def yt_vid(client: Client, message: Message):
    input_st = message.text
    input_str = input_st.split(" ", 1)[1]
    Man = await edit_or_reply(message, "`Processing...`")
    if not input_str:
        await Man.edit_text(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    await Man.edit_text(f"`Searching {input_str} From Youtube. Please Wait.`")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await Man.edit_text(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    time.time()
    file_path = f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{vid_title}` \n**Requested For ➠** `{input_str}` \n**Channel ➠** `{uploade_r}` \n**Link ➠** `{url}`"
    await client.send_video(
        message.chat.id,
        video=open(file_path, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=downloaded_thumb,
        caption=capy,
        supports_streaming=True,
    )
    await Man.delete()
    for files in (downloaded_thumb, file_path):
        if files and os.path.exists(files):
            os.remove(files)


@Client.on_message(
    filters.command(["song"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def song(client: Client, message: Message):
    input_str = get_text(message)
    rep = await edit_or_reply(message, "`Processing...`")
    if not input_str:
        await rep.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    await rep.edit(f"`Getting {input_str} From Youtube Servers. Please Wait.`")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "720",
            }
        ],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await rep.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    time.time()
    file_path = f"{ytdl_data['id']}.mp3"
    capy = f"**Song Name ➠** `{vid_title}` \n**Requested For ➠** `{input_str}` \n**Channel ➠** `{uploade_r}` \n**Link ➠** `{url}`"
    await client.send_audio(
        message.chat.id,
        audio=open(file_path, "rb"),
        title=str(ytdl_data["title"]),
        performer=str(ytdl_data["uploader"]),
        thumb=downloaded_thumb,
        caption=capy,
    )
    await rep.delete()
    for files in (downloaded_thumb, file_path):
        if files and os.path.exists(files):
            os.remove(files)



add_command_help(
    "•─╼⃝𖠁 ʏᴏᴜᴛᴜʙᴇ ᴅʟ",
    [
        ["song", "Dᴏᴡɴʟᴏᴀᴅ Aᴜᴅɪᴏ Fʀᴏᴍ YᴏᴜTᴜʙᴇ."],
        [
            "video",
            "Dᴏᴡɴʟᴏᴀᴅ Vɪᴅᴇᴏ ғʀᴏᴍ YᴏᴜTᴜʙᴇ ",
        ],
    ],
)
