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
            else:
              channel = self.bot.get_channel(message.channel.id)
              
              await channel.send("We don't support that product/ you may have spelled it incorrectly")
              
          
            await message.author.add_roles(role)

        elif(splitMsg[0].lower() == "test"):

            channel = self.bot.get_channel(826572317844176913)
            
            embedVar = discord.Embed(title="PS5 DIGITAL IN STOCK!!", description="<@&826577176727781376>", color=0x2559FF)
            embedVar.set_image(url = 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6430/6430161_sd.jpg;maxHeight=640;maxWidth=550')
            embedVar.add_field(name="Link", value="https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161", inline=False)
            

            await channel.send(embed=embedVar)

            channelx = self.bot.get_channel(832077275059060747)
            
            embedVarx = discord.Embed(title="XBOX SERIES X IN STOCK!!", description="<@&826577207555391559>", color=0x00CA22)
            embedVarx.set_image(url = 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428324cv15d.jpg;maxHeight=640;maxWidth=550')
            embedVarx.add_field(name="Link", value="https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324", inline=False)
            

            await channelx.send(embed=embedVarx)
        else:
          channel = self.bot.get_channel(message.channel.id)
              
          await channel.send("We don't support that command: try using 'add' ")
          
