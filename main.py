import os
import asyncio
import aiohttp
import yaml
from aiohttp import web
from routes import setup_routes
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp.web import run_app

from app.web.app import setup_app

if __name__ == "__main__":
    run_app(
        setup_app(
            config_path=os.path.join(os.path.dirname(__file__), "config.yml")
        )
    )
