.import --csv meteorites.csv temp

DELETE FROM "temp"
WHERE "nametype" = 'Relict';

UPDATE "temp"
SET "mass" = NULL
WHERE "mass" = '';

UPDATE "temp"
SET "year" = NULL
WHERE "year" = '';

UPDATE "temp"
SET "lat" = NULL
WHERE "lat" = '';

UPDATE "temp"
SET "long" = NULL
WHERE "long" = '';

CREATE TABLE "meteorites" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT,
    "class" TEXT,
    "mass" DECIMAL (10,2),
    "discovery" TEXT,
    "year" INTEGER,
    "lat" DECIMAL (10,2),
    "long" DECIMAL (10,2)
);

INSERT INTO "meteorites" ("name","class","mass","discovery","year","lat","long")
SELECT
    "name",
    "class",
    ROUND(CAST("mass" AS DECIMAL),2),
    "discovery",
    CAST("year" AS INTEGER),
    ROUND(CAST("lat" AS DECIMAL),2),
    ROUND(CAST("long" AS DECIMAL),2)
FROM "temp"
ORDER BY CAST("year" AS INTEGER),"name";

DROP TABLE "temp";

