import asyncio
from datetime import datetime, timedelta
from telegram import Bot

BOT_TOKEN = "8656512383:AAGU6u6D1YyeKu--YFOJ0tsTKL36YbDuKR8"
CHAT_ID = "-5017877523"

async def main():
    today = datetime.now()
    weekday = today.weekday()

    if weekday == 6:
        target_day = "Пн"
        target_date = today + timedelta(days=1)
    elif weekday == 1:
        target_day = "Ср"
        target_date = today + timedelta(days=1)
    elif weekday == 3:
        target_day = "Пт"
        target_date = today + timedelta(days=1)
    else:
        print("Сегодня не день отправки")
        return

    question = f"Треня {target_day} {target_date.strftime('%d.%m')} 6:30-8:00"
    bot = Bot(token=BOT_TOKEN)
    await bot.send_poll(chat_id=CHAT_ID, question=question,
                        options=["Буду", "Еще думаю", "Не буду"], is_anonymous=False)
    print("Опрос отправлен!")

asyncio.run(main())
