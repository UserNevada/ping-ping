# Ping-Ping 🚨
Personal Discord Bot that sends a message to a text channel when someone joins a voice channel.

- [x] Add discord.py
- [x] Go online
- [x] When entering voice channel...
    - [x] Log
    - [x] Send message
- [x] Wait to avoid accidental alert
- [x] format with ruff
- [ ] improve the logs, because they're trash
- Do I really need that?

- I guess it needs more refactor and perhaps creating more files...

---

You need to be the first one to join for it to alert.

---

To run you need to create a .env where the configuration lives.
it needs the following variables:

```.env
DISCORD_BOT_TOKEN=
DISCORD_BOT_ALERT_CHANNEL_ID=
```

Pretty self-explanatory names.
If it's not clear enough the ALERT_CHANNEL_ID field is the text channel where the bot sends messages.
I guess you will want it to be a private channel where only members with a specific role will be able to see inside.

I wouldn't trust this bot with an important server, it REALLY needs testing.
