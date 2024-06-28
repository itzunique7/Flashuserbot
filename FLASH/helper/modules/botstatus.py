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
from config import SUDO_USERS

@Client.on_message(
    filters.command(["bstats"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def bstats(client, message):
    msg = f"""
    ** ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ **

    • **ᴅᴇᴠᴇʟᴏᴘᴇʀ** » **[Kᴜɴᴀʟ࿐](https://t.me/kexx_xd)**
    • **ᴠᴇʀꜱɪᴏɴ** » **2.1.1**
    • **ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇꜱ** » **107+**
    • **ᴛᴏᴛᴀʟ ᴄᴏᴍᴍᴀɴᴅꜱ** » **134+**  
    • **ʙʀᴀɴᴄʜ** » **2.1.1@main**
    • **ᴜꜱᴇʀʙᴏᴛ ʀᴇᴘᴏ** » **[ꜱᴛᴏʀᴍ-ᴜꜱᴇʀʙᴏᴛ](https://github.com/VARC9210/STORM-USERBOT)**
    • **ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** » **[ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ](https://t.me/STORM_CHATZ)**
    • **ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ** » **[ꜱᴛᴏʀᴍ ᴛᴇᴄʜ](https://t.me/STORM_TECHH)**    
    
    **ʙʏ @kexx_xd**
    """
    await message.reply(msg)
