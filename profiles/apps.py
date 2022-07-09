"""
Config file for profiles app
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Profiles app Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
