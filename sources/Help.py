import discord
from discord.ext import commands,tasks


help_content = """
  ```connect - Kết nối voice chat
disconnect - Ngắt kết nối từ voice chat
play - Phát nhạc
pause - Tạm dừng
resume - Tiếp tục
nowplaying - Bài hát đang được chơi
queue - Xem playlist hiện tại
loop - Lặp lại bài hát/playlist```
"""

class Help(commands.Cog):
    def __init__(self,client):
        self.bot = client

    @commands.command()
    async def help(self,ctx):
        await ctx.send(help_content)
