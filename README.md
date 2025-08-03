** Court Info Submission Tracker (Simulated)**

This Django mini project allows users to enter court case details (Case Type, Number, Filing Year) through a simple form, simulates fetching a court response, stores the query in the database, and displays recent submissions in a dashboard format.

---
Objective:-

Build a clean Django-based web app that:

- Accepts court case details
- Simulates fetching court information
- Stores each submission in a database
- Shows recent user queries in a mini dashboard
- Designed in a way that real court scraping logic can be added later

---

##  Technologies Used

- Python 3
- Django Web Framework
- SQLite (default Django DB)
- HTML + CSS (basic frontend)

---

## Why Simulated?

Some Indian court websites (like:

- [Delhi High Court](https://delhihighcourt.nic.in/)
- [District Courts eCourts](https://districts.ecourts.gov.in/)

) use CAPTCHA and dynamic view tokens, which makes automated scraping complex.

So, this version **uses dummy logic** to simulate responses, but the code is ready for real scraping using tools like Selenium or Playwright.

---

## Features

- Django form to enter:
  - Case Type
  - Case Number
  - Filing Year
- Server-side form validation
- Stores every query to database
- Displays last 5 recent queries
- Displays simulated case result
- User-friendly UI

---

## Folder Structure
court_project/
│
├── court_project1/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── court_app/
│ ├── migrations/
│ ├── templates/
│ │ └── court_app/
│ │ └── index.html
│ ├── forms.py
│ ├── models.py
│ ├── scraper.py
│ ├── views.py
│ └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md

Create and activate virtual environment
  [python -m venv venv]
  [venv\Scripts\activate   # On Windows]
Install Django
  [pip install django]
Run migrations
  [python manage.py makemigrations,
  python manage.py migrate]
Start the development server
  [python manage.py runserver]
Now open your browser and go to:
  [http://127.0.0.1:8000/court_app/]


