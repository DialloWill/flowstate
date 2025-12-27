"""
Database models for FlowState application.

Defines the Song and Lyrics models with SQLAlchemy ORM.
Implements cascade delete to maintain referential integrity.

Models:
    Song: Represents a song with metadata and status tracking
    Lyrics: Represents individual verses linked to songs
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Song(db.Model):
    """
     Song model representing a musical composition.
    
    Stores song metadata including title, status, and creation tracking.
    One song can have many verses (lyrics) through a one-to-many relationship.
    
    Attributes:
        id (int): Primary key, auto-incremented
        title (str): Song title, required (max 200 characters)
        status (str): Current status - 'draft', 'recording', or 'complete' (default: 'draft')
        is_ai_generated (bool): Whether lyrics were AI-assisted (default: False)
        date_created (datetime): Timestamp when song was created (auto-set)
        last_modified (datetime): Timestamp of last update (auto-set)
        lyrics (relationship): One-to-many relationship with Lyrics model
    
    Relationships:
        - One Song has many Lyrics (verses)
        - Cascade delete enabled: deleting a song deletes all its verses
    
    Example:
        new_song = Song(title="My Track", status="draft")
        db.session.add(new_song)
        db.session.commit()
    """
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='draft')
    is_ai_generated = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, default=datetime.utcnow)

    # FIXED: Added cascade='all, delete-orphan'
    lyrics = db.relationship('Lyrics', backref='song', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Song {self.title}>"
    
class Lyrics(db.Model):
    """
    Lyrics model representing individual verses of a song.
     Stores verse content linked to a parent song via foreign key.
    Multiple verses can belong to one song.
    
    Attributes:
        id (int): Primary key, auto-incremented
        song_id (int): Foreign key to songs table, required
        verse_number (int): Verse number/order within the song, required
        lyrics_text (str): The actual lyrics content, required (unlimited length)
        date_created (datetime): Timestamp when verse was created (auto-set)
        song (relationship): Backref to parent Song object
    
    Relationships:
        - Many Lyrics belong to one Song
        - Automatically deleted when parent song is deleted (cascade)
    
    Example:
        new_verse = Lyrics(song_id=1, verse_number=1, lyrics_text="Bars here...")
        db.session.add(new_verse)
        db.session.commit()
     """
    __tablename__ = 'lyrics'
    
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    verse_number = db.Column(db.Integer, nullable=False)
    lyrics_text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Lyrics Verse {self.verse_number} for Song {self.song_id}>"