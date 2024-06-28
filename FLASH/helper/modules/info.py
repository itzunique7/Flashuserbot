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
from pyrogram import Client, filters
from config import SUDO_USERS

def user(user):
    text = "**ᴜꜱᴇʀ-ᴅᴇᴛᴀɪʟꜱ**\n"
    text += f"\n**• ꜰɪʀꜱᴛ ɴᴀᴍᴇ:** `{user.first_name}`"
    text += f"\n\n**• ʟᴀꜱᴛ ɴᴀᴍᴇ:** `{user.last_name},`" if user.last_name else ""
    text += f"\n\n**• ᴜꜱᴇʀ ɪᴅ:** `{user.id}`"
    text += f"\n\n**• ᴜꜱᴇʀɴᴀᴍᴇ:** @{user.username}" if user.username else ""
    text += f"\n\n**• ᴜꜱᴇʀ ʟɪɴᴋ:** {user.mention}" if user.username else ""
    text += f"\n\n**• ᴅᴄ ɪᴅ:** `{user.dc_id}`" if user.dc_id else ""
    text += f"\n\n**• ɪꜱ ᴅᴇʟᴇᴛᴇᴅ:** ᴛᴜʀᴇ" if user.is_deleted else ""
    text += f"\n\n**• ɪꜱ ʙᴏᴛ:** ᴛᴜʀᴇ" if user.is_bot else ""
    text += f"\n\n**• ɪꜱ ᴠᴇʀɪꜰɪᴇᴅ:** ᴛᴜʀᴇ" if user.is_verified else ""
    text += f"\n\n**• ɪꜱ ʀᴇꜱᴛʀɪᴄᴛᴇᴅ:** ᴛᴜʀᴇ" if user.is_verified else ""
    text += f"\n\n**• ɪꜱ ꜱᴄᴀᴍ:** ᴛᴜʀᴇ" if user.is_scam else ""
    text += f"\n\n**• ɪꜱ ꜰᴀᴋᴇ:** ᴛᴜʀᴇ" if user.is_fake else ""
    text += f"\n\n**• ɪꜱ ꜱᴜᴘᴘᴏʀᴛ:** ᴛᴜʀᴇ" if user.is_support else ""
    text += f"\n\n**• ʟᴀɴɢᴜᴀɢᴇ:** {user.language_code}" if user.language_code else ""
    text += f"\n\n**• ꜱᴛᴀᴛᴜꜱ:** {user.status}" if user.status else ""
    return text


def chat(chat):
    text = "**ᴄʜᴀᴛ-ᴅᴇᴛᴀɪʟꜱ**\n" 
    text += f"\n\n**• ᴛɪᴛʟᴇ:** `{chat.title}`"
    text += f"\n\n**• ᴄʜᴀᴛ ɪᴅ:** `{chat.id}`"
    text += f"\n\n**• ᴜꜱᴇʀɴᴀᴍᴇ:** @{chat.username}" if chat.username else ""
    text += f"\n\n**• ᴛʏᴘᴇ:** `{chat.type}`"
    text += f"\n\n**• ᴅᴄ ɪᴅ:** `{chat.dc_id}`"
    text += f"\n\n**• ɪꜱ ᴠᴇʀɪꜰɪᴇᴅ:** ᴛᴜʀᴇ" if chat.is_verified else ""
    text += f"\n\n**• ɪꜱ ʀᴇꜱᴛʀɪᴄᴛᴇᴅ:** ᴛᴜʀᴇ" if chat.is_verified else ""
    text += f"\n\n**• ɪꜱ ᴄʀᴇᴀᴛᴏʀ:** ᴛᴜʀᴇ" if chat.is_creator else ""
    text += f"\n\n**• ɪꜱ ꜱᴄᴀᴍ:** ᴛᴜʀᴇ" if chat.is_scam else ""
    text += f"\n\n**• ɪꜱ ꜰᴀᴋᴇ:** ᴛᴜʀᴇ" if chat.is_fake else ""
    return text

@Client.on_message(
    filters.command(["info"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def info(client, message):
    if (not message.reply_to_message) and ((not message.forward_from) or (not message.forward_from_chat)):
        info = user(message.from_user)
    elif message.reply_to_message and message.reply_to_message.forward_from:
        info = user(message.reply_to_message.forward_from)
    elif message.reply_to_message and message.reply_to_message.forward_from_chat:
        info = chat(message.reply_to_message.forward_from_chat)
    elif (message.reply_to_message and message.reply_to_message.from_user) and (not message.forward_from or not message.forward_from_chat):
        info = user(message.reply_to_message.from_user)
    else:
        return
    try:
        await message.edit(info)
    except Exception as error:
        await message.edit(error)
