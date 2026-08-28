import random
from discord.ext import tasks
import discord
from utils.class_module import BreadChanClient
from discord.ext import commands


class TaskCog(commands.Cog):
    def __init__(self, bot: BreadChanClient):
        self.client = bot
        self.reload_presence.start()
        self.status_list = [
            {
                "id": 0,
                "type": discord.ActivityType.listening,
                "status": "du Bring Me The Horizon",
            },
            {
                "id": 1,
                "type": discord.ActivityType.watching,
                "status": f"dans **{len(self.client.guilds)}** serveurs",
            },
            {
                "id": 2,
                "type": discord.ActivityType.watching,
                "status": "ma nouvelle page Discover !",
            },
            {
                "id": 3,
                "type": discord.ActivityType.competing,
                "status": "pour 500k $ sur Marvel Rivals",
            },
            {},
        ]
        self.last_status = random.choice(self.status_list)

    async def cog_unload(self):
        self.reload_presence.stop()

    @tasks.loop(minutes=2)
    async def reload_presence(self):
        """Change the bot's presence every 5 minutes"""

        list_copy = self.status_list.copy()
        list_copy.remove(self.last_status)
        status = random.choice(list_copy)
        self.last_status = status
        activity = discord.Activity(type=status.get("type"), name=status.get("status"))
        await self.client.change_presence(activity=activity)

    @reload_presence.before_loop
    async def before_reload_presence(self):
        await self.client.wait_until_ready()


async def setup(bot: BreadChanClient):
    await bot.add_cog(TaskCog(bot))
