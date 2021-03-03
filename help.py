import discord
import os
from discord.ext import commands

client = discord.Client()
client.remove_command("help")

@client.command()
async def help(ctx):
    em = discord.Embed(title = 'Commands', description = 'How to use the available commands')
  
    em.add_field(name = 'Example', value = '.AAPL\n.ss AAPL')
    em.add_field(name = 'Returns', value ='Stock info from Finviz.com\nShort info from Shortsqueeze.com')

    await ctx.send(embed = em)
