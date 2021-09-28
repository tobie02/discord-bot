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
from urllib import parse, request
from discord.utils import get
from time import *


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(help="Meme de gatito")
    async def gatito(self, ctx):
        image = "https://cdn.discordapp.com/attachments/651665041422024707/760564712924250142/65alc5tvvqm51.png"
        phrase = "Miau Miau xd"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="burrito", help="Pass the burrito down")   # BURRITO
    async def burrito(self, ctx):
        image = "https://media.discordapp.net/attachments/808701239143038996/808702169069912064/burrito.gif" + "\n"
        for i in range(3):
            await ctx.send(image)
    @commands.command(name="tobi", help="Meme de Tobi")   # TOBI
    async def tobi(self, ctx):
        image = "https://media.discordapp.net/attachments/808701239143038996/808702239052922890/20201213_152709.jpg?width=380&height=676"
        phrase = "Soy vegana"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="elian", help="Meme de Elian")   # ELIAN
    async def elian(self, ctx):
        image = "https://media.discordapp.net/attachments/808701239143038996/808702202738769982/asdfdfasdfas.png"
        phrase = "Me voy a hacer una leche"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="mateo", help="Meme de Mateo")   # MATEO
    async def mateo(self, ctx):
        image = "https://cdn.discordapp.com/attachments/808701239143038996/808703772565438465/cc25effe-911c-4489-ba1e-b58a90c7c03e.jpg"
        phrase = "DAAALE VIEJO SE FUMA LAS BAAALAAAS"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="leo", help="Meme de Leo")     # LEO
    async def leo(self, ctx):
        image = "https://media.discordapp.net/attachments/808701239143038996/808702223394930688/81368d02-399f-4e0d-a057-169dd6417f47.jpg?width=380&height=676"
        phrase = "Daaaa como hizo eso? Tshh Tshh"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="blodi", help="Meme de Blodi")   # BLODI
    async def blodi(self, ctx):
        image = "https://media.discordapp.net/attachments/808701239143038996/808702212154196018/d1c5605b82d3b47aee12be1e4befd74f.png"
        phrase = "Y bueno negro"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="rama", help="Meme de Rama")    # RAMA
    async def rama(self, ctx):
        image = "https://media.discordapp.net/attachments/808701239143038996/808703763396427836/12592285_184781848544332_6015410344180830709_n.png?width=676&height=676"
        phrase = "Hace lo que se te cante leo libre de hacer lo que se te cante el ogt"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="peter", help="Meme de peter")    # blodi 2
    async def rama(self, ctx):
        image = "https://cdn.discordapp.com/attachments/808701239143038996/883470097400885289/IMG-20190924-WA0033.jpg"
        phrase = "Hola Peter"
        await ctx.send(image)
        await ctx.send(phrase)
    @commands.command(name="zurdo", help="Meme del zurdo")    # zurdo
    async def zurdo(self, ctx):
        image = "https://cdn.discordapp.com/attachments/808701239143038996/883471659288391740/IMG-20191222-WA0078.jpg"
        phrase = "Mmmmm este huele raro eh"
        await ctx.send(image)
        await ctx.send(phrase)