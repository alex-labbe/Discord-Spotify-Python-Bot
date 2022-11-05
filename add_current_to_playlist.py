import requests
import spotipy
import spotipy.util as util

client_id = '22dc1d51502945e58fcb78c2dbd73be0'
client_secret = '499aab7e66144e9fa70166be7c3b177b'
client_uri = 'https://www.google.com/'
scopes = 'user-modify-playback-state, user-read-currently-playing, playlist-modify-private, playlist-modify-public'

token = util.prompt_for_user_token('dryodaswag', scope=scopes, client_id=client_id, client_secret=client_secret, redirect_uri=client_uri)

spotipyObject = spotipy.Spotify(auth=token)
def add_current_to_playlist(spotipyObject):
    song_uri_list = []
    current_song = spotipyObject.current_user_playing_track()
    song_uri_list.append(current_song['item']['uri'])
    current_song_name = current_song['item']['name']

    playlists = spotipyObject.current_user_playlists()
    playlist_dict = {}
    for playlist in playlists['items']:
        playlist_dict[playlist['name']] = playlist['id']

    name = ''

    while True:
        print('What playlist would you like to add your currently playing song to? (enter \'list\' to see a list of your playlists (up to most recent 50)) ')
        name = input()
        if name == 'list':
            list_of_names = ''
            for playlist in playlist_dict.keys():
                list_of_names += playlist+', '
            print(list_of_names)
        if name != 'list':
            break


    playlist_uri = playlist_dict[name]

    spotipyObject.playlist_add_items(playlist_id=playlist_uri, items=song_uri_list)
    print(f'Added {current_song_name} to {name}')

if __name__ == '__main__':
    add_current_to_playlist(spotipyObject=spotipyObject)
