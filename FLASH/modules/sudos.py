#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

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

import heroku3
from os import getenv
from config import SUDO_USERS, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(OWNER_ID) & filters.command(["addsudo"], ["."]))
async def add_sudo(_, message: Message):
    if not message.reply_to_message:
        await message.reply_text("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ")
        return

    if not HEROKU_APP_NAME or not HEROKU_API_KEY:
        await message.reply_text("ʜᴇʀᴏᴋᴜ ᴄʀᴇᴅᴇɴᴛɪᴀʟꜱ ɴᴏᴛ ꜱᴇᴛ")
        return

    try:
        heroku = heroku3.from_key(HEROKU_API_KEY)
        app = heroku.app(HEROKU_APP_NAME)
    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ ᴀᴄᴄᴇꜱꜱɪɴɢ ʜᴇʀᴏᴋᴜ: {str(e)}")
        return

    ok = await message.reply_text("ᴘʀᴏᴍᴏᴛɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...")

    try:
        heroku_var = app.config()
        target = message.reply_to_message.from_user.id
        sudousers = getenv("SUDO_USERS", "")
        newsudo = f"{sudousers} {target}".strip() if sudousers else str(target)
        heroku_var["SUDO_USERS"] = newsudo
        await ok.edit(f"ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ ᴀᴅᴅᴇᴅ: `{target}`")
    except Exception as e:
        await ok.edit(f"ᴇʀʀᴏʀ ᴀᴅᴅɪɴɢ ꜱᴜᴅᴏ ᴜꜱᴇʀ: {str(e)}")

@Client.on_message(
    filters.command(["sudolist"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gbanlist(client: Client, message: Message):
    users = SUDO_USERS
    ex = await message.edit_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    if not users:
        return await ex.edit("ɴᴏ ᴜꜱᴇʀꜱ ʜᴀᴠᴇ ʙᴇᴇɴ ꜱᴇᴛ ʏᴇᴛ")
    gban_list = "**sᴜᴅᴏ ᴜꜱᴇʀs:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count}** `{i}`\n"
    return await ex.edit(gban_list)
