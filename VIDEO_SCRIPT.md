# 🎬 FLOWSTATE VIDEO DEMO SCRIPT (12-15 Minutes)

## 🎙️ RECORDING SETUP CHECKLIST

**Before Recording:**
- [ ] Close all unnecessary browser tabs
- [ ] Clear notifications (turn on Do Not Disturb - Windows: Win+N)
- [ ] Have FlowState running at `http://127.0.0.1:5000`
- [ ] Have VS Code open with project loaded
- [ ] Test your microphone in recording software
- [ ] Have water nearby (for voice clarity)
- [ ] Read script once out loud (practice pacing)

**Recording Software Options:**
1. **OBS Studio** (Free, professional) - https://obsproject.com/
2. **Loom** (Free tier, easy) - https://www.loom.com/
3. **Windows Game Bar** (Built-in) - Press `Win + G`
4. **ShareX** (Free, lightweight) - https://getsharex.com/

**Recording Settings:**
- Resolution: 1080p (1920x1080)
- Frame rate: 30fps minimum
- Audio: Enable microphone
- **TEST AUDIO FIRST** - Record 30 seconds and play back to verify voice is captured

---

## 🎬 SECTION 1: Introduction (1 minute)

**SCRIPT:**
> "Hi, I'm Diallo Williams, and this is FlowState - a song lyrics management application I built for artists across all genres. As both a hip-hop artist and software developer, I created this tool to solve a problem I experienced myself: keeping track of lyrics, verses, and song progress in one organized place.
>
> FlowState is built with Flask, SQLAlchemy, SQLite, and features a modern glassmorphic UI with Tailwind CSS. Let me show you how it works."

**ON SCREEN:**
- FlowState dashboard loaded and visible
- Cursor ready to interact

---

## 🎬 SECTION 2: Quick Feature Demo (4-5 minutes)

### A) Dashboard View (30 seconds)

**SCRIPT:**
> "This is the main dashboard where you can see all your songs at a glance. Each song has a status badge - Draft, Recording, or Complete - and shows when it was last modified."

**ACTIONS:**
- Scroll through existing songs slowly
- Hover over song cards to show hover effects
- Point out (with cursor) the status badges
- Show the date information

---

### B) Create New Song (1 minute)

**SCRIPT:**
> "Let's create a new song. I'll click 'Add New Song,' give it a title, and mark it as a draft since we're just starting."

**ACTIONS:**
- Click "Add New Song" button
- Fill in form:
  - Title: "Demo Track"
  - Status: Select "Draft"
  - AI Generated: Leave unchecked
- Click "Create Song" button
- Show it appearing on dashboard (scroll to find it if needed)

---

### C) Add Verses (1.5 minutes)

**SCRIPT:**
> "Now let's add some lyrics. I can add verses one at a time, and the system automatically numbers them. This keeps everything organized as I write."

**ACTIONS:**
- Click on "Demo Track" to view song
- Click "Add Lyrics" button
- Add Verse 1:
```
  First verse coming through the speakers
  Building something new for all the seekers
```
- Click "Add Lyrics" button
- Show verse appearing
- Click "Add Lyrics" again for Verse 2:
```
  Second verse flowing with the beat
  Making sure this project is complete
```
- Show both verses displayed with verse numbers

---

### D) Edit Verse (45 seconds)

**SCRIPT:**
> "If I need to revise a verse, I can edit it directly. Let me fix a line in verse 1."

**ACTIONS:**
- Click "Edit" button on Verse 1
- Change text to:
```
  First verse coming through crystal clear
  Building something new without any fear
```
- Click "Update Lyrics" button
- Show updated verse with changes

---

### E) Delete Operations (45 seconds)

**SCRIPT:**
> "I can delete individual verses if I decide I don't need them, or delete the entire song. The system uses cascade delete, so removing a song automatically removes all its verses - keeping the database clean."

**ACTIONS:**
- Click "Delete" button on Verse 2
- Show confirmation message (if any)
- Show verse removed
- Go back to dashboard
- Click "Delete" button on "Demo Track" song
- Show confirmation
- Show dashboard updates with song removed

---

## 🎬 SECTION 3: Code Walkthrough (5-6 minutes)

### A) Project Structure (1 minute)

**SCRIPT:**
> "Let me show you the code structure. FlowState follows a clean MVC pattern with templates for views, models for data, and Flask routes handling the logic."

**ACTIONS:**
- Switch to VS Code
- Show file explorer (left sidebar)
- Expand folders to show:
  - `app.py` (main application)
  - `database/` folder (models.py, db_setup.py)
  - `templates/` folder (all HTML files)
  - `requirements.txt`
  - `README.md`

---

### B) Database Models (1.5 minutes)

