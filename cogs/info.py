import discord
from discord import app_commands
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree
        self.tree.add_command(self.info)

    @app_commands.command(name="info", description="Information om TEKID")
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🛠️ TEKID – Teknisk Infrastruktur och Design",
            description="Föreningen för alla teknikintresserade inom IT, nätverk, säkerhet och infrastruktur.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Hemsida", value="[www.tekid.se](https://www.tekid.se)", inline=False)
        embed.add_field(name="Kontakt", value="kontakt@tekid.se", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=False)

async def setup(bot):
    await bot.add_cog(Info(bot))
