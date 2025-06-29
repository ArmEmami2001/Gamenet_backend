from ninja.security import HttpBearer
from ninja.errors import HttpError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import jwt
from django.conf import settings
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):        
        token = super().get_token(user)
        if hasattr(user, 'worker'):
            token['role'] = 'employee'
        elif hasattr(user, 'customer'):
            token['role'] = 'customer'
        else:
            token['role'] = 'unknown' 
        token['username'] = user.username
        return token
class IsEmployee(HttpBearer):
     def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            role = payload.get('role')
            if role == 'employee':
                return True  
            raise HttpError(403, "You do not have permission to perform this action.")
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
            return None