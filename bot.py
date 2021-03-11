import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import member

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

class BotData:
    def _init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

botdata = BotData()

@bot.event
async def on_ready():
    print("BOT READY")

@bot.event
async def on_member_join(ctx, member):
    role = discord.utils.get(ctx.guild.roles, name='•member•')#•member•
    await ctx.add_roles(role)
    if botdata.welcome_channel.send != None:
        await botdata.welcome_channel.send(f'Привет! {member.mention}! Добро пожаловать на редьюс сервер, хорошего пребывания')

@bot.event
async def on_member_remove(member):
    if botdata.goodbye_channel != None:
        await botdata.goodbye_channel.send(f" Прощай {member.mention}! Жаль, что ты ушел ")

@bot.command()
async def set_welcome_channel(ctx, channel_name=None):
    if channel_name != None:
        for channel in ctx.guild.chanels:
            if channel.name == channel_name:
                botdata.welcome_channel = channel
                await ctx.channel.send(f"Welcome channel = {channel.name}")
                await channel.send("Это новый канал приветсвия")

@bot.command()
async def set_goodbye_channel(ctx, channel_name=None):
    if channel_name != None:
        for channel in ctx.guild.chanels:
            if channel.name == channel_name:
                botdata.goodbye_channel = channel
                await ctx.channel.send(f"Goodbye channel = {channel.name}")
                await channel.send("Это новый канал прощания")

 
bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')