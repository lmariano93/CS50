CREATE TABLE "ingredients" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "price_unit" DECIMAL(10,2),
    PRIMARY KEY("id")
);

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "gluten_free" TEXT NOT NULL CHECK("gluten_free" IN ('yes', 'no')),
    "price" DECIMAL(10,2),
    "ingredient_id" INTEGER,
    PRIMARY KEY("id"),

    FOREIGN KEY ("ingredient_id") REFERENCES "ingredients"("id")
);

CREATE TABLE "orders" (
    "id" INTEGER,
    "donut_id" TEXT NOT NULL,
    "customer_id" TEXT NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY ("customer_id") REFERENCES "costumers"("id")
);

CREATE TABLE "costumers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "history" (
    "id" INTEGER,
    "customer_id" TEXT NOT NULL,
    "order_id" INTEGER,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id"),
    FOREIGN KEY ("customer_id") REFERENCES "costumers"("id"),
    FOREIGN KEY ("order_id") REFERENCES "orders"("id")
);
