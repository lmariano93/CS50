# Design Document

By Lucas Pinheiro Mariano

Video overview: <URL https://youtu.be/e4hs7WbTq9o>

## Scope

The purpose of this database is to manage and track information related to movies, TV shows, directors, and actors. The scope includes:

- Directors: Captures essential details about directors.
- Actors: Includes information about actors.
- Movies: Tracks movies, their attributes, and associations with directors and actors.
- TV Shows: Manages TV show data, including seasons and episodes.
- Movie Cast: Links movies with actors.
- TV Show Cast: Links TV shows with actors and their roles.

## Functional Requirements

Users should be able to:

- Retrieve movies directed by a specific director.
- List TV shows by genre and other attributes.
- Find movies released in a given year.
- Get the cast of a specific movie.
- List TV shows an actor appeared in as a regular.
- Count movies grouped by genre.
- Show top movies of a specific genre.
- Get the average rating of TV shows by genre.
- Find out in which series an actor appears and the number of episodes.
- Find movies directed by directors who acted in their own films.
- Identify directors who have worked with the same actor in multiple movies.
- List top actors who appeared in the most number of highly rated movies.

## Representation

### Entities

1. Directors
    - Attributes: id (INTEGER, PRIMARY KEY), first_name (TEXT, NOT NULL), last_name (TEXT, NOT NULL), birth_date (DATE), nationality (TEXT).
    - Reasoning: Chosen types are appropriate for storing names and dates. The id is unique for identification, and other attributes are added to capture relevant director details.

2. Actors
    - Attributes: id (INTEGER, PRIMARY KEY), first_name (TEXT, NOT NULL), last_name (TEXT, NOT NULL), birth_date (DATE), nationality (TEXT).
    - Reasoning: Similar to directors, the types and constraints ensure uniqueness and proper storage of actor information.

3. Movies
    - Attributes: id (INTEGER, PRIMARY KEY), title (TEXT, NOT NULL), release_year (INTEGER, NOT NULL), genre (TEXT, NOT NULL), director_id (INTEGER, FOREIGN KEY), duration (INTEGER), rating (DECIMAL(4,2), NOT NULL).
    - Reasoning: Chosen attributes capture essential movie information. The FOREIGN KEY constraint links to the directors table, ensuring data integrity.

4. TV Shows
    - Attributes: id (INTEGER, PRIMARY KEY), title (TEXT, NOT NULL), seasons (INTEGER), episodes (INTEGER), release_year (INTEGER, NOT NULL), genre (TEXT, NOT NULL), rating (DECIMAL(4,2), NOT NULL).
    - Reasoning: Attributes capture key details about TV shows. The rating and release_year attributes are used for sorting and filtering.

5. Movie Cast
    - Attributes: movie_id (INTEGER, FOREIGN KEY), actor_id (INTEGER, FOREIGN KEY), PRIMARY KEY (movie_id, actor_id).
    - Reasoning: This table establishes many-to-many relationships between movies and actors.

6. TV Show Cast
    - Attributes: tv_show_id (INTEGER, FOREIGN KEY), actor_id (INTEGER, FOREIGN KEY), season (INTEGER), role_type (TEXT, CHECK(role_type IN ('Regular', 'Recurring', 'Guest'))), PRIMARY KEY (tv_show_id, actor_id, season).
    - Reasoning: Captures actor roles in TV shows, including season and role type. The CHECK constraint ensures valid role types.

### Relationships

The relationships between entities are as follows:
    - A director can direct multiple movies, but each movie has only one director.
    - An actor can appear in multiple movies and TV shows, and each movie or TV show can have multiple actors.
    - Movies and TV shows are linked to actors through the movie_cast and tv_show_cast tables, respectively.

## Optimizations

    - Directors: Index on last_name.
    - Actors: Index on last_name.
    - Movies: Indexes on director_id, release_year, and genre.
    - TV Shows: Indexes on release_year and genre.
    - Movie Cast: Index on actor_id.
    - TV Show Cast: Indexes on actor_id and tv_show_id, season.

## Limitations

- The schema does not include information about directors, writers or producers of TV shows once each episode or/and season can have differents people in these positions.
- The design does not support multiple directors or co-directors, it assumes a single director per movie. Also, it does not have information about producers.
- Additional details such as detailed production budgets, detailed episode scripts, reviews or specific episode data are not included.


