from bot.core.config import config

DATABASE_CONFIG = {
    "connections": {
        "default": f'postgres://{config.POSTGRES_USER}:'
                   f'{config.POSTGRES_PASSWORD}@'
                   f'{config.POSTGRES_HOST}:'
                   f'{config.POSTGRES_PORT}/'
                   f'{config.POSTGRES_NAME}'},
    "apps": {
        "models": {
            "models": ["bot.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}