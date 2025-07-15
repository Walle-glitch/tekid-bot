import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} är nu online!")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synkade {len(synced)} kommandon.")
    except Exception as e:
        print(f"⚠️ Misslyckades med att synka: {e}")

# Ladda slash-kommandon från cogs/
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)
