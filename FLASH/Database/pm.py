#MIT License

#Copyright (c) 2024 ᴅʜɪʀᴀᴊ [AFK]

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

pm_data = {"pm": 0}
pmwarn_data = {"w": "w", "warns": 10}
pmap_data = []
warner_data = {}

async def toggle_pm():
    global pm_data
    if pm_data:
        pm_data = {}
    else:
        pm_data = {"pm": 0}

async def is_pm_on():
    global pm_data
    return bool(pm_data)

async def update_warns(w: int):
    global pmwarn_data
    pmwarn_data["warns"] = w

async def limit():
    global pmwarn_data
    return pmwarn_data.get("warns", 0)

async def approve(user_id: int):
    global pmap_data
    if user_id not in pmap_data:
        pmap_data.append(user_id)

async def disapprove(user_id: int):
    global pmap_data
    if user_id in pmap_data:
        pmap_data.remove(user_id)

async def is_approved(user_id: int):
    global pmap_data
    return user_id in pmap_data

async def list_approved():
    global pmap_data
    return pmap_data

async def add_warn(user_id: int):
    global warner_data
    warner_data[user_id] = warner_data.get(user_id, 0) + 1

async def reset_warns(user_id: int):
    global warner_data
    warner_data[user_id] = 0

async def get_warns(user_id: int):
    global warner_data
    return warner_data.get(user_id, 0)
