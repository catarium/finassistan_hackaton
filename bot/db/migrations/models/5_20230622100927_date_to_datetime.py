from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE TIMESTAMPTZ USING "date"::TIMESTAMPTZ;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;
        ALTER TABLE "operations" ALTER COLUMN "date" TYPE DATE USING "date"::DATE;"""
