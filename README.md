# Smart Society - HTML + JavaScript + Python

## Technologies
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: SQLite

## Run backend
Open a terminal:
    cd backend
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py

Backend: http://localhost:5000

## Run frontend
Because the frontend calls the Flask API, use a local web server from the project root.
For example, with Python:
    cd frontend
    python -m http.server 5500

Then open:
http://localhost:5500/

Do not open index.html directly with file:// if your browser blocks API requests.

## Included
Dashboard, residents, notices, complaints and bills, with SQLite persistence.
