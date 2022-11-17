import discord
from discord.ext import commands

import requests
import spotipy
import spotipy.util as util

client_id = '22dc1d51502945e58fcb78c2dbd73be0'
client_secret = '499aab7e66144e9fa70166be7c3b177b'
client_uri = 'https://www.google.com/'
scopes = 'user-modify-playback-state, user-read-currently-playing, playlist-modify-public'



class Spotify_Controller(commands.Cog):

    def __init__(self, client):
        self.client = client
        token = util.prompt_for_user_token('dryodaswag', scope=scopes, client_id=client_id, client_secret=client_secret, redirect_uri=client_uri)
        self.spotipyObject = spotipy.Spotify(auth=token)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Spotify_Controller is online.')

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
            await ctx.send('That playlist is not in your library. Please try again daddy.')
        else:
            self.spotipyObject.playlist_add_items(playlist_id=playlist_dict[playlist_name], items=song_uri_list)
            await ctx.send(f'Added {current_song_name} to {playlist_name}')


async def setup(client):
    await client.add_cog(Spotify_Controller(client))