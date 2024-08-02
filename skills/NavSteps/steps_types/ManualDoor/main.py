from ..Point import Point
from ..AutomaticDoor.main import AutomaticDoor

class ManualDoor(AutomaticDoor):
    
    def __init__(self,
            name: str,
            after_door_point: dict,
            target_ids: list,
            tags_sizes: list,
            tags_family: str = '36h11',
            phone_call_timeout: float = 60.0,
            call_user_id: str = None,
            timeout: float = 60.0
        ) -> None:
        super.__init__(
            name=name,
            after_door_point=after_door_point,
            target_ids=target_ids,
            tags_family=tags_family,
            tags_sizes=tags_sizes,
            timeout=timeout,
        )
        
        self.phone_call_timeout = phone_call_timeout
        self.call_user_id = call_user_id
