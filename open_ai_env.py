import os
from dotenv import load_dotenv, find_dotenv


def env_func():
    load_dotenv(dotenv_path=find_dotenv(), override=True)
