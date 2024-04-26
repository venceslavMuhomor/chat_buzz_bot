from aiogram import Bot
from aiogram.types import BufferedInputFile

from config import config

async def send_to_chat(file: bytes, chat_id: int):
    bot = Bot(config.bot_token.get_secret_value())
    input_file = BufferedInputFile(file=file, filename="image.png")
    await bot.send_photo(chat_id, input_file)