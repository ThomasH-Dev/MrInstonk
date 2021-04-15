import discord

class Handler():

    @staticmethod
    async def content(self, message):

        splitMsg = message.content[1:].lower().split()

        role = None

        if(splitMsg[0].lower() == "add"):

            if(splitMsg[1].lower() == "ps5"):

                role = discord.utils.get(message.guild.roles, name = "PS5")
            
            elif(splitMsg[1].lower() == "xbox"):

                role = discord.utils.get(message.guild.roles, name = "Xbox Series X")

            await message.author.add_roles(role)

        elif(splitMsg[0].lower() == "test"):

            print("test")
