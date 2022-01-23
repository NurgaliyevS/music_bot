from discord.ext import commands
import discord
import random


class Tips(commands.Cog):
    """Commands for providing tips about using the bot."""

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config[__name__.split(".")[-1]]
        self.tips = ["Немедленно пропускать песни могут только администраторы и автор запроса песни. Всем остальным придется голосовать!",
                     "clearqueue == cq","leave == stop","nowplaying == np",
                     "pause == p","play == resume","queue == q == playlist", 
                     "volume == vol == v",]

    @commands.command()
    async def tip(self, ctx):
        """Получите случайный совет об использовании бота."""
        index = random.randrange(len(self.tips))
        await ctx.send(f"**Tip #{index+1}:** {self.tips[index]}")
