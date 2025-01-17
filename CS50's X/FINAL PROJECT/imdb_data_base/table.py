import csv
import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('imdb_titles.db')
cursor = conn.cursor()

# Create the unified table
cursor.execute("""
CREATE TABLE IF NOT EXISTS titles (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    release_year INTEGER,
    imdb_rating REAL,
    duration INTEGER,
    episodes INTEGER,
    type TEXT CHECK (type IN ('movie', 'series'))
)
""")

# Dictionary to store title information from title.basics
title_data = {}

# Read title.basics.tsv to gather information on type, title, release year, and duration
with open('title.basics.tsv', newline='', encoding='utf-8') as basics_file:
    reader = csv.DictReader(basics_file, delimiter='\t')
    for row in reader:
        title_type = row['titleType']

        # Categorize types into 'movie' and 'series'
        if title_type in ['movie', 'tvMovie', 'short']:
            title_data[row['tconst']] = {
                "title": row['primaryTitle'],
                "release_year": int(row['startYear']) if row['startYear'] != '\\N' else None,
                "duration": int(row['runtimeMinutes']) if row['runtimeMinutes'] != '\\N' else None,
                "type": 'movie'  # 'movie' category
            }
        elif title_type in ['tvSeries', 'tvMiniSeries']:
            title_data[row['tconst']] = {
                "title": row['primaryTitle'],
                "release_year": int(row['startYear']) if row['startYear'] != '\\N' else None,
                "duration": None,  # Duration is not applicable for series, only episodes
                "type": 'series'  # 'series' category
            }
        else:
            # Log unexpected types for later review
            print(f"Skipping title with unexpected type: {title_type} (ID: {row['tconst']})")

# Read title.ratings.tsv to get IMDb rating for each title
with open('title.ratings.tsv', newline='', encoding='utf-8') as ratings_file:
    reader = csv.DictReader(ratings_file, delimiter='\t')
    for row in reader:
        tconst = row['tconst']
        if tconst in title_data:
            title_data[tconst]["imdb_rating"] = float(row['averageRating']) if row['averageRating'] != '\\N' else None

# Count episodes for each series by reading title.episode.tsv
episode_counts = {}

with open('title.episode.tsv', newline='', encoding='utf-8') as episodes_file:
    reader = csv.DictReader(episodes_file, delimiter='\t')
    for row in reader:
        parent_tconst = row['parentTconst']
        if parent_tconst in title_data and title_data[parent_tconst]['type'] == 'series':
            if parent_tconst in episode_counts:
                episode_counts[parent_tconst] += 1
            else:
                episode_counts[parent_tconst] = 1

# Insert data into the titles table
for tconst, info in title_data.items():
    episodes = episode_counts.get(tconst, None) if info["type"] == 'series' else None
    cursor.execute("""
        INSERT INTO titles (id, title, release_year, imdb_rating, duration, episodes, type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (tconst, info["title"], info["release_year"], info.get("imdb_rating"), info["duration"], episodes, info["type"]))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data successfully loaded into the database.")
