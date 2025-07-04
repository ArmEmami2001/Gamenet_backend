from ninja_extra import api_controller, route
from . import models
from django.shortcuts import get_object_or_404
from . import schema
from django.contrib.auth import login
from django.db import IntegrityError
from django.utils import timezone
from typing import List
from datetime import date
from ninja_jwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from ninja.responses import Response
from django.contrib.auth.models import User
import logging
from . import router
from ninja_jwt.authentication import JWTAuth
from .router import IsEmployee,MyTokenObtainPairSerializer
logger = logging.getLogger(__name__)

@api_controller("/auth")
class AuthController:

    @route.post("/login", auth=None, response={200: schema.TokenResponseSchema, 401: schema.Errorresponseschema})
    def login(self, request, payload: schema.LoginSchema):
        user = authenticate(username=payload.username, password=payload.password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        
        return Response({"message": "Invalid credentials"}, status=401)
@api_controller("/customer", auth=None)
class customercontrol:

    @route.post("/create-customer", response={201:schema.customerschema,200:schema.customerschema, 409:schema.Errorresponseschema, 500:schema.Errorresponseschema})
    def create_customer(self, request, payload: schema.LoginSchema):
        
        # ip_address = request.META.get("REMOTE_ADDR")
        logger.info(f"User creation attempt for '{payload.username}'")

        try:
            
            new_user = User.objects.create_user(
                username=payload.username,
                password=payload.password
            )
        except IntegrityError:
            
            return 409, {"message": f"Username '{payload.username}' already exists."}
        except Exception as e:

            logger.error(f"Failed to create user '{payload.username}'. Error: {e}")
            return 400, {"message": "Failed to create user."}

        
        new_customer = models.Customer.objects.create(
            user=new_user, 
            subs=timezone.now().date()
        )

        
        login(request, new_user)
        logger.info(f"User '{new_user.username}' created and logged in successfully.")

        return 201, new_customer
    
    @route.get("/me" ,auth=JWTAuth(), response=schema.customerschema)
    def get_my_profile(self, request):
        customer = get_object_or_404(models.Customer, user=request.user)
        
        return customer
    
@api_controller("/employee", auth=JWTAuth())
class Employeecontrol:
    @route.post("add_employee",auth=None, response={201:schema.workerschema,200:schema.workerschema, 409:schema.Errorresponseschema, 500:schema.Errorresponseschema})
    def addemployee (self,request,payload:schema.LoginSchema):
        
        logger.info(f"User creation attempt for '{payload.username}'")

        try:
            
            new_user = User.objects.create_user(
                username=payload.username,
                password=payload.password,

            )
        except IntegrityError:
            
            return 409, {"message": f"Username '{payload.username}' already exists."}
        except Exception as e:

            logger.error(f"Failed to create user '{payload.username}'. Error: {e}")
            return 400, {"message": "Failed to create user."}
        
        new_empolyee = models.Worker.objects.create(user=new_user)

        
        
        
        login(request, new_user)
        logger.info(f"User '{new_user.username}' created and logged in successfully.")

        return 201, new_empolyee
    @route.get("/me", response=schema.workerschema)
    def get_my_profile(self, request):
        return request.user.worker
    
    @route.put("/worktime/{pk}", response=schema.workerschema)
    def change_work_time(self, request,pk, payload: schema.WorkTimeUpdateSchema):
        employee_profile = get_object_or_404(models.Worker, id=pk)

        employee_profile.worktime = payload.worktime
        employee_profile.save()

        return employee_profile
    
    @route.get("",response=List[schema.workerschema])
    def employeerstat(self,request):
        return models.Worker.objects.all()
    
    @route.get("/addsub",response=List[schema.customerschema]) 
    def addsub(self,request):
        return models.Customer.objects.all()
    
    @route.put("/addsub/{pk}",response=schema.customerschema)
    def addsubs(self,request,pk,payload:schema.subsschema):
        customer = get_object_or_404(models.Customer, id=pk)
        customer.subs=payload.subtime
        customer.save()
        return customer
    