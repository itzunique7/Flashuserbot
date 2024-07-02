#MIT License

#Copyright (c) 2024 DHIRAJ [AFK]

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

hl = "."

@Client.on_message(
    filters.command(["wallpaper"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def wallpaper(client, message):
    args = message.text.split(" ")[1:]
    walldata = [
        "https://graph.org/file/c7059cd48bc3d88e6305c.jpg",
        "https://graph.org/file/6afb4abad7a5dfbf8457a.jpg",
        "https://graph.org/file/e1e1d4162b57a5723633d.jpg",
        "https://graph.org/file/edfda1673d62374cea8d0.jpg",
        "https://graph.org/file/0ce33c286c8051c831c04.jpg",
        "https://graph.org/file/23e2747fbcd1ca70886f4.jpg",
        "https://graph.org/file/667ebd334de898f345693.jpg",
        "https://graph.org/file/f024b680143b9977031b5.jpg",
        "https://graph.org/file/7d194e5f8c6ff345ce845.jpg",
        "https://graph.org/file/e036aa8337c39e6a09f59.jpg",
        "https://graph.org/file/f66864b6c9920dca16e3c.jpg",
        "https://graph.org/file/b62c6c4fc5fe21ee9a716.jpg",
        "https://graph.org/file/d75fdd510c8e4887bbedd.jpg",
        "https://graph.org/file/c3404d06268339712dfba.jpg",
        "https://graph.org/file/995e6ced2c3f6217a2e6f.jpg",
        "https://graph.org/file/18cbafd2f1f6c4ee3e8a8.jpg",
        "https://graph.org/file/6fb9212fe0d8dbb66f93d.jpg",
        "https://graph.org/file/c166f6bd8ecdd6be4e6df.jpg",
        "https://graph.org/file/683a4b8231c92d053d05f.jpg",
        "https://graph.org/file/cf7f97c0eda1728a4e1db.jpg",
        "https://graph.org/file/8c5a7d726b68a59160cc6.jpg",
        "https://graph.org/file/e28632aeddddf6daa5570.jpg",
        "https://graph.org/file/e5b7bd13f88127473c498.jpg",
        "https://graph.org/file/20f9420d6607c614f544e.jpg",
        "https://graph.org/file/7f18ea5b3dda556b46ca0.jpg",
        "https://graph.org/file/8a8919af9e7d24e4001b6.jpg",
        "https://graph.org/file/7d054f01b6f116cd1f45f.jpg",
    ]
    wallpaper_url = random.choice(walldata)
    await message.reply_photo(wallpaper_url)
