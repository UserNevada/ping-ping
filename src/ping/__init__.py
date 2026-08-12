from os import getenv
from time import sleep

import discord
from discord import Member, VoiceState
from discord.errors import NotFound
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
ALERT_CHANNEL_ID = getenv("DISCORD_BOT_ALERT_CHANNEL_ID")
TIME_TO_CONFIRM: int = 10
INTENTS = discord.Intents.default()


class MyClient(discord.Client):
    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

    async def on_voice_state_update(self, member: Member, before: VoiceState, after: VoiceState) -> None:
        if after.channel == None: # if joining and not leaving
            return
        if before.channel == after.channel:
            # this way we make sure that this won't get triggered by
            # mute or deaf states
            return
        if len(after.channel.members) > 1: # If you're the first one
            print(len(after.channel.members))
            print(f"{member.name} is not the first")
            return


        print(f"{member.name} Joined a Voice Channel")

        # Wait to avoid doing ping on accidental join
        self.wait_before_ping()

        # Are you still here?
        # Maybe another channel or disconnected?

        # if joining and not changing.
        # We fetch_voice for checking if the user is still in a voice channel
        # if not it will throw an error, let's take advantage of that
        try:
            await member.fetch_voice()
            if not before.channel is None:
                self.voice_channel_alert(member.display_name).close()
                print(f"{member.name} changed channel...")
            else:
                await self.voice_channel_alert(member.display_name)
        except NotFound:
            print(f"{member.name} left...")

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
        🚨 {member_name} Joined {channel_name}! 🚨
        Go join him, now!
        """
        return alert_message

    def wait_before_ping(self) -> None:
        time: int = 0
        print("Start countdown...")
        while time < TIME_TO_CONFIRM:
            sleep(1)
            time += 1
        print("Countdown done!")


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
