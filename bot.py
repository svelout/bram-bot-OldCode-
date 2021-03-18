import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import member
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

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def kick(ctx, member : discord.Member,reason):
    role_mute = discord.utils.get(ctx.guild.roles, id=822120846725218385)
    emb = discord.Embed(title='Mute', color=0xff0000)
    emb.add_field(name='Moderator',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Member',value=member.mention,inline=False)
    emb.add_field(name='Reason ',value=reason,inline=False)
    emb.add_field(name='Time',value=time,inline=False)
    await ctx.kick()
    await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, member : discord.Member,reason):
    rolemute = discord.utils.get(ctx.guild.roles, id=822120846725218385)
    emb = discord.Embed(title='Mute', color=0xff0000)
    emb.add_field(name='Moderator',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Member',value=member.mention,inline=False)
    emb.add_field(name='Reason ',value=reason,inline=False)
    emb.add_field(name='Time',value=time,inline=False)
    await ctx.add_roles(rolemute)
    await ctx.send(embed = emb)
    await asyncio.sleep()
    await ctx.remove_roles(rolemute)

 
bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')