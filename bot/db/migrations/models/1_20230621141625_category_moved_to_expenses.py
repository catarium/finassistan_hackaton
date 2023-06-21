from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "expenses" ADD "category_id" BIGINT NOT NULL;
        ALTER TABLE "incomes" DROP COLUMN "category_id";
        ALTER TABLE "expenses" ADD CONSTRAINT "fk_expenses_categori_b8733eb5" FOREIGN KEY ("category_id") REFERENCES "categories" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "expenses" DROP CONSTRAINT "fk_expenses_categori_b8733eb5";
        ALTER TABLE "incomes" ADD "category_id" BIGINT NOT NULL;
        ALTER TABLE "expenses" DROP COLUMN "category_id";
        ALTER TABLE "incomes" ADD CONSTRAINT "fk_incomes_categori_1a3d45b0" FOREIGN KEY ("category_id") REFERENCES "categories" ("id") ON DELETE CASCADE;"""
