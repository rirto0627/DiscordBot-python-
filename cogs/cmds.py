import discord
import time
import os
from discord.ext import commands


class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=1000):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def cls(self, ctx):
        os.system('cls')

    @commands.command()
    async def about(ctx):
        em = discord.Embed(color=discord.Color.green())
        em.title = '機器人資訊'
        em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        try:
            em.description = bot.psa + '\n[伺服器連結](https://discord.gg/Q5ruvyK)'
        except AttributeError:
            em.description = '\n[伺服器連結](https://discord.gg/Q5ruvyK)'
        em.add_field(name="伺服器機器人數量", value=len(bot.guilds))
        em.add_field(name="線上人數",
                     value=str(len({m.id for m in bot.get_all_members() if m.status is not discord.Status.offline})))
        em.add_field(name='總人數', value=len(bot.users))
        em.add_field(name='頻道', value=f"{sum(1 for g in bot.guilds for _ in g.channels)}")
        em.add_field(name="機器人延遲", value=f"{bot.ws.latency * 1000:.0f} ms")

        em.set_footer(text="設計者:熊熊 | 請多多指教")
        await ctx.send(embed=em)

    @commands.command()
    async def move(self, ctx, source, target):
        voiceChannels = ctx.guild.voice_channels
        for voiceChannel in voiceChannels:
            if str(voiceChannel.id) == source:
                sourceChannel = voiceChannel
            if str(voiceChannel.id) == target:
                targetChannel = voiceChannel
        for member in sourceChannel.members:
            await member.move_to(targetChannel)


def setup(bot):
    bot.add_cog(cmds(bot))
