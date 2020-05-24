import discord
import json  # 設定檔
import random
import os
import time
from time import gmtime, strftime
from discord.ext import commands, tasks

with open('setting.json', 'r', encoding='utf8') as jfile:  # setting.json設定檔 'r'=讀取
    jdata = json.load(jfile)  # 呼叫jfile

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(">>機器人已啟動<<")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'讀取 {extension} 成功')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'卸載 {extension} 成功')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'重新載入 {extension} 成功')


@bot.command()
async def stop(ctx):
    await bot.logout()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['token'])
