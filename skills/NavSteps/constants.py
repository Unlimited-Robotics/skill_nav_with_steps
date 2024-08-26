from raya.enumerations import UI_THEME_TYPE

from .steps_types.CommonType import constants as CommonTypeConstants
from .steps_types.NavToPoint import constants as NavToPointConstants
from .steps_types.AutomaticDoor import constants as AutomaticDoorConstants
from .steps_types.Teleoperation import constants as TeleoperationConstants

NAV_TO_POINT_TYPE_NAME = NavToPointConstants.TYPE_NAME
AUTOMATIC_DOOR_TYPE_NAME = AutomaticDoorConstants.TYPE_NAME
TELEOPERATION_TYPE_NAME = TeleoperationConstants.TYPE_NAME

# TODO remove this
TEST_TYPE_NAME = CommonTypeConstants.TYPE_NAME

TYPES_AVAILABLE = [
    NAV_TO_POINT_TYPE_NAME,
    AUTOMATIC_DOOR_TYPE_NAME,
    TELEOPERATION_TYPE_NAME,
    TEST_TYPE_NAME,
]

UI_COMMON_OPTIONS = {
    'theme': UI_THEME_TYPE.WHITE,
    'back_button_text': '',
}
UI_LOTTIE_DELIVERING_PACKAGE = 'res:lottie_package_walking.json'

UI_SCREEN_NAVIGATING = {
    'title':'Hello! I\'m Gary, your delivery robot',
    'lottie': UI_LOTTIE_DELIVERING_PACKAGE,
    **UI_COMMON_OPTIONS
}
