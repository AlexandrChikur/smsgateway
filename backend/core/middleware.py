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


# @database_sync_to_async
# def get_user(token):
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
#         print(f"payload: {payload}")
#     except Exception as exc:
#         raise
#         return AnonymousUser()
#
#     token_exp = datetime.fromtimestamp(payload['exp'])
#     if token_exp < datetime.now():
#         return AnonymousUser()
#
#     try:
#         user = User.objects.get(id=payload['user_id'])
#     except User.DoesNotExist:
#         return AnonymousUser()
#
#     return user

@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()


# class TokenAuthMiddleware(BaseMiddleware):
#     async def __call__(self, scope, receive, send):
#         close_old_connections()
#         print(scope)
#         try:
#             token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token')
#             print(token_key)
#         except ValueError:
#             token_key = None
#
#         scope['user'] = await get_user(token_key)
#         print(scope['user'])
#         return await super().__call__(scope, receive, send)
#
#
# def JwtAuthMiddlewareStack(inner):
#     return TokenAuthMiddleware(inner)

class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        # print("============SCOPE============")
        # for k,v in scope.items():
        #     print('{0}:{1}'.format(k,v))
        #
        # print("============RECEIVE============")
        # print(receive)
        # print(type(receive))
        # print(dir(receive))
        #
        # print("============SEND============")
        # print(send)
        # print(type(send))
        # print(dir(send))

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