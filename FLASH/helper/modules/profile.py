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
from asyncio import sleep
import os
import sys
from re import sub
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import SUDO_USERS

flood = {}
profile_photo = "cache/pfp.jpg"


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]


@Client.on_message(
    filters.command(["unblock"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ......")
    if not user_id:
        return await message.edit(
            "ᴘʀᴏᴠɪᴅᴇ ᴜꜱᴇʀ ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴜɴʙʟᴏᴄᴋ"
        )
    if user_id == client.me.id:
        return await tex.edit("ᴅᴏɴᴇ ✅")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**ᴜɴʙʟᴏᴄᴋᴇᴅ** {umention}")


@Client.on_message(
    filters.command(["block"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ......")
    if not user_id:
        return await tex.edit_text(
            "ᴘʀᴏᴠɪᴅᴇ ᴜꜱᴇʀ ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙʟᴏᴄᴋ"
        )
    if user_id == client.me.id:
        return await tex.edit_text("ᴅᴏɴᴇ ✅")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**ʙʟᴏᴄᴋᴇᴅ** {umention}")


@Client.on_message(
    filters.command(["setname"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def setname(client: Client, message: Message):
    tex = await message.reply_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ.....")
    if len(message.command) == 1:
        return await tex.edit(
            "ᴘʀᴏᴠɪᴅᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ꜱᴇᴛ ᴀꜱ ʏᴏᴜʀ ɴᴀᴍᴇ"
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(f"**ᴄʜᴀɴɢᴇᴅ ʏᴏᴜʀ ɴᴀᴍᴇ ᴛᴏ** `{name}`")
        except Exception as e:
            await tex.edit(f"**ᴇʀʀᴏʀ** `{e}`")
    else:
        return await tex.edit(
            "ᴘʀᴏᴠɪᴅᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ꜱᴇᴛ ᴀꜱ ʏᴏᴜʀ ɴᴀᴍᴇ"
        )


@Client.on_message(
    filters.command(["setbio"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def set_bio(client: Client, message: Message):
    tex = await message.edit_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ....")
    if len(message.command) == 1:
        return await tex.edit("ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ ꜱᴇᴛ ᴀꜱ ʙɪᴏ")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"**ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʙɪᴏ ᴛᴏ** `{bio}`")
        except Exception as e:
            await tex.edit(f"**ᴇʀʀᴏʀ** `{e}`")
    else:
        return await tex.edit("Provide text to set as bio.")


@Client.on_message(
    filters.command(["setpfp"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("**ʏᴏᴜʀ ᴘʀᴏꜰɪʟᴇ ᴘʜᴏᴛᴏ ᴄʜᴀɴɢᴇᴅ**")
    else:
        await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ꜱᴇᴛ ᴀꜱ ᴘʀᴏꜰɪʟᴇ ᴘʜᴏᴛᴏ"
        )
        await sleep(3)
        await message.delete()


@Client.on_message(
    filters.command(["vpfp"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.reply_text("ᴘʀᴏꜰɪʟᴇ ᴘʜᴏᴛᴏ ɴᴏᴛ ꜰᴏᴜɴᴅ...")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=message.message_id
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)
