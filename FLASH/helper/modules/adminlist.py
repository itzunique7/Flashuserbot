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
from config import SUDO_USERS

@Client.on_message(
    filters.command(["admins", "adminlist", "staff"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def allstaff(client, message):
    creator = None
    admins = []
    bots = []
    deleted = []
    ok = await message.edit("ꜰᴇᴛᴄʜɪɴɢ ᴀᴅᴍɪɴꜱ...")
    async for x in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if x.user.is_bot:
            bots.append(x.user.mention)
        elif x.status.name == "OWNER":
            creator = x.user.mention
        elif x.user.is_deleted:
            deleted.append(x.user.mention)
        else:
            admins.append(x.user.mention)

    txt = f"**{message.chat.title} ꜱᴛᴀꜰꜰ :**"
    txt += "\n\n"
    txt += " 👑**ᴄʀᴇᴀᴛᴏʀ :**"
    txt += "\n"
    txt += f" • {creator}"
    txt += "\n"
    if admins:
        txt += "\n"
        txt += " 👨‍💻**ᴀᴅᴍɪɴꜱ :**"
        txt += "\n"
        for adm in admins:
            txt += f" • {adm}"
            txt += "\n"
    if bots:
        txt += "\n"
        txt += " 🤖**ʙᴏᴛꜱ :**"
        txt += "\n"
        for adm in bots:
            txt += f" • {adm}"
            txt += "\n"
    if deleted:
        txt += "\n"
        txt += " 👻**ᴀᴅᴍɪɴꜱ :**"
        txt += "\n"
        for adm in deleted:
            txt += f" • **None**"
            txt += "\n"
    try:
        await ok.edit(txt)
    except:
        await message.reply(txt)
