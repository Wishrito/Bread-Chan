import datetime as dat
import json
import os
import re
from typing import Any, Optional, Union, cast

import discord
import mysql.connector as db
import sqlalchemy
from discord import Locale, app_commands
from discord.ext import commands
from dotenv import load_dotenv
from googletrans import Translator
from googletrans.models import Translated
from sqlalchemy.orm import Mapped, mapped_column

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

sensitiveClass = SensitveClass()


