from typing import List
from discord import Embed, version_info, __version__
from discord.ext.commands import Cog
from discord.ext.commands import bot
from discord.ext import tasks

from commandhandler import Handler
import scraper
import discord

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
        if message.channel.id != 826575197409771540:
            return
        if not message.content.startswith("@"):
            return

        await Handler.content(self, message)
    
    @tasks.loop(seconds=10)
    async def stock(self):
        if scraper.ps5Availability():
            channel = self.bot.get_channel(826572317844176913)

            embedVar = discord.Embed(title="PS5 IN STOCK!!", description="<@&826577176727781376>", color=0x2559FF)
            embedVar.set_image(url = 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6426/6426149_sd.jpg;maxHeight=640;maxWidth=550')
            embedVar.add_field(name="Link", value="https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149", inline=False)
            

            await channel.send(embed=embedVar)
        if scraper.ps5DigitalAvailability():
            channel = self.bot.get_channel(826572317844176913)
            
            embedVar = discord.Embed(title="PS5 DIGITAL IN STOCK!!", description="<@&826577176727781376>", color=0x2559FF)
            embedVar.set_image(url = 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6430/6430161_sd.jpg;maxHeight=640;maxWidth=550')
            embedVar.add_field(name="Link", value="https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161", inline=False)
            

            await channel.send(embed=embedVar)

        if scraper.xboxAvailability():
            channel = self.bot.get_channel(832077275059060747)
            
            embedVar = discord.Embed(title="XBOX SERIES X IN STOCK!!", description="<@&826577207555391559>", color=0x00CA22)
            embedVar.set_image(url = 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428324cv15d.jpg;maxHeight=640;maxWidth=550')
            embedVar.add_field(name="Link", value="https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324", inline=False)
            

            await channel.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Listeners(bot))
