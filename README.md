###################################################################################
# spotifinder-new
###################################################################################

Techonology used -

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

###################################################################################

The Webapp -
Spotifinder is a song library that shows information about a song in a playlist created by user.
It generate data such as- song name, artist name, lyrics and the option to play the song on the application.

###################################################################################
How to run the app - 

python3 -m venv venv              
pip install -r requierments.txt
flask run

###################################################################################

DataBase (table) -

The database is pretty simple and by using certaing constraints with WTForms, and relationships between models. 

###################################################################################
API used (User Flow to Api)-
 
# https://lyricsovh.docs.apiary.io/#?ref=apilist.fun

(1) Lyric.ovh: 

Simple API to retrieve the lyrics of a song.


(2) Spotify:

# https://developer.spotify.com/documentation/web-api/

Spotify for Developers to create or work with user's exsiting playlist.

In this webapp you interact with the API to retrive songs details such as - song name, song artist, song id.
In adition if finds the correct URL for the song to be added to the Webapp and let the user play it.


###################################################################################
How is it working (UI) -

(1) Create user on Spotifinder page and Edit if necessery.
(2) Create new playlists and insert songs to them.
(3) Search for songs by title and artist name, find lyrics and gives the option to add to playlist.
(4) interact with Spotify by playing your songs on the playlist's page and show their lyrics.
