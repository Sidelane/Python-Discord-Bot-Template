from discord.ext.commands import Bot


def ready(bot: Bot):
    print(f"{bot.user} has Connected")