SELECT "year", ROUND(AVG("salary"),2) AS "avarage salary" FROM "salaries"
GROUP BY "year"
ORDER BY "year" DESC;
