import spotipy
import spotipy.util as util
from config import CLIENT_ID, CLIENT_SECRET, PLAY_LIST, USER
import random

token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

results1 = spotify.user_playlist_tracks(USER, PLAY_LIST, limit=100, offset=0)

