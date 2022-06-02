from turtle import pos
import requests
import json 
import discord
import animec
import datetime
from animec import Charsearch
from discord.ext import commands,tasks
import urllib.parse


class Anime(commands.Cog):
    def __init___(self,client):
        self.bot = client
    @commands.command()
    async def animer(self,ctx):
        query = {
            "is_nsfw" : "false",
            "many": "false",
            "gif":"false",
        }
        response = requests.get('https://api.waifu.im/random', params=query)
        image = json.loads(response.text)['images'][0]
        url = image['url']
        tags = image['tags'][0]
        des = tags['description']
        name = tags['name']
        embed=discord.Embed(title= ("Gái alime cho {user}".format(user = ctx.message.author.name)),url = url ,describe="Muong14Wibu")
        embed.set_image(url=url)
        await ctx.send(embed = embed) 

    @commands.command()
    async def animegif (self,ctx):
        url = animec.waifu.Waifu.random_gif()
        embed=discord.Embed(title= ("Gái alime cho {user}".format(user = ctx.message.author.name)),url = url ,describe="Muong14Wibu")
        embed.set_image(url=url)
        await ctx.send(embed = embed) 
    @commands.command()
    async def cry(self,ctx):
        url = animec.waifu.Waifu.cry()
        embed=discord.Embed(title= ("{user} đang khóc".format(user = ctx.message.author.name)),url = url ,describe="Muong14Wibu")
        embed.set_image(url=url)
        await ctx.send(embed = embed) 
    @commands.command()
    async def kiss(self,ctx):
        url = animec.waifu.Waifu.kiss()
        embed=discord.Embed(title= "{user} hun hít các kỉu {name} mụt cách chết tịt".format(user = ctx.message.author.name,name = ctx.message.mentions[0].name),url = url ,describe="Muong14Wibu")
        embed.set_image(url=url)
        await ctx.send(embed = embed) 

    @commands.command()
    async def animes(self,ctx):
        url = ctx.message.attachments[0].url
        response = requests.get("https://api.trace.moe/search?anilistInfo&url={}"
        .format(urllib.parse.quote_plus(url))
        ).json()
        data = response['result']
        name = list()
        await ctx.send("Kết quả tìm kiếm gần nhất")
        for i in range(3):
            similarity = data[i]['similarity']
            url_img = data[i]['image']
            anilist = data[i]['anilist']['title']
            title = str(anilist['english'])
            if title is None:
                title = str(anilist['native'])
            embed = discord.Embed(title = title)
            url_video = data[i]['video']
            episode = data[i]['episode']
            ep_from = round(data[i]['from'])
            ep_to = round(data[i]['to'])
            embed.set_image(url = url_img)
            embed.add_field(name ="Tỷ lệ khớp " , value = "{}%".format(round(similarity*100,2)))
            embed.add_field(name = "Trích xuất video", value ="[click]({})".format(url_video))
            embed.set_footer(text = ("Tập {ep} , từ {f} đến {t}. ".format(ep=episode,f=str(datetime.timedelta(seconds = ep_from)),t=str(datetime.timedelta(seconds = ep_to)))))
            await ctx.send(embed = embed)