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

from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from STORMDB.data import STORMS, TRUTH
from config import OWNER_ID, SUDO_USERS

@Client.on_message(
    filters.command(["truth"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def truth(x: Client, e: Message):
      kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(kex) == 2:
          ok = await x.get_users(kex[1])
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(TRUTH)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(TRUTH)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text(".ᴛʀᴜᴛʜ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  
