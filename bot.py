import discord
import pytz
from discord.ext.commands import bot
from discord.ext import commands
from discord import client, guild, member, member, user
import time
from discord.utils import get
from datetime import datetime

from pip._vendor import requests
from pytz import timezone

intents = discord.Intents.default()
intents.members = True

now = datetime.now()

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Моргенчлена"))
    print('GO')

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
async def mute(ctx, member : discord.Member,reason):
    rolemute = discord.utils.get(ctx.guild.roles, name='Задержан')
    rolemem = discord.utils.get(ctx.guild.roles, id=817487190720118825)
    guild = ctx.guild
    if not rolemute:
        rolemute = await guild.create_role(name='Задержан')
    
        for channel in guild.channels:
            await channel.set_permissions(rolemute, speak=False, send_message=False, read_message=True, read_message_history=True)
   
    await member.add_roles(rolemute, reason=reason, time=time)
    await member.remove_roles(rolemem)
    await ctx.send(f'{member.mention} был арестован по причине {reason}, на {time}')
    await member.send(f'Вы были арестованы на сервере {guild.name} по причине {reason}, на {time}')
    await time.sleep(time)
    await member.add_roles(rolemem)
    await member.remove_roles(rolemute)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx, member : discord.Member,reason):
    guild = ctx.guild
    emb = discord.Embed(title='Ban', color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Участник',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.ban()
    await ctx.send(embed=emb)
    await member.send(f'Вы были забанены на сервере {guild.name} по причине:{reason}')

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
async def unmute(ctx, member : discord.Member):
    rolemute = discord.utils.get(ctx.guild.roles, name='Задержан')
    rolemem = discord.utils.get(ctx.guild.roles, id=817487190720118825)
    if not rolemute:
        await ctx.send(f'{member.mention} не арестован')
        return
    if member.has_role(rolemute):
        await member.remove_roles(rolemute)
        await member.add_roles(rolemem)
        await ctx.send(f'{member.mention} был освобожден')

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
    await time.sleep(time)
    await member.unban()


@bot.event
async def on_voice_state_update(ctx, self, member, before, after):
    logchannel = discord.utils.get(ctx.guild.channels, id=818896571928281099)
    if member.bot:
        return
    if not before.channel:
        logchannel.send(f'{member.name} joined {after.channel.name}')

    if before.channel and not after.channel:
        logchannel.send("User left channel")

    if before.channel and after.channel:
        if before.channel.id != after.channel.id:
            logchannel.send("user switched voice channel")
        else:
            logchannel.send("Something else happened")

@bot.event
async def on_voice_state_update(message,ctx,member, before, after):
    if after.channel != None:
        if after.channel.id == 818882604681658441:
            for guild in bot.guilds:
                maincategory = discord.utils.get(
                    guild.categories, id=817599060419936256)
                channel2 = await guild.create_voice_channel(name=f'канал {member.display_name}', category=maincategory)
                await channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                await member.move_to(channel2)

                def check(x, y, z):
                    return len(channel2.members) == 0
                await bot.wait_for('voice_state_update', check=check)
                await channel2.delete()
                name = message.content
                if message.content.startwith(".voicename" + name):
                    await channel2.set_name(name)

bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')