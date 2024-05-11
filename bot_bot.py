import discord
from discord.ext import commands
from bot_token import token
from bird_class import bird_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def algila(ctx):
    attachments = ctx.message.attachments
    if attachments:
        await ctx.send('Resim algılandı kaydediliyor')
        for attachment in attachments:
            file_name = attachment.filename
            file_path = f'images/{file_name}'
            await attachment.save(file_path)
            await ctx.send('resim kaydedildi')
            class_name, score = bird_class(file_path)
            await ctx.send(class_name)
            

    else:
        await ctx.send('lütfen komutla beraber bir resim yükleyin')

bot.run(token)