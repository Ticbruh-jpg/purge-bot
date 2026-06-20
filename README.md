# purge-bot

A Discord bot that scans all channels in a server, counts messages per member, and kicks users with fewer than 15 messages.

## What it does

1. Connects to the first guild the bot is in
2. Scans message history across all text channels
3. Lists members with fewer than 15 total messages
4. Prompts for confirmation before kicking them

## Setup

1. Install dependencies:

```bash
pip install discord.py
```

2. Create a bot at [discord.com/developers](https://discord.com/developers/applications) and copy the token.

3. Paste your token at the bottom of `purge.py`:

```python
bot.run("YOUR_TOKEN_HERE")
```

4. Invite the bot to your server with `Kick Members` and `Read Message History` permissions.

5. Run it:

```bash
python purge.py
```

## Notes

- The bot requires the `members` and `messages` intents to be enabled in the Developer Portal.
- Channels the bot lacks permission to read are skipped automatically.
