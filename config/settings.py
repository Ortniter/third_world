from decouple import config

# DATABASE ENVS
DB_HOST = config('POSTGRES_HOST')
DB_PORT = config('POSTGRES_PORT')
DB_DB = config('POSTGRES_DB')
DB_USER = config('POSTGRES_USER')
DB_PASSWORD = config('POSTGRES_PASSWORD')

# COMMON ENVS
SHARED_FOLDER_PATH = config('SHARED_FOLDER_PATH')
TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
