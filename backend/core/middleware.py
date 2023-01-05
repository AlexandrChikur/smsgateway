import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")
django.setup()

import jwt
from django.db import close_old_connections
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.authtoken.models import Token
from datetime import datetime

ALGORITHM = "HS256"


@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        close_old_connections()
        try:
            token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
            limit = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('limit', None)
        except ValueError:
            token_key = None
            limit = 10
        scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
        scope['limit'] = limit
        return await super().__call__(scope, receive, send)