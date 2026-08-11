import discord
from dotenv import load_dotenv
from os import getenv


load_dotenv()
BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
INTENTS = discord.Intents.default()


class MyClient(discord.Client):
    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")


def run_client() -> None:
    client = MyClient(intents=INTENTS)

    if not BOT_TOKEN is None:
        client.run(BOT_TOKEN)
    else:
        raise ValueError("DISCORD_BOT_TOKEN environment variable is none")


def main() -> None:
    print("Hello from ping!")
    run_client()


if __name__ == "__main__":
    main()
