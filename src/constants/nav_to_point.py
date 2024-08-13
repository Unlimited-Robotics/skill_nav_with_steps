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
        'behavior_tree': 'nav_with_cart_restricted39'
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
    # 'teleoperator_timeout': 10.0,
    # 'custom_ui_screen' : {},
}

NAV_TO_POINT_EXIT_WAREHOUSE = {
    'name': 'navigation to exit',
    'type': 'nav_to_point',
    'point' : {
        'x':        1761.0,
        'y':        904.0,
        'angle':    0.22435328773765226,
        'pos_unit': POSITION_UNIT.PIXELS,
        'ang_unit': ANGLE_UNIT.RADIANS,
        **TEST_POINT_OPTIONS
    },
    'teleoperator_if_fail': True,
    # 'teleoperator_timeout': 10.0,
    # 'custom_ui_screen' : {},
}

NAV_TO_POINT_ELEVATORS = {
    'name': 'navigation to elevators',
    'type': 'nav_to_point',
    
    'point' : {
        'x': 2833.0,
        'y': 706.0,
        'angle': 0.2177464694155388,
        'pos_unit': POSITION_UNIT.PIXELS,
        'ang_unit': ANGLE_UNIT.RADIANS,
        **TEST_POINT_OPTIONS
    },
    'teleoperator_if_fail': True,
    # 'teleoperator_timeout': 10.0,
    # 'custom_ui_screen' : {},
}