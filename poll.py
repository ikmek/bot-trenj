import os
import asyncio
from datetime import datetime, timedelta
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

async def main():
    today = datetime.now()
    
    # ТЕСТОВЫЙ РЕЖИМ: отправляем опрос прямо сейчас без проверки дня
    target_day = "Ср"  # тест
    target_date = today
    
    question = f"Треня {target_day} {target_date.strftime('%d.%m')} 6:30-8:00 (ТЕСТ)"
    bot = Bot(token=BOT_TOKEN)
    await bot.send_poll(chat_id=CHAT_ID, question=question,
                        options=["Буду", "Еще думаю", "Не буду"], is_anonymous=False)
    print("Опрос отправлен!")

asyncio.run(main())
