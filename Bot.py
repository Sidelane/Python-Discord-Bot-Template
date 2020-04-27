from discord.ext import commands
import discord

class AzubiBot(commands.Bot):

    def __init__(self, Token: str):
        super().__init__(command_prefix="!")
        self.TOKEN = Token

    def startup(self):
        super().run(self.TOKEN, bot=True, reconnect=True)
