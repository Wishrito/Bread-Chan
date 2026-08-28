from utils.class_module import BreadChanClient
import datetime as dat
from typing import Optional

import discord
from blagues_api import BlaguesAPI, BlagueType
from discord import app_commands
from discord.ext import commands

from utils.class_module import sensitiveClass

@app_commands.allowed_contexts(True, True, True)
@app_commands.allowed_installs(True, True)
class FunGroupCog(commands.GroupCog, group_name="blague"):
    def __init__(self, bot: BreadChanClient):
        self.client = bot
        self.blagues_client = BlaguesAPI(str(sensitiveClass.get_blagues_token()))

    @app_commands.command(name="random", description="envoie une blague au hasard parmi une sélection")
    async def rand_joke(self, interaction: discord.Interaction):
        random_joke = await self.blagues_client.random()
        await interaction.response.send_message(f"{random_joke.joke}\n\n||{random_joke.answer}||")


    @app_commands.command(name="specifique", description="envoie une blague d'un type spécifique")
    @app_commands.choices(blaguetype=[app_commands.Choice(name=f"blague {blague.lower()}", value=blague) for blague in dir(BlagueType) if "__" not in blague and blague.isupper()])
    async def joke(self, interaction: discord.Interaction, blaguetype: app_commands.Choice[str]):
        categorized_joke = await self.blagues_client.random_categorized(blaguetype.value.lower())
        await interaction.response.send_message(f"{categorized_joke.joke}\n\n||{categorized_joke.answer}||")


async def setup(bot: BreadChanClient):
    await bot.add_cog(FunGroupCog(bot))
