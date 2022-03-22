import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv('APP_ENV', '*******')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', '*******')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '*******')
DATABASE_HOST = os.getenv('DATABASE_HOST', '*******')
DATABASE_PORT = os.getenv('DATABASE_PORT', '*******')
DATABASE_NAME = os.getenv('DATABASE_NAME', '*******')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'test_db')

ALLOWED_HOSTS = ['http://loacalhost:3000', 'http://127.0.0.1:3000']
