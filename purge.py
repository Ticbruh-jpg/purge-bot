import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    guild = bot.guilds[0]
    print(f"Connected to: {guild.name}")

    # pokupi sve membere
    all_members = {member.id: member for member in guild.members if not member.bot}
    
    # Dict za trackanje usera
    user_message_counts = {user.id: 0 for user in all_members.values()}

    print(f"Scanning {len(guild.text_channels)} channels for messages...")

    # Loopaj kroz kanale
    for channel in guild.text_channels:
        try:
            async for message in channel.history(limit=None):  # Fetchaj sve poruke
                if message.author.id in user_message_counts:
                    user_message_counts[message.author.id] += 1  # izbroji poruke po useru
        except discord.Forbidden:
            print(f"Skipping {channel.name} (No permission)")
        except discord.HTTPException:
            print(f"Skipping {channel.name} (Rate limit)")

    # pronadi tko ima manje od 15 poruka
    low_activity_users = [user for user_id, user in all_members.items() if user_message_counts[user_id] < 15]

    print(f"\nUsers with less than 15 messages ({len(low_activity_users)} total):")
    for user in low_activity_users:
        print(user.name)

    # pitaj za kick
    confirm = input("\nDo you want to kick these users? (yes/no): ").strip().lower()
    if confirm == "yes":
        await kick_low_activity_users(guild, low_activity_users)

async def kick_low_activity_users(guild, low_activity_users):
    for user in low_activity_users:
        try:
            await user.kick(reason="Low activity (less than 15 messages)")
            print(f"Kicked: {user.name}")
        except discord.Forbidden:
            print(f"Failed to kick {user.name} (Missing permissions)")
        except discord.HTTPException:
            print(f"Failed to kick {user.name} (Rate limited)")


bot.run(" ")
