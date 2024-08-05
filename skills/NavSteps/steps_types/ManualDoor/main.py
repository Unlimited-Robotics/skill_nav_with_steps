from ..Point import Point
from . import ManualDoorFSM

from .constants import *
from .helpers import Helpers

from ..Point import Point
from ..AutomaticDoor.main import AutomaticDoor

class ManualDoor(AutomaticDoor):
    
    def __init__(self,
            name: str,
            after_door_point: dict,
            tags_ids: list,
            tags_sizes: list,
            tags_family: str = '36h11',
            phone_call_timeout: float = 60.0,
            call_user_id: str = None,
            timeout: float = 60.0
        ) -> None:
        super.__init__(
            name=name,
            after_door_point=after_door_point,
            tags_ids=tags_ids,
            tags_family=tags_family,
            tags_sizes=tags_sizes,
            timeout=timeout,
        )
        self.fsm = ManualDoorFSM(
            self_object=self,
            name=self.name,
            log_transitions=True,
        )
        
        self.phone_call_timeout = phone_call_timeout
        self.call_user_id = call_user_id
