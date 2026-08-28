import discord
from discord.ext import commands
from discord import app_commands

from utils import BreadChanClient

class ErrorCog(commands.Cog):
    def __init__(self, bot: BreadChanClient):
        self.client = bot

        self.on_error = self.on_error
    

    async def on_error(self, event: str):
        print(event)



async def setup(bot: BreadChanClient):
    await bot.add_cog(ErrorCog(bot))