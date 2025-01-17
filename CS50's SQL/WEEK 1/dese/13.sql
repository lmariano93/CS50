SELECT "districts"."name", "staff_evaluations"."exemplary" AS "% Staff exemplary", ROUND(AVG("graduation_rates"."graduated"),2) AS "District graduation rates"
FROM "districts"
LEFT JOIN "staff_evaluations" ON "districts"."id" = "staff_evaluations"."district_id"
LEFT JOIN "schools" ON "districts"."id" = "schools"."district_id"
LEFT JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id"
WHERE "districts"."name" NOT LIKE "%(District)%"
AND "districts"."name" NOT LIKE "%non-op%"
GROUP BY "districts"."name"
ORDER BY "staff_evaluations"."exemplary" DESC, "districts"."name";




