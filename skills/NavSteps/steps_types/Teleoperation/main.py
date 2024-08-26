from . import TeleoperationFSM

from .constants import *

class Teleoperation:

    def __init__(self,
            name: str,
            custom_ui_screen: dict = UI_SCREEN_NAVIGATING,
        ) -> None:
        self.name = name
        self.type = TYPE_NAME
        self.custom_ui_screen = custom_ui_screen
        self.fsm = TeleoperationFSM(
            self_object=self,
            name=self.name, 
            log_transitions=True,
        )
