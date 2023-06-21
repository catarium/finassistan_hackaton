from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "operations" ADD "date" DATE NOT NULL;
        ALTER TABLE "operations" ADD "user_id" BIGINT NOT NULL;
        ALTER TABLE "operations" ADD CONSTRAINT "fk_operatio_users_125d68af" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "operations" DROP CONSTRAINT "fk_operatio_users_125d68af";
        ALTER TABLE "operations" DROP COLUMN "date";
        ALTER TABLE "operations" DROP COLUMN "user_id";"""
