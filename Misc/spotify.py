import spotipy
import spotipy.util as util

scope = 'user-library-read'

token = util.prompt_for_user_token('snow3842', scope, client_id='1f72c8bc568548299a16cc7f66a3e054', client_secret='d0722932d263462f8c96a5138b28dc1f', redirect_uri ='http://localhost/')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit=50, offset=1)
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for snow3842")



'''
Client ID: 1f72c8bc568548299a16cc7f66a3e054
Client Secret: d0722932d263462f8c96a5138b28dc1f
'''