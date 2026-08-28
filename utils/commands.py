import datetime as dat
from utils import searchGroup
import discord
from discord import app_commands, ChannelType

from utils import client
from utils.ui import SayModal


@client.tree.command(
    name="spotify-send-track", description="envoie la musique écoutée sur Spotify"
)
@app_commands.allowed_contexts(True, True, True)
@app_commands.allowed_installs(True, True)
async def spotify_track(interaction: discord.Interaction):
    msg = ""
    ephemeral = False
    member = interaction.user.mutual_guilds[0].get_member(interaction.user.id)
    if member:
        spotify_activity = discord.utils.find(
            lambda a: isinstance(a, discord.Spotify), member.activities
        )
        if isinstance(spotify_activity, discord.Spotify):
            msg = spotify_activity.track_url
        else:
            msg = "Aucune musique en cours d'écoute 🥲"
            ephemeral = True
    else:
        msg = "nous n'avons pas de serveurs en commun, je ne peux donc pas accéder à ce que tu écoutes :("
        ephemeral = True
    await interaction.response.send_message(msg, ephemeral=ephemeral)

