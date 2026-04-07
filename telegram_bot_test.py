# testing the telegram bot by sending a message to the specified chat ID.
# Make sure to replace BOT_TOKEN and CHAT_ID with your actual bot token and
# chat ID before running this code.

from telegram import Bot # type: ignore
import asyncio

BOT_TOKEN = "8548472739:AAGU39od72gMvno2jGVrq5bKaZe6rexWHaY"
CHAT_ID = "1066562563"

async def test():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID,
                           text="✅ Telegram bot working!")

asyncio.run(test())