from discord import app_commands
import discord
from utils.class_module import BreadChanClient


intents = discord.Intents.all()

client = BreadChanClient(intents=intents)


blagueGroup = app_commands.Group(name="blague", description="système de blagues")

searchGroup = app_commands.Group(
    name="search", description="groupe contenant les différentes commandes de recherche")

# command group for games
# gamegroup = app_commands.Group(name="game", description="group de commandes de jeux")
hsrGroup = app_commands.Group(name="hsr", description="commandes du jeu Honkai Star Rail")
# fortniteGroup = app_commands.Group(parent=gamegroup, name="fortnite")
