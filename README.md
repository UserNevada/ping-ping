# Ping-Ping 🚨
Personal Discord Bot that sends a message to a text channel when someone joins a voice channel.

- [x] Add discord.py
- [x] Go online
- [x] When entering voice channel...
    - [x] Log
    - [x] Send message
- [x] Wait to avoid accidental alert
- [x] format with ruff
- [x] improve the logs, because they're trash

---

You need to be the first one to join for it to alert.

---

To run you need to create a .env where the configuration lives.
it needs the following variables:

```.env
DISCORD_BOT_TOKEN=
DISCORD_BOT_ALERT_CHANNEL_ID=
DISCORD_BOT_TIME_TO_CONFIRM=
```

Pretty self-explanatory names.
If it's not clear enough the ALERT_CHANNEL_ID field is the text channel where the bot sends messages.
I guess you will want it to be a private channel where only members with a specific role will be able to see inside.

TIME_TO_CONFIRM refers to how long does the bot have to wait before sending the alert.
This way we should avoid alerts when joining a voice channel by accident.
Or something like that... idk.

I wouldn't trust this bot with an important server, it REALLY needs testing.
