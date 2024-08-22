#devggn


import asyncio
import logging
from pyromod import listen
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from telethon.sync import TelegramClient
from pyrogram import Client as tgClient, enums, utils as pyroutils



# Create a new event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Configure logging
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

sex = TelegramClient('sexrepo', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Initialize Pyrogram Client
app = Client(
    ":RestrictBot:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=10,
    sleep_threshold=20
)

async def restrict_bot():
    # Start the client
    await app.start()

    # Retrieve bot details
    bot_details = await app.get_me()
    bot_id = bot_details.id
    bot_username = bot_details.username
    bot_name = bot_details.first_name
    if bot_details.last_name:
        bot_name += " " + bot_details.last_name

    logging.info(f"Bot {bot_username} (ID: {bot_id}) initialized as {bot_name}")

# Run the bot setup
loop.run_until_complete(restrict_bot())
