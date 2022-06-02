import discord
from discord.ext import commands,tasks


help_content = """
==============================================
  ___  ___                        __    ___ 
  |  \/  |                       /  |  /   |
  | .  . |_   _  ___  _ __   __ _`| | / /| |
  | |\/| | | | |/ _ \| '_ \ / _` || |/ /_| |
  | |  | | |_| | (_) | | | | (_| || |\___  |
  \_|  |_/\__,_|\___/|_| |_|\__, \___/   |_/
                            __/ |          
                            |___/   
================================================
*Hệ thống*
- setprefix + list() : thay đổi prefix mặc định
*Anime*
- animer: Random ảnh anime
- animegif: Random ảnh anime dạng .gif
- cry: khóc
- kiss: Hun
- animes: Tìm tên anime dựa trên ảnh hoặc video
*Rút gọn link*
- tiny : Rút gọn link sang tinyurl
*Random món ăn*
- fadd: Thêm món vào list
- fshow: Danh sách món đã thêm
- frandom: Lựa chọn bất kỳ s1 chón 1 món trong danh sách 
- fclear: Xoá danh sách vừa tạo
*Ngoài lề*
- ck: Chửi chó khoa :>
"""

class Help(commands.Cog):
    def __init__(self,client):
        self.bot = client

    @commands.command()
    async def help(self,ctx):
        await ctx.send("```"+ help_content + "```")
