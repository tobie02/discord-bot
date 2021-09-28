# GENERAL COMMANDS

import os
import random
import discord
import asyncio
import re
import datetime
import youtube_dl
import calendar

from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.voice_client import VoiceClient
from urllib import parse, request
from discord.utils import get
from time import *


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

 
    @commands.command(name="botinfo", help="Muesta información relacionada con el bot")
    async def botinfo(self, ctx):
        icon = "https://cdn.discordapp.com/attachments/808701239143038996/818151908148772934/gatito.png"
        description = "Soy un bot desarrollado en Python 3 por @Tobie#1929. Un programa informático con un rol específico que opera en internet con comandos y funciones, haciendo tareas repetitivas, y aportando comodidad y control a los usuarios. Utiliza el comando >help para ver en que puedo ayudarte :)"
        embed=discord.Embed(title=" Gatito Bot  :smirk_cat:  :rose: ", description=description, color=discord.Color.lighter_gray())
        embed.set_thumbnail(url=icon)
        await ctx.channel.send(embed=embed)



    @commands.command(name="say", help='Generas una cadena que repite el bot. ej:>say hola que tal')        # SAY
    async def say(self, ctx, *, arg):
        member = ctx.message.author
        await ctx.message.delete()
        print(f"{member.name} asked to '{ctx.message.content}'")
        if ctx.message.channel.name == "console":
            channel = discord.utils.get(member.guild.channels, name="general")
            await channel.send(arg)
        else:
            await ctx.channel.send(arg)
    

     
    @commands.command(help="Embed MSG")
    async def emb(self, ctx, title, *, message):
        member = ctx.message.author
        emb = discord.Embed(title=title, description=f"{message}")
        print(f"{member.name} asked to '{ctx.message.content}'")
        await ctx.message.delete()
        if ctx.message.channel.name == "console":
            channel = discord.utils.get(member.guild.channels, name="general")
            await channel.send(embed=emb)
        else:
            await ctx.channel.send(embed=emb)
    


    @commands.command(pass_context=True, help="Obtiene la ID del canal actual")       # ID CANAL
    async def get_id(self, ctx):
        await ctx.send("Channel id: {}".format(ctx.message.channel.id))                




    @commands.command(name="youtube", help="Busca un video de Youtube")        # BUSQUEDA YOUTUBE
    async def youtube(self, ctx, *, search):
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
        print(search_results)
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
        



    @commands.command(name="clear", help="Elimina un número determinado de mensajes, ej: >clear 25")         # CLEAR DEL CHAT
    async def clear(self, ctx, limit: int=None):
        autor = ctx.message.author
        autorid = ctx.message.author.id
        if ctx.message.author.guild_permissions.manage_messages:
            passed = 0
            failed = 0
            async for msg in ctx.message.channel.history(limit=limit+1):
                try:
                    await msg.delete()
                    passed += 1
                except:
                    failed += 1
            await ctx.send(f"{passed-1} mensajes borrados a pedido de {autor}")
        else:
            await ctx.send("No tienes poder para tal acción.")
        print(f"[Complete] Removed {passed} messages with {failed} fails as {autor}{autorid} required")



    
    @commands.command(help="Clear del chat INSTANTANEO(solo OWNERS)(mensajes antiguos a 14 días)")      # PURGE DEL CHAT
    async def purge(self, ctx, num:int):
        if ctx.message.author.id == 209879067879669760 or ctx.message.author.id == 211649196724322307:
            await ctx.channel.purge(limit=num+1)
            await ctx.channel.send(f"{str(num)} mensajes **purgados** a pedido de {ctx.message.author.name}")
            print(f"PURGED {str(num)} messages as {ctx.message.author.name}{ctx.message.author.id} required")
        else:
            await ctx.send("No tienes poder aquí.")
            print(ctx.message.author.id)




    @commands.command(name="search", help='Busca varios videos de youtube: >search [cantidad de busquedas] ["busqueda"]')        # BUSQUEDA YOUTUBE
    async def search(self, ctx, num:int, search:str):
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
        print(search_results)
        yt = "https://www.youtube.com/watch?v="
        for i in range(num):
            searched = yt + search_results[i]
            await ctx.send(str(i+1) + ". " + searched)


    @commands.command(name="server", help="Muestra información del servidor")                  # SERVER INFO
    async def server(self, ctx):
        name = str(ctx.guild.name)
        description = "Servidor de LA PATRULLA forjado por los 4 principales y bueno negro nonono amumu full ap agarrame un huevo aca se juega todo y estamos re locos"

        created = str(ctx.guild.created_at)
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " - Información",
            description=description,
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Creación", value=created, inline=True)
        embed.add_field(name="País", value="Argentina", inline=True)
        embed.add_field(name="Miembros", value=memberCount, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Owners", value="Elian, Tobi, Leo, Mateo", inline=True)

        await ctx.send(embed=embed)

    
    @commands.command(help="Realiza una votacion")                             # VOTACION
    async def vote(self, ctx, *, message):
        emb=discord.Embed(title=" VOTACION", description=f"{message}")
        msg=await ctx.channel.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')


    @commands.command(help="Calendario por si estas perdido")
    async def calendar(self, ctx, y, m):
        cal = calendar.month(int(y), int(m))
        emb = discord.Embed(title="Calendar", description=f"{cal}")
        msg = await ctx.channel.send(embed=emb)
        print(cal)
