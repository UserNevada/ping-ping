from os import getenv

from discord import Intents
from dotenv import load_dotenv

if not load_dotenv():
    print("No environment variables!")

BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
DISCORD_BOT_ALERT_CHANNEL_ID = getenv("DISCORD_BOT_ALERT_CHANNEL_ID")
TIME_TO_CONFIRM: int = 3
INTENTS = Intents.default()
