from input_emitter import Input
import routes.main_routes
from view import VIEW
from state import STATE

##### CONTROLLER MODULE #####
class Controller:
    def start_application(self):
        print("_____Started_Python_SMS_Tool_____")
        while not STATE.exited:
            Input.emit(VIEW.prompt())

CTRL = Controller()



##### EXECUTION #####
CTRL.start_application()