**SCRIPT:**
> "The database has two models: Song and Lyrics. A song can have many lyrics verses, and I implemented cascade delete so removing a song automatically cleans up all its verses. Here's the relationship setup in SQLAlchemy."

**ACTIONS:**
- Open `database/models.py`
- Scroll to Song model
- Highlight with cursor:
  - Class definition
  - All attributes (id, title, status, etc.)
  - The `lyrics` relationship
- Scroll to Lyrics model
- Highlight:
  - Class definition
  - song_id foreign key
  - The relationship back to Song
- Point to `cascade='all, delete-orphan'` in Song model

---

### C) Flask Routes (2 minutes)

**SCRIPT:**
> "The app has seven routes handling full CRUD operations. Let me show you the main ones."

**ACTIONS:**
- Open `app.py`
- Scroll to and explain:
  1. **Dashboard route (`/`):**
     > "This queries all songs from the database and renders them on the dashboard."
     - Show the query: `Song.query.all()`
  
  2. **Add song route (`/song/new`):**
     > "This handles both GET requests to show the form, and POST requests to create the song."
     - Show GET/POST if-else structure
  
  3. **View song route (`/song/<id>`):**
     > "This fetches a specific song and all its verses using the relationship."
     - Show the query and relationship usage
  
  4. **Delete route (`/song/<id>/delete`):**
     > "This demonstrates cascade delete - removing the song automatically removes all verses."
     - Show `db.session.delete(song)`

---

### D) UI Design (1 minute)

**SCRIPT:**
> "For the frontend, I used Tailwind CSS with a glassmorphic design - that backdrop blur effect you see. The purple, cyan, and pink gradient accents give it a modern, music-industry feel. Everything is responsive and mobile-friendly."

**ACTIONS:**
- Open `templates/base.html`
- Scroll to show Tailwind classes:
  - `backdrop-blur`
  - `bg-gradient-to-br`
  - Responsive classes (`md:`, `lg:`)
- Switch to browser
- Open DevTools (F12)
- Click device toolbar (mobile icon)
- Show responsive design on different screen sizes

---

## 🎬 SECTION 4: Tech Stack & Future Plans (2 minutes)

**SCRIPT:**
> "The tech stack includes:
> - Backend: Flask and SQLAlchemy for the ORM
> - Database: SQLite for development - easily swappable to PostgreSQL for production
> - Frontend: Jinja2 templates with Tailwind CSS
> - Deployment: I'll be deploying this to Render with PostgreSQL
>
> Future enhancements I'm planning include:
> - Audio integration - upload beats and link verses to timestamps
> - Rhyme analysis using the Pronouncing library
> - Collaborative features for co-writing sessions
> - Export to PDF or text files
>
> This project demonstrates my full-stack capabilities and my understanding of the music production workflow - combining my background as an artist with my technical skills as a developer."

**ACTIONS:**
- Show `requirements.txt` (scroll through dependencies)
- Open `README.md` in browser or VS Code preview
- Scroll to "Future Enhancements" section
- Show the roadmap items

---

## 🎬 SECTION 5: Closing (30 seconds)

**SCRIPT:**
> "Thanks for watching. You can find the full source code on my GitHub at github.com/DialloWill/flowstate, and the live deployed version will be at [ADD RENDER URL AFTER DEPLOYMENT]. Feel free to connect with me on LinkedIn or check out my other projects. I'm currently seeking junior to mid-level software developer positions, particularly in music tech. Thanks again!"

**ACTIONS:**
- Switch to browser
- Show GitHub repo: `https://github.com/DialloWill/flowstate`
- Show your LinkedIn profile (optional)
- Show live deployment (after you deploy to Render)

---

## 🎯 RECORDING TIPS

**Voice & Delivery:**
- Speak at 80% of your normal pace (gives clarity)
- Smile while talking (it comes through in your voice)
- Pause for 2 seconds between sections (easier to edit)
- If you mess up: Pause 3 seconds, then restart that sentence
- Don't say "um" or "uh" - just pause instead

**Technical:**
- Close Slack, Discord, email (avoid notifications)
- Use wired headphones/mic if possible (better audio)
- Record in a quiet room
- Face away from windows (reduces echo)
- Test audio levels before full recording

**Editing:**
- Cut out long pauses
- Remove mistakes/restarts
- Add text overlays for key points (optional)
- Ensure transitions between sections are smooth

---

## 📤 AFTER RECORDING

**Upload Options:**
1. **YouTube** (unlisted) - Best for portfolio
2. **Loom** - Auto-hosted, easy sharing
3. **Vimeo** - Professional look

**Then:**
- Add video link to README.md
- Add to LinkedIn projects
- Include in job applications
- Share with recruiters

---

**Good luck! You've got this! 🎬🔥**