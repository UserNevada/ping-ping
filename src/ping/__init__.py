import discord
from discord import Member, VoiceState
from dotenv import load_dotenv
from os import getenv


load_dotenv()
BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
ALERT_CHANNEL_ID = getenv("DISCORD_BOT_ALERT_CHANNEL_ID")
INTENTS = discord.Intents.default()


class MyClient(discord.Client):
    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

    async def on_voice_state_update(self, member: Member, before: VoiceState, after: VoiceState) -> None:
        if after.channel == None:
            return
        if not before.channel != after.channel:
            # this way we make sure that this won't get triggered by
            # mute or deaf states
            return

        print(f"{member.name} Joined a Voice Channel")
        await self.voice_channel_alert(member.display_name)

    async def voice_channel_alert(self, member_name: str) -> None:
        print("Alert!")
        if not ALERT_CHANNEL_ID is None:
            alert_channel_id = int(ALERT_CHANNEL_ID)
            alert_channel = self.get_channel(alert_channel_id)
            alert_channel_name: str = alert_channel.name

            alert_message: str = self.create_alert_message(member_name, alert_channel_name)
            await alert_channel.send(alert_message)
        else:
            raise ValueError("DISCORD_BOT_ALERT_CHANNEL_ID environment variable is none")

    def create_alert_message(self, member_name: str, channel_name: str) -> str:
        alert_message: str = f"""
        🚨 @{member_name} Joined {channel_name}! 🚨
        Go join him, now!
        """
        return alert_message


def run_client() -> None:
    INTENTS.voice_states = True
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
