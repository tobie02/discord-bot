
# NUMEROS

import os
import random
import discord
import asyncio
import re
import datetime

from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from time import *



class Numeros(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="roll", help="Genera números aleatorios: >roll desde hasta cuantos.ej:>roll 1 10 2")      # ROLL DE NUM ALEATORIO
    async def roll(self, ctx, desde_el: int, hasta_el: int, veces: int):
        dice = [
            str(random.choice(range(desde_el, hasta_el + 1)))
            for _ in range(veces)
        ]
        await ctx.send(', '.join(dice))


    #   CALCULADORA

    @commands.command(help="Suma dos números")
    async def sum(self, ctx, numOne: int, numTwo: int):
        await ctx.send(numOne + numTwo)

    @commands.command(help="Resta dos números")
    async def res(self, ctx, numOne: int, numTwo: int):
        await ctx.send(numOne - numTwo)

    @commands.command(help="Multiplica dos números")
    async def mul(self, ctx, numOne: int, numTwo: int):
        await ctx.send(numOne * numTwo)

    @commands.command(help="Divide dos números")
    async def div(self, ctx, numOne: int, numTwo: int):
        await ctx.send(numOne / numTwo)