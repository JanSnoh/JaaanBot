import discord
import RoleList
import discord
from discord.ext import commands
import csv
import pprint
from os import listdir
from os.path import isfile, join

class JaanBot(commands.Bot):
    #defines:
    global role_message_id
    role_message_id = 990004488381272204
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')    
        raw = await self.tree.fetch_commands()
        res = await self.tree.sync(guild=self.get_guild(977274077905584148))    
        print(raw, res)
        
    @commands.hybrid_command(name="pong")
    async def ping_command(self, ctx: commands.Context) -> None:
        await ctx.send("Yo whassup")


    async def on_message(self, message):
        msg_text = message.content.lower()
        if(message.author == self.user):
            return
        if msg_text == "hello":
            await message.channel.send("fack off \n  <:mortar:989994064910889050>")
            
        elif(msg_text.startswith("!zauber")):
            if(msg_text == "!zauber"):
                answ = "Im Sortiment sind: \n"
                with open("Zauber.tsv", "r", encoding='UTF-8', newline='') as file:
                    raw = csv.DictReader(file, delimiter="\t", quotechar="'")
                    for row in raw:
                        print(row["Name"])
                        answ+=f"{row['Name']}\n"
                await message.channel.send(answ)
            else:
                arg = msg_text[8:]
                answ = ""
                with open("Zauber.tsv", "r", encoding='UTF-8', newline='') as file:
                    raw = csv.DictReader(file, delimiter="\t", quotechar="'")
                    for row in raw:
                        #print(f"{row['Beschreibung']} und {arg}")
                        if (row["Name"].lower() == arg):
                            if ("Timestamp" in row):
                                del row["Timestamp"]
                                answ+=f"{pprint.pformat(row, sort_dicts=False, width=80)}\n"
                                #answer+=
                    answ = answ.replace("{", "```python\n")
                    answ = answ.replace("}", "```")
                    print(answ)
                await message.channel.send("Error!" if answ=="css \n" else answ)
            
        
        print(f'Message from {message.author}: {message.content}')
                     

    async def on_raw_reaction_add(self, payload):
        print(f'{payload.member} reacted to \'{payload.message_id}\' with {payload.emoji}')
        
        if(payload.message_id == role_message_id):
            for emoji in RoleList.roles:
                #print(f"{payload.emoji} == {emoji}   =>  {str(payload.emoji) == emoji}")
                if(str(payload.emoji) == emoji):
                    new_role=self.get_guild(payload.guild_id).get_role(RoleList.roles[emoji])
                    print(f"Giving out: {new_role}")
                    await payload.member.add_roles(new_role)
    
    async def on_raw_reaction_remove(self, payload):
        print(f'{payload.member} reacted to \'{payload.message_id}\' with {payload.emoji}')
        
        if(payload.message_id == role_message_id):
            for emoji in RoleList.roles:
                #print(f"{payload.emoji} == {emoji}   =>  {str(payload.emoji) == emoji}")
                if(str(payload.emoji) == emoji):
                    new_role=self.get_guild(payload.guild_id).get_role(RoleList.roles[emoji])
                    print(f"Taking away: {new_role}")
                    member = await self.get_guild(payload.guild_id).fetch_member(payload.user_id)
                    await member.remove_roles(new_role)
    
    async def setup_hook(self):
        path = 'extensions'
        extensions = [file for file in listdir(path) if isfile(join(path, file)) and file.endswith(".py")]
        for extension in extensions:
            try:
                await bot.load_extension(f'{path}.{extension[:-3]}')
                print(f"{extension}")
            except Exception as exception:
                print(f'Failed to load extension {extension[:-3]}.')
                print(exception)
                exit()

                


intents = discord.Intents.all()

bot = JaanBot(intents=intents, command_prefix="!")


if(__name__ == "__main__"):
    with open("Tokens.lmfao", mode="r") as file:
        tokens = file.readlines()
        print(tokens)
        



bot.run(tokens[0])
