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

FUN_TEXT = f"""
**ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}lover` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}earth` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}stupid` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}football` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}luck` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}sex` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}chance` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}kiss` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}dare` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}truth` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}hack` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}hate` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}haters` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}lovestory` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}legend` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}emoji` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>

• `{hl}trumptwt` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}tweet` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}waifu` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....
"""

@Client.on_message(
    filters.command(["helpfun"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def help(x: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await x.send_photo(msg.chat.id, HELP_PIC, caption=FUN_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await x.send_video(msg.chat.   id, HELP_PIC, caption=FUN_TEXT) 
