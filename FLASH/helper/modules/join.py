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

from config import SUDO_USERS
from STORMDB.data import GROUP
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(["join"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def join(client: Client, message: Message):
    kex = message.text.split(" ")
    if len(kex) == 1:
        return await message.reply_text("ɴᴇᴇᴅ ᴀ ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ-ɪᴅ ᴏʀ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴛᴏ ᴊᴏɪɴ")
    try:
        await client.join_chat(kex[1])
        await message.reply_text(f"ᴊᴏɪɴᴇᴅ ✅")
    except Exception as ex:
        await message.reply_text(f"ᴇʀʀᴏʀ\n\n{str(ex)}")
  

@Client.on_message(
    filters.command(["leave"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def leave(xspam: Client, message: Message):
    kex = message.text.split(" ")
    if len(kex) > 1:
        if kex[1] in GROUP:
            return
        try:
           await xspam.leave_chat(kex[1])
           await message.reply_text(f"ʟᴇꜰᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🥀")
        except Exception as ex:
           await message.reply_text(f"ᴇʀʀᴏʀ\n\n{str(ex)}")
    else:
        chat = message.chat.id
        ok = message.from_user.id
        if chat == ok:
            return await message.reply_text(f"!ʟᴇᴀᴠᴇ <ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ>")
        elif chat in GROUP:
              return
        try:
           await xspam.leave_chat(chat)
           await message.reply_text(f"ʟᴇꜰᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🥀")
        except Exception as ex:
           await message.reply_text(f"ᴇʀʀᴏʀ\n\n{str(ex)}")
