from ninja import Schema, ModelSchema
from . import models
from datetime import date
from typing import Optional

class subsschema(ModelSchema):
    class Meta:
        model = models.Subs
        fields = ['id', 'subtime']

# class CustomerInSchema(Schema):
#     name: str
#     password: str
class LoginSchema(Schema):
    username: str
    password: str

class TokenResponseSchema(Schema):
    access: str
    refresh: str

class customerschema(ModelSchema):
    # Resolver for username
    username: str
    @staticmethod
    def resolve_username(obj):
        if obj.user:
            return obj.user.username
        return "N/A"

    # Resolver for days_remaining
    days_remaining: int
    # Ensure this resolver is a @staticmethod
    @staticmethod
    def resolve_days_remaining(obj):
        if obj.subs and obj.subs.subtime:
            remaining = (obj.subs.subtime - date.today()).days
            # Return 0 or a negative number, but ensure it's an int
            return remaining if remaining > 0 else 0
        return 0

    class Meta:
        model = models.Customer
        # Only include fields directly on the Customer model.
        # The 'subrem' method has been removed as it was invalid.
        fields = ['id', 'subs']
# class customerschema(ModelSchema):
#     username: str

    
#     @staticmethod
#     def resolve_username(obj):
        
#         return obj.user.username

#     def resolve_days_remaining(obj):
#         if obj.subs and obj.subs.subtime:
#             remaining = (obj.subs.subtime - date.today()).days
#             return remaining 
#     days_remaining: int
#     class Meta:
#         model = models.Customer
#         fields = ['id','subs']
#         def subrem(self,object:models.Customer)-> int :
#             return object.subs
        
class workerschema(ModelSchema):
    username: str
    @staticmethod
    def resolve_username(obj):
        if obj.user:
            return obj.user.username
        return "N/A"
    class Meta:
        model = models.Worker
        fields = ['id','worktime']


class Errorresponseschema(Schema):
    message:str
    detail: Optional[str]=None