# bot.py
import os
import random
import discord
import asyncio
import re
import datetime
import youtube_dl

from general import General
from memes import Memes
from num import Numeros
from channel import Canal
from clasetat import Tateti
from users import Users

from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.voice_client import VoiceClient
from urllib import parse, request
from discord.utils import get
from time import *

intents = discord.Intents.all()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
help_command = commands.DefaultHelpCommand(no_category = "Ayuda")
bot = commands.Bot(command_prefix=[">","?"], intents = intents, help_command = help_command, description="Hi")
voice = discord.VoiceChannel



# GENERAL ON EVENT


@bot.event
async def on_ready():
    act = discord.Activity(type=discord.ActivityType.listening, name=">help or @Tobie")
    await bot.change_presence(status=discord.Status.online, activity=act)
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    print(f"{member.name} has joined {member.guild.name}")
    response = [f"Bienvenid@ {member.mention}! :)", f"{member.mention} entró al servidor.", f"{member.mention} cayó al servidor :thinking:"]
    for i in range(3):
        r = random.choice(response)
    await channel.send(r)

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    print(f"{member.name} left the server")
    await channel.send(f"{member.mention}({member.name}) dejó el servidor.")

@bot.event
async def on_reaction_add(reaction, user):
    Channel = bot.get_channel(member.guild.channels, name="info")
    if reaction.message.channel.id != Channel:
        return
    else:
        await bot.add_roles(user, role)  




# ON MESSAGE EVENTS

preguntas = 0

@bot.listen("on_message")                    # SI / NO ANSWERS
async def on_message(message):
    global preguntas
    if message.author == bot.user:
        return
    message.content = message.content.lower()
    if message.content.startswith("gatito") or message.content.endswith("gatito?"):
        if message.content.endswith("?"):
            if preguntas >= 3:
                await message.channel.send("No me rompan más las bolas.")
                preguntas = 0
            else:
                lista = ["Si", "No"]
                al = random.choice(lista)
                await message.channel.send(al)
                preguntas += 1



@bot.listen("on_message")
async def on_message(message):
    if message.channel.name == "general":
        print(f"        {message.guild.name} - {message.author.name}: {message.content}")
    


@bot.listen("on_message")              # MSGEVENT1
async def on_message(message):
    if message.author == bot.user:
        return
    message.content = message.content.lower()
    if message.content == "hola gatito":
        response = f"Hola {message.author.name}! :)"
        await message.channel.send(response)


@bot.listen("on_message")              # MSGEVENT2
async def on_message(message):
    if message.author == bot.user:
        return
    message.content = message.content.lower()
    if message.content == "chau gatito":
        response = f"Chau {message.author.name}! ໒(ᵔᴥᵔ)७"
        await message.channel.send(response)


@bot.listen("on_message")               # MSGEVENT3
async def on_message(message):
    if message.author == bot.user:
        return
    message.content = message.content.lower()
    if "anda a cagar gatito" in message.content:
        response = f"y vos chupame un huevo {message.author.name} ಠ_ಠ"
        await message.channel.send(response)
 

@bot.listen("on_message")                     # FILTRADOR
async def on_message(message):
    if message.author == bot.user:
        return
    message.content = message.content.lower()
    if "https://discord.gg/" in message.content and message.author.name != "Tobie":
        await message.delete()
        print(f"deleted spam message from {message.author.name}")
        print(f"message: {message.content}")
        response = f"Nada de spam {message.author.mention} ಠ_ಠ"
        await message.channel.send(response)





# REACTROLE EVENT

@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    member = payload.member
    if message_id == 821502204728967188 or 821507847853441025:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == "Minecraft":
            role = get(member.guild.roles, name="Minecraft")
            await member.add_roles(role, reason=None, atomic=True)

        elif payload.emoji.name == "LeagueofLegends":
            role = get(member.guild.roles, name="LeagueofLegends")
            await member.add_roles(role, reason=None, atomic=True)
        elif payload.emoji.name == "Valorant":
            role = get(member.guild.roles, name="Valorant")
            await member.add_roles(role, reason=None, atomic=True)
        elif payload.emoji.name == "CSGO":
            role = get(member.guild.roles, name="CSGO")
            await member.add_roles(role, reason=None, atomic=True)
        elif payload.emoji.name == "RocketLeague":
            role = get(member.guild.roles, name="RocketLeague")
            await member.add_roles(role, reason=None, atomic=True)

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            if member is not None:
                await member.add_roles(role)
                print(f"{member.name} added himself {role.name} role.")
            else: print("Void member.")
        else:
            print("Void role")

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    guild = await bot.fetch_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    if message_id == 821502204728967188:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == "Minecraft":
            role = get(member.guild.roles, name="Minecraft")
            await member.remove_roles(role, reason=None, atomic=True)

        elif payload.emoji.name == "LeagueofLegends":
            role = get(member.guild.roles, name="LeagueofLegends")
            await member.remove_roles(role, reason=None, atomic=True)
        elif payload.emoji.name == "Valorant":
            role = get(member.guild.roles, name="Valorant")
            await member.remove_roles(role, reason=None, atomic=True)
        elif payload.emoji.name == "CSGO":
            role = get(member.guild.roles, name="CSGO")
            await member.remove_roles(role, reason=None, atomic=True)
        elif payload.emoji.name == "RocketLeague":
            role = get(member.guild.roles, name="RocketLeague")
            await member.remove_roles(role, reason=None, atomic=True)

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            if member is not None:
                await member.remove_roles(role)
                print(f"{member.name} removed himself {role.name} role.")
            else: print("Void member.")
        else:
            print("Void role.")


