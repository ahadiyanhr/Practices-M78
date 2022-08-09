CREATE TABLE "User"(
    "user_id" INTEGER NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "national_id" CHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "phone_number" CHAR(255) NULL,
    "authentication_code" CHAR(255) NOT NULL,
    "is_admin" BOOLEAN NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("user_id");
CREATE TABLE "Bank_Account"(
    "account_id" INTEGER NOT NULL,
    "owner" INTEGER NOT NULL,
    "balance" INTEGER NOT NULL
);
ALTER TABLE
    "Bank_Account" ADD PRIMARY KEY("account_id");
CREATE TABLE "Credit_Card"(
    "credit_id" INTEGER NOT NULL,
    "owner" INTEGER NOT NULL,
    "balance" INTEGER NOT NULL
);
ALTER TABLE
    "Credit_Card" ADD PRIMARY KEY("credit_id");
CREATE TABLE "Trip"(
    "trip_id" INTEGER NOT NULL,
    "origin" VARCHAR(255) NOT NULL,
    "destination" VARCHAR(255) NOT NULL,
    "fare" INTEGER NOT NULL,
    "authentication_code" CHAR(255) NOT NULL,
    "card_type" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Trip" ADD PRIMARY KEY("trip_id");
CREATE TABLE "Limited_Card"(
    "limited_id" INTEGER NOT NULL,
    "owner" INTEGER NOT NULL,
    "balance" INTEGER NOT NULL
);
ALTER TABLE
    "Limited_Card" ADD PRIMARY KEY("limited_id");
CREATE TABLE "Single_Card"(
    "single_id" INTEGER NOT NULL,
    "owner" INTEGER NOT NULL,
    "balance" INTEGER NOT NULL
);
ALTER TABLE
    "Single_Card" ADD PRIMARY KEY("single_id");
ALTER TABLE
    "Bank_Account" ADD CONSTRAINT "bank_account_owner_foreign" FOREIGN KEY("owner") REFERENCES "User"("user_id");
ALTER TABLE
    "Credit_Card" ADD CONSTRAINT "credit_card_owner_foreign" FOREIGN KEY("owner") REFERENCES "User"("user_id");
ALTER TABLE
    "Limited_Card" ADD CONSTRAINT "limited_card_owner_foreign" FOREIGN KEY("owner") REFERENCES "User"("user_id");
ALTER TABLE
    "Single_Card" ADD CONSTRAINT "single_card_owner_foreign" FOREIGN KEY("owner") REFERENCES "User"("user_id");