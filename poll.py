import os
import asyncio
from datetime import datetime, timedelta
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

async def main():
    today = datetime.now()
    
    # ТЕСТОВЫЙ РЕЖИМ: отправляем сейчас
    target_day = "Пт"
    target_date = today + timedelta(days=2)  # через 2 дня для примера
    
    line1 = "ЖК столичный площадка"
    line2 = f"Треня {target_day} {target_date.strftime('%d.%m')} 6:30-8:00"
    
    # Объединяем с переносом строки
    question = f"{line1}\n{line2}"
    
    print(f"Отправляю опрос:\n{question}")
    
    bot = Bot(token=BOT_TOKEN)
    await bot.send_poll(chat_id=CHAT_ID, question=question,
                        options=["Буду", "Еще думаю", "Не буду"], is_anonymous=False)
    print("Опрос отправлен!")

asyncio.run(main())
