import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix='u!') #command prefix

async def bot_status():
 await client.wait_until_ready()
 statuses = ["Need help? u!helpme",f"listening on {len(client.guilds)} server's","When was I created? u!created me"]
 while not client.is_closed():
   status = random.choice(statuses)
   await client.change_presence(activity=discord.Game(name=status))
   await asyncio.sleep(180) #180 seconds
client.loop.create_task(bot_status())

@client.command()
async def id(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    await ctx.send(member.id)

@client.command()
async def helpme(ctx):
    embed = discord.Embed(title="List of all commands", description="This is a bot that will give you information about a users account. To get info on another account, mention them after the command. e.g. u!avatar @chefski", color=0x76ea6c)
    embed.add_field(name="u!helpme", value="Menu with all commands", inline=False)
    embed.add_field(name="u!avatar", value="Sends a picture of the users avatar", inline=False)
    embed.add_field(name="u!created", value="Sends the creation date of the users account (year:month:day hour:minute:second", inline=False)
    embed.add_field(name="u!username", value="Sends the username of the user", inline=False)
    embed.add_field(name="u!status", value="Sends the status of the user", inline=False)
    embed.add_field(name="u!bot", value="Checks if the user is a bot", inline=False)
    embed.add_field(name="Need more help?", value="Feel free to join our Discord and contact support. https://discord.gg/YourLinkToDiscord", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(ctx.author.avatar_url)
    else:
        await ctx.send(member.avatar_url)

@client.command()
async def created(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(ctx.author.created_at)
    else:
        await ctx.send(member.created_at)

@client.command()
async def username(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(ctx.author.name)
    else:
        await ctx.send(member.name)

@client.command()
async def status(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(ctx.author.status)
    else:
        await ctx.send(member.status)

@client.command()
async def bot(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(ctx.author.bot)
    else:
        await ctx.send(member.bot)

client.run('PasteTokenHere')