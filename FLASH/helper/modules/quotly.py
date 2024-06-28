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

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from STORM.powers import get_arg
hl = "."

@Client.on_message(
    filters.command(["q", "quotly"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴍᴇssᴀɢᴇ...**")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("ᴍᴀᴋɪɴɢ ᴀ Qᴜᴏᴛᴇ...")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**ғᴀɪʟᴇᴅ ᴛᴏ ᴍᴀᴋᴇ sᴛɪᴄᴋᴇʀ ǫᴜᴏᴛʟʏ....**")
