from ninja_extra import NinjaExtraAPI
from usersapi import controller
from ninja_jwt.controller import NinjaJWTDefaultController 

api = NinjaExtraAPI(
    title="GameNet",
    version="1.0.0",
    urls_namespace="gamenet_api"
)
api.register_controllers(NinjaJWTDefaultController) 

api.register_controllers(controller.customercontrol)
api.register_controllers(controller.Employeecontrol)
