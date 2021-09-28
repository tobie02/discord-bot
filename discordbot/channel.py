import os
import random
import discord
import asyncio
import re
import datetime
import youtube_dl


from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.voice_client import VoiceClient
from urllib import parse, request
from discord.utils import get
from time import *



# CHANNEL COMMANDS

class Canal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        

    @commands.command(help="Entra al bot al canal de voz actual")      # JOIN CANAL
    async def join(self, ctx):
        channel = ctx.author.voice
        if channel:
            try:
                await channel.channel.connect() 
                await ctx.send("Entrando al canal de voz.")
            except:
                await ctx.send("No me llames si ya estoy en el canal de voz.")
        else:
            await ctx.send("Asegurate de estar en un canal de voz.")


    @commands.command(help="MuteAll (solo admins)")                     # MUTE ALL
    async def vcmute(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            vc = ctx.author.voice.channel
            for member in vc.members:
                await member.edit(mute=True)
        else:
            ctx.channel.send("No tienes poder para tal acción.")


    @commands.command(help="UnmuteAll (solo admins)")                       # UNMUTE ALL
    async def vcunmute(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            vc = ctx.author.voice.channel
            for member in vc.members:
                await member.edit(mute=False)
        else:
            ctx.channel.send("No tienes poder para tal acción.")