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

from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

EXTRA_TEXT = f"""
**ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ** 

• `{hl}ping` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ ᴀɴᴅ ᴜᴘᴛɪᴍᴇ....

• `{hl}restart` » ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ....

• `{hl}instantboot` » ɢɪᴠᴇ ᴀ ɪɴꜱᴛᴀɴᴛ/ᴄʜᴀʀɢᴇ ʙᴏᴏᴛ ᴛᴏ ʏᴏᴜʀ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ....

• `{hl}alive` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ...

• `{hl}repo` » ᴛᴏ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ...

• `{hl}id` » ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ'ꜱ ᴜꜱᴇʀ_ɪᴅ....

• `{hl}addsudo` » ᴛᴏ ᴀᴅᴅ ꜱᴜᴅᴏ....

• `{hl}sudolist` » ᴛᴏ ɢᴇᴛ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ʟɪꜱᴛ....

• `{hl}hping` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ'ꜱ ɴᴏɴ ʙᴏᴏꜱᴛᴇᴅ ᴘɪɴɢ ᴀɴᴅ ᴜᴘᴛɪᴍᴇ....

• `{hl}eval` » ᴛᴏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜᴇ ꜰᴜɴᴄᴛɪᴏɴ ᴏꜰ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ....

• `{hl}mystats` » ᴛᴏ ᴄʜᴋ ᴄʟɪᴇɴᴛ ꜱᴛᴀᴛꜱ....

• `{hl}bstats` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛꜱ....

• `{hl}join` » ᴛᴏ ᴊᴏɪɴ ᴄʜᴀᴛ....

• `{hl}leave` » ᴛᴏ ʟᴇᴀᴠᴇ ᴄʜᴀᴛ...
"""

@Client.on_message(
    filters.command(["helpbot"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def help(x: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await x.send_photo(msg.chat.id, HELP_PIC, caption=EXTRA_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await x.send_video(msg.chat.   id, HELP_PIC, caption=EXTRA_TEXT)
