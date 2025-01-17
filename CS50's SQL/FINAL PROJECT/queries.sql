--Retrieve all movies by a specific director
SELECT "title", "release_year", "genre", "rating"
FROM "movies"
WHERE "director_id" = (
    SELECT "id"
    FROM "directors"
    WHERE "last_name" = 'Nolan' AND "first_name" = 'Christopher'
);

--List all TV Shows in a specific genre
SELECT "title", "seasons", "episodes", "release_year", "rating"
FROM "tv_shows"
WHERE "genre" = 'Drama'
ORDER BY "rating" DESC;

--Find all movies released in a given year
SELECT "title", "genre", "rating"
FROM "movies"
WHERE "release_year" = 2022
ORDER BY "rating" DESC;

--Get the cast of a specific movie
SELECT "actors"."first_name", "actors"."last_name"
FROM "actors"
WHERE "actors"."id" IN (
    SELECT "movie_cast"."actor_id"
    FROM "movie_cast"
    WHERE "movie_cast"."movie_id" = (
        SELECT "movies"."id"
        FROM "movies"
        WHERE "movies"."title" = 'Inception'
    )
);

--List all TV shows an actor appeared in as a regular
SELECT "tv_shows"."title", "tv_shows"."seasons","tv_shows"."release_year", "tv_shows"."genre"
FROM "tv_shows"
WHERE "tv_shows"."id" IN (
    SELECT "tv_show_cast"."tv_show_id"
    FROM "tv_show_cast"
    WHERE "tv_show_cast"."actor_id" = (
        SELECT "actors"."id"
        FROM "actors"
        WHERE "actors"."last_name" = 'Cranston'
        AND "actors"."first_name" = 'Bryan'
    )
    AND "tv_show_cast"."role_type" = 'Regular'
);

-- Count movies grouped by genre
SELECT "genre", COUNT(*) AS "movie_count"
FROM "movies"
GROUP BY "genre";

-- Show the top 10 movies of a specific genre
SELECT "title", "release_year", "rating"
FROM "movies"
WHERE "genre" = 'Action'
ORDER BY "rating" DESC
LIMIT 10;

--Get the average rating of TV Shows by genre
SELECT "title", "release_year", "rating"
FROM "tv_shows"
WHERE "genre" = 'Comedy'
ORDER BY "rating" DESC
LIMIT 10;

--Find which tv show the actor appears in and how many episodes he appears in each one
SELECT
    "actors"."first_name" AS "actor_first_name",
    "actors"."last_name" AS "actor_last_name",
    "tv_shows"."title" AS "tv_show_title",
    COUNT("tv_show_cast"."season") AS "episode_count"
FROM "actors"
JOIN "tv_show_cast" ON "actors"."id" = "tv_show_cast"."actor_id"
JOIN "tv_shows" ON "tv_show_cast"."tv_show_id" = "tv_shows"."id"
WHERE "actors"."id" = (
    SELECT "actors"."id"
    FROM "actors"
    WHERE "actors"."first_name" = 'Leonardo'
    AND "actors"."last_name" = 'DiCaprio'
)
GROUP BY "actors"."first_name", "actors"."last_name", "tv_shows"."title"
ORDER BY "tv_shows"."title";

--Find all movies directed by directors Who also ccted in their own films
SELECT "movies"."title", "movies"."release_year", "directors"."first_name", "directors"."last_name"
FROM "movies"
JOIN "directors" ON "movies"."director_id" = "directors"."id"
WHERE "directors"."id" IN (
    SELECT DISTINCT "movies"."director_id"
    FROM "movies"
    JOIN "movie_cast" ON "movies"."id" = "movie_cast"."movie_id"
    JOIN "actors" ON "movie_cast"."actor_id" = "actors"."id"
    WHERE "actors"."first_name" = "directors"."first_name"
    AND "actors"."last_name" = "directors"."last_name"
)
ORDER BY "movies"."release_year" DESC;

--Find directors who Have Worked with the Same Actor on Multiple Movies
SELECT
    "directors"."first_name" AS "director_first_name",
    "directors"."last_name" AS "director_last_name",
    "actors"."first_name" AS "actor_first_name",
    "actors"."last_name" AS "actor_last_name",
    COUNT(DISTINCT "movies"."id") AS "movie_count"
FROM "directors"
JOIN "movies" ON "directors"."id" = "movies"."director_id"
JOIN "movie_cast" ON "movies"."id" = "movie_cast"."movie_id"
JOIN "actors" ON "movie_cast"."actor_id" = "actors"."id"
GROUP BY "directors"."id", "actors"."id"
HAVING COUNT(DISTINCT "movies"."id") > 1
ORDER BY "movie_count" DESC, "directors"."last_name", "actors"."last_name";

--List the Top 5 Actors Who Have Appeared in the Most Number of Highly Rated Movies
SELECT "actors"."first_name", "actors"."last_name", COUNT("movies"."id") AS "high_rating_movie_count"
FROM "actors"
JOIN "movie_cast" ON "actors"."id" = "movie_cast"."actor_id"
JOIN "movies" ON "movie_cast"."movie_id" = "movies"."id"
WHERE "movies"."rating" >= 9.0
GROUP BY "actors"."first_name", "actors"."last_name"
ORDER BY "high_rating_movie_count" DESC
LIMIT 5;

