from ninja_extra import api_controller, route
from . import models
from django.shortcuts import get_object_or_404
from . import schema
from django.utils import timezone
from typing import List
from datetime import date
@api_controller("/customer")
class customercontrol:
    
    @route.get("/{pk}" , response=schema.customerschema)
    def personal_greeting(self, pk: int):
        customer = get_object_or_404(models.Customer, id=pk)
        return customer
    
@api_controller("/worker")
class Workercontrol:
    
    @route.post("/create-customer", response={201:schema.customerschema,200:schema.customerschema, 422:schema.Errorresponseschema, 500:schema.Errorresponseschema})
    def create_customer(self, payload: schema.CustomerInSchema):
        # new_customer = models.Customer.objects.create(**payload.dict(), subs=date.today())
        # return new_customer
        new_subscription = models.Subs.objects.create(subtime=timezone.now().date())
        
        # 2. Assign the new Subs instance to the customer's 'subs' field
        new_customer = models.Customer.objects.create(
            **payload.dict(), 
            subs=new_subscription
        )
        return new_customer
    
    @route.get("",response=List[schema.workerschema])
    def workerstat(self):
        return models.Worker.objects.all()
    
    @route.get("/addsub",response=List[schema.customerschema]) 
    def addsub(self):
        return models.Customer.objects.all()
    
    @route.post("/addsub/{pk}",response=schema.customerschema)
    def addsubs(self,pk,time:date):
        customer = get_object_or_404(models.Customer, id=pk)
        sub=customer.subs
        sub.subtime=time
        sub.save()
        return customer
    