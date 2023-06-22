from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "incomes" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "expenses" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;"""
