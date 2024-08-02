from .steps_types.CommonType import constants as CommonTypeConstants
MANUAL_DOOR_TYPE_NAME = 'manual_door'
AUTOMATIC_DOOR_TYPE_NAME = 'automatic_door'

# TODO remove this
TEST_TYPE_NAME = CommonTypeConstants.TYPE_NAME

TYPES_AVAILABLE = [
    NAV_TO_POINT_TYPE_NAME,
    MANUAL_DOOR_TYPE_NAME,
    AUTOMATIC_DOOR_TYPE_NAME,
    TEST_TYPE_NAME
]
