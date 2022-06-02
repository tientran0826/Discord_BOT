import discord
from discord.ext import commands,tasks
import random


class Food(commands.Cog):
    def __init__(self,client):
        self.bot = client
        self.list = list()
    @commands.command()
    async def fhelp(self,ctx):
        await ctx.send("Random món ăn")
    
    @commands.command()
    async def fadd(self,ctx,arg):
        food = arg
        if food:
            self.list.append(food)
            await ctx.send("Đã thêm {monan} vào danh sách thành công . Danh sách hiện có {somon} món".format(monan = food,somon = len(self.list)))
        else:
            await ctx.send("Chưa thêm món vào pé ơi.")
    @commands.command()
    async def fshow(self,ctx):
        if len(self.list):
            content = """Danh sách món ăn đã thêm```"""
            i = 1
            for food in self.list:
                content = content + "\n" + str(i) +"." + food
                i = i + 1
            content = content + "```"
            await ctx.send(content)
        else:
            await ctx.send("Danh sách món hiện tại đang rỗng.")
    @commands.command()
    async def fclear(self,ctx):
        self.list.clear()
        await ctx.send("Xoá danh sách thành công.")

    @commands.command()
    async def frandom(self,ctx):
        await ctx.send(random.choice(self.list))