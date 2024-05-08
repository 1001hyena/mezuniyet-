


import discord
from discord.ext import commands
from bot_token import token



intents = discord.Intents.default()
intents.message_content = True



bot = commands.Bot(command_prefix='@hyenabot ', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')



@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir botum ve bu sunucunun modiratörluğunu yapıyorum')



@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("hahaha" * count_heh)



bot.run(token)


