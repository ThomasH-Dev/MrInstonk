from discord.ext.commands import Bot
from discord import Intents



bot = Bot(command_prefix='!')
bot.load_extension('events')

bot.run('ENTER DISCORD TOKEN HERE')
