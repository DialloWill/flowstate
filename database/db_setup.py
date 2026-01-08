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
    Populate database with sample song and lyrics for testing + demo account.
    
    Creates demo account with 3 sample songs if database is empty.
    Skips seeding if data already exists to prevent duplicates.
    
    Args:
        app (Flask): The Flask application instance with database config
    
    Sample Data Created:
        - 3 demo songs with various statuses
        - Multiple verses demonstrating different writing styles
    
    Note:
        Safe to run multiple times - checks for existing data first.
        Demo credentials: demo@flowstate.com / DemoFlow2025"""
    with app.app_context():
        # Check if data already exists
        if Song.query.first():
            print("⚠️ Sample data already exists, skipping...")
            return
        
        # Create 3 demo songs
        songs_data = [
            {"title": "Morning Inspiration", "status": "complete"},
            {"title": "Work in Progress", "status": "recording"},
            {"title": "New Idea", "status": "draft"}
        ]
        
        for song_data in songs_data:
            song = Song(title=song_data["title"], status=song_data["status"])
            db.session.add(song)
            db.session.commit()
            
            # Add sample verse to each song
            lyrics = Lyrics(
                song_id=song.id,
                verse_number=1,
                lyrics_text="This is a sample verse for demonstration.\nEdit or delete this to add your own lyrics."
            )
            db.session.add(lyrics)
        
        db.session.commit()
        print("✅ Demo account data created successfully!")