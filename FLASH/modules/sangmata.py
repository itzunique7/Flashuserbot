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
from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *
from STORM.modules.profile import extract_user
from config import SUDO_USERS

@Client.on_message(
    filters.command(["sg", "sa", "sangmata"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.edit_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀ.......")
    bot = "SangMata_BOT"
    try:
        await client.send_message(bot, f"allhistory {user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"allhistory {user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=1):
        if not stalk:
            await message.edit_text("**ᴛʜɪꜱ ᴘᴇʀꜱᴏɴ ʜᴀꜱ ɴᴇᴠᴇʀ ᴄʜᴀɴɢᴇᴅ ʜɪꜱ ɴᴀᴍᴇ**")
            return
        elif stalk:
            await message.edit(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()
