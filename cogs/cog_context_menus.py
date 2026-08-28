
import datetime as dat

import discord
from discord import AppCommandType, app_commands, ChannelType
from utils import BreadChanClient # custom implementation of a regular ext.commands.Bot, you can replace them it won't affect the code itself
from discord.ext import commands

from utils.ui import SayModal

class ContextMenuCog(commands.Cog):
    def __init__(self, bot: BreadChanClient):
        self.client = bot
        self.context_commands = [
            app_commands.ContextMenu(name="Say", callback=self.say_callback, type=AppCommandType.message),
            app_commands.ContextMenu(name="Profil", callback=self.profil_callback, type=AppCommandType.user,allowed_contexts=app_commands.AppCommandContext(guild=True, dm_channel=True, private_channel=True), allowed_installs=app_commands.AppInstallationType(guild=True, user=True))
        ]
        for command in self.context_commands:
            self.client.tree.add_command(command)

    # @app_commands.checks.cooldown(1, 30, key=lambda i: (i.guild_id, i.user.id))
    async def say_callback(self, interaction: discord.Interaction, message: discord.Message):
        assert interaction.channel
        if interaction.channel.type == ChannelType.text:
            await interaction.response.send_modal(SayModal(message))


    async def profil_callback(self, interaction: discord.Interaction, user: discord.Member):
        assert self.client.user
        badges_class = []
        if user.public_flags.all() is not None:
            badges_class.extend(
                [
                    f"{discord.utils.get(self.client.emojis, name=badge.name)}"
                    for badge in user.public_flags.all()
                ]
            )
        else:
            badges_class = ["aucun badge"]
        badges = " ".join(badges_class)
        if user.accent_color is not None:
            nitro_role = discord.utils.get(self.client.emojis, id=1222184055156637726)
            badges_class.append(f"{nitro_role}")

        emb = discord.Embed(
            title=f"Profil de {user.display_name}",
            url=f"https://discord.com/users/{user.id}",
            color=user.color,
            timestamp=dat.datetime.now(),
        )
        emb.add_field(
            name="Date de création du compte :",
            value=f"le {discord.utils.format_dt(user.created_at)}",
        )
        if interaction.context.guild:
            emb.add_field(name="Badges :", value=badges)
            # Pour ajouter la pp du type
        emb.set_thumbnail(url=f"{user.display_avatar}")
        # Perso je fous les infos du bot la dessus
        emb.set_footer(text=self.client.user, icon_url=self.client.user.avatar)
        # type: ignore
        await interaction.response.send_message(embed=emb, ephemeral=True)



async def setup(bot: BreadChanClient):
    await bot.add_cog(ContextMenuCog(bot))