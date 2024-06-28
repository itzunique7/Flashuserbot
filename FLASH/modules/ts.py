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

from pyrogram import Client, filters, enums
from gtts import gTTS
from config import SUDO_USERS

def convert(txt):
    tts = gTTS(txt)
    x = "Kex.mp3"
    tts.save(x)
    return x
  
@Client.on_message(
    filters.command(["tts"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def texttospeech(client, message):
    reply = message.reply_to_message
    if not reply:
        if len(message.command) < 2:
            return await message.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ɢɪᴠᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ...")
    
    if reply:
        if not reply.text and not reply.caption:
            return await message.edit("ᴛᴇxᴛ ɴᴏᴛ ꜰᴏᴜɴᴅ... : (")
        txt = reply.text if reply.text else reply.caption
        path = convert(txt)
    else:
        txt = message.text.split(None, 1)[1]
        path = convert(txt)
    try:
        await message.delete()
    except:
        pass
    try:
        await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
        await message.reply_voice(path)
        await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    except:
        await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
        await message.reply_audio(path)
        await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
