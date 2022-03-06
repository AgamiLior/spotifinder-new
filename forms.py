from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, InputRequired, EqualTo


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    confirm_pswd = PasswordField('Confirm Password', validators=[InputRequired(message="Password Required"), EqualTo('password', message="Password must match")])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    
class UserEditForm(FlaskForm):
    """Form for editing user."""
    
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    image_url = StringField('Personal Img')
    password = PasswordField('Password', validators=[Length(min=6)])
    
class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    title = StringField("Title", validators=[DataRequired()])

class SongForm(FlaskForm):
    """Form for adding song to playlist."""
    
    song_title = StringField('Song Name', validators=[DataRequired()],  render_kw={"placeholder": "Song Name"})
    song_artist = StringField('Artist', validators=[DataRequired()],  render_kw={"placeholder": "Artist"})

class BlankForm(FlaskForm):
    """This form is just blank form."""