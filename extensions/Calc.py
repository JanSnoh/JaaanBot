import math
from tokenize import String
import discord
from discord.ext import commands
import re
import random

class Calc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        content=msg.content.lower()
        #TODO: Add Unit Conversion!
        #if(content.):

        if(len(msg.content)>1 and msg.content[1] == "d"):
            match = re.match("(\d+[\+\-d])+\d?", msg.content)
            #match[0].replace("-","+-")
            result = evalDiceSum(match[0].replace("-","+-"))
            await msg.channel.send(f"Die Summe ist {result[0]}, und du hast {result[1:]} gewürfelt")
    
    #@discord.app_commands.context_menu()
    #async def react(interaction: discord.Interaction, message: discord.Message):
    #    await interaction.response.send_message('Very cool message!', ephemeral=True)


async def setup(bot):
    await bot.add_cog(Calc(bot)) 

#Static Methods!
#Rechnet einen String des gleichen Formates wie "2d6+3d6+5+4 aus."
def evalDiceSum(s:String) -> int:
    print(s)
    print(terms:=re.findall("-?\d+|[\+d]",s))
    diceRolls=[]
    #dice
    i=0
    while(i<len(terms)):
        if terms[i] == "d":
            numbr = int(terms.pop(i-1))
            size = int(terms.pop(i))
            newdiceRolls=[random.randint(1,size) for i in range(numbr)]
            diceRolls.append(newdiceRolls)
            terms[i-1]=sum(newdiceRolls)
        else:
            i+=1

    #Addition        
    i=0
    while(i<len(terms)):
        if terms[i] == "+":
            numbr = int(terms.pop(i-1))
            size = int(terms.pop(i))
            terms[i-1]=numbr+size
        else:
            i+=1
    if(len(terms)==1):
        return (terms[0], diceRolls)
    else:            
        return "_error"
