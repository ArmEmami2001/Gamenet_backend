from ninja import Schema, ModelSchema
from . import models

class subsschema(ModelSchema):
    class Meta:
        model = models.Subs
        fields = ['id', 'subtime']

class CustomerInSchema(Schema):
    name: str
    password: str

class customerschema(ModelSchema):
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