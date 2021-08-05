import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.')/'.env'

load_dotenv(dotenv_path=env_path) # This sets the path of the env file
class Config:
    DEBUG = os.getenv("DEBUG")
    TESTING = os.getenv("TESTING")
    SERVER = os.getenv("SERVER")
    SECRET_KEY = os.getenv("SECRET_KEY")

