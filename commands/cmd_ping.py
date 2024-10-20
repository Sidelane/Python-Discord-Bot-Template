from discord.ext.commands import Context


async def cmd_ping(ctx: Context):
    await ctx.send("pong")