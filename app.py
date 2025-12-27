"""
FlowState - Song Lyrics Management Application

A Flask-based web application for managing song lyrics.
Allows artists to create songs, add verses, edit lyrics, and track song status.

Author: Diallo Williams
Tech Stack: Flask, SQLAlchemy, SQLite, Tailwind CSS
Date: December 2025
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from database.models import db, Song, Lyrics
from database.db_setup import init_db, seed_sample_data
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flowstate-secret-key-change-later'
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "flowstate.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create tables and add sample data if database doesn't exist
with app.app_context():
    init_db(app)
    seed_sample_data(app)

# Route 1: Dashboard - shows all songs
@app.route('/')
def index():
    """
    Display the dashboard with all songs.
    
    Shows a list of all songs in the database with their status,
    verse count, and creation date. Main landing page of the app.
    
    Returns:
        Rendered HTML template (index.html) with list of all songs
    """
    # Get all songs from database, ordered by most recent first
    all_songs = Song.query.order_by(Song.date_created.desc()).all()

    # Render the dashboard template and pass the songs to it
    return render_template('index.html', songs=all_songs)

# Route 2: Add a new song
@app.route('/song/new', methods=['GET', 'POST'])
def add_song():
    """
    Create a new song.
    
    GET: Display the form to add a new song
    POST: Process form data and create song in database
    
    Form Fields:
        title (str): Song title (required)
        status (str): Song status - 'draft', 'recording', or 'complete' (default: 'draft')
    
    Returns:
        GET: Rendered add_song.html template
        POST: Redirect to dashboard with success message
    """
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        status = request.form.get('status', 'draft')

        # Validate title exists
        if not title:
            flash('Song title is required!', 'danger')
            return redirect(url_for('add_song'))
        
        # Create a new song
        new_song = Song(title=title, status=status)
        db.session.add(new_song)
        db.session.commit()

        flash(f'Song "{title}" added successfully!', 'success')
        return redirect(url_for('index'))
    
    # GET request - show the form to add a new song
    return render_template('add_song.html')

# Route 3: View a single song with its lyrics
@app.route('/song/<int:song_id>')
def view_song(song_id):
    """
     Display a single song with all its lyrics.
    
    Shows song details (title, status, creation date) and all verses
    ordered by verse number. Includes options to add, edit, or delete verses.
    
    Args:
        song_id (int): The ID of the song to display
    
    Returns:
        Rendered view_song.html template with song and lyrics data
    
    Raises:
        404: If song with given ID doesn't exist"""
    # Get the song by ID (or return 404 if not found)
    song = Song.query.get_or_404(song_id)
    
    # Get all lyrics for this song, ordered by verse number
    lyrics = Lyrics.query.filter_by(song_id=song_id).order_by(Lyrics.verse_number).all()
    
    # Render the view_song template with song and lyrics data
    return render_template('view_song.html', song=song, lyrics=lyrics)

# Route 4: Add lyrics to a song
@app.route('/song/<int:song_id>/add_lyrics', methods=['GET', 'POST'])
def add_lyrics(song_id):
    """
     Add new lyrics/verse to a song.
    
    GET: Display form to add a new verse
    POST: Process form data and create new lyrics entry
    
    Args:
        song_id (int): The ID of the song to add lyrics to
    
    Form Fields:
        verse_number (int): Verse number (required)
        lyrics_text (str): The actual lyrics text (required)
    
    Returns:
        GET: Rendered add_lyrics.html template
        POST: Redirect to view_song page with success message
    
    Raises:
        404: If song with given ID doesn't exist"""
    # Get the song (or return 404 if not found)
    song = Song.query.get_or_404(song_id)
    
    if request.method == 'POST':
        # Get form data
        verse_number = request.form.get('verse_number')
        lyrics_text = request.form.get('lyrics_text')
        
        # Validate data
        if not verse_number or not lyrics_text:
            flash('Both verse number and lyrics are required!', 'danger')
            return redirect(url_for('add_lyrics', song_id=song_id))
        
        # Create new lyrics entry
        new_lyrics = Lyrics(
            song_id=song.id,
            verse_number=int(verse_number),
            lyrics_text=lyrics_text
        )
        
        # Save to database
        db.session.add(new_lyrics)
        db.session.commit()
        
        flash(f'Verse {verse_number} added successfully!', 'success')
        return redirect(url_for('view_song', song_id=song_id))
    
    # GET request - show the form
    return render_template('add_lyrics.html', song=song)

