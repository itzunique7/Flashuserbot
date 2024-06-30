
#MIT License

#Copyright (c) 2024 DHIRAJ [AFK]

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

• `{hl}cat` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}dino` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}drugs` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}fuck` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}gangster` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}gf` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}heli` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}kill` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}nolove` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}pat` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}run` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}tank` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}thumb` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}wtf` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

"""

@Client.on_message(
    filters.command(["helpfunny"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def help(x: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await x.send_photo(msg.chat.id, HELP_PIC, caption=FUN_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await x.send_video(msg.chat.   id, HELP_PIC, caption=FUN_TEXT) 
