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

@bot.command(name='delete')
async def on_message_delete(ctx):
    guild = ctx.get_guild(817341710228521010)
    delmsg = ctx.get_message({guild.message.id})
    await ctx.message_delete(delmsg)
 
bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')