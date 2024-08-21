from django.apps import AppConfig
from fastapi import FastAPI
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
