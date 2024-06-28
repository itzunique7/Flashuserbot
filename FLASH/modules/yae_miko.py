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

import random
from pyrogram import Client, filters
from config import SUDO_USERS
from .help import * 

hl = "."

@Client.on_message(
    filters.command(["miko"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def demon(client, message):
    args = message.text.split(" ")[1:]
    demondata = [
  "https://graph.org/file/d68e4d0111a07d9e5835d.jpg",
  "https://graph.org/file/5ce76ba089ae46f8d5d5d.jpg",
  "https://graph.org/file/d2937a948070442165bb2.jpg",
  "https://graph.org/file/599a7d1bac34d648861cf.jpg",
  "https://graph.org/file/30eaea94745143bf34557.jpg",
  "https://graph.org/file/d68e4d0111a07d9e5835d.jpg",
  "https://graph.org/file/30eaea94745143bf34557.jpg",
  "https://graph.org/file/d2937a948070442165bb2.jpg",
    ]
    demon_url = random.choice(demondata)
    await message.reply_photo(demon_url)

add_command_help(
    "•─╼⃝𖠁 Yᴀᴇ ᴍɪᴋᴏ",
    [
       ["miko", "Gɪᴠᴇ random Yᴀᴇ ᴍɪᴋᴏ pic."],
        ],
)
