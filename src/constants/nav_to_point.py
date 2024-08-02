from raya.enumerations import ANGLE_UNIT, POSITION_UNIT

TEST_POINT = {
    'x':        2016.0,
    'y':        472.0,
    'angle':    179.133528312283026,
    'pos_unit': POSITION_UNIT.PIXELS, 
    'ang_unit': ANGLE_UNIT.DEGREES,
}

TEST_POINT_OPTIONS = {
    'options': {
        'behavior_tree': 'compute_path'
    },
}


NAV_TO_POINT_EXAMPLE = {
    'name': 'navigation to point',
    'type': 'nav_to_point',
    
    'point' : {
        **TEST_POINT,
        **TEST_POINT_OPTIONS
    },
    'teleoperator_if_fail': True,
    'teleoperator_timeout': 60.0
}
