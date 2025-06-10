from ninja import Schema, ModelSchema
from . import models
from datetime import date
from typing import Optional

class subsschema(ModelSchema):
    class Meta:
        model = models.Subs
        fields = ['id', 'subtime']

class CustomerInSchema(Schema):
    name: str
    password: str

class customerschema(ModelSchema):
    @staticmethod
    def resolve_days_remaining(obj):
        if obj.subs and obj.subs.subtime:
            remaining = (obj.subs.subtime - date.today()).days
            return remaining 
    days_remaining: int
    class Meta:
        model = models.Customer
        fields = ['id', 'name','subs']
        def subrem(self,object:models.Customer)-> int :
            return object.subs
        
class workerschema(ModelSchema):
    class Meta:
        model = models.Worker
        fields = ['id', 'name','worktime']


class Errorresponseschema(Schema):
    message:str
    detail: Optional[str]=None