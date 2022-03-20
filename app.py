import os
from flask import Flask, render_template, flash, redirect, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
from spotify_client import SpotifyClient
import re

from forms import *
from models import *

CURR_USER_KEY = "curr_user"
app = Flask(__name__)

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    uri, 'postgresql:///spotifinder')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)


##############################################################################
# User signup/login/logout


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""
    session[CURR_USER_KEY] = user.id

def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                image_url=form.image_url.data or User.image_url.default.arg,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)
        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()
    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            return redirect('/')

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""
    do_logout()
    return redirect("/")
    # IMPLEMENT THIS

##############################################################################
#Playlists and Songs

"""Shows song in a specific playlist"""
@app.route('/users/<int:user_id>/playlists/<int:playlists_id>', methods=["GET","POST"])

def add_song_to_playlist(user_id,playlists_id):
    if not g.user:
        flash("No Access!", "danger")
        return redirect("/")
    
    user = User.query.get_or_404(user_id)
    playlists = Playlist.query.get_or_404(playlists_id)
    
    form = SongForm()
  
    if form.validate_on_submit():
        song_title = form.song_title.data
        song_artist = form.song_artist.data
        playlist_id = playlists.id
        spotify_client = SpotifyClient()
        spotify_client.call_refresh()
        spotify_song_id = spotify_client.search_song(song_artist,song_title)
        new_song = Song(song_title=song_title, song_artist=song_artist, playlist_id=playlist_id, spotify_song_id=spotify_song_id)
        db.session.add(new_song)
        db.session.commit()

        return redirect(f"/users/{ user_id }/playlists/{ playlists_id }")
    
    songs = Song.query.filter_by(playlist_id = playlists_id)

        
        
    return render_template("users/playlists.html",songs=songs, playlists=playlists, user=user, form=form, user_id=user_id, playlists_id=playlists_id)

"""Delete a song from a playlist"""
@app.route('/users/<int:user_id>/playlists/<int:playlists_id>/song/<int:song_id>/delete', methods=["POST"])
def delete_song_from_playlist(user_id, playlists_id, song_id):
    """Delete Song from Playlist"""
    if not g.user:
        flash("No Access!", "danger")
        return redirect("/")
    user = User.query.get_or_404(user_id)
    playlists = Playlist.query.get_or_404(playlists_id)
    
    song = Song.query.get(song_id)
    db.session.delete(song)
    db.session.commit()
    
    return redirect(f"/users/{ user_id }/playlists/{ playlists_id }")

"""Delete Playlist from user's page"""
@app.route('/users/<int:user_id>/playlists/<int:playlists_id>/delete', methods=["POST"])
def delete_playlist(user_id, playlists_id):
    """Delete Playlist from User's Page"""
    if not g.user:
        flash("No Access!", "danger")
        return redirect("/")

    playlists = Playlist.query.get(playlists_id)
    db.session.delete(playlists)
    db.session.commit()
    return redirect("/")
##############################################################################
# General user routes:

"""Show user's page"""
@app.route('/users/<int:user_id>', methods=["GET", "POST"])
def users_show(user_id):
    """Show user profile."""

    if not g.user:
        flash("No Access!", "danger")
        return redirect("/")
    user = User.query.get_or_404(user_id)
    form = PlaylistForm(obj=user)
    
    if form.validate_on_submit():
        
        title = form.title.data
        new_playlist = Playlist(title=title, user_id=user.id)
        
        db.session.add(new_playlist)
        db.session.commit()
        
        return redirect(f"/users/{ user_id }")
    
    playlists = Playlist.query.filter_by(user_id=g.user.id)
    
    return render_template('users/detail.html', user=user, playlists=playlists, form=form)




"""Edit's user profile"""
@app.route('/users/profile', methods=["GET", "POST"])
def profile():
    """Update profile for current user."""

    if not g.user:
        flash("No Access!", "danger")
        return redirect("/")
    
    user = g.user

    form = UserEditForm(obj=user)

    if form.validate_on_submit():
        
        if User.authenticate(user.username, form.password.data): 
            user.email = form.email.data
            user.image_url = form.image_url.data or User.image_url.default.arg

            
            db.session.commit()
            flash('Information has been updated!')
            return redirect(f"/users/{user.id}")
        
        flash("Invalid credentials - wrong password.", 'danger')

    return render_template('users/edit.html', user_id=user.id, form=form)

"""Delete User's profile"""
@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete user."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    user = User.query.get(user_id)
    playlists = Playlist.query.get(user_id)
    
    if user.playlists:
        flash("You must delete all playlists first!", "danger")
        return redirect("/")
    form = BlankForm() 
    if form.validate_on_submit():
        session.pop('user_id')
            
        do_logout()   
    db.session.delete(user)
    db.session.commit() 


    flash("Your User Account has been deleted", "danger")
    return redirect("/")

##############################################################################
# Homepage and error pages


@app.route('/')
def homepage():
    """Show homepage:

    - anon users: no messages
    - logged in: 100 most recent messages of followed_users
    """

    if g.user:

        return redirect(f"/users/{g.user.id}")

    else:
        return render_template('home-anon.html')


##############################################################################
# Turn off all caching in Flask
#   (useful for dev; in production, this kind of stuff is typically
#   handled elsewhere)
#
# https://stackoverflow.com/questions/34066804/disabling-caching-in-flask

@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req
