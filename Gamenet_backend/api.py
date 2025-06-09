from ninja_extra import NinjaExtraAPI
from usersapi import controller

api = NinjaExtraAPI(
    title="GameNet",
    version="1.0.0",
    urls_namespace="gamenet_api"
)

api.register_controllers(controller.customercontrol,
                         controller.Workercontrol
                         )
# api.register_controllers(controller.Workercontrol)
