import discord
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await channel.send(file=discord.File('my_file.png'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODE0NjI3MzUyNDIzMzAxMTMx.YDgm1w.4V241uSspBjY9VsKzXLGyPhznB4')
