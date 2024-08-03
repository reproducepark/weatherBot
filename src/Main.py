import logging, os
import asyncio, telegram, time, pytz
from datetime import datetime, timedelta
from dotenv import load_dotenv
from getWeather import makeMsg

load_dotenv()
botToken = os.environ.get('token')
chatId = os.environ.get('main_chat_id')

async def send_message(bot):
    await bot.send_message(chatId,makeMsg())

async def main():
    print("starting service...")

    timeZone = pytz.timezone('Asia/Seoul')

    now = datetime.now(timeZone)
    target = now.replace(hour=6, minute=0, second=0, microsecond=0)
    
    if now >= target:
        target += timedelta(days=1)
    timeRemaining = target - now
    secondsRemaining = timeRemaining.total_seconds()

    bot = telegram.Bot(token = botToken)
    await send_message(bot)
    
    time.sleep(secondsRemaining)
    while True:
        await send_message(bot)
        time.sleep(86400)

if __name__ == "__main__":
    asyncio.run(main())


