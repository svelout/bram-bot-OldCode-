import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import guild, member, member, user
import asyncio
import time

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
    await ctx.send(f'Привет! Добро пожаловать на сервер редьюсеров, здесь ты можешь найти себе много новых собеседников и просто приятно провести время. Удачи!')

@bot.command(name='kick')
@commands.has_permissions(view_audit_log=True)
async def kick(ctx, member : discord.Member,reason):
    emb = discord.Embed(title='Kick', color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Участник',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.kick()
    await ctx.send(embed = emb)
    await member.send(f'Вы были кикнуты с сервера по причине:{reason}')

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, member : discord.Member,reason,time):
    rolemute = discord.utils.get(ctx.guild.roles, id=822120846725218385)
    emb = discord.Embed(title='Задержан', color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Участник',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.add_field(name='Время',value=time,inline=False)
    await member.add_roles(rolemute)
    await ctx.send(embed = emb)
    await asyncio.sleep()
    await member.remove_roles(rolemute)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx, member : discord.Member,reason):
    emb = discord.Embed(title='Ban', color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Участник',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.ban()
    await ctx.send(embed=emb)
    await member.send(f'Вы были забанены на сервере по причине:{reason}')

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
 
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} был разбанен')
            return

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx, *, member):
    await member.remove_roles(822120846725218385)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def tempban(ctx, member : discord.Member,reason):
    emb = discord.Embed(title='Tempban', color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Участник',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.add_field(name='Время',value=time,inline=False)
    await member.ban()
    await ctx.send(embed=emb)
    await member.send(f'Вы были забанены на сервере по причине:{reason}')
    await asyncio.sleep()
    await member.unban()


bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')