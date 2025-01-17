# **MY TRACKER**
#### Video Demo:  <URL https://youtu.be/k8QORGbCaog>
#### Description:

**My Tracker** is a web-based app designed to help users organize and keep track of the movies and TV series they’ve watched. Built with Flask, the platform provides features like adding, deleting, and sorting titles, as well as user authentication and summaries of recently watched content. With a simple yet efficient design, it connects users to an SQLite database for secure data storage. This document explains how each part of the project works and how the files come together to create an engaging experience.

---

## The Core: Routing and Logic

The main file, `app.py`, acts as the engine of the project. It connects user actions (like adding a movie or logging in) to the backend processes that handle these requests.

Here’s a breakdown of the key features in `app.py`:
- **Adding a Movie or Series:** Users can search for titles in the database and add them to their watched list. The `add_movie` and `add_series` routes handle this process by accepting user inputs like watch dates and, for series, the number of episodes viewed.
- **Deleting Titles:** The `delete` route lets users remove movies or series they no longer want in their list, ensuring they maintain a clean record.
- **Authentication:** Routes like `login` and `register` secure the platform by managing user access. Logged-in users’ sessions are tracked so they can only see and manage their own data.
- **Summaries and Browsing:** The `summary`, `movies`, and `series` routes give users insights into their watched content, organized by criteria like IMDb rating or release year.

With these features, the platform is both functional and easy to navigate.

---

## Tools for Reusability

The `helpers.py` file is a set of tools to make the app work more efficiently:
- **Error Messages:** The `apology` function creates custom messages when something goes wrong, like trying to add a duplicate movie.
- **Access Control:** The `login_required` decorator ensures that certain parts of the app can only be accessed by logged-in users, protecting sensitive features.

These utilities keep the code clean and allow functions to be reused across the app.

---

## The Database: Organizing Content

The SQLite database (`data.db`) is the backbone of the app. It stores all the data users interact with, divided into three tables:
1. **`users`:** Keeps track of usernames and password hashes for secure login.
2. **`titles`:** Stores details about movies and series, including the title, release year, IMDb rating, and type (movie or series).
3. **`user_titles`:** Links users to the titles they’ve watched, with information like watch dates and, for series, the number of episodes viewed.

The website uses a database derived from the official IMDb dataset, which is updated regularly. Therefore, to ensure the efficiency of My Tracker, this database must also be updated regularly, a process that is currently done manually. This guarantees access to a comprehensive and up-to-date catalog of films and TV series.

Two additional files help with processing and importing IMDb data:
- **`copy.py`:** Extracts relevant data from the official IMDb dataset.
- **`table.py`:** Structures the extracted data into a format compatible with the `titles` table in `data.db`.

These files ensure that the database remains accurate and that My Tracker has access to an extensive library of content for users to explore.

---

## User Interface: Templates and Styling

The app’s user interface is powered by templates in the `templates` folder and styled with `style.css`. The design prioritizes simplicity and usability.

### Landing and Layout
- **`index.html`:** The first page users see, welcoming them to the platform. It offers options to log in or register, setting the tone for the app.
- **`layout.html`:** A base template that provides a consistent structure across all pages, including a navigation bar, footer, and space for flash messages (like success or error notifications).

### Adding and Deleting Titles
- **`add_movie.html` and `add_series.html`:** These forms let users add movies or series to their watched lists. The forms include fields for watch dates and, for series, the number of episodes viewed.
- **`delete.html`:** A simple form to remove unwanted titles using their IMDb ID.

### Browsing and Summaries
- **`movies.html` and `series.html`:** These pages display lists of watched titles in a table format. Users can sort the lists by criteria like IMDb rating, release year, or watch date, making it easy to find what they’re looking for.
- **`summary.html`:** A quick overview of the most recent movies and series a user has watched, providing an at-a-glance update.

---

## Styling and Branding

The `style.css` file gives the app its visual identity. It uses a modern color palette to style the navigation bar and highlight the "MyTracker" brand. The design is clean, making the interface intuitive and easy to use.

---

## Managing Users

The app takes user security seriously. Passwords are never stored in plain text; instead, they’re hashed using the `werkzeug.security` library. The `login.html` and `register.html` templates guide users through secure login and registration processes.

---

## Searching and Sorting

One of the standout features is the ability to search for and sort content.
- **Searching:** Users can search for titles using `search_movies.html` or `search_series.html`. The app fetches results from the database and displays them in an organized list.
- **Sorting:** On the `movies.html` and `series.html` pages, users can sort their watched titles by different criteria, such as release year or IMDb rating. The sorting feature makes use of query parameters, allowing for dynamic updates without complex reloads.

---

## Bringing It All Together

**My Tracker** combines a clean design, powerful functionality, and robust data handling to create an easy-to-use tool for organizing movies and series. With support for regular updates from IMDb, the app ensures its users have access to the latest information. By focusing on both user experience and backend efficiency, My Tracker stands out as a practical and scalable solution for entertainment management.
