import discord
import os
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    random_img = random.choice(images)
    with open(f'images/{random_img}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def bsmem(ctx):
    BSSimages = os.listdir('BSimages')
    random_BSimg = random.choice(BSSimages)
    with open(f'BSimages/{random_BSimg}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)



bot.run('MTI1NDM0MjQ5NjQxOTMxOTg2OA.GjBkHU.TrKnjW9kBGq7mdluel-SEqMnE2mkcYhAo4nABQ')

