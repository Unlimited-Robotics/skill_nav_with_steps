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
        'behavior_tree': 'nav_with_cart_restricted'
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

NAV_TO_POINT_LIST = {
    'name': 'navigation list example',
    'type': 'nav_to_point',
    
    'points' : [ 
        # [ 390, 1189, 0.19944054677423476  ], 
        # [ 572, 1151, 0.20273168849747414 ],
        # [ 982, 1060, 0.2541843869601435  ],
        # [ 1428, 988, 0.23974310887045658 ],
        # [ 1627, 931, 0.22157591442968716 ],
        [ 1761, 904, 0.22435328773765226 ],
    ],
    'nav_options': {
        'pos_unit': POSITION_UNIT.PIXELS,
        'ang_unit': ANGLE_UNIT.RADIANS,
        **TEST_POINT_OPTIONS
    },
    'finish_when_distance_less_than': 3.0,
    'teleoperator_if_fail': True,
}