from ..Point import Point
from ..CommonType.main import CommonType

class NavToPoint(CommonType):

    def __init__(self,
            name: str ,
            point: dict,
            teleoperator_if_fail: bool = False,
            teleoperator_timeout: float = 60.0,
        ) -> None:
        self.name = name
        self.point: Point = Point(point)
        self.teleoperator_if_fail = teleoperator_if_fail
        self.teleoperator_timeout = teleoperator_timeout
