from ..Point import Point
from . import NavToPointFSM

from .constants import *

class NavToPoint:

    def __init__(self,
            name: str,
            point: dict,
            teleoperator_if_fail: bool = True,
            teleoperator_timeout: float = -1.0,
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


    async def nav_feedback_async(self, code, msg, distance, speed):
        self.fsm.log.debug(
            'nav_feedback_async: '
            f'{code}, {msg}, {distance}, {speed}'
        )


    async def nav_finish_async(self, code, msg):
        self.fsm.log.debug(
            f'nav_finish_async: {code}, {msg}'
        )
