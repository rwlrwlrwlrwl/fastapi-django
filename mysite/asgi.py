"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()

from fastapi import FastAPI
from polls.routers import choices_router
from polls.routers import questions_router

fastapp = FastAPI()
fastapp.include_router(questions_router, tags=["questions"], prefix="/question")
fastapp.include_router(choices_router, tags=["choices"], prefix="/choice")
