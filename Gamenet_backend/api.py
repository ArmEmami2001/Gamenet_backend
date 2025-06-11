from ninja_extra import NinjaExtraAPI
from usersapi import controller
from ninja import Router
from ninja.security import HttpBearer

api = NinjaExtraAPI(
    title="GameNet",
    version="1.0.0",
    urls_namespace="gamenet_api"
)

api.register_controllers(controller.customercontrol)
api.register_controllers(controller.Employeecontrol)
api.register_controllers(controller.AuthController)