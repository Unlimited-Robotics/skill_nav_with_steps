from ..Point import Point

class AutomaticDoor:
    
    def __init__(self,
            name: str,
            after_door_point: dict,
            target_ids: list,
            tags_sizes: list,
            tags_family: str = '36h11',
            timeout: float = 60.0
        ) -> None:
        self.name = name
        self.after_door_point: Point = Point(after_door_point)
        self.target_ids = target_ids
        self.tags_family = tags_family
        self.tags_sizes = tags_sizes
        self.timeout = timeout
