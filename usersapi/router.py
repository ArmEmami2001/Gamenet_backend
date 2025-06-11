
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from ninja.security import HttpBearer


class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        
        try:
           
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['id'])
            return user

        except jwt.ExpiredSignatureError:
            return None
        except (jwt.InvalidTokenError, User.DoesNotExist):
            return None
class EmployeeAuth(HttpBearer):
    
    def authenticate(self, request, token):
        try:
            
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['id'])
            
            if hasattr(user, 'worker'):
                
                return user
            
        except (jwt.InvalidTokenError, User.DoesNotExist):
            
            return None
            
        
        return None