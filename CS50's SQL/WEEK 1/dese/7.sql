SELECT "schools"."name" FROM "schools"
JOIN "districts" ON "schools"."district_id" = "districts"."id"
WHERE "schools"."city" = 'Cambridge'
AND "schools"."district_id" = (
    SELECT "districts"."id" FROM "districts"
    WHERE "districts"."name" Like '%Cambridge%'
);


