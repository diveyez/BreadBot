import discord
from discord.ext import commands
import config
import json
from datetime import datetime, timedelta
import time
import sys
import finvizz
import shortsqueeze
import help


# Connect to Discord
client = commands.Bot(command_prefix = '.')

@client.event
@commands.has_role("Admin")
async def on_message(message):
    if(message.author.bot):
        return

    channels = ["breadbot"]
    
    if str(message.channel) in channels:
        if message.content.find(".ss") != -1:
            ticker = message.content[4:]
            shortdata = shortsqueeze.get_shortSqueeze_data(str(ticker))
            if shortdata == -1:
                await message.channel.send(":cry: Could not find ticker: $" + ticker.upper() + " :cry:")
            else:   
                await message.channel.send(shortsqueeze.prettify(shortdata))
        elif message.content.find(".") != -1:
            ticker = message.content[1:]
            finviz_data = finvizz.get_finviz_data(str(ticker))
            if finviz_data == -1:
                await message.channel.send(":cry: Could not find ticker: $" + ticker.upper() + " :cry:")
            else:   
                await message.channel.send(finvizz.prettify(finviz_data))
        elif message.content.find(".help") != -1:
            help.help()
            
print("Connecting")
client.run(config.token)
