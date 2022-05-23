import discord
from discord.ext import commands
#from discord.ext import commands
#import requests
#import json
from os.path import exists

files = {}
path_to_open = ""

if exists("/home/rmonaghan/TheFedsAreHere/.env"):
    path_to_open = "/home/rmonaghan/TheFedsAreHere/.env"
else:
    path_to_open = ".env"

with open(path_to_open, "r") as f:
    spl = f.read().split("\n")
    for line in spl:
        if line == '':
            break
        broken = line.split("=")
        files[broken[0]] = broken[1]

TOKEN = 'OTc2NTU1NTgzODMyNDc3NzE2.GsPXBh.BBsVVe_E3GqFfpr6LQPriBlyNQEjEkbFTYb2iY'

bot = commands.Bot(command_prefix = '~')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def Feds(ctx, number):  
    number = int(number)
    if number == None:
        number = 1
    async for x in ctx.channel.history(limit = number+1):
        await x.delete()
    await ctx.channel.send(file = discord.File(files["federal-investigation"]))

@bot.command()
async def Roast(ctx):
    async for x in ctx.channel.history(limit = 1):
        await x.delete()
    await ctx.send(f'Shut yo skin tone chicken bone google chrome flip phone disowned icecream cone extra chromosome full blown student loan overgrown x y hormone sylvester stallone autozone silver patrone headass up', file = discord.File(files["superknucklecahnucklebeltbucklebananatruffle"]))

@bot.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, memeber : discord.Member):
    await memeber.ban(reason = "The Feds got you")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong {0}'.format(round(bot.latency, 1)))


bot.run(TOKEN) 