
import discord
from discord.ext import commands
import os
import asyncio
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '.', intents=intents)
token = 'MTA0MjYwOTQ2MTM4ODM4MjI3OA.GB9v7f.359QyEbPSZhSXzPWOfxFokiVsWqrJEB9UGy4Os'

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
    await client.login(token)
    await client.start(token)

asyncio.run(main())