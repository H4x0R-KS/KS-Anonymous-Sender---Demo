from pyrogram import (
    Client,
    filters
    )

MESSAGE = """
Hey, You want to use me In Group ?\nTell this thing
to @King_Sahan !!\nCurrently Leaving 👋
"""


@Client.on_message(filters.group)
async def leave(client, message):
    await message.reply_text(MESSAGE)