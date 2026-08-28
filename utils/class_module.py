import os
from discord import Forbidden

import discord
from discord.ext import commands
from dotenv import load_dotenv

class SensitveClass:
    def __init__(self):
        pass

    def get_discord_token(self) -> str:
        load_dotenv()
        DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        return DISCORD_TOKEN if DISCORD_TOKEN is not None else ''

    def get_blagues_token(self) -> str | None:
        load_dotenv()
        BLAGUES_TOKEN = os.getenv("BLAGUES_API_TOKEN")
        if BLAGUES_TOKEN is None:
            return None
        return BLAGUES_TOKEN

class SupportGuild(discord.Object):
    def __init__(self):
        load_dotenv()
        self.id = self._get_id()
        self.type = discord.Guild

    def _get_id(self):
        load_dotenv()
        return int(os.getenv("SUPPORT_GUILD_ID", 0))

class BreadChanClient(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        self.support_guild = SupportGuild()
        super().__init__(command_prefix='!', intents=intents)


    async def setup_hook(self):
        try:
            await self.tree.sync(guild=self.support_guild)
        except Forbidden as nope:
            print(f"support check : {nope.response}")
        try:
            await self.tree.sync()
        except Forbidden as nope2:
            print(f"global check : {nope2}")


sensitiveClass = SensitveClass()


