import discord
import json
import os
import time
import json
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import Bot


with open('setting.json', 'r', encoding='utf8') as jfile:  # setting.json設定檔 'r'=讀取
    jdata = json.load(jfile)  # 呼叫jfile


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# 主要身分組分類
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        bot = self.bot
        message_id = payload.message_id
        if message_id == int(jdata['msg_id']):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

            if payload.emoji.name == (jdata['emoji1']):
                role = discord.utils.get(guild.roles, name=(jdata['role1']))
            elif payload.emoji.name == (jdata['emoji2']):
                role = discord.utils.get(guild.roles, name=(jdata['role2']))
            elif payload.emoji.name == (jdata['emoji3']):
                role = discord.utils.get(guild.roles, name=(jdata['role3']))
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    with open(f'log/rolelog.txt', 'a', encoding='UTF-8') as f:
                        f.write(f'{member}-->成功授予'f'『{role}』身分組\n')
                    print(f'{member}-->成功授予'f'『{role}』身分組')
                else:
                    print("沒有找到成員")
            else:
                print("身分組沒找到")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        bot = self.bot
        message_id = payload.message_id
        if message_id == int(jdata['msg_id']):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

            if payload.emoji.name == (jdata['emoji1']):
                role = discord.utils.get(guild.roles, name=(jdata['role1']))
            elif payload.emoji.name == (jdata['emoji2']):
                role = discord.utils.get(guild.roles, name=(jdata['role2']))
            elif payload.emoji.name == (jdata['emoji3']):
                role = discord.utils.get(guild.roles, name=(jdata['role3']))
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    with open(f'log/rolelog.txt', 'a', encoding='UTF-8') as f:
                        f.write(f'{member}-->成功移除'f'『{role}』身分組\n')
                    print(f'{member}-->成功移除'f'『{role}』身分組')
                else:
                    print("沒有找到成員")
            else:
                print("身分組沒找到")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        embed = discord.Embed(
            title="-------------------------使用者資料-------------------------", color=0x57EEE6)
        embed.add_field(name="使用者帳號", value=str(member), inline=True)
        embed.add_field(name="使用者暱稱", value=str(
            member.display_name), inline=True)
        embed.add_field(name="加入日期", value=str(
            member.joined_at.strftime("%Y-%m-%d %H:%M:%S")), inline=True)
        if str(member.status) == 'online':
            a = '線上'
        elif str(member.status) == 'idle':
            a = '閒置'
        elif str(member.status) == 'dnd':
            a = '請勿打擾'
        elif str(member.status) == 'offline':
            a = '隱形/下線'
        embed.add_field(name="使用者狀態", value=str(a), inline=True)
        embed.set_author(name=member, icon_url=member.avatar_url)
        await channel.trigger_typing()
        time.sleep(1)
        await channel.send(f'>歡迎<{member} 加入伺服器')
        await channel.send(embed=embed)
        with open(f'log/joinlog.txt', 'a', encoding='UTF-8') as f:
                        # f.write('使用者帳號\t使用者暱稱\t加入日期\n')
            f.write(
                f'{member}\t{member.display_name}\t{time.strftime("%Y-%m-%d", time.localtime())}\n')
        await channel.send('-------------------------分隔線-------------------------')

        with open("伺服器規章.txt", "r", encoding='utf8') as f:  # 開啟檔案
            data = f.read()  # 讀取檔案
            channel = await member.create_dm()
            await channel.send(data)
        print(f'{member} 已經加入伺服器')

    @commands.Cog.listener() 
    async def on_message(self, message):
        if message.author != self.bot.user:
            key = ['幹', '靠']
            for k in key:
                if k in message.content:
                    await msg.channel.send('請勿罵髒話!')
            if message.channel.id == 680097937954832471:
                if "Accept" in message.content:
                    role = discord.utils.get(message.guild.roles, name="成員")
                    await message.author.add_roles(role)
                    await message.delete()

                    channel = self.bot.get_channel(int(jdata['check_channel']))
                    embed = discord.Embed(
                        title="-------------------------使用者資料-------------------------", color=0x57EEE6)
                    embed.add_field(name="使用者帳號", value=str(message.author), inline=True)
                    embed.add_field(name="使用者暱稱", value=str(
                        message.author.display_name), inline=True)
                    embed.add_field(name="加入日期", value=str(
                        message.author.joined_at.strftime("%Y-%m-%d %H:%M:%S")), inline=True)
                    if str(message.author.status) == 'online':
                        a = '線上'
                    elif str(message.author.status) == 'idle':
                        a = '閒置'
                    elif str(message.author.status) == 'dnd':
                        a = '請勿打擾'
                    elif str(message.author.status) == 'offline':
                        a = '隱形/下線'
                    embed.add_field(name="使用者狀態", value=str(a), inline=True)
                    embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                    await channel.trigger_typing()
                    time.sleep(1)
                    await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))
