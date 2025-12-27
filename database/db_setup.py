"""
Database initialization and seeding utilities for FlowState.

Provides functions to create database tables and populate with sample data
for testing and demonstration purposes.

Functions:
    init_db: Creates all database tables from models
    seed_sample_data: Adds sample song and lyrics for testing
"""


from database.models import db, Song, Lyrics

def init_db(app):
    """
    Initialize the database and create all tables.
    
    Creates all tables defined in models.py if they don't already exist.
    Safe to run multiple times - won't overwrite existing data.
    
    Args:
        app (Flask): The Flask application instance with database config
    
    Note:
        Must be called within app context. Automatically run on app startup"""
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully!")

def seed_sample_data(app):
    """
    Populate database with sample song and lyrics for testing.
    
    Creates one sample song with one verse if database is empty.
    Skips seeding if data already exists to prevent duplicates.
    
    Args:
        app (Flask): The Flask application instance with database config
    
    Sample Data Created:
        - 1 song titled "Sample Track" with draft status
        - 1 verse with sample lyrics demonstrating the format
    
    Note:
        Safe to run multiple times - checks for existing data first.
        Automatically run on app startup for demo purposes."""
    with app.app_context():
        # Check if data already exists
        if Song.query.first():
            print("⚠️ Sample data already exists, skipping...")
            return
        
        # Create sample song
        sample_song = Song(
            title="Sample Track",
            status="draft"
        )
        db.session.add(sample_song)
        db.session.commit()

        # Add sample lyrics
        sample_lyrics = Lyrics(
            song_id=sample_song.id,
            verse_number=1,
            lyrics_text="""All gas no brakes cuz I'm in my flow state,
        She fell in love cuz I gave her rounds and don't need no breaks,
        She said I'm a keeper cuz I like to eat a whole cake,
        Eat your heart out or die cuz its a waste if her legs don't shake"""
        )

        db.session.add(sample_lyrics)
        db.session.commit()

        print("✅ Sample data added successfully!")