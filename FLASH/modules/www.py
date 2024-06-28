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



import time
import asyncio
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions

from config import CMD_HANDLER
from config import BOT_VER, BRANCH as brch
from X import CMD_HELP, StartTime
from X.helpers.basic import edit_or_reply
from X.helpers.constants import WWW
from X import app 
from X.helpers.PyroHelpers import SpeedConvert
from config import SUDO_USERS
from X.utils.tools import get_readable_time
from X.modules.bot.inline import get_readable_time
from X.helpers.adminHelpers import DEVS

from .help import *

modules = CMD_HELP

@Client.on_message(
    filters.command(["speed", "speedtest"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(
    filters.command(["dc"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command(["cping"], ".") & (filters.me | filters.user(SUDO_USERS))
)
@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def module_ping(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="ping")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")


@Client.on_message(
    filters.command(["alive"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def module_peler(client: Client, message: Message):
    cdm = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="alive")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
            )
        except BaseException:
            pass


add_command_help(
    "•─╼⃝𖠁 ꜱᴘᴇᴇᴅᴛᴇꜱᴛ",
    [
        ["dc", "Tᴏ ꜱᴇᴇ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ DC."],
        [
            f"speedtest `or` {cmd}speed",
            "Tᴏ ᴛᴇꜱᴛ ʏᴏᴜʀ ꜱᴇʀᴠᴇʀ ꜱᴘᴇᴇᴅ.",
        ],
    ],
)


add_command_help(
    "•─╼⃝𖠁 Pɪɴɢ",
    [
        ["ping", "Tᴏ Sʜᴏᴡ Yᴏᴜʀ Bᴏᴛ'ꜱ Pɪɴɢ."],
        ["pink", "Tᴏ Sʜᴏᴡ Yᴏᴜʀ Bᴏᴛ'ꜱ Pɪɴɢ ( Tʜᴇ ᴀɴɪᴍᴀᴛɪᴏɴ ɪꜱ ɪᴜꜱᴛ ᴅɪғғᴇʀᴇɴᴛ )."],
    ],
  )
