from typing import List
from discord import Embed, version_info, __version__
from discord.ext.commands import Cog
from discord.ext.commands import bot
from discord.ext import tasks

from commandhandler import Handler
import scraper

class Listeners(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('Logged on as {}!'.format(self.bot.user.name))
        self.stock.start()

    @Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        if not message.content.startswith("@"):
            return

        await Handler.content(self, message)
    
    @tasks.loop(seconds=10)
    async def stock(self):
        if not scraper.ps5Availability():
            channel = self.bot.get_channel(826572317844176913)
            await channel.send('ps5')
        if not scraper.ps5DigitalAvailability():
            channel = self.bot.get_channel(826572317844176913)
            await channel.send('ps5')
        if not scraper.xboxAvailability():
            channel = self.bot.get_channel(832077275059060747)
            await channel.send('xbox')

def setup(bot):
    bot.add_cog(Listeners(bot))
