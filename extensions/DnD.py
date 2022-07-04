import math
import discord
from discord.ext import commands
import csv
import pprint
import random

class DnD(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.hybrid_command(name="d", description="Wuerfeln ist lustig!")
    async def dice_command(self, ctx: commands.Context, arg:int=20):
        await ctx.send(random.randint(1,arg))

    #Zauber Dictionary Commando!
    @commands.hybrid_command(name="zauber")
    async def spell_command(self, ctx: commands.Context, arg:str=None):
            if(arg==None):
                answ = "Im Sortiment sind: \n"
                with open("Zauber.tsv", "r", encoding='UTF-8', newline='') as file:
                    raw = csv.DictReader(file, delimiter="\t", quotechar="'")
                    for row in raw:
                        print(row["Name"])
                        answ+=f"{row['Name']}\n"
                await ctx.send(answ)
            else:
                answ = ""
                with open("Zauber.tsv", "r", encoding='UTF-8', newline='') as file:
                    raw = csv.DictReader(file, delimiter="\t", quotechar="'")
                    for row in raw:
                        print(f"{row['Name']} und {arg} ist {row['Name'] ==arg}")
                        if (row["Name"].lower() ==  arg.lower()):
                            if ("Timestamp" in row):
                                del row["Timestamp"]
                                answ+=f"{pprint.pformat(row, sort_dicts=False, width=80)}\n"
                                #answer+=
                    answ = answ.replace("{", "```python\n")
                    answ = answ.replace("}", "```")
                    print(answ)
                await ctx.send(f"Error! {arg}" if answ=="" else answ)


    #@discord.app_commands.context_menu()
    #async def react(interaction: discord.Interaction, message: discord.Message):
    #    await interaction.response.send_message('Very cool message!', ephemeral=True)


async def setup(bot):
    await bot.add_cog(DnD(bot), guilds=[discord.Object(id=977274077905584148)]) 