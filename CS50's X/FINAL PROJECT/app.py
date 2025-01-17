import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from helpers import apology, login_required

# Initialize Flask application
app = Flask(__name__)

# Configure session to use the filesystem instead of signed cookies
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data.db")

# Route for adding a movie
@app.route("/add_movie", methods=["GET", "POST"])
@login_required
def add_movie():
    if request.method == "GET":
        # Retrieve title ID from the query string
        title_id = request.args.get("title_id")

        if title_id:
            # Fetch the selected movie details
            movie_info = db.execute("SELECT * FROM titles WHERE id = ?", title_id)
            if movie_info:
                movie_info = movie_info[0]
                return render_template("add_movie.html", movie_info=movie_info)

        # Redirect to the search page if no title ID is provided
        return redirect("/search_movies")

    elif request.method == "POST":
        # Retrieve form data
        title_id = request.form.get("title_id")
        watched_on = request.form.get("watched_on")

        if title_id and watched_on:
            # Check if the movie is already in the user's title list
            existing_movie = db.execute("""
                SELECT * FROM user_titles WHERE user_id = ? AND title_id = ?
            """, session["user_id"], title_id)

            if existing_movie:
                # If the movie is already in the list, displays an error message
                flash("You have already added this movie to your watched list.", "danger")
                return redirect("/search_movies")

            # If it doesn't exist, add the movie
            db.execute("""
                INSERT INTO user_titles (user_id, title_id, watched_on)
                VALUES (?, ?, ?)
            """, session["user_id"], title_id, watched_on)

            flash("Movie added to your watched list!", "success")
            return redirect("/summary")

        # Flash an error message if the form data is invalid
        flash("Error adding movie", "danger")
        return redirect("/search_movies")


# Route for adding a series
@app.route("/add_series", methods=["GET", "POST"])
@login_required
def add_series():
    # Adds a series to the user's watched list with a date and number of episodes viewed
    if request.method == "GET":
        # Retrieve the title ID from the query string
        title_id = request.args.get("title_id")

        if title_id:
            # Fetch the selected series details
            series_info = db.execute("SELECT * FROM titles WHERE id = ?", title_id)
            if series_info:
                series_info = series_info[0]
                return render_template("add_series.html", series_info=series_info)

        # Redirect to the search page if no title ID is provided
        return redirect("/search_series")

    elif request.method == "POST":
        # Retrieve form data
        title_id = request.form.get("title_id")
        watched_on = request.form.get("watched_on")
        viewed_episodes = request.form.get("viewed_episodes")

        if title_id and watched_on and viewed_episodes:
            # Check if the series is already in the user's watched list
            existing_series = db.execute("""
                SELECT * FROM user_titles WHERE user_id = ? AND title_id = ?
            """, session["user_id"], title_id)

            # If the series is already in the list, display an error message
            if existing_series:
                flash("You have already added this series to your watched list.", "danger")
                flash("If you want to update the number of episodes watched, remove this series from your list, add it again, and take the opportunity to update the 'watched on' date as well.", "warning")
                return redirect("/search_series")

            # Otherwise, insert the series into the user_titles table
            db.execute("""
                INSERT INTO user_titles (user_id, title_id, watched_on, viewed_episodes)
                VALUES (?, ?, ?, ?)
            """, session["user_id"], title_id, watched_on, viewed_episodes)

            flash("Series added to your watched list!", "success")
            return redirect("/summary")

        # Flash an error message if the form data is incomplete
        flash("Error adding series. Please make sure all fields are filled in.", "danger")
        return redirect("/search_series")


# Route for deleting a movie or series
@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    # Delete a movie or series from the user's watched list
    if request.method == "POST":
        # Retrieve IMDb ID and user ID
        imdb_id = request.form.get("imdb_id")
        user_id = session["user_id"]

        # Check if the IMDb ID exists in the user's watched list
        result = db.execute("""
            SELECT * FROM user_titles
            WHERE user_id = ? AND title_id = (SELECT id FROM titles WHERE id = ?)
        """, user_id, imdb_id)

        if result:
            # Delete the title from the user's watched list
            db.execute("""
                DELETE FROM user_titles
                WHERE user_id = ? AND title_id = (SELECT id FROM titles WHERE id = ?)
            """, user_id, imdb_id)

            flash("Movie or Series deleted successfully.", "success")
        else:
            flash("IMDb ID not found in your watched list.", "danger")

    return render_template("delete.html")

# Route for the home page
@app.route("/")
def index():
    # Display the homepage
    # Redirect logged-in users to the summary page
    if session.get("user_id"):
        return redirect("/summary")
    return render_template("index.html")

# Route for logging in
@app.route("/login", methods=["GET", "POST"])
def login():
    # Log the user in
    session.clear()  # Clear any existing session

    if request.method == "POST":
        # Retrieve form data
        username = request.form.get("username")
        password = request.form.get("password")

        # Validate input
        if not username or not password:
            flash("Must provide username and password", "danger")
            return redirect("/login")

        # Query the database for the user
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Verify username and password
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username and/or password", "danger")
            return redirect("/login")

        # Remember the user's ID in the session
        session["user_id"] = rows[0]["id"]
        flash("Logged in successfully", "success")
        return redirect("/summary")

    return render_template("login.html")

# Route for logging out
@app.route("/logout")
def logout():
    # Log the user out by clearing the session
    session.clear()
    return redirect("/")

# Route for listing all movies
@app.route("/movies")
@login_required
def movies():
    # Display all movies watched by the user
    user_id = session["user_id"]

    # Get the sort criteria from the URL parameter, default to 'title'
    sort_by = request.args.get("sort_by", "title")  # Default sorting by 'title'

    # Query the database for all movies watched by the user with dynamic sorting
    query = f"""
        SELECT t.id AS imdb_id, t.title, t.release_year, t.imdb_rating, ut.watched_on, t.duration
        FROM user_titles ut
        JOIN titles t ON ut.title_id = t.id
        WHERE ut.user_id = ? AND t.type = 'movie'
        ORDER BY {sort_by} ASC
    """

    movies = db.execute(query, user_id)

    # Pass the 'sort_by' value to the template to highlight the selected sorting option
    return render_template("movies.html", movies=movies, sort_by=sort_by)


# Route for registering a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    # Register a new user
    if request.method == "POST":
        # Retrieve form data
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate input
        if not username or not password or not confirmation:
            flash("Must provide username, password, and confirmation", "danger")
            return redirect("/register")

        # Ensure passwords match
        if password != confirmation:
            flash("Passwords do not match", "danger")
            return redirect("/register")

        # Hash the password
        hashed = generate_password_hash(password)

        # Insert new user into the database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed)

        flash("Registered successfully", "success")
        return redirect("/login")

    return render_template("register.html")

# Route for searching movies
@app.route("/search_movies", methods=["GET"])
@login_required
def search_movies():
    # Search movies by title
    movie_list = []

    # Retrieve the movie title from the query string
    movie_title = request.args.get("movie_title")
    if movie_title:
        # Query the database for movies matching the title
        movie_list = db.execute(
            "SELECT * FROM titles WHERE (LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) = ?) AND type = 'movie' ORDER BY release_year DESC",
            f"% {movie_title.lower()} %",
            f"{movie_title.lower()} %",
            f"% {movie_title.lower()}",
            f"%{movie_title.lower()}:%",
            f"%{movie_title.lower()}.%",
            f"%{movie_title.lower()}!%",
            movie_title.lower()
        )
        if not movie_list:
            flash("No movies found. Please check the title.", "danger")

    return render_template("search_movies.html", movie_list=movie_list)

# Route for searching series
@app.route("/search_series", methods=["GET"])
@login_required
def search_series():
    # Search series by title
    series_list = []

    # Retrieve the series title from the query string
    series_title = request.args.get("series_title")
    if series_title:
        series_list = db.execute(
            "SELECT * FROM titles WHERE (LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) LIKE ? OR LOWER(title) = ?) AND type = 'series' ORDER BY release_year DESC",
            f"% {series_title.lower()} %",
            f"{series_title.lower()} %",
            f"% {series_title.lower()}",
            f"%{series_title.lower()}:%",
            f"%{series_title.lower()}.%",
            f"%{series_title.lower()}!%",
            series_title.lower()
        )

        if not series_list:
            flash("No series found. Please check the title.", "danger")

    return render_template("search_series.html", series_list=series_list)

# Route for listing all series
@app.route("/series")
@login_required
def series():
    # Display all series watched by the user
    user_id = session["user_id"]
    sort_by = request.args.get("sort_by", "title")  # Sort parameter

    # Sort based on parameter
    query = f"""
        SELECT t.id AS imdb_id, t.title, t.release_year, t.imdb_rating, ut.watched_on, ut.viewed_episodes, t.episodes AS total_episodes
        FROM user_titles ut
        JOIN titles t ON ut.title_id = t.id
        WHERE ut.user_id = ? AND t.type = 'series'
        ORDER BY {sort_by} ASC
    """

    series = db.execute(query, user_id)

    return render_template("series.html", series=series, sort_by=sort_by)


# Route for the summary page
@app.route("/summary")
@login_required
def summary():
    # Display a summary of the 10 most recent movies and series watched by the user
    user_id = session["user_id"]

    # Query the database for the 5 most recent movies
    movies = db.execute("""
        SELECT t.id AS imdb_id, t.title, t.release_year, t.imdb_rating, ut.watched_on, t.duration
        FROM user_titles ut
        JOIN titles t ON ut.title_id = t.id
        WHERE ut.user_id = ? AND t.type = 'movie'
        ORDER BY ut.watched_on DESC
        LIMIT 5
    """, user_id)

    # Query the database for the 5 most recent series
    series = db.execute("""
        SELECT t.id AS imdb_id, t.title, t.release_year, t.imdb_rating, ut.watched_on, ut.viewed_episodes, t.episodes AS total_episodes
        FROM user_titles ut
        JOIN titles t ON ut.title_id = t.id
        WHERE ut.user_id = ? AND t.type = 'series'
        ORDER BY ut.watched_on DESC
        LIMIT 5
    """, user_id)

    return render_template("summary.html", movies=movies, series=series)
