import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import guild, member
import time
import asyncio

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
    await ctx.member.send(f'Привет {member.mention}! Добро пожаловать на сервер редьюсеров, здесь ты можешь найти себе много новых собеседников и просто приятно провести время. Удачи!')

@bot.command(name='kick')
@commands.has_permissions(view_audit_log=True)
async def kick(ctx, member : discord.Member,reason):
    emb = discord.Embed(title='Kick', color=0xff0000)
    emb.add_field(name='Moderator',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Member',value=member.mention,inline=False)
    emb.add_field(name='Reason',value=reason,inline=False)
    await member.kick()
    await ctx.send(embed = emb)
    await member.send(f'Вы были кикнуты с сервера по причине:{reason}')

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, member : discord.Member,reason):
    rolemute = discord.utils.get(ctx.guild.roles, id=822120846725218385)
    emb = discord.Embed(title='Mute', color=0xff0000)
    emb.add_field(name='Moderator',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Member',value=member.mention,inline=False)
    emb.add_field(name='Reason ',value=reason,inline=False)
    emb.add_field(name='Time',value=time,inline=False)
    await member.add_roles(rolemute)
    await ctx.send(embed = emb)
    await asyncio.sleep()
    await member.remove_roles(rolemute)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx, member : discord.Member,reason):
    rolemute = discord.utils.get(ctx.guild.roles, id=822120846725218385)
    await member.remove_roles(rolemute)

 
bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')