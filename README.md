# Spotifinder

Spotifinder is a song library that shows information about a song in a playlist created by user.
It generate data such as- song name, artist name, lyrics and the option to play the song on the application.

Link to app: <ins>https://spotifinder-core.herokuapp.com/

## Installation


```
# python3 -m venv venv              
# pip install -r requierments.txt
# flask run
```

## Technology Used

```
HTML
CSS
JAVASCRIPT
JQUERY
AJAX
PYTHON
FLASK
JINJA
WTFORMS
POSTGRESQL
SQLALCHEMY
HEROKU
```
## DataBase
 ![ ](https://raw.githubusercontent.com/AgamiLior/spotifinder-new/main/DB-Table.png "DB-Table") 

The database is pretty simple and by using certaing constraints with WTForms, and relationships between models.
Using Heroku addon (Postgresql) the app isn't using local database for it's users.
As one can see at the picture above, there are three tables that they all have relationship:
- Table users generate an ID (as his primary key), email, username, image, and password
- Table playlists generate an ID (as his primary key), title, and user_id (which considered as Foregin key as fetched from the users's table).
- Table songs generate and ID (as his primary key), song_title, song_artist, spotify_id and playlist_id (which considered as Foregin key fetched froim playlists's table).



## API used
![ ](https://raw.githubusercontent.com/AgamiLior/spotifinder-new/main/User%20Flow%20to%20Api.png "API")

<ins>(1) Lyric.ovh:</ins>
* <ins>https://lyricsovh.docs.apiary.io/#?ref=apilist.fun

API to retrieve the lyrics of a song.


<ins>(2) Spotify:</ins>
* <ins>https://developer.spotify.com/documentation/web-api/

Spotify for Developers to create or work with user's existing playlist.

You interact with the API to retrieve songs details such as - song name, song artist, song id.
In addition it finds the correct URL for the song to be added to the application and let the user play the song.

## How is it working (UI) 
![ ](https://raw.githubusercontent.com/AgamiLior/spotifinder-new/main/UI.png "UI")  

(1) Create user on Spotifinder page and Edit if necessary.   
(2) Create new playlists and insert songs to them.  
(3) Search for songs by title and artist name, find lyrics and gives the option to add to playlist.  
(4) interact with Spotify by playing your songs on the playlist's page and show their lyrics.



#### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



### Made By
![ ](https://raw.githubusercontent.com/AgamiLior/spotifinder-new/main/myLogo.png "myLogo") 