import disnake
from disnake.ext import commands

PREFIX = '!'

client = commands.Bot(command_prefix = PREFIX, sync_commands = False)

@client.slash_command(description = "Hello bro)")
async def hello(ctx, member: disnake.Member):
  await ctx.send(f'Hi {member.mention}')
  
@client.slash_command(description = "Help for you)")
async def help(ctx):
  await ctx.send('команды')
  
