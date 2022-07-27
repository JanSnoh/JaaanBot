import math
import os
from typing import Union
import discord
from discord.ext import commands
import csv
import pprint
import random

class DnD(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @discord.app_commands.command(name="d", description="Wuerfeln ist lustig!")
    @discord.app_commands.choices(dice=[
        discord.app_commands.Choice(name="4",  value=1),
        discord.app_commands.Choice(name="6",  value=2),
        discord.app_commands.Choice(name="8",  value=3),
        discord.app_commands.Choice(name="10", value=4),
        discord.app_commands.Choice(name="20", value=5)])
    async def dice_command(self, ctx: commands.Context, dice: discord.app_commands.Choice[int], ):
        result =random.randint(1, int(dice.name))
        if(ctx.bot.DnD_ActiveSkillcheck == None):
            await ctx.send(result)
        else:
            dc = ctx.bot.DnD_ActiveSkillcheck["dc"]
            await ctx.send(f"{ctx.author} hat den Skillcheck mit einer {result} : {'verkackt' if dc>result else 'geschafft'}")

    #TODO: Add dnd expression calculator   e.g. "2d7+5"


    @discord.app_commands.command(name="skillcheck",description="Startet einen Skillcheck")
    async def skillcheck(self, interaction: discord.Interaction, text: str, dc: int):
        interaction.client.DnD_ActiveSkillcheck = {"dc": dc, "msg":None}
        await interaction.response.send_message(f"Skillcheck mit einer dc von {dc} erstellt!", ephemeral=True)
        interaction.client.DnD_ActiveSkillcheck["msg"]=await interaction.channel.send(f"{interaction.user} hat einen Skillcheck erstellt!")

    @discord.app_commands.command(name="endskillcheck",description="Beendet einen Skillcheck")
    async def endskillcheck(self, interaction: discord.Interaction ):
        interaction.client.DnD_ActiveSkillcheck = None
        await interaction.response.send_message("Skillcheck beendet!")


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
                    raw = csv.DictReader(file, delimiter="\t", quotechar="'", quoting=csv.QUOTE_NONE)
                    for row in raw:
                        print(f"{row['Name']} und {arg} ist {row['Name'] ==arg}")
                        if (row["Name"].lower() ==  arg.lower()):
                            if ("Timestamp" in row):
                                del row["Timestamp"]
                            answ+=f"{(row)}\n"
                            #answer+=
                    answ = answ.replace("{", "```python\n")
                    answ = answ.replace("}", "```")
                    print(answ)
                await ctx.send(f"Error! {arg}" if answ=="" else answ)


    #@discord.app_commands.context_menu()
    #async def react(interaction: discord.Interaction, message: discord.Message):
    #    await interaction.response.send_message('Very cool message!', ephemeral=True)


async def setup(bot):
    await bot.add_cog(DnD(bot)) 