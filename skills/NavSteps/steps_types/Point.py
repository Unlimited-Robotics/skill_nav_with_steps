from raya.enumerations import POSITION_UNIT, ANGLE_UNIT

class Point:
    
    def __init__(self, **kwargs) -> None:
        self.x: float = kwargs.pop('x')
        self.y: float = kwargs.pop('y')
        self.angle: float = kwargs.pop('angle')
        self.pos_unit: POSITION_UNIT = POSITION_UNIT.PIXELS
        self.ang_unit: ANGLE_UNIT = ANGLE_UNIT.DEGREES
        self.nav_options = kwargs
