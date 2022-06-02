
import os
from pydoc import describe
import re
import discord
import dismusic
import requests
import json 
from sources.url_shortener import URLShoter
from sources.food_random import Food
from sources.waifu import Anime
from discord.ext import commands,tasks
from sources.outside import Outside

prefix = ["?"]
custom_prefixes = {}

async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return custom_prefixes.get(guild.id, prefix)
    else:
        return prefix

client = commands.Bot(command_prefix = determine_prefix)

@client.command()
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or prefix
    await ctx.send(f"Chuyển prefix thành `{prefixes}` ")

#Lavalink server
client.lavalink_nodes = [
    {"host": "lavalink.islantay.tk", "port": 8880, "password": "waifufufufu"},
]
#Run server
if __name__=="__main__":
  client.add_cog(Anime(client))
  client.add_cog(Food(client))
  client.add_cog(Outside(client))
  client.add_cog(URLShoter(client))
  client.load_extension('dismusic')
  client.run(os.getenv('TOKEN'))
