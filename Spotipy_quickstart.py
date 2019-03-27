import spotipy
from spotipy import oauth2
from pprint import pprint

client_ID = 'e9ddaa3b0c35491b8ab175459ccdf2fe'
client_secret = '074f6e3ddfe34b74a35985161ba264c1'

auth = oauth2.SpotifyClientCredentials\
    (client_id = client_ID, client_secret =client_secret)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)

results = spotify.search(q='artist:shakira', type='artist')
#pprint(dir(spotify))
pprint(results)


# import random
#
# token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
#
# cache_token = token.get_access_token()
# spotify = spotipy.Spotify(cache_token)
#
# results1 = spotify.user_playlist_tracks(USER, PLAY_LIST, limit=100, offset=0)
#
# 81
# ddca1ee4774aa5bd5343beec81c8f1

