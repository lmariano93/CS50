SELECT "friend_id" FROM "friends"
WHERE "user_id" = (
    SELECT "id" FROM "users"
    WHERE "username" = 'lovelytrust487'
)

INTERSECT

SELECT "friend_id" FROM "friends"
WHERE "user_id" = (
    SELECT "users"."id" FROM "users"
    WHERE "username" = 'exceptionalinspiration482'
);
