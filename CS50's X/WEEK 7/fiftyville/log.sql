-- Find crime scene description
SELECT description
FROM crime_scene_reports
WHERE year = 2023 AND month = 7 AND day = 28
AND street = 'Humphrey Street';

--From the scene description it was possible to infer that the crime occurred at 10:15am and that all witnesses
--mentioned "bakery" in their testimonials
SELECT name, transcript
FROM interviews
WHERE transcript LIKE "%bakery%"
AND year = 2023 AND month = 7 AND day = 28;

--The witness "Ruth" reported that the thief's car left the bakery between 10:15am and 10:25am
SELECT name
FROM people
WHERE people.license_plate IN
    (SELECT bakery_security_logs.license_plate
    FROM bakery_security_logs
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND hour BETWEEN 10 AND 11
    AND minute BETWEEN 10 AND 25
    AND activity = 'exit')

INTERSECT

-- The witness "Eugene" reported that the thief used the ATM on Legeet Street to withdrain some money
SELECT name
FROM people
WHERE id IN
    (SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE year = 2023 AND month = 7 AND day = 28
        AND transaction_type = 'withdraw'
        AND atm_location = 'Leggett Street'))

INTERSECT

--The witness "Raymond" reported that the thief made a call lasting less than a minute after leaving the bakery
SELECT name
FROM people
WHERE phone_number IN
    (SELECT caller
    FROM phone_calls
    WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60)

INTERSECT

--"Raymond" also said that the thief would take the first flight on the 29th to leave Fiftyville
SELECT name
FROM people
WHERE passport_number IN
    (SELECT passport_number
    FROM passengers
    WHERE flight_id =
        (SELECT flights.id
        FROM flights
        WHERE origin_airport_id = (SELECT airports.id FROM airports WHERE city = 'Fiftyville')
        AND year = 2023 AND month = 7 AND day = 29
        ORDER BY hour, minute LIMIT 1)
    );

--Intersecting information from witnesses leads to Bruce as a thief

--To discover your accomplice, we checked to whom Bruce's call of less than a minute on the 28th was made
SELECT name
FROM people
WHERE phone_number IN
    (SELECT receiver
    FROM phone_calls
    WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
    AND caller IN
        (SELECT phone_number
        FROM people
        WHERE name = "Bruce")
    );

--In the query where we look for passengers on the first flight on the 29th (line 55) we can see that Robin didn't take the flight,
--even so, his name is the only one that fits what the witness "Raymond" said, being the likely accomplice.

--We discovered Bruce's destine by checking the destination of the first flight leaving on the 29th from Fiftyville
SELECT city
FROM airports
WHERE airports.id =
    (SELECT destination_airport_id
    FROM flights
    WHERE origin_airport_id = (SELECT airports.id FROM airports WHERE city = 'Fiftyville')
    AND year = 2023 AND month = 7 AND day = 29
    ORDER BY hour, minute LIMIT 1);










