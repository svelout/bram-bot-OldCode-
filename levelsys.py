from discord.ext import commands
import discord
from pymongo import MongoClient
from discord.ext.commands import bot

lolxbot_channel = 817597386184327209
talk_channels = [817488159075991643]

level = ["Начинающий reducer", "Reducer на любителя", "PRO-REDUCER", "Активный PRO-REDUCER", "Master of REDUCE", "God of REDUCE"]
levelnum = [5,10,15,20,25,50]

cluster = MongoClient("mongodb+srv://Levels:<Stepa123>@levels123.3ydrh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

levelling = cluster["discord"]["leveling"]

class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = levelling.find_one({"id" : message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id" : message.author.id, "xp" : 100}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id":message.author.id},{"$set":{"xp":xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl += 1
                    xp -= ((50*(lvl**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"Отличные новости {message.author.mention}! Ты повысил свой уровень до: {lvl}")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(description=f"{message.author.mention} теперь у тебя есть роль {level[i]}!")
                                embed.set_thumbnail(url=message.author.avatar_url)
                                await message.channel.send(embed=embed)
    
    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == bot.channel:
            stats = levelling.find_one({"id" : ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="Увы, но у вас еще нет уровня")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl += 1
                xp -= ((50*(lvl**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = levelling.find().sort('xp',-1)
                for x in rankings:
                    rank += 1
                    if stats['id'] == x["id"]:
                        break
                    embed = discord.Embed(title="{}'s уровень стата".format(ctx.author.name))
                    embed.add_field(name="Имя", value=ctx.author.mention, inline=True)
                    embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                    embed.add_field(name="Уровень", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                    embed.add_field(name="Шкала прогресса [lvl]", value=boxes * ":blue_square:" + (20-boxes) * ":white_large_square", inline=True)
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(levelsys(client))




