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
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from FLASH.helper.basic import edit_or_reply, get_text
import asyncio
hl = "."

@Client.on_message(
    filters.command(["nolove"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def nolove(client: Client, message: Message):
    typew = await edit_or_reply(
        message, "`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 *This is for you`"
    )
    await asyncio.sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  *tap IB OO that one`")
