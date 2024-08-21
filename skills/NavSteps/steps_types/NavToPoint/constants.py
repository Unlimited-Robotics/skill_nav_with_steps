TYPE_NAME = 'nav_to_point'

OBSTACLE_DETECTION_THRESHOLDS = [2, 4]

NAV_CODES_IS_NAVIGATING = [4, 6]
# 14, checking if path is valid
# 4, new path compute

NAV_CODES_OBSTACLE_DETECTED = [9]
# 19, plan NOT VALID
# 9, could not navigate

from raya.enumerations import LEDS_EXECUTION_CONTROL, UI_THEME_TYPE
from raya.enumerations import UI_ANIMATION_TYPE

SOUND_OBSTACLE_DETECTED_1 = {
        'name': 'clear_the_way_1',
        'volume': 100,
        'duration': 2.0,
    }
SOUND_OBSTACLE_DETECTED_2 = {
        'name': 'clear_the_way_2',
        'volume': 100,
        'duration': 6.0,
    }

SOUNDS_OBSTACLES_DETECTED = [
    SOUND_OBSTACLE_DETECTED_1, 
    SOUND_OBSTACLE_DETECTED_2
]

SOUND_TANK_YOU = {
        'name': 'thank_you_1',
        'volume': 100,
        'duration': 1.0,
    }

LEDS_NOTIFY_OBSTACLE = {
    'group': 'head',
    'color': 'YELLOW',
    'animation': 'MALFUNCTION_VER_1',
    'speed': 1,
    'repetitions': 1,
    'execution_control': LEDS_EXECUTION_CONTROL.OVERRIDE,
}

LEDS_NAVIGATING = {
    'group': 'head',
    'color': 'CYAN',
    'animation': 'MOTION_12',
    'speed': 1,
    'repetitions': 0,
    'execution_control': LEDS_EXECUTION_CONTROL.OVERRIDE, 
}

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


UI_OBSTACLE_DETECTED = 'res:caution.gif'
UI_SCREEN_OBSTACLE_DETECTED = {
    'title': 'Please clear the way',
    'subtitle': 'I\'m on duty',
    'path': UI_OBSTACLE_DETECTED,
    'format': UI_ANIMATION_TYPE.GIF,
    **UI_COMMON_OPTIONS
}
