import discord
import logging
import sys
from discord.ext import commands
from .cogs import music, error, time, tips
# from .cogs import music, error, meta, tips
from . import config

cfg = config.load_config()

bot = commands.Bot(command_prefix=cfg["prefix"])


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")


COGS = [time.Time, music.Music, error.CommandErrorHandler,  tips.Tips]
# COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]

def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    if cfg["token"] == "":
        raise ValueError(
            "Токен не был предоставлен. Убедитесь, что config.toml содержит токен бота."
        )
        sys.exit(1)
    bot.run(cfg["token"])
