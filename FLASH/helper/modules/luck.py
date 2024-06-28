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


import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

@Client.on_message(
    filters.command(["luck"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def luck(client, message):
    if hl + "luck " in message.text:
        text = message.text.split(hl + "luck ", maxsplit=1)[1]
        score = ["👎 \n 1", "👎 \n 2", "💩 \n -1", "💩 \n -5", "💩 \n -10", "🍀 \n 100", "💩 \n -99", "💩 \n -100", "🍀 \n 100", "💩 \n -10000", "💩 \n -50""💩 \n -100", "🍀 \n 100", "💩 \n -99", "💩 \n -98", "💩 \n -97", "💩 \n -96", "🍀 \n 100", "💩 \n -95", "💩 \n -94", "💩 \n -93", "💩 \n -92", "🍀 \n 100", "💩 \n -91", "💩 \n -90", "💩 \n -89", "💩 \n -88", "💩 \n -87", "💩 \n -86", "💩 \n -85", "💩 \n -84", "💩 \n -83", "💩 \n -82", "💩 \n -81", "💩 \n -80", "💩 \n -79", "💩 \n -78", "💩 \n -77", "💩 \n -76", "💩 \n -75", "💩 \n -74", "💩 \n -73", "💩 \n -72", "💩 \n -71", "💩 \n -70", "💩 \n -69", "💩 \n -68", "💩 \n -67", "💩 \n -66", "💩 \n -65", "💩 \n -64", "💩 \n -63", "💩 \n -62", "💩 \n -61", "💩 \n -60", "💩 \n -59", "💩 \n -58", "💩 \n -57", "💩 \n -56", "💩 \n -55", "💩 \n -54", "💩 \n -53", "💩 \n -52", "💩 \n -51", "💩 \n -50", "💩 \n -49", "💩 \n -48", "💩 \n -47", "💩 \n -46", "💩 \n -45", "💩 \n -44", "💩 \n -43", "💩 \n -42", "💩 \n -41", "💩 \n -40", "💩 \n -39", "💩 \n -38", "💩 \n -37", "💩 \n -36", "💩 \n -35", "💩 \n -34", "💩 \n -33", "💩 \n -32", "💩 \n -31", "💩 \n -30", "💩 \n -29", "💩 \n -28", "💩 \n -27", "💩 \n -26", "💩 \n -25", "💩 \n -24", "💩 \n -23", "💩 \n -22", "💩 \n -21", "💩 \n -20", "💩 \n -19", "💩 \n -18", "💩 \n -17", "💩 \n -16", "💩 \n -15", "💩 \n -14", "💩 \n -13", "💩 \n -12", "💩 \n -11", "🍀 \n 100", "💩 \n -10", "💩 \n -9", "💩 \n -8", "💩 \n -7", "💩 \n -6", "💩 \n -5", "🍀 \n 100", "💩 \n -4", "💩 \n -3", "💩 \n -2", "💩 \n -1"]
        luck_score = random.choice(score)
        await message.reply(f"**{text}**\n\n**ʟᴜᴄᴋ**: **{luck_score}** %\n**")
    else:
        await message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ. ᴘʟᴇᴀꜱᴇ ᴜꜱᴇ `.luck` <ʏᴏᴜʀ ɴᴀᴍᴇ>")
