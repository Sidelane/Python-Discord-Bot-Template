import discord
from discord.ext import commands

from events.ready import ready
from events.message import msg

class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        ready(self.bot)

    @commands.Cog.listener()
    async def on_message(self, message: discord.message):
        msg(self.bot, message)

async def setup(bot):
    await bot.add_cog(Test(bot))
