import os
from functools import lru_cache

from dotenv import load_dotenv


class Settings:
    """Singleton setting class from .env file"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self._load_env()

    def _load_env(self):
        load_dotenv(
            os.path.join(os.path.dirname(__file__), f".env.{os.getenv('FAST_MODE')}")
        )
        self.FAST_MODE = os.getenv("FAST_MODE")
        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT")
        self.RELOAD = os.getenv("RELOAD")

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def to_dict(self):
        return self.__dict__


@lru_cache()
def get_settings():
    return Settings()
