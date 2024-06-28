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

from pyrogram import filters, Client
from pyrogram.types import Message

from STORMDB.data import RAID, STORMS
from config import SUDO_USERS


@Client.on_message(
    filters.command(["dmraid"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def dmraid(x: Client, message: Message):
      kex = message.text.split(" ")

      if len(kex) == 3:
          ok = await x.get_users(kex[2])
          id = ok.id

          if id in STORMS:
                await message.reply_text(f"ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
          elif id in SUDO_USERS:
                await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
          else:
              counts = int(kex[1])
              await message.reply_text("ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await x.send_message(id, msg)
                    await asyncio.sleep(0.1)

      elif message.reply_to_message and (len(kex) == 2):
          user_id = message.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          id = ok.id

          if id in STORMS:
                await message.reply_text(f"ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
          elif id in SUDO_USERS:
                await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
          else:
              counts = int(kex[1])
              await message.reply_text("ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await x.send_message(id, msg)
                    await asyncio.sleep(0.1)

      else:
            await message.reply_text(".ᴅᴍʀᴀɪᴅ 13 <ᴜꜱᴇʀ ɪᴅ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")


@Client.on_message(
    filters.command(["dmspam"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def dmspam(client: Client, message: Message):
    kex = message.text.split(" ", 3)

    if  len(kex) == 4:
        uid = int(kex[2])
        if uid in STORMS:
            await message.reply_text(f"ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
        elif uid in SUDO_USERS:
            await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
        else:
            quantity, spam_text = int(kex[1]), kex[3]
            await message.reply_text("ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(kex) == 3):
        id = message.reply_to_message.from_user.id

        if id in STORMS:
            await message.reply_text(f"ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
        elif id in SUDO_USERS:
            await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
        else:
            quantity = int(kex[1])
            spam_text = kex[2]
            await message.reply_text("ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text(".ᴅᴍꜱᴘᴀᴍ 13 <ᴜꜱᴇʀ ɪᴅ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ> ꜱᴛᴏʀᴍ")
