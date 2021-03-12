import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import member

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def on_ready():
    print("BOT READY")

@bot.event
async def on_member_join(ctx):
   await ctx.add_roles(role)
    	
    
@bot.command()
async def set_role(ctx, role=None):
  if role != None:
  	for role in ctx.guild.roles:
  		if role.name == role:
  			role = guild.role
  			await ctx.send('default role was: {role.name}')
  else
  	await ctx.send('Role not found')
  
bot.run('Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.Zzq1j2Z8LycA-W8n4cW99DsiFzU')
