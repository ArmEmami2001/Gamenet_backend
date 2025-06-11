
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from ninja.security import HttpBearer


class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        
        try:
           
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload['id']
            user = User.objects.get(id=user_id)
            return user

        except jwt.ExpiredSignatureError:
            return None
        except (jwt.InvalidTokenError, User.DoesNotExist):
            return None