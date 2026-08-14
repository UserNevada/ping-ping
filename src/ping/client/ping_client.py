import discord
from discord import Member, VoiceState
from discord.channel import TextChannel
from discord.errors import Forbidden, HTTPException, NotFound

from ping.configuration import DISCORD_BOT_ALERT_CHANNEL_ID, TIME_TO_CONFIRM


class PingClient(discord.Client):
    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

    @staticmethod
    def _joining(after: VoiceState) -> bool:
        return after.channel is None

    @staticmethod
    def _not_mute_or_deaf(before: VoiceState, after: VoiceState) -> bool:
        # this way we make sure that this won't get triggered by
        # mute or deaf states
        return before.channel == after.channel

    @staticmethod
    def _first_to_join(after: VoiceState) -> bool | None:
        if after.channel is not None:
            return len(after.channel.members) == 1
        else:
            print("Channel is none?")

    @staticmethod
    async def _wait_before_ping(time_to_confirm: int) -> None:
        print("Start countdown...")
        import asyncio
        await asyncio.sleep(time_to_confirm)
        print("Countdown done!")

    async def on_voice_state_update(self, member: Member, before: VoiceState, after: VoiceState) -> None:
        if self._joining(after):
            print(f"{member.name} Changed or left voice channel...")
            return
        if self._not_mute_or_deaf(before, after):
            print(f"{member.name} muted/unmuted or deafen/undeafen...")
            return
        if not self._first_to_join(after):
            print(f"{member.name} was not the first in its channel...")
            return

        print(f"{member.name} Joined a Voice Channel")

        # Wait to avoid doing ping on accidental join
        await self._wait_before_ping(TIME_TO_CONFIRM)

        await self._user_is_here(member, before)

    async def _user_is_here(self, member: Member, before: VoiceState) -> None:
        # if joining and not changing the channel.
        # We fetch_voice for checking if the user is still in a voice channel
        # if not it will throw an error, let's take advantage of that
        try:
            voice_state = await member.fetch_voice()
            if voice_state.channel is None:
                print("Could not find user channel")
                return

            if before.channel is not None:
                self.voice_channel_alert(member.display_name, voice_state.channel.name, DISCORD_BOT_ALERT_CHANNEL_ID).close()
                print(f"{member.name} changed channel...")
            else:
                await self.voice_channel_alert(member.display_name, voice_state.channel.name, DISCORD_BOT_ALERT_CHANNEL_ID)
        except NotFound, Forbidden, HTTPException:
            print(f"{member.name} left...")

    async def voice_channel_alert(self, member_name: str, channel_to_announce: str, alert_channel_id: str | None) -> None:
        if alert_channel_id is None:
            raise ValueError("DISCORD_BOT_ALERT_CHANNEL_ID environment variable is none")

        alert_channel_id_int = int(alert_channel_id)
        alert_channel = self.get_channel(alert_channel_id_int)

        if alert_channel is None or not isinstance(alert_channel, TextChannel):
            return

        alert_message: str = self.create_alert_message(member_name, channel_to_announce)
        _send = await alert_channel.send(alert_message)
        print("Alert!")

    def create_alert_message(self, member_name: str, channel_name: str) -> str:
        alert_message: str = f"""
        🚨 {member_name} Joined {channel_name}! 🚨
        Go join him, now!
        """
        return alert_message
