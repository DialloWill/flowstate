# 🎵 FlowState - Song Lyrics Management Application

A modern web application for managing song lyrics across all genres. Built with Flask and SQLAlchemy, FlowState helps artists organize their creative process from draft to final recording.

![FlowState Dashboard](https://via.placeholder.com/800x400/1a1a2e/eee?text=FlowState+Dashboard)
*We'll replace this placeholder with a real screenshot tomorrow*

## ✨ Features

- **Song Management** - Create, view, edit, and delete songs with status tracking (draft/recording/complete)
- **Verse Organization** - Add multiple verses to each song with automatic numbering
- **Real-time Editing** - Edit lyrics on the fly with instant updates
- **Clean UI** - Modern glassmorphic design with Tailwind CSS
- **Database Integrity** - Cascade delete ensures clean data relationships

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)

**Frontend:**
- HTML5
- Tailwind CSS (Styling)
- Jinja2 Templates (Templating)

**Design:**
- Glassmorphism UI
- Responsive Design
- Modern Gradient Accents

## 📁 Project Structure
```
flowstate/
│
├── app.py                      # Main Flask application with 7 routes
├── flowstate.db                # SQLite database (auto-generated)
├── requirements.txt            # Python dependencies
│
├── database/
│   ├── __init__.py
│   ├── models.py               # Song and Lyrics models
│   └── db_setup.py             # Database initialization and seeding
│
├── templates/
│   ├── base.html               # Base template with navigation
│   ├── index.html              # Dashboard - view all songs
│   ├── add_song.html           # Create new song form
│   ├── view_song.html          # View single song with all verses
│   ├── add_lyrics.html         # Add new verse form
│   └── edit_lyrics.html        # Edit existing verse form
│
└── static/
    └── (Tailwind CSS via CDN)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/flowstate.git
cd flowstate
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`

## 📖 Usage Guide

### Creating Your First Song
1. Click **"New Song"** button on the dashboard
2. Enter song title and select status (draft/recording/complete)
3. Click **"Add Song"** to save

### Adding Verses
1. Click **"View Song"** on any song card
2. Click **"Add Lyrics"** button
3. Enter verse number and lyrics text
4. Click **"Add Verse"** to save

### Editing Verses
1. Navigate to song view page
2. Click **"Edit"** button on any verse card
3. Modify verse number or lyrics text
4. Click **"Update Verse"** to save changes

### Deleting Content
- **Delete Verse:** Click "Delete" button on verse card (confirmation required)
- **Delete Song:** Click "Delete Song" button at bottom of song page (deletes all verses automatically)

## 🗄️ Database Schema

### Songs Table
| Column         | Type      | Description                              |
|----------------|-----------|------------------------------------------|
| id             | Integer   | Primary key (auto-increment)             |
| title          | String    | Song title (max 200 characters)          |
| status         | String    | Status: draft/recording/complete         |
| is_ai_generated| Boolean   | AI-assisted flag (default: False)        |
| date_created   | DateTime  | Creation timestamp (auto-set)            |
| last_modified  | DateTime  | Last update timestamp (auto-set)         |

### Lyrics Table
| Column         | Type      | Description                              |
|----------------|-----------|------------------------------------------|
| id             | Integer   | Primary key (auto-increment)             |
| song_id        | Integer   | Foreign key to songs table               |
| verse_number   | Integer   | Verse position/number                    |
| lyrics_text    | Text      | Actual lyrics content (unlimited length) |
| date_created   | DateTime  | Creation timestamp (auto-set)            |

**Relationship:** One Song → Many Lyrics (one-to-many with cascade delete)

## 🔮 Future Enhancements

- [ ] Search and filter songs by title or status
- [ ] Export lyrics to PDF or TXT format
- [ ] Audio file upload for beats/instrumentals
- [ ] Verse reordering with drag-and-drop
- [ ] Collaboration features for multiple artists
- [ ] Mobile app version
- [ ] Cloud deployment

## 👨‍💻 Author

**Diallo Williams**
- Master's in IT Management
- Bachelor's in Software Development
- Hip-Hop Artist & Software Developer

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built as a portfolio project demonstrating full-stack development skills
- Inspired by the need for better lyric management tools for independent artists
- Tailwind CSS for modern UI components

---

**Built with ❤️ for the creative community**