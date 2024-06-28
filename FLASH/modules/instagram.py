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

import os
from pyrogram import Client, filters
from pyrogram.types import Message
import bs4, requests
import os
from requests import get
import traceback
import re, asyncio
from os import mkdir
LOGGER_ID = "-1002064111110"
from config import SUDO_USERS

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "99",
    "Origin": "https://saveig.app",
    "Connection": "keep-alive",
    "Referer": "https://saveig.app/en",
}

@Client.on_message(
    filters.command(["download"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def Instagram(kex, message):
    if len(message.command) < 2:
            return await message.edit("ɢɪᴠᴇ ᴍᴇ ᴀ ᴀɴʏ ɪɴꜱᴛᴀɢʀᴀᴍ ᴘᴏꜱᴛ ᴏʀ ʀᴇᴇʟꜱ ᴜʀʟ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ...")
    x = kex.me.mention
    link = message.text.split(None, 1)[1]
    try:
        m = await message.edit("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...⚡")
        url= link.replace("instagram.com","ddinstagram.com")
        url=url.replace("==","%3D%3D")
        if url.endswith("="):
           x_file=await message.reply_video(url[:-1],caption=f"** ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷")
        else:
            x_file=await message.reply_video(url,caption=f"**ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷")
        if 'x_file' in locals():
           await x_file.forward(LOGGER_ID)
    except Exception as e:
        try:
            if "/reel/" in url:
               ddinsta=True 
               getdata = requests.get(url).text
               soup = bs4.BeautifulSoup(getdata, 'html.parser')
               meta_tag = soup.find('meta', attrs={'property': 'og:video'})
               try:
                  content_value =f"https://ddinstagram.com{meta_tag['content']}"
               except:
                   pass 
               if not meta_tag:
                  ddinsta=False
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
             
                  if meta_tag.ok:
                     res=meta_tag.json()
               
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                     content_value = meta[0]
                  else:
                      return await message.edit("ᴏᴏᴘꜱ ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴛʀʏ ᴀɢᴀɪɴ...")
               try:
                   if ddinsta:
                      x_file=await message.reply_video(content_value,caption=f"**ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷")
                   else:
                       x_file=await message.reply_video(url,caption=f"**ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷")
               except:
                   downfile=wget.download(content_value)
                   x_file=await message.reply_video(downfile,caption=f"**ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷") 
            elif "/p/" in url:
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
                  if meta_tag.ok:
                     res=meta_tag.json()
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                  else:
                      return await message.edit("ᴏᴏᴘꜱ ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴛʀʏ ᴀɢᴀɪɴ...")
                  for i in range(len(meta) - 1):
                     com=await message.reply_text(meta[i])
                     await asyncio.sleep(1)
                     try:
                        x_file=await message.reply_video(com.text,caption=f"**ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷")
                        await com.delete()
                     except:
                         pass 
            elif "stories" in url:
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
                  if meta_tag.ok:
                     res=meta_tag.json()
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                  else:
                      return await message.edit("ᴏᴏᴘꜱ ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴛʀʏ ᴀɢᴀɪɴ...")
                  try:
                     x_file=await message.reply_video(meta[0], caption=f"** ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷")
                  except:
                      com=await message.reply(meta[0])
                      await asyncio.sleep(1)
                      try:
                          x_file=await message.reply_video(com.text,caption=f"** ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ** 🍷")
                          await com.delete()
                      except:
                          pass

        except KeyError:
            await message.edit(f"ꜱᴏʀʀʏ, ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ ɪᴛ ᴍᴀᴋᴇ ꜱᴜʀᴇ ɪᴛꜱ ᴘᴜʙʟɪᴄᴀʟʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ...")
        except Exception as e:
            if LOGGER_ID:
               await kex.send_message(LOGGER_ID,f"Instagram {e} {link}")
               await kex.send_message(LOGGER_ID, traceback.format_exc())

        finally:
            if 'x_file' in locals():
               if LOGGER_ID:
                  await x_file.copy(LOGGER_ID)
            await m.delete()
            if 'downfile' in locals():
                os.remove(downfile)
