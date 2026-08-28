from discord import app_commands
from pathlib import Path

from discord.ext import commands
from utils.class_module import BreadChanClient
from discord.app_commands.tree import _log
import sys
import discord
from discord.app_commands import Choice

async def guild_autocomplete(interaction: discord.Interaction, current = ""):
    liste = [
        Choice(name=f"{g.name}", value=f"{g.id}") for g in interaction.client.guilds if current.lower() in g.name.lower()
        or current in str(g.id)
    ][:10]
    print(current, liste)
    return liste


# Fonction pour charger les cogs
async def load_cogs(bot: BreadChanClient):
    modules = [
        file.stem for file in (
            Path(__file__)
            .parent.parent
            / "cogs"
        ).glob("cog_*.py")
    ]
    for module in modules:
        try:
            await bot.load_extension(f"cogs.{module}")
        except commands.ExtensionError as e:
            msg = f"Failed to load {module}: {e}"
        else:
            cog = bot.cogs.get(f"cogs.{module}")
            msg = f"Loaded {module}"
        print(msg)

# mobile status


async def identify(self):
    payload = {
        'op': self.IDENTIFY,
        'd': {
            'token': self.token,
            'properties': {
                '$os': sys.platform,
                '$browser': 'Discord Android',
                '$device': 'Discord Android',
                '$referrer': '',
                '$referring_domain': ''
            },
            'compress': True,
            'large_threshold': 250,
            'v': 3
        }
    }

    if self.shard_id is not None and self.shard_count is not None:
        payload['d']['shard'] = [self.shard_id, self.shard_count]

    state = self._connection
    if state._activity is not None or state._status is not None:
        payload['d']['presence'] = {
            'status': state._status,
            'game': state._activity,
            'since': 0,
            'afk': False
        }

    if state._intents is not None:
        payload['d']['intents'] = state._intents.value

    await self.call_hooks('before_identify', self.shard_id, initial=self._initial_identify)
    await self.send_as_json(payload)
    _log.info('Shard ID %s has sent the IDENTIFY payload.', self.shard_id)

