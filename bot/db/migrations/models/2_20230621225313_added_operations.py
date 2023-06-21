from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "operations" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "operation_type" TEXT NOT NULL,
    "operation_id" BIGINT NOT NULL,
    "date" DATE NOT NULL
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "operations";"""
