from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **KS ANONYMOUS SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!
Credits: Sahan Sachintha
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("❤️ Support Group ❤️",
                          url="t.me/KingSahan380Group")],
    [InlineKeyboardButton("🧑‍💻 Dev 🧑‍💻",
                          url="t.me/King_Sahan")]])
    [InlineKeyboardButton("🧑‍💻 KS bot 🧑‍💻",
                          url="t.me/KingSahanBot")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)