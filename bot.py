import discord
from discord.ext import commands

from config import COMMAND_PREFIX, INTENTS


class DiscordBot(commands.Bot):
    def __init__(self, token: str):
        intents = discord.Intents.default() if INTENTS == "default" else discord.Intents.all()
        super().__init__(command_prefix=COMMAND_PREFIX, intents=intents)
        self._token = token

    def startup(self):
        super().run(self._token, reconnect=True)
