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

FACTION_TEXT = f"""
**ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}ftyping` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴛʏᴘɪɴɢ....

• `{hl}fvideo` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴠɪᴅ....

• `{hl}faudio` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴀᴜᴅ......

• `{hl}fround` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ʀᴏᴜɴᴅ.....

• `{hl}fphoto` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴘɪᴄ....

• `{hl}fsticker` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ꜱᴛɪᴄ...

• `{hl}fdocument` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴅᴏᴄ..

• `{hl}flocation` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ʟᴏᴄ...

• `{hl}fgame` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ᴘʟᴀʏɪɴɢ ɢᴀᴍᴇ...

• `{hl}fcontact` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴄᴏɴᴛᴀᴄᴛ..

• `{hl}fscreen` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ...

• `{hl}fstop` ᴛᴏ ꜱᴛᴏᴘ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ...
"""

@Client.on_message(
    filters.command(["helpfaction"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def help(x: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await x.send_photo(msg.chat.id, HELP_PIC, caption=FACTION_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await x.send_video(msg.chat.   id, HELP_PIC, caption=FACTION_TEXT) 