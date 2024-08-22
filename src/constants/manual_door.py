from raya.enumerations import ANGLE_UNIT, POSITION_UNIT

TEST_POINT = {
    'x':        2016.0,
    'y':        472.0,
    'angle':    179.133528312283026,
    'pos_unit': POSITION_UNIT.PIXELS, 
    'ang_unit': ANGLE_UNIT.DEGREES,
}

TAGS_IDS = [18]
TAGS_FAMILY = '36h11'
TAGS_SIZE = [0.10]

MANUAL_DOOR_EXAMPLE ={
    'name': 'manual_door example',
    'type': 'manual_door',
    'zone_name': 'basement',
    'after_door_point': {**TEST_POINT},
    'tags_ids': TAGS_IDS,
    'tags_family': TAGS_FAMILY,
    'tags_sizes': TAGS_SIZE,
    'phone_call_user_id': '[unit1_user_id]',
    # 'phone_call_timeout': 20.0,
    # 'timeout': -1.0,
}
