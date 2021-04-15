import discord
import json
from users import MyUsers
from commandhandler import Handler
import scraper
import asyncio
import logging
import threading
import time

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        ##await self.stock()

        x = threading.Thread(target=self.stock, args=())

        x.start()


    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content[0:1] != "@":
            return

        await Handler.content(self, message)

    def stock(self):

        condition = True

        while condition:

            if not scraper.ps5Availability():

                

                print('meme')

            if not scraper.ps5DigitalAvailability():

                

                print('meme')

            if not scraper.xboxAvailability():

                

                print('meme')   

            time.sleep(10)
    
    async def psStock():

        channel = client.get_channel(826572317844176913)
        await channel.send('ps5')

    async def xboxStock():

        channel = client.get_channel(832077275059060747)
        await channel.send('xbox')




client = MyClient()
client.run('ODE0NjI3MzUyNDIzMzAxMTMx.YDgm1w.4V241uSspBjY9VsKzXLGyPhznB4')