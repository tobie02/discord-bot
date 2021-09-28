import os
import random
import discord
import asyncio
import re

from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.voice_client import VoiceClient
from discord.utils import get
from time import *

class Tateti():

    global tablero
    global turno
    global ganador
    global terminado
    global contenido
    tablero = [":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":nine:"]
    turno = ':x:'
    ganador = ''
    terminado = False
    contenido = ''

    def __init__(self):
        self.tablero = [":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":nine:"]
        self.turno = ':x:'
        self.ganador = ''
        self.terminado = False

    def mostrar(self):
        mostrar = f"{self.tablero[0]} {self.tablero[1]} {self.tablero[2]}\n{self.tablero[3]} {self.tablero[4]} {self.tablero[5]}\n{self.tablero[6]} {self.tablero[7]} {self.tablero[8]}"
        return mostrar

    def proximo_turno(self):
        return self.turno

    def contenido(self, indice):
        return self.tablero[indice]

    def jugada(self, indice):
        if self.terminado == True:
            return f"El juego ya terminó :)"
        elif indice < 0 or indice > 8:
            return f"La posición {indice+1} está fuera del tablero"
        elif contenido(self, indice) == ":x:" or contenido(self, indice) == ":o:":
            return f"Esa posición ya se jugó"

        self.tablero[indice] = self.turno

        self.verificar_terminado()

        jugo = f"Jugó {self.turno}\n"

        if self.terminado == False:
            if self.turno == ':x:':
                self.turno = ':o:'
            else:
                self.turno = ':x:'
        
        return jugo

    def verificar_terminado(self):
        for i in range(0,7,3):
            # verifica horizontal
            if (self.tablero[0 + i] == self.tablero[1 + i] == self.tablero[2 + i]) and (self.tablero[2 + i] == ':x:' or self.tablero[2 + i] == ':o:'):
                self.ganador = self.tablero[0 + i]
                self.terminado = True 
        for i in range(0,3):
            # verifica vertical
            if (self.tablero[0 + i] == self.tablero[3 + i] == self.tablero[6 + i]) and (self.tablero[0 + i] == ':x:' or self.tablero[0 + i] == ':o:'):
                self.ganador = self.tablero [0 + i]
                self.terminado = True
            # verifica diagonal uno
        if (self.tablero[0] == self.tablero[4] == self.tablero[8]) and (self.tablero[0] == ':x:' or self.tablero[0] == ':o:'):
            self.ganador = self.tablero[0]
            self.terminado = True
            # verifica diagonal dos
        if (self.tablero[2] == self.tablero[4] == self.tablero[6]) and (self.tablero[2] == ':x:' or self.tablero[0] == ':o:'):
            self.ganador = self.tablero[2]
            self.terminado = True

        cont = 0
        for i in range(0,9):
            if self.tablero[i] != ':x:' and self.tablero[i] != ':o:':
                cont = cont + 1
        
        if cont == 0 and terminado == False:
            self.ganador = 'nadie :man_facepalming:'
            self.terminado = True
            
    def terminado(self):
        return self.terminado

    def ganador(self):
        if self.terminado == False:
            return
        return self.ganador
