import math
from tokenize import String
import discord
from discord.ext import commands
import re
import random
from Units import UnitsFlat

def conversionCondition(msgch: discord.TextChannel): return ((msgch.id in [987028481730838638, 997308502638874705, 986385232703942656]) or msgch.guild.id ==190846007582392320)
class Calc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if(msg.author == self.bot.user): return
        content=msg.content.lower()

        #TODO: Add Unit Conversion!
        if(conversionCondition(msg.channel)):
            has_answ=False
            embed = discord.Embed(title="Unit Conversion", colour=discord.Colour(0x7c4bf0))
            matches = re.findall("(\d+)\s?([A-Za-z]+)",content)
            for mymatch in matches:
                print("CONVERSION ATTEMPTED")
                if(mymatch[1].lower() in UnitsFlat):
                    match mymatch:
                        case (n, og_unit) if og_unit in UnitsFlat:
                            has_answ = True
                            inputVal=f"{n} {og_unit}"
                            for unit in UnitsFlat[og_unit]:
                                embed.add_field(name=inputVal, value=f"{round(UnitsFlat[og_unit][unit]*float(n),2)} {unit}", inline=True)


            embed.set_footer(text="This conversion was brought to you by Hetap!")
            embed.set_author(name="JaaanBot", icon_url="https://cdn.discordapp.com/avatars/138060982953050112/af662a7d9363c370b4ff5548d86524eb.webp")


            if(has_answ): await msg.channel.send(embed=embed)

        #DnD Calculator
        if(len(msg.content)>1 and msg.content[1] == "d"):
            match = re.match("(\d+[\+\-d\*])+\d?", msg.content)
            result = evalDiceSum(match[0].replace("-","+-"))
            print(result[1])
            await msg.channel.send(f"Die Summe ist {result[0]}, und du hast {result[1]} gewürfelt")
    
    #@discord.app_commands.context_menu()
    #async def react(interaction: discord.Interaction, message: discord.Message):
    #    await interaction.response.send_message('Very cool message!', ephemeral=True)


async def setup(bot):
    await bot.add_cog(Calc(bot)) 


#Static Methods!
#Rechnet einen String des gleichen Formates wie "2d6+3d6+5+4 aus."
def evalDiceSum(s:str) -> tuple[int, list]:
    print(s)
    print(terms:=re.findall("-?\d+|[\+d\*]",s))
    diceRolls=[]
    #dice
    evalListUsing(terms, "d", lambda numbr,size:[random.randint(1,size) for i in range(numbr)], rolls=diceRolls)
    print(terms)
    #Multiplication
    evalListUsing(terms, "*", lambda a,b: a*b)
    print(terms)
    #Addition        
    evalListUsing(terms, "+", lambda a,b: a+b)


    if(len(terms)==1):
        return (terms[0], diceRolls)
    else:            
        return "_error"

#Fuck you me from the future if you are trying to understand this
#You did this to yourself
def evalListUsing(terms: list, operator: str, operation, *, rolls:list=None):
    i=0
    while(i<len(terms)):
        if terms[i] == operator:
            arg1 = int(terms.pop(i-1))
            arg2 = int(terms.pop(i))
            if(operator == "d"):
                newdiceRolls=operation(arg1,arg2)
                print(rolls)
                if (rolls is not None): rolls.append(newdiceRolls)
                result = sum(newdiceRolls)
            else: result = operation(arg1,arg2)
            terms[i-1]= result
        else:
            i+=1
    return terms


