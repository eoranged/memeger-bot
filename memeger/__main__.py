import asyncio

import aiogram
from aiogram import html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from pyrogram import Client, filters

from . import config

dp = aiogram.Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def message_handler(message: Message) -> None:
    """
    Download message content by t.me link.

    Special user should be added to private group/channel and requesting user should be member of this chat.
    """
    if message.chat.type != "private":
        # silently ignore all messages in group chats
        return

    # TODO: check if user is a chat member
    text = message.text
    if "t.me/c/" not in text:
        await message.reply("This is not a Telegram link!")
        return
    # TODO: parse link
    chat_id, message_id = None, None
    # check if chat in whitelist
    if chat_id not in config.WHITELISTED_CHATS:
        return
    # TODO: download message content via pyrogram app and return it to user
    pass


# TODO: register in main
@client.on_message(filters.private)
async def hello(client, message):
    # check if message is from whitelisted chat
    if message.chat.id not in config.WHITELISTED_CHATS:
        return
    # TODO: check if there is content and it is allowed for download (by default always allowed)

    # TODO: download message content via pyrogram app and store it in temporary directory
    # temporary directory should be be mounted in docker
    pass


async def main():

    # TODO: initialize and store pyrogram session (need to mount directory in docker)

    client = Client(
        "app",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        app_version=config.CLIENT_VERSION,
    )
    bot = aiogram.Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    async with client:
        # await client.send_message("me", "Hi!")
        # TODO: register pyrogram handlers
        # TODO: listen for join requests and update chat members list daily via pyrogram

        # looks like start_polling will never return unless interrupted (TODO: test)
        await dp.start_polling(bot)


if __name__ == "__main__":
    # from https://docs.pyrogram.org/start/invoking#using-asyncio-run
    # the Client instance (and possibly other asyncio resources you are going to use)
    # must be instantiated inside the main function
    asyncio.run(main())
