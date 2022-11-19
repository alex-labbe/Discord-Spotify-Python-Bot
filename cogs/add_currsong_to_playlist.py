import discord
from discord.ext import commands

import requests
import spotipy
import spotipy.util as util

client_id = '22dc1d51502945e58fcb78c2dbd73be0'
client_secret = '499aab7e66144e9fa70166be7c3b177b'
client_uri = 'https://www.google.com/'
scopes = 'user-modify-playback-state, user-read-currently-playing, playlist-modify-public, user-read-playback-state, user-modify-playback-state'



class Spotify_Controller(commands.Cog):

    def __init__(self, client):
        self.client = client
        token = util.prompt_for_user_token('dryodaswag', scope=scopes, client_id=client_id, client_secret=client_secret, redirect_uri=client_uri)
        self.spotipyObject = spotipy.Spotify(auth=token)
        


    @commands.Cog.listener()
    async def on_ready(self):
        print('Spotify_Controller is online.')
       #user = await self.client.fetch_user('User id')
        #await user.send('What is your spotify username?')
        #text_channel_list = []
        #for server in self.client.servers:
        #    for channel in server.channels:
        #        if channel.type == 'Text':
        #            text_channel_list.append(channel)
        
        #username = await self.client.wait_for('message')
        #token = util.prompt_for_user_token(username.content, scope=scopes, client_id=client_id, client_secret=client_secret, redirect_uri=client_uri)
        #self.spotipyObject = spotipy.Spotify(auth=token)

    @commands.command()
    async def add_curr(self, ctx, *, playlist_name):
        #initalize list of song uris to add to playlist (only going to be one song)
        song_uri_list = []
        #get current song
        current_song = self.spotipyObject.current_user_playing_track()
        #append uri to song uri list
        song_uri_list.append(current_song['item']['uri'])
        #store the name
        current_song_name = current_song['item']['name']

        #get a dict of all playlists
        playlists = self.spotipyObject.current_user_playlists()
        playlist_dict = {}
        for playlist in playlists['items']:
            playlist_dict[playlist['name']] = playlist['id']

        if playlist_name not in playlist_dict:
            #not a playlist in your library
            await ctx.send('That playlist is not in your library. Please try again.')
        else:
            self.spotipyObject.playlist_add_items(playlist_id=playlist_dict[playlist_name], items=song_uri_list)
            await ctx.send(f'Added {current_song_name} to {playlist_name}')

    @commands.command()
    async def pause(self, ctx):
        #get current playback information
        playback = self.spotipyObject.current_playback()
        #if music is playing, pause the playback.
        if playback is None:
            await ctx.send('There is no music playing to be paused.')
        elif playback['is_playing']:
            self.spotipyObject.pause_playback()
            await ctx.send('Paused your music!')
    
    @commands.command()
    async def skip(self, ctx):
        #skip to next track
        self.spotipyObject.next_track()
        await ctx.send('Skipped!')



async def setup(client):
    await client.add_cog(Spotify_Controller(client))