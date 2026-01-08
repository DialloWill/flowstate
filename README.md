# 🎵 FlowState™ - Lyric Management for Creatives

**🎥 [Watch Video Demo](https://youtu.be/athd7N1YsQE)** | **🌐 [Live Demo](https://flowstate-1xcb.onrender.com)**

A modern web application for managing song lyrics and creative writing. Built with Flask and SQLAlchemy, FlowState™ helps musicians, songwriters, poets, and content creators organize their creative process from draft to final recording.

![FlowState Dashboard](https://via.placeholder.com/800x400/1a1a2e/eee?text=FlowState+Dashboard)

---

## ✨ Features

### Core Functionality
- **Song Management** - Create, view, edit, and delete songs with status tracking (draft/recording/complete)
- **Verse Organization** - Add multiple verses to each song with automatic numbering
- **Real-time Editing** - Edit lyrics on the fly with instant updates
- **Database Integrity** - Cascade delete ensures clean data relationships

### Public Pages
- **About Page** (`/about`) - Learn about FlowState™ with embedded demo video and feature showcase
- **Gear Recommendations** (`/gear`) - Curated music production equipment for creatives (affiliate-supported)

### Analytics & Support
- **Google Analytics** - Track visitor engagement and site performance (GA4)
- **Affiliate Disclosure** - Transparent affiliate program participation to support free access

### Design
- **Modern UI** - Glassmorphic design with Tailwind CSS
- **Responsive Layout** - Works seamlessly on desktop, tablet, and mobile
- **Dark Theme** - Easy on the eyes during late-night creative sessions
- **Gradient Accents** - Purple-to-cyan branding throughout

---

## 🧪 Try It Out - Demo Account

**Live Demo:** [https://flowstate-1xcb.onrender.com](https://flowstate-1xcb.onrender.com)

**Demo Credentials:**
- **Username:** `demo@flowstate.com`
- **Password:** `DemoFlow2025`

The demo account includes 3 sample songs with pre-written verses to explore all features.

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Flask (Web Framework)
- SQLAlchemy (ORM)
- PostgreSQL (Production on Render)
- SQLite (Local Development)

**Frontend:**
- HTML5
- Tailwind CSS (Styling via CDN)
- Jinja2 Templates (Templating)
- Lucide Icons (Modern icon set)

**Analytics:**
- Google Analytics 4 (GA4)

**Deployment:**
- Render.com (Cloud hosting)
- GitHub (Version control)

---

## 📁 Project Structure
```
flowstate/
│
├── app.py                      # Main Flask application with 9 routes
├── instance/
│   └── flowstate.db            # SQLite database (local dev only)
├── requirements.txt            # Python dependencies
│
├── database/
│   ├── __init__.py
│   ├── models.py               # Song and Lyrics models
│   └── db_setup.py             # Database initialization and demo data seeding
│
├── templates/
│   ├── base.html               # Base template with navigation, footer, GA4
│   ├── index.html              # Dashboard - view all songs
│   ├── about.html              # Public about page with demo video
│   ├── gear.html               # Gear recommendations (affiliate products)
│   ├── add_song.html           # Create new song form
│   ├── view_song.html          # View single song with all verses
│   ├── add_lyrics.html         # Add new verse form
│   └── edit_lyrics.html        # Edit existing verse form
│
└── static/
    └── gear.css                # Custom styling for gear page
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/DialloWill/flowstate.git
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

**Note:** Demo data (3 sample songs) will automatically populate on first run.

---

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

### Exploring Public Pages
- **About:** Click "About" in navbar to learn about FlowState™
- **Gear:** Click "Gear" in navbar to browse recommended music production equipment

---

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

---

## 🔮 Future Enhancements

**Planned Features:**
- [ ] Search and filter songs by title or status
- [ ] Export lyrics to PDF or TXT format
- [ ] Audio file upload for beats/instrumentals
- [ ] Verse reordering with drag-and-drop
- [ ] Collaboration features for multiple artists
- [ ] User authentication and multi-user support
- [ ] Mobile app version (iOS/Android)
- [ ] Real affiliate links integration (Amazon, AliExpress, ShareASale)

---

## 💰 Affiliate Disclosure

FlowState™ participates in Amazon Associates, AliExpress Portals, and other affiliate programs. We may earn commissions from qualifying purchases made through links on our Gear page, at no additional cost to you.

**Your support helps us:**
- Keep FlowState™ free for all users
- Continue developing new features
- Maintain and improve our servers
- Create helpful content for creatives

All product recommendations are based on quality, value, and user reviews—not just commission rates.

---

## 👨‍💻 Author

**Diallo Williams**
- Master's in IT Management (3.94 GPA) - DeVry University
- Bachelor's in Software Development (3.53 GPA) - DeVry University
- Hip-Hop Artist & Software Developer
- **GitHub:** [github.com/DialloWill](https://github.com/DialloWill)
- **LinkedIn:** [linkedin.com/in/diallowilliams](https://linkedin.com/in/diallowilliams)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Built as a portfolio project demonstrating full-stack development skills
- Inspired by the need for better lyric management tools for independent artists
- Tailwind CSS for modern UI components
- Lucide Icons for clean, modern iconography
- Render.com for cloud hosting

---

**Built with ❤️ for the creative community**

**FlowState™ © 2025. All rights reserved.**