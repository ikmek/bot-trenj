import os
import asyncio
from datetime import datetime, timedelta
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

async def main():
    today = datetime.now()
    weekday = today.weekday()
    
    if weekday == 0:  # Понедельник → Среда
        target_day = "Ср"
        target_date = today + timedelta(days=2)
    elif weekday == 2:  # Среда → Пятница
        target_day = "Пт"
        target_date = today + timedelta(days=2)
    elif weekday == 4:  # Пятница → Понедельник
        target_day = "Пн"
        target_date = today + timedelta(days=3)
    else:
        print("Сегодня не день отправки (нужны: Пн, Ср, Пт)")
        return
    
    line1 = "ЖК столичный площадка"
    line2 = f"Треня {target_day} {target_date.strftime('%d.%m')} 6:30-8:00"
    question = f"{line1}\n{line2}"
    
    bot = Bot(token=BOT_TOKEN)
    await bot.send_poll(chat_id=CHAT_ID, question=question,
                        options=["Буду", "Еще думаю", "Не буду"], is_anonymous=False)
    print("Опрос отправлен!")

asyncio.run(main())
