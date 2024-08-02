from ..Point import Point
from . import NavToPointFSM

from .constants import *

class NavToPoint:

    def __init__(self,
            name: str,
            point: dict,
            teleoperator_if_fail: bool = False,
            teleoperator_timeout: float = 60.0,
        ) -> None:
        self.name = name
        self.type = TYPE_NAME
        self.point = Point(**point)
        self.teleoperator_if_fail = teleoperator_if_fail
        self.teleoperator_timeout = teleoperator_timeout
        self.fsm = NavToPointFSM(
            self_object=self,
            name=self.name, 
            log_transitions=True,
        )
