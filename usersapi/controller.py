from ninja_extra import api_controller, route
from . import models
from django.shortcuts import get_object_or_404
from . import schema

@api_controller("/customer")
class customercontrol:
    
    @route.get("/{pk}" , response=schema.customerschema)
    def personal_greeting(self, pk: int):
        customer = get_object_or_404(models.Customer, id=pk)
        return customer
    
@api_controller("/worker")
class Workercontrol:

    @route.get("",response=schema.workerschema)
    def workerstat(self):
        return models.Worker.objects.all()
    
    @route.get("/addsub",response=schema.customerschema) 
    def addsub(self):
        return models.Customer.objects.all()
    
    @route.post("/addsub/{pk}",response=schema.customerschema)
    def addsubs(self,pk,subtime:int):
        customer = get_object_or_404(models.Customer, id=pk)
        subs=customer.sub
        subs.subtime=subtime
        subs.save()
        return customer
    