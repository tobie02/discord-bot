import os
import random
import discord
import asyncio
import re
import datetime

from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.voice_client import VoiceClient

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='kickear un usuario')
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            await member.kick(reason=reason)
            if ctx.message.channel.name == 'console':
                channel = discord.utils.get(member.guild.channels, name='general')
                await channel.send(f'{member.name} ha sido expulsad@.')
            else:
                await ctx.channel.send(f'{member.name} ha sido expulsad@.')