import discord
from discord.ext import commands,tasks

cho_khoa = """```
 ██████ ██   ██  ██████      ██   ██ ██   ██  ██████   █████  
██      ██   ██ ██    ██     ██  ██  ██   ██ ██    ██ ██   ██ 
██      ███████ ██    ██     █████   ███████ ██    ██ ███████ 
██      ██   ██ ██    ██     ██  ██  ██   ██ ██    ██ ██   ██ 
 ██████ ██   ██  ██████      ██   ██ ██   ██  ██████  ██   ██ 
```"""

class Outside(commands.Cog):
    def __init__(self,client):
        self.bot = client

    @commands.command()
    async def ck(self,ctx):
        await ctx.send(cho_khoa)
