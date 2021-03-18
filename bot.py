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

@bot.command(name='kick')
async def on_member_kick(ctx, member : discord.Member=None, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} был кикнут по причине:{reason}')
    await member.send(f"Вы были кикнуты из сервера по причинк:{reason}")

@bot.command()
async def mute(ctx, member : discord.Member=None, *,reason=None, time=None):
    role_mute = discord.utils.get(ctx.guild.roles, name='Muted')
    emb = discord.Embed(title='Mute', color=0xff0000)
    emb.add_field(name='Moderator',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Member',value=member.mention,inline=False)
    emb.add_field(name='Reason ',value=reason,inline=False)
    emb.add_field(name='Time',value=time,inline=False)
    await member.add_roles(role_mute)
    await ctx.send(embed = emb)

@bot.command()
async def unmute(ctx, member):
    await member.unmute
    await ctx.send(f'{member.mention} был размучен')

    
    
    
   



 
bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')