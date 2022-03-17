from urllib import response
from wsgiref import headers
import requests
import urllib.parse
from flask import flash
from refresh import Refresh


class SpotifyClient(object):
    def __init__(self):
        self.spotify_token = ""

    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        response_json = response.json()     
        results = response_json['tracks']['items']
        if results:
            return results[0]['id']
        else:
            flash(f"No Song found for {artist} = {track}")
        
        
    def call_refresh(self):
                
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()

    
    