from ninja import Schema, ModelSchema
from . import models
from datetime import date
from typing import Optional

class subsschema(Schema):
    subtime:date

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
    
    username: str
    @staticmethod
    def resolve_username(obj):
        if obj.user:
            return obj.user.username
        return "N/A (No User Linked)"

    
    days_remaining: int
    
    @staticmethod
    def resolve_days_remaining(obj):
        if obj.subs: 
            remaining = (obj.subs - date.today()).days 
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
class WorkTimeUpdateSchema(Schema):
    worktime: str

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