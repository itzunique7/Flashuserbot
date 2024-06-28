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

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file
from STORM.powers import *
from config import SUDO_USERS

hl = "."
telegraph = Telegraph()
r = telegraph.create_account(short_name="KEX")
auth_url = r["auth_url"]

@Client.on_message(
    filters.command(["tgm", "telegraph"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def uptotelegraph(client: Client, message: Message):
    Client = await message.edit("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...⚡")
    if not message.reply_to_message:
        await Client.edit(
            "**ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ, ᴛᴏ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ....**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Client.edit(f"**ᴇʀʀᴏʀ:** `{exc}`")
            os.remove(m_d)
            return
        dones = (
            f"**ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await Client.edit(dones)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await Client.edit(f"**ᴇʀʀᴏʀ:** `{exc}`")
            return
        geek = f"**ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ** [Telegraph](https://telegra.ph/{response['path']})"
        await Client.edit(geek)
