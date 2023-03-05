# pylint: disable=too-few-public-methods

import os
import pathlib
import sys
from email.contentmanager import raw_data_manager

from pydantic import BaseSettings


class Settings(BaseSettings):
    """load setting values from .env file"""
    disable_all_logging: bool
    is_debugging: bool
    
    class Config:
        """The configuration for the settings class."""

        case_sensitive = False


def get_default_settings_file() -> str:
    """Return default settgins"""

    env_file = ".env"  # private.env for real transaction
    # env_file = "private.env"  # private.env for real transaction
    root = pathlib.Path(__file__).parent.absolute()
    env_path = os.path.join(root, env_file)
    return env_path


def load_settings():
    """Load settings"""
    env_file = get_default_settings_file()
    return Settings(_env_file=env_file)


SETTINGS = load_settings()