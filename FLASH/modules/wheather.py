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

from pyrogram import Client, filters
import requests
from config import SUDO_USERS

WEATHER_API = "fadd97c7821d568d82f1cceaa06c7def"
api_key = WEATHER_API

@Client.on_message(
    filters.command(["weather"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def get_weather_info(client, message):
    location = message.text.split(' ', 1)
    if len(location) > 1:
        city = location[1]
        weather_info = fetch_weather_info(city)
        await message.edit(weather_info)
    else:
        await message.edit("ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ᴛʜᴇ ᴄɪᴛʏ ꜰᴏʀ ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ...")

def fetch_weather_info(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_info = f"ᴡᴇᴀᴛʜᴇʀ ɪɴ {city}\n\n {description}, \n\n• ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ: {temperature}°C, \n\n• ʜᴜᴍɪᴅɪᴛʏ: {humidity}%, \n\n• ᴡɪɴᴅ ꜱᴘᴇᴇᴅ: {wind_speed} m/s"
            return weather_info
        else:
            return "ꜰᴀɪʟᴇᴅ ᴛᴏ ꜰᴇᴛᴄʜ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰᴏʀ ᴛʜᴇ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴄɪᴛʏ"
    except Exception as e:
        return "ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ꜰᴇᴛᴄʜɪɴɢ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ"
