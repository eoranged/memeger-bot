import aiogram
from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message
from pyrogram import Client, filters

from . import config

app = Client(
    "app",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    app_version=config.CLIENT_VERSION,
)
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

    Bot account should be added to private group/channel and requesting user should be member of this chat.
    """
    # TODO: check if message is from private chat
    if message.chat.type != "private":
        # silently ignore all messages in group chats
        return
    text = message.text
    if "t.me/c/" not in text:
        await message.reply("This is not a Telegram link!")
        return
    # TODO: download message content via pyrogram app and return it to user
    pass


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


def main():
    # TODO: initialize and store pyrogram session in some external storage (redis?)
    # TODO: connect pyrogram client instance
    # TODO: initialize bot
    # TODO: run both bot and pyrogram app
    pass


if __name__ == "__main__":
    main()
