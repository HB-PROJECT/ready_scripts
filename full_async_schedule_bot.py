from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message,CallbackQuery
import asyncio
import time
import aioschedule as schedule
import logging

bot = Bot('1251528088:AAECXGaHJx7J7PsDPKsot5rpWlThNN-hpuw')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['start'])
async def start(message : Message):
    print(message.text)
    await bot.send_message(message.chat.id, 'hello_0')
    await asyncio.sleep(120)
    await bot.send_message(message.chat.id, 'hello_120')
    await asyncio.sleep(180)
    await bot.send_message(message.chat.id, 'hello_300')
    await asyncio.sleep(240)
    await bot.send_message(message.chat.id, 'hello_540')


async def job():
    print('hello')
    await bot.send_message(626420006, 'job done!')
    

async def scheduler():
    
    # schedule.every(1).seconds.do(job)

    # loop = asyncio.get_event_loop()
    while True:
        await schedule.run_pending()
        await asyncio.sleep(2)



if __name__ == "__main__":
    # dp.loop.create_task(scheduler())
    executor.start_polling(dp,skip_updates=True)
    