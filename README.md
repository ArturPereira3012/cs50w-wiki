# CS50W Wiki - Markdown Wikipedia-like Application

An online encyclopedia platform inspired by Wikipedia that allows users to view, search, create, and edit encyclopedia entries using Markdown formatting, built as part of Harvard's **CS50's Web Programming with Python and JavaScript** course.

## 🚀 Features

- **Entry Page:** Navigating to a specific route displays the content of that encyclopedia entry. The content is saved in Markdown format on the backend and dynamically converted to clean HTML for the user.
- **Index Page:** The home page lists the titles of all currently available encyclopedia entries, clicking on any title takes the user directly to that entry's page.
- **Search System:** A sidebar search utility that allows users to look up entries. If the query matches an exact title, the user is redirected there. If it matches a substring, a list of all matching entries is generated.
- **New Page Creation:** Authenticated actions allowing users to create entirely new entries by typing a title and Markdown content. The system prevents duplicates.
- **Edit Page:** Users can edit existing entries. The editing page is pre-populated with the existing Markdown text, allowing quick modifications.
- **Random Page:** A feature button that selects a random encyclopedia entry from the database and displays it to the user.

## 🛠️ Tech Stack

- **Backend:** Python, Django framework
- **Libraries:** Python-Markdown (for dynamic MD to HTML rendering)
- **Frontend:** HTML5, CSS3, Bootstrap framework

## 📦 Installation and Local Setup

Follow these steps to get this project running on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ArturPereira3012/cs50w-wiki.git](https://github.com/ArturPereira3012/cs50w-wiki.git)
   cd cs50w-wiki

2.Create and activate a virtual environment (Recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`

3.Install the required packages:
pip install django markdown

4.Start the development server:
python manage.py runserver

5. Access the application:
Open your preferred web browser and navigate to http://127.0.0.1:8000/.

This project was developed as an academic assignment for the CS50W course, fulfilling all the strict design specifications provided by Harvard University.
