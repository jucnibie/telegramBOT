# Telegram BOt
import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from utils.images import get_image, get_image_nsfw, get_some_image_nsfw
from utils.videos import get_vid_url
from utils.configs import NSFW_CATEGORIES, IMAGE_CATEGORIES, API_TOKEN

# variables
_commands = [val for val in IMAGE_CATEGORIES.keys()]
nsfw_commands = [val for val in NSFW_CATEGORIES.keys()]

help_messages = """
HELP
/roses - get roses blackpink images
/mlem - get sexy girl images
/meme - get meme images
/beauty - get beautiful girl image
Have fun!
"""


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


"""
Start
"""
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI'm Naught Sperm!\nPowered by aiogram.")


"""
Helps
"""
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply(help_messages)


"""
Image categories
"""
@dp.message_handler(commands=_commands)
async def send_image(message: types.Message):
    """
    This handler will be called when user sends images command
    """
    try:
        category = message.get_command()[1:]
        image_url = get_image(category)
        print(f"User get {image_url}")
        caption = f"{category.capitalize()} are here 😺"
        await message.reply_photo(image_url, caption)
    except:
        await message.reply("Something went wrong 😭")


"""
TEST
"""
@dp.message_handler(commands=['test'])
async def send_test(message: types.Message):
    """
    This handler will be called when user sends images command
    """
    try:
        arguments = message.get_args()
        await message.reply(arguments)
    except:
        await message.reply("Loi con me roi 😭")


"""
NSFW images
"""
@dp.message_handler(commands=nsfw_commands)
async def send_nsfw(message: types.Message):
    """
    This handler will be called when user sends images command
    """
    try:
        category = message.get_command()[1:]
        image_url = get_image_nsfw(category)
        print(f"User get {image_url}")
        caption = f"{category.capitalize()} for you 😈"
        await message.reply_photo(image_url, caption)
    except:
        await message.reply("Something went wrong 😭")


"""
Porn Vietnamese
"""
@dp.message_handler(commands=['vids'])
async def send_porn(message: types.Message):
    """
    This handler will be called when user sends images command
    """
    try:
        print(f"User get videos")
        video_url = get_vid_url()
        caption = f"Porn video for you 😈"
        await message.reply_video(video_url, caption)
    except:
        await message.reply("Something went wrong 😭")

"""
Echo
"""
@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    if text[0] == '/':
        await message.answer('Command not found 😭')
    else:
        await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
