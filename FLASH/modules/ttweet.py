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

from pyrogram.types import Message
import requests
from STORM.powers import get_text
from pyrogram import Client, filters
from config import SUDO_USERS
hl = "."

@Client.on_message(
    filters.command(["trumptwt"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ttweet(client: Client, message: Message):
    text = get_text(message)
    if not text:
        await message.edit(f"ɢɪᴠᴇ ᴍᴇ sᴏᴍᴛʜɪɴɢ ᴛᴏ ᴛᴡᴇᴇᴛ....")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    await message.edit(f"ᴛʀᴜᴍᴘ ɪs ᴛᴡᴇᴇᴛɪɴɢ....⚡")
    await client.send_photo(message.chat.id, tweet)
    await message.delete()
