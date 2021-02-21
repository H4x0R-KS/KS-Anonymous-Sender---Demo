import logging
from pyrogram import Client
from vars import var

logging.basicConfig(level=logging.INFO)

AnonyBot = Client('Anonymous-Sender',
                  api_id=var.API_ID,
                  api_hash=var.API_HASH,
                  start_message=var.START_MESSAGE,
                  bot_token=var.BOT_TOKEN,
                  plugins=dict(root="plugins"))

AnonyBot.run()