from secrets import refresh_token, base_64
import requests




class Refresh:
    
    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64
        
        
    def refresh(self):

        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                data={"grant_type": "refresh_token",
                                    "refresh_token": refresh_token},
                                headers={"Authorization": "Basic " + base_64})
        
        res = response.json()
        SPOTIFY_AUTH_TOKEN =  res["access_token"]
        return SPOTIFY_AUTH_TOKEN


# a = Refresh()
# a.refresh()

