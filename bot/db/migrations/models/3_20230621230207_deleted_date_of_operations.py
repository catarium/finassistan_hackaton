from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "operations" DROP COLUMN "date";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "operations" ADD "date" DATE NOT NULL;"""
