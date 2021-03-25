import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('@hi'):
            await message.author.send('hello')
        #print('Message from {0.author}: {0.content}'.format(message))
        

client = MyClient()
client.run('ODE0NjI3MzUyNDIzMzAxMTMx.YDgm1w.4V241uSspBjY9VsKzXLGyPhznB4')