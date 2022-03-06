from flask import Flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
app = Flask(__name__)


app.secret_key = 'Randomm'
app.config['SEESION_COOKIE_NAME'] = 'Jasons Cookie'
TOKEN_INFO = "token_info"



def index():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    print


def getToken():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    print (token_info)
    session[TOKEN_INFO] = token_info
    print (token_info)
    
    
def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = '9ced409b66dc42daa9eb652545391f74',
        client_secret = '86eac40fc8fc4ccd893b4b8f8096bbbe',
        redirect_uri = 'http%3A%2F%2F127.0.0.1%3A5000%2F',
        scope = "user-library-modify")

# app.route('/searchSong')
# def search_song():
#     try:
#         token_info = get_token()
#     except:
#         print('user not logged in')
#         redirect("/something")
#     sp = spotipy.Spotipy(auth=token_info['access_token'])
#     return (sp.current_user_saved_tracks)
# def get_token():
#     token_info = session.get(TOKEN_INFO, None)
#     if not token_info:
#         raise "exception"
#     now = int(time.time())
#     is_expired = token_info['expires_at'] - now < 60
#     if (is_expired):
#         sp_oauth = create_spotify_oauth()
#         token_info = sp_oauth.refesh_access_token(token_info['refresh_token'])
#     return token_info
#     return 'API OAUTH'



        
        
        
# http%3A%2F%2F127.0.0.1%3A5000%2F
# user-library-modify

# https://accounts.spotify.com/authorize?client_id=9ced409b66dc42daa9eb652545391f74&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2F&scopes=user-library-modify

# curl -H "Authorization: Basic OWNlZDQwOWI2NmRjNDJkYWE5ZWI2NTI1NDUzOTFmNzQ6ODZlYWM0MGZjOGZjNGNjZDg5M2I0YjhmODA5NmJiYmU=" -d grant_type=authorization_code -d code=MQCbyKe...44KN -d redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2F https://accounts.spotify.com/api/token

