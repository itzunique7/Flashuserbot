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

from datetime import datetime
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(
    filters.command(["mystats", "mystatus"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def stats(client: Client, message: Message):
    bunny = await message.edit("ᴄᴏʟʟᴇᴄᴛɪɴɢ ꜱᴛᴀᴛꜱ...⚡")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await bunny.edit_text(
        """
**ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ꜱᴛᴀᴛꜱ ʙʏ ꜱᴛᴏʀᴍ**

**• `{}` ᴘʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇs**

**• `{}` ɢʀᴏᴜᴘs**

**• `{}` sᴜᴘᴇʀ ɢʀᴏᴜᴘs**

**• `{}` ᴄʜᴀɴɴᴇʟs**

**• `{}` ᴄʜᴀᴛs ᴜʀ ᴀᴅᴍɪɴ ɪɴ**

**• `{}` ʙᴏᴛs**""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )
