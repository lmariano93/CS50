-- Represent information about directors
CREATE TABLE "directors" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "birth_date" DATE,
    "nationality" TEXT,
    PRIMARY KEY ("id")
);

-- Represent information about actors
CREATE TABLE "actors" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "birth_date" DATE,
    "nationality" TEXT,
    PRIMARY KEY ("id")
);

-- Represent information about movies
CREATE TABLE "movies" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "release_year" INTEGER NOT NULL,
    "genre" TEXT NOT NULL,
    "director_id" INTEGER,
    "duration" INTEGER,
    "rating" DECIMAL (4,2) NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY ("director_id") REFERENCES "directors" ("id")
);

-- Represent information about TV shows
CREATE TABLE "tv_shows" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "seasons" INTEGER,
    "episodes" INTEGER,
    "release_year" INTEGER NOT NULL,
    "genre" TEXT NOT NULL,
    "rating" DECIMAL (4,2) NOT NULL,
    PRIMARY KEY("id")
);

-- Table to link movies with actors
CREATE TABLE "movie_cast" (
    "movie_id" INTEGER,
    "actor_id" INTEGER,
    PRIMARY KEY("movie_id","actor_id"),
    FOREIGN KEY ("movie_id") REFERENCES "movies" ("id"),
    FOREIGN KEY ("actor_id") REFERENCES "actors" ("id")
);

-- Table to link TV shows with actors, including roles and seasons
CREATE TABLE "tv_show_cast" (
    "tv_show_id" INTEGER,
    "actor_id" INTEGER,
    "season" INTEGER,
    "role_type" TEXT CHECK("role_type" IN ('Regular', 'Recurring', 'Guest')),
    PRIMARY KEY("tv_show_id","actor_id","season"),
    FOREIGN KEY ("tv_show_id") REFERENCES "tv_shows" ("id"),
    FOREIGN KEY ("actor_id") REFERENCES "actors" ("id")
);


-- Indexes for the "directors" table
CREATE INDEX "directors_last_name_index" ON "directors"("last_name");

-- Indexes for the "actors" table
CREATE INDEX "actors_last_name_index" ON "actors"("last_name");

-- Indexes for the "movies" table
CREATE INDEX "movies_director_id_index" ON "movies"("director_id");
CREATE INDEX "movies_release_year_index" ON "movies"("release_year");
CREATE INDEX "movies_genre_index" ON "movies"("genre");

-- Indexes for the "tv_shows" table
CREATE INDEX "tv_shows_release_year_index" ON "tv_shows"("release_year");
CREATE INDEX "tv_shows_genre_index" ON "tv_shows"("genre");

-- Indexes for the "movie_cast" table
CREATE INDEX "movie_cast_actor_id_index" ON "movie_cast"("actor_id");

-- Indexes for the "tv_show_cast" table
CREATE INDEX "tv_show_cast_actor_id_index" ON "tv_show_cast"("actor_id");
CREATE INDEX "tv_show_cast_show_season_index" ON "tv_show_cast"("tv_show_id", "season");
