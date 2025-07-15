from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.send("🛠️ TEKID - Föreningen för Teknisk Infrastruktur och Design.")

def setup(bot):
    bot.add_cog(Info(bot))
