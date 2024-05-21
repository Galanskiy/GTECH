import asyncio
from telegram import Bot
from asgiref.sync import async_to_sync
from django.conf import settings

# Chat ID getiing func
# async def get_chat_id():
#     bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
#     updates = await bot.get_updates()
#     if updates:
#         chat_id = updates[-1].message.chat.id
#         print("Chat ID:", chat_id)
#     else:
#         print("No messages received yet")
#
# asyncio.run(get_chat_id())

def send_telegram_message(message):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    chat_id = 898453178
    sync_send_message = async_to_sync(bot.send_message)
    sync_send_message(chat_id=chat_id, text=message)
