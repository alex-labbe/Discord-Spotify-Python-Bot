#MTA0MjYwOTQ2MTM4ODM4MjI3OA.GajtpU.5fABMBZx9CSjLBMGfJs3x3bbhAVo6tVdEw48Js

import discord
from discord.ext import commands
import os
import asyncio
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '.', intents=intents)
"""
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
"""
@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await client.login('MTA0MjYwOTQ2MTM4ODM4MjI3OA.GajtpU.5fABMBZx9CSjLBMGfJs3x3bbhAVo6tVdEw48Js')
    await client.start('MTA0MjYwOTQ2MTM4ODM4MjI3OA.GajtpU.5fABMBZx9CSjLBMGfJs3x3bbhAVo6tVdEw48Js')

asyncio.run(main())
#anclient.run('MTA0MjYwOTQ2MTM4ODM4MjI3OA.GajtpU.5fABMBZx9CSjLBMGfJs3x3bbhAVo6tVdEw48Js')