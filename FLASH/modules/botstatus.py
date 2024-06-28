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
    ** ғʟᴀsʜ ᴜꜱᴇʀʙᴏᴛ **

    • **ᴅᴇᴠᴇʟᴏᴘᴇʀ** » **[ᴅʜɪʀᴀᴊ](https://t.me/II_DHIRAJ_II)**
    • **ᴠᴇʀꜱɪᴏɴ** » **2.1.1**
    • **ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇꜱ** » **107+**
    • **ᴛᴏᴛᴀʟ ᴄᴏᴍᴍᴀɴᴅꜱ** » **134+**  
    • **ʙʀᴀɴᴄʜ** » **2.1.1@main**
    • **ᴜꜱᴇʀʙᴏᴛ ʀᴇᴘᴏ** » **[ғʟᴀsʜ-ᴜꜱᴇʀʙᴏᴛ](https://github.com/itzunique7/FLASHUSERBOT)**
    • **ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** » **[ғʟᴀsʜ ᴄʜᴀᴛᴢ](https://t.me/FLASH_CHATZ)**
    • **ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ** » **[ғʟᴀsʜ ᴛᴇᴄʜ](https://t.me/FLASH_TECHH)**    
    
    **ʙʏ @II_DHIRAJ_II**
    """
    await message.reply(msg)
