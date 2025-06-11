
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from ninja.security import HttpBearer
from ninja.errors import HttpError


class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        
        try:
           
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])
            return user

        except jwt.ExpiredSignatureError:
            return None
        except (jwt.InvalidTokenError, User.DoesNotExist):
            return None
class EmployeeAuth(HttpBearer):
    
    def authenticate(self, request, token):
        try:
            
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])
            
            if hasattr(user, 'worker'):
                
                return user
            
        except (jwt.InvalidTokenError, User.DoesNotExist):
            
            return None
            
        
        return None
    
class IsEmployee(JWTAuth):

    def authenticate(self, request, token):
        
        user, payload = super().authenticate(request, token)

        if not hasattr(user, 'worker'):
            raise HttpError(403, "You do not have permission to perform this action.")

        return user, payload