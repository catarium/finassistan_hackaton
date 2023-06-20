from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "category" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL
);;
        CREATE TABLE IF NOT EXISTS "expenses" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "sum" BIGINT NOT NULL,
    "date" DATE NOT NULL
);;
        ALTER TABLE "incomes" ADD "category_id" BIGINT NOT NULL;
        ALTER TABLE "incomes" ADD CONSTRAINT "fk_incomes_category_c69421d1" FOREIGN KEY ("category_id") REFERENCES "category" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "incomes" DROP CONSTRAINT "fk_incomes_category_c69421d1";
        ALTER TABLE "incomes" DROP COLUMN "category_id";
        DROP TABLE IF EXISTS "category";
        DROP TABLE IF EXISTS "expenses";"""
