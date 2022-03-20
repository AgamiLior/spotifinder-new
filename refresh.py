import requests
spotify_token = "BQAdcXCG5G7yv5lfVaLDXd2fJM-uQ6ObH9pl6WW6t5nvekViilv1drMhF6ZxF4JcBLitq2jzihnSb5QW3Z24h4jUMs9Jbc4IHHYTeymUeVsJ3KTsooGTYcIOIViCe0Z542uRMzt6crBH8VfP8qqtroJapEqCP0TxNkiwc39CO2jnT6a3hXyyOBVFkg"
refresh_token = "AQBQPWjpz6HR3N150jH16p7Ij0YP1JOWiIOP5Ga_LbKf8nI5RnjKFIwH173NNdhAQub3OnyDC1kxVYw2ePQhr6BBKgMyrev0Z4YuqZ9woNy2Ja_WISL1NAdD0mow2rGxkfo"
base_64 = 'OWNlZDQwOWI2NmRjNDJkYWE5ZWI2NTI1NDUzOTFmNzQ6ODZlYWM0MGZjOGZjNGNjZDg5M2I0YjhmODA5NmJiYmU='



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

