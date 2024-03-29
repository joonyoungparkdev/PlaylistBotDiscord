# Joon Bot

import discord
import os
import json
import requests
import builtins

from discord.ext import commands
from discord.utils import get
from discord import Spotify
from secrets import spotify_token, spotify_user_id, discord_token

client = commands.Bot(command_prefix='.')


# ex: '.load example'
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded!')


# ex: '.unload example'
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded!')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded!')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(discord_token)
