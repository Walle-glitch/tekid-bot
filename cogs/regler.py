import discord
from discord import app_commands
from discord.ext import commands

class Regler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree
        self.tree.add_command(self.regler)

    @app_commands.command(name="regler", description="Visa föreningens regler")
    async def regler(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📜 Regler för TEKID Discord-servern",
            color=discord.Color.orange()
        )

        regler = [
            ("1. Visa respekt", "All kommunikation ska ske med respekt. Diskriminering, trakasserier eller nedsättande kommentarer tolereras inte."),
            ("2. Håll det relevant", "Diskussioner ska vara relevanta för teknik, infrastruktur, design eller föreningsrelaterade ämnen. Använd rätt kanal för rätt ämne."),
            ("3. Ingen reklam eller spam", "Det är inte tillåtet att posta reklam, spam eller obehöriga länkar utan godkännande från styrelsen."),
            ("4. Använd ditt riktiga förnamn", "För transparens och gemenskap ska alla medlemmar använda sitt riktiga förnamn som smeknamn på servern."),
            ("5. Respektera sekretess", "Dela inte skärmdumpar eller loggar från diskussioner utan samtycke. Intern information ska stanna inom föreningen."),
            ("6. Följ Discords användarvillkor", "[Läs reglerna här](https://discord.com/guidelines) – dessa gäller också på vår server."),
            ("7. Fråga om du är osäker", "Vid frågor eller rapporter – kontakta styrelsen via `#kontakt-styrelsen`.")
        ]

        for titel, beskrivning in regler:
            embed.add_field(name=titel, value=beskrivning, inline=False)

        embed.set_footer(text="Tack för att du följer reglerna och bidrar till en trygg och professionell miljö!")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Regler(bot))