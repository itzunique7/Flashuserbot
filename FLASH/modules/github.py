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

import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(
    filters.command(["gitinfo"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def githubuser(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply_text(f". ɢɪᴛɪɴꜰᴏ [ᴜꜱᴇʀɴᴀᴍᴇ]")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("ᴇʀʀᴏʀ: ᴜsᴇʀɴᴀᴍᴇ ɴᴏᴛ ғᴏᴜɴᴅ....")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**• ɪɴꜰᴏ {name}**
**• ᴜsᴇʀɴᴀᴍᴇ:** `{username}`
**• ʙɪᴏ:** `{bio}`
**• ᴘʀᴏғɪʟᴇ ʟɪɴᴋ:** [Here]({url})
**• ᴄᴏᴍᴘᴀɴʏ:** `{company}`
**• ᴄʀᴇᴀᴛᴇᴅ ᴏɴ:** `{created_at}`
**• ʀᴇᴘᴏsɪᴛᴏʀɪᴇs:** `{repositories}`
**• ʙʟᴏɢ:** `{blog}`
**• ʟᴏᴄᴀᴛɪᴏɴ:** `{location}`
**• ғᴏʟʟᴏᴡᴇʀs:** `{followers}`
**• ғᴏʟʟᴏᴡɪɴɢ:** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
