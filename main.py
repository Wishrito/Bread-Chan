import asyncio
from discord.gateway import DiscordWebSocket


from utils import client
from utils.functions import load_cogs, identify
from utils.class_module import SensitveClass

DiscordWebSocket.identify = identify

# Crée une instance de SensitveClass
sensitiveClass = SensitveClass()


async def main():
    await load_cogs(client)
    await client.start(sensitiveClass.get_discord_token())


if __name__ == "__main__":
    asyncio.run(main())