# Route 5: Delete a song
@app.route('/song/<int:song_id>/delete', methods=['POST'])
def delete_song(song_id):
    """
     Delete a song and all its lyrics.
    
    Permanently removes a song from the database. All associated lyrics
    are automatically deleted due to cascade relationship.
    
    Args:
        song_id (int): The ID of the song to delete
    
    Returns:
        Redirect to dashboard with success message
    
    Raises:
        404: If song with given ID doesn't exist
    
    Note:
        This action cannot be undone. Confirmation prompt shown in UI."""
    # Get the song (or return 404 if not found)
    song = Song.query.get_or_404(song_id)
    
    # Store title for success message
    song_title = song.title
    
    # Delete the song (lyrics will be deleted automatically due to cascade)
    db.session.delete(song)
    db.session.commit()
    
    flash(f'Song "{song_title}" deleted successfully!', 'success')
    return redirect(url_for('index'))

# Route 6: Edit existing lyrics
@app.route('/song/<int:song_id>/lyrics/<int:lyrics_id>/edit', methods=['GET', 'POST'])
def edit_lyrics(song_id, lyrics_id):
    """
    Edit an existing verse.
    
    GET: Display form pre-filled with current verse data
    POST: Update verse with new data
    
    Args:
        song_id (int): The ID of the song
        lyrics_id (int): The ID of the specific verse to edit
    
    Form Fields:
        verse_number (int): Updated verse number (required)
        lyrics_text (str): Updated lyrics text (required)
    
    Returns:
        GET: Rendered edit_lyrics.html template with current verse data
        POST: Redirect to view_song page with success message
    
    Raises:
        404: If song or lyrics with given IDs don't exist"""
    # Get the song (or return 404 if not found)
    song = Song.query.get_or_404(song_id)
    
    # Get the specific lyrics entry (or return 404 if not found)
    lyric = Lyrics.query.get_or_404(lyrics_id)

    if request.method == 'POST':
        # Get updated data from form
        verse_number = request.form.get('verse_number')
        lyrics_text = request.form.get('lyrics_text')

        # Validate data exists
        if not verse_number or not lyrics_text:
            flash('Both verse number and lyrics are required!', 'danger')
            return redirect(url_for('edit_lyrics', song_id=song_id, lyrics_id=lyrics_id))
        

        # Update the lyrics in the database
        lyric.verse_number = int(verse_number)
        lyric.lyrics_text = lyrics_text
        db.session.commit()

        flash(f'Verse {verse_number} updated successfully!', 'success')
        return redirect(url_for('view_song', song_id=song_id))
    
    # GET request - show the edit form with current data
    return render_template('edit_lyrics.html', song=song, lyric=lyric)

# Route 7: Delete lyrics
@app.route('/song/<int:song_id>/lyrics/<int:lyrics_id>/delete', methods=['POST'])
def delete_lyrics(song_id, lyrics_id):
    """
    Delete a single verse from a song.
    
    Permanently removes one verse while keeping the song and other verses intact.
    
    Args:
        song_id (int): The ID of the song
        lyrics_id (int): The ID of the specific verse to delete
    
    Returns:
        Redirect to view_song page with success message
    
    Raises:
        404: If lyrics with given ID doesn't exist
    
    Note:
        This action cannot be undone. Confirmation prompt shown in UI."""
    lyrics = Lyrics.query.get_or_404(lyrics_id)
    db.session.delete(lyrics)
    db.session.commit()
    flash(f'Verse deleted successfully!', 'success')
    return redirect(url_for('view_song', song_id=song_id))

# Run the app when this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)