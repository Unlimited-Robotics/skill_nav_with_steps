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

TAGS_IDS = [17]
TAGS_FAMILY = '36h11'
TAGS_SIZE = [0.10]

AUTOMATIC_DOOR_EXAMPLE = {
    'name': 'automatic door example',
    'type': 'automatic_door',
    'zone_name': 'warehouse',
    'after_door_point': {
        **TEST_POINT,
        **TEST_POINT_OPTIONS,
    },
    'tags_ids': TAGS_IDS,
    'tags_family': TAGS_FAMILY,
    'tags_sizes': TAGS_SIZE,
    # 'timeout': -1.0,
}

AUTOMATIC_DOOR_WITH_CALL_EXAMPLE ={
    'name': 'call door example',
    'type': 'automatic_door',
    'zone_name': 'warehouse',
    'after_door_point': {**TEST_POINT},
    'tags_ids': TAGS_IDS,
    'tags_family': TAGS_FAMILY,
    'tags_sizes': TAGS_SIZE,
    'phone_call_user_id': '[user_id]',
    
    'time_before_first_call': 10.0,
    'time_beetween_calls': 30.0,
    
    # 'phone_call_timeout': 20.0,
    # 'timeout': -1.0,
}


AUTOMATIC_DOOR_WAREHOUSE = {
    'name': 'warehouse door',
    'type': 'automatic_door',
    'zone_name': 'warehouse',
    'after_door_point': {
        'x': 2833.0,
        'y': 706.0,
        'angle': 0.2177464694155388,
        'pos_unit': POSITION_UNIT.PIXELS,
        'ang_unit': ANGLE_UNIT.RADIANS,
        **TEST_POINT_OPTIONS,
    },
    'tags_ids': TAGS_IDS,
    'tags_family': TAGS_FAMILY,
    'tags_sizes': TAGS_SIZE,
    # 'timeout': -1.0,
}