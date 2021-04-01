import discord
import json
from users import MyUsers
from commandhandler import Handler

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content[0:1] != "@":
            return

        await Handler.content(self, message)

        #print(message.channel.id == 826572317844176913)

        #if message.channel.id != 826572317844176913:
         #   return
        
        #if message.content.startswith('@add PS5'):

            #MyUsers.adduser(message)

            #role = discord.utils.get(message.guild.roles, name = "PS5")

            #await message.author.add_roles(role)

            #await message.author.send('DM')
            #print('Message from {0.author}: {0.content}'.format(message))


        

client = MyClient()
client.run('ODE0NjI3MzUyNDIzMzAxMTMx.YDgm1w.4V241uSspBjY9VsKzXLGyPhznB4')

