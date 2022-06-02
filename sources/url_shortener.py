import discord
from discord.ext import commands,tasks
import requests
import os
class URLShoter(commands.Cog):
    def __init__(self,client):
        self.bot = client
    @commands.command()
    async def tiny(self,ctx,arg):
        short_url = requests.post('https://tinyurl.com/api-create.php?url='+ arg).text
        qr= requests.get('https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=' + short_url)
        file = open("./qr.png", "wb")
        file.write(qr.content)
        file.close
        file = discord.File("./qr.png", filename="image.png")
        embed = discord.Embed(title="Rút gọn link").set_image(url="attachment://image.png")
        embed.add_field(name= "Tiny url",value=short_url)
        await ctx.send(file = file,embed=embed)
        os.remove("./qr.png")