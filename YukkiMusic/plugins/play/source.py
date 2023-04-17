import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس سيمو","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/GJK_E/333",
        caption=f"""**╭── • [⌯𝗦𝗨𝗢𝗥𝗖𝗘:𝗘𝗟𝗡𝗚𝗢𝗢𝗠⌯](https://t.me/SOURCE_ELNGOM) • ──╮**

**[⌯𝗗𝗘𝗩: Iyad](https://t.me/GJQKP)**

**[⌯𝗦𝗨𝗣𝗣𝗨𝗥𝗧: Iyad](https://t.me/vvinl)**

**[⌯𝗖𝗛𝗔𝗡𝗡𝗘𝗟: Iyad](https://t.me/gjk_e)**

**[⌯𝗠𝗔𝗞𝗘𝗥: Iyad](https://t.me/san3_ibot)**

**╰── • [⌯𝗦𝗨𝗢𝗥𝗖𝗘:Iyad](https://t.me/vvinl) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "صانع ميوزك مجانا ◍", url=f"https://t.me/san3_ibot"), 
                ],[
                    InlineKeyboardButton(
                        "𝗗𝗘𝗩 iyad ◍", url=f"https://t.me/gjqkp"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك ◍", url=f"https://t.me/ms1tbot?startgroup=true"),
                ],

            ]

        ),

    )
    
    