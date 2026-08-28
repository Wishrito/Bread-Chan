from discord import HTTPException
from utils.functions import guild_autocomplete
from discord import Permissions
from random import randint
from time import sleep
from utils.class_module import SupportGuild
from xmlrpc.client import Boolean
from utils.class_module import BreadChanClient
import datetime as dat
from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands


class DevGroup(app_commands.Group):
    def __init__(self, support_guild: SupportGuild):
        super().__init__(name="sudo", description="commandes reservées aux devs", guild_ids=[support_guild.id])
        self.guilds_whitelist = [
            discord.Object(1538590303944974511, type=discord.Guild).id,
            support_guild.id
        ]
        self.default_permissions = Permissions(administrator=True)

    @app_commands.command()
    async def clear_guilds(self, interaction: discord.Interaction, all: Optional[Boolean] = False):
        for g in interaction.client.guilds:
            match g.id in self.guilds_whitelist:
                case True:
                    if all == True:
                        try:
                            await g.leave()
                        except discord.HTTPException as http_fail:
                            print(http_fail)
                        else:
                            sleep(randint(10, 15))
                case False:
                    try:
                        await g.leave()
                    except discord.HTTPException as http_fail:
                        print(http_fail)
                    else:
                        sleep(randint(10, 15))
    
    @app_commands.command()
    async def list_guilds(self, interaction: discord.Interaction):
        guilds = interaction.client.guilds
        await interaction.response.send_message("Voici les serveurs sur lesquels je suis :" + "\n".join([g.name for g in guilds]), ephemeral=True)


    @app_commands.command()
    @app_commands.autocomplete(guild=guild_autocomplete)
    async def leave_guild(self, interaction: discord.Interaction, guild: str):
        leavable = interaction.client.get_guild(int(guild))
        if isinstance(leavable, discord.Guild):
            try:
                await leavable.leave()
            except HTTPException as err:
                msg = err
            else: 
                msg = f"le serveur {leavable.name} a été quitté"
            
            await interaction.response.send_message(msg, ephemeral=True)
            

class DevCog(commands.Cog):
    def __init__(self, bot: BreadChanClient):
        self.client = bot
        self.dev_group = DevGroup(self.client.support_guild)
        self.client.tree.add_command(self.dev_group)
    


async def setup(bot: BreadChanClient):
    await bot.add_cog(DevCog(bot))
