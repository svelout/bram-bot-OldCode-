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
async def on_member_join(ctx, member):
    role = discord.utils.get(ctx.guild.roles, name='•member•')#•member•
    guild = ctx.get_guild(817341710228521010)
    channel = ctx.get_channel(817488304869474316)
    await ctx.add_roles(role)
    await channel.send('Привет {member.mention}! Добро пожаловать на сервер редьюсеров! ')
    await member.send('Совет от бота для тебя {member.name} , не забудь прочитать правила на сервере {guild.name} , иначе будет больно)')


bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')