import asyncio

from os import listdir

from bot import DiscordBot
from config import TOKEN


Bot = DiscordBot(TOKEN)


async def load_extensions():
    for filename in listdir('./cogs'):
        if filename.endswith('.py'):
            await Bot.load_extension(f'cogs.{filename[:-3]}')


def main():
    asyncio.run(load_extensions())
    Bot.startup()


if __name__ == '__main__':
    main()
