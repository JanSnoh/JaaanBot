import discord
from discord.ext import commands

class DnD(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="test2", description="super test")
    async def test(self, interaction, message: str):
        await interaction.response.send_message('Very cool message!', ephemeral=True)

    @commands.hybrid_command(name="ping")
    async def ping_command(self, ctx: commands.Context) -> None:
        await ctx.send("Yo whassup")


    #@discord.app_commands.context_menu()
    #async def react(interaction: discord.Interaction, message: discord.Message):
    #    await interaction.response.send_message('Very cool message!', ephemeral=True)


async def setup(bot):
    await bot.add_cog(DnD(bot), guilds=[discord.Object(id=977274077905584148)]) 