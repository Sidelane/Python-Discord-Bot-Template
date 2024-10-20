from discord.ext import commands

from commands.cmd_ping import cmd_ping


class Cmds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await cmd_ping(ctx)

async def setup(bot: commands.Bot):
    await bot.add_cog(Cmds(bot))
