from ping.client.ping_client import PingClient
from ping.configuration import BOT_TOKEN, INTENTS


def run_client() -> None:
    INTENTS.voice_states = True
    client = PingClient(intents=INTENTS)

    if BOT_TOKEN is None:
        raise ValueError("DISCORD_BOT_TOKEN environment variable is none")

    client.run(BOT_TOKEN)

def main() -> None:
    print("Hello from ping!")
    run_client()


if __name__ == "__main__":
    main()
