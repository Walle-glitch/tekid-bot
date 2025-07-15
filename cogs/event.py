import discord
from discord import app_commands
from discord.ext import commands
import json
import os

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree
        self.tree.add_command(self.event)

    @app_commands.command(name="event", description="Visa kommande evenemang")
    async def event(self, interaction: discord.Interaction):
        try:
            with open("events.json", "r", encoding="utf-8") as f:
                events = json.load(f)

            if not events:
                await interaction.response.send_message("📭 Inga planerade evenemang just nu.")
                return

            embed = discord.Embed(
                title="📅 Kommande Evenemang – TEKID",
                color=discord.Color.green()
            )

            for event in events:
                name = f"📌 {event['title']}"
                value = (
                    f"📅 **Datum:** {event['date']} kl {event['time']}\n"
                    f"📍 **Plats:** {event['location']}\n"
                    f"📝 {event['description']}"
                )
                embed.add_field(name=name, value=value, inline=False)

            await interaction.response.send_message(embed=embed, ephemeral=False)

        except Exception as e:
            await interaction.response.send_message(f"⚠️ Fel vid inläsning av event: {e}")

async def setup(bot):
    await bot.add_cog(Event(bot))
