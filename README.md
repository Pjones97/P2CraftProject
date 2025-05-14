Projexis

Projexis is a web platform designed for crafting enthusiasts to brainstorm, create, and connect. With smart tools and a collaborative community, Projexis makes it easy to go from idea to reality.

Features:
AI Chatbot – Converse with an AI to brainstorm crafting ideas and get project guidance.

YouTube Video Finder – Pull in helpful tutorial videos based on your idea using the YouTube Data API.

Local Resource Finder – Use Google Maps API to locate nearby stores or suppliers for your crafting needs.

Crafting Community – Share projects, tips, and ideas with fellow creators in a supportive environment.


Tech Stack:
Backend: Django (Python)
Frontend: React.js (integrated with Django)
Database: SQL (SQLite or PostgreSQL depending on setup)
APIs Used:
OpenAI API
YouTube Data API
Google Maps API
Image Processing: Pillow (for image uploads and manipulation)
Getting Started

Prerequisites:
Python 3.x and pip
Node.js and npm
Git
Virtual environment tool (venv, virtualenv, or pipenv)
API Keys for:
OpenAI
YouTube Data API
Google Maps API

Installation
Clone the repository:
- git clone https://github.com/your-username/projexis.git
- cd projexis
  
Set up and activate a Python virtual environment:
python -m venv env
source env/bin/activate   
# On Windows use `env\Scripts\activate`
Install Python dependencies:
pip install -r requirements.txt


Set up your .env file in the Django project root:
OPENAI_API_KEY=your_openai_api_key
YOUTUBE_API_KEY=your_youtube_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key

Run Django migrations:
python manage.py migrate
Start the Django development server:
python manage.py runserver

Usage

Navigate to http://localhost:8000 to use the platform.
Use the AI Chatbot to brainstorm.
Search for tutorial videos using keywords.
Use the map to find nearby stores.
Post or browse community projects.
Contributing

Contributions are welcome! Please fork the repo and submit a pull request. Bug reports, feature ideas, and documentation improvements are especially appreciated.

