from os import listdir
from bot import AzubiBot
from config import TOKEN

Bot = AzubiBot(TOKEN)

for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        Bot.load_extension(f'cogs.{filename[:-3]}')

try:
    Bot.startup()
except Exception:
    print("Exception while starting the Bot")
