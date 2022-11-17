import discord
from discord.ext import commands

class Basics(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
        #print(self.client.latency)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! Your ping is {round(self.client.latency * 1000)}')

async def setup(client):
    await client.add_cog(Basics(client))