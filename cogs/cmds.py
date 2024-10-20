from discord.ext import commands

from commands.cmd_ping import cmd_ping


class Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await cmd_ping(ctx)

async def setup(bot):
    await bot.add_cog(Cmds(bot))
