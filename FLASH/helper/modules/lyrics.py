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
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
import lyricsgenius
SUDO_USER = SUDO_USERS
hl = "."
genius = lyricsgenius.Genius("jPnYlXn0YEF4xJLJJJ0V2fngWTmyK4c9scfIxFMpofO4-aKIWJ8t9f_11oCeZCLj")
async def search_lyrics(song_title, artist_name):
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            return song.lyrics
        else:
            return f"ʟʏʀɪᴄꜱ ꜰᴏʀ '{song_title}' ʙʏ {artist_name} ɴᴏᴛ ꜰᴏᴜɴᴅ..."
    except Exception as e:
        return f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {str(e)}"
        
@Client.on_message(
    filters.command(["lyrics"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def handle_lyrics_command(client: Client, message: Message):
    try:
        cmd = message.command
        song_title = cmd[1] if len(cmd) > 1 else ""
        artist_name = cmd[2] if len(cmd) > 2 else ""

        if not song_title:
            await message.edit("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ꜱᴏɴɢ ᴛɪᴛʟᴇ...")
            await asyncio.sleep(2)
            await message.delete()
            return

        if not artist_name:
            await message.edit("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ᴀʀᴛɪꜱᴛ ɴᴀᴍᴇ..")
            await asyncio.sleep(2)
            await message.delete()
            return

        await message.edit(f"ꜰᴇᴛᴄʜɪɴɢ ʟʏʀɪᴄꜱ ꜰᴏʀ '{song_title}' ʙʏ {artist_name}...")
        lyrics = await search_lyrics(song_title, artist_name)
        await message.edit(lyrics)

    except Exception as e:
        await message.edit("ꜰᴀɪʟᴇᴅ ᴛᴏ ꜰᴇᴛᴄʜ ʟʏʀɪᴄꜱ....")
        await asyncio.sleep(2)
        await message.delete()
