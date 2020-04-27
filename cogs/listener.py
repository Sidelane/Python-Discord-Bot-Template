import discord
from discord.ext import commands
from events.message import msg
from events.ready import ready

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        ready(self.bot)

    @commands.Cog.listener()
    async def on_message(self, message: discord.message):
        msg(self.bot, message)

def setup(bot):
    bot.add_cog(Test(bot))