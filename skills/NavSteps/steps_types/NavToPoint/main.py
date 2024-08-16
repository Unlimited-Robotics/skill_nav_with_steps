from ..Point import Point
from . import NavToPointFSM

from .constants import *

class NavToPoint:

    def __init__(self,
            name: str,
            point: dict,
            teleoperator_if_fail: bool = True,
            teleoperator_timeout: float = -1.0,
            custom_ui_screen: dict = UI_SCREEN_NAVIGATING,
            custom_ui_screen_obstacle: dict = UI_SCREEN_OBSTACLE_DETECTED,
            partial_navigation: bool = False,
            finish_when_distance_less_than: float = -1.0,
        ) -> None:
        self.name = name
        self.type = TYPE_NAME
        self.point = Point(**point)
        self.teleoperator_if_fail = teleoperator_if_fail
        self.teleoperator_timeout = teleoperator_timeout
        self.custom_ui_screen = custom_ui_screen
        self.custom_ui_screen_obstacle = custom_ui_screen_obstacle
        
        self.partial_navigation = partial_navigation
        self.finish_when_distance_less_than = finish_when_distance_less_than
        
        self.fsm = NavToPointFSM(
            self_object=self,
            name=self.name, 
            log_transitions=True,
        )