# MUSICA


class Musica(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    search1 = ""
    search2 = ""
    search3 = ""
    search4 = ""
    search5 = ""
    global alreadySearched
    global alreadyPlaying
    alreadyPlaying = False
    alreadySearched = False
    urlsearch = False
    



    @commands.command(help='Busca y reproduce una cancion en el canal actual >play "cancion" >play 2')                                      # PLAY COMMAND
    async def play(self, ctx, *, search : str):
        global alreadySearched
        global alreadyPlaying
        global urlsearch
        global search1
        global search2
        global search3
        global search4
        global search5
        urlsearch = False
        try:
            if "www.youtube.com/" in search:
                alreadySearched = True
                urlsearch = True
            if not alreadySearched:
                query_string = parse.urlencode({'search_query': search})
                html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
                search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
                print(search_results)
                yt = "https://www.youtube.com/watch?v="
                search1 = yt + search_results[0]
                search2 = yt + search_results[1]
                search3 = yt + search_results[2]
                search4 = yt + search_results[3]
                search5 = yt + search_results[4]
                await ctx.send("1. " + search1)
                await ctx.send("2. " + search2)
                await ctx.send("3. " + search3)
                await ctx.send("4. " + search4)
                await ctx.send("5. " + search5)
                alreadySearched = True
                return


            elif alreadyPlaying:
                await ctx.send("Ya se está reproduciendo algo, prueba >stop antes de >play.")


            else:
                if search.startswith("1"):
                    url = search1
                elif search.startswith("2"):
                    url = search2
                elif search.startswith("3"):
                    url = search3
                elif search.startswith("4"):
                    url = search4
                elif search.startswith("5"):
                    url = search5
                else:
                    url = search

                song_there = os.path.isfile("song.mp3")
                try:
                    if song_there:
                        os.remove("song.mp3")
                except PermissionError:
                    await ctx.send("Espera que termine la cancion actual, o usa el comando '>stop'")
                    return

                voiceChannel=ctx.message.author.voice.channel
                try:
                    await voiceChannel.connect()
                except:
                    print("Already connected")
                if not urlsearch:
                    await ctx.channel.purge(limit=6)
                voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)


                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        name = file
                        os.rename(file, "song.mp3")
                await ctx.send(f"Reproduciendo **{name}**")
                voice.play(discord.FFmpegPCMAudio("song.mp3"))
                alreadySearched = False
        except:
            await ctx.send("Error de conexión x.x")
            




    @commands.command(help="Termina con la canción actual.")                                         # STOP COMMAND
    async def stop(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        voice.stop()





    @commands.command(help="Pausa la canción.")                                       # PAUSE COMMAND
    async def pause(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        try:
            voice.pause()
        except:
            await ctx.send("El bot no está reproduciendo nada.")





    @commands.command(help="Despausa la canción.")                                        # RESUME COMMAND
    async def resume(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        try:
            voice.resume()
        except:
            await ctx.send("El bot no está pausado.")





    @commands.command(help="Retira al bot del canal.")                                      # LEAVE COMMAND
    async def leave(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        try:
            await voice.disconnect()
        except:
            await ctx.send("El bot no esta en un canal de voz.")

       
# TATETI

class Tateticog(commands.Cog):
    global tablero
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tateti", help="Iniciar un tablero TaTeTi")
    async def tateti(self, ctx):
        global tablero
        tablero = Tateti()
        await ctx.channel.send(tablero.mostrar())
  
    @commands.command(name="tat", help="Movimiento en el tablero TaTeTi")
    async def tat(self, ctx, indice: int):
        await ctx.channel.send(tablero.jugada(indice-1))
        await ctx.channel.send(tablero.mostrar())
        tablero.verificar_terminado()
        if tablero.terminado:
            await ctx.channel.send(f"Ganador: {tablero.ganador} *ඞ ඞ ඞ*")


bot.add_cog(General(bot))
bot.add_cog(Musica(bot))
bot.add_cog(Canal(bot))
bot.add_cog(Users(bot))
bot.add_cog(Numeros(bot))
bot.add_cog(Memes(bot))
bot.add_cog(Tateticog(bot))

bot.run(TOKEN)
