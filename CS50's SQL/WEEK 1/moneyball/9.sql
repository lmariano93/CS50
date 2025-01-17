SELECT "teams"."name", ROUND(AVG("salaries"."salary"),2) AS "avarage salary"
FROM "teams"
JOIN "salaries" ON "teams"."id" = "salaries"."team_id"
WHERE "salaries"."year" = '2001'
GROUP BY "salaries"."team_id"
ORDER BY "avarage salary" 
LIMIT 5;
