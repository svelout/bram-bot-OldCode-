import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import member

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("BOT READY")

@bot.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name='•member•')#•member•
    await ctx.add_roles(role)

@bot.event
async def on_member_join(ctx):
    guild = ctx.get_guild(817341710228521010)
    channel = ctx.get_channel(817488304869474316)
    await channel.send(f'Добро пожаловать на сервер {member.mention} ! :pig: накажет тебя здесь)')
    await member.send(f'Привет {member.name} теперь ты редьюсер, надеюсь тебе понравится на сервере {guild.name}')



bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')