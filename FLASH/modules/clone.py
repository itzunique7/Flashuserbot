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

import os
from pyrogram import *
from pyrogram.types import *
from STORM.helper.basic import edit_or_reply, get_text, get_user
from config import SUDO_USERS

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "404 : Bio Lost")

@Client.on_message(
    filters.command(["clone"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await message.edit_text("ᴄʟᴏɴɪɴɢ.....")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("ᴡʜᴏᴍ ɪ ꜱʜᴏᴜʟᴅ ᴄʟᴏɴᴇ.....?")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**ɴᴏᴡ ɪ'ᴍ** {f_name}")

@Client.on_message(
    filters.command(["revert"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def revert(client: Client, message: Message):
    await message.edit("ʀᴇᴠᴇʀᴛɪɴɢ......")
    r_bio = BIO

    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("ɪ ᴀᴍ ʙᴀᴄᴋ....!")
