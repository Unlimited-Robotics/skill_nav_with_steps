TYPE_NAME = 'automatic_door'

CAMERAS_DETECTING_DOOR = ['nav_bottom']

DOOR_TAG_TIMEOUT = 3.0


from raya.enumerations import UI_THEME_TYPE, LEDS_EXECUTION_CONTROL

SOUND_OPEN_DOOR_REQUEST = {
        'name': 'open_door_1',
        'volume': 100,
        'duration': 4.0,
    }

SOUND_OPEN_DOOR_THANKS = {
        'name': 'thank_you_door_1',
        'volume': 100,
        'duration': 3.0,
    }

LEDS_DOOR_OPENED = {
    'group': 'head',
    'color': 'GREEN',
    'animation': 'MOTION_10_VER_3',
    'speed': 1,
    'repetitions': 1,
    'execution_control': LEDS_EXECUTION_CONTROL.OVERRIDE, 
}

UI_COMMON_OPTIONS = {
    'theme': UI_THEME_TYPE.WHITE,
    'back_button_text': '',
}
UI_LOTTIE_DOOR = 'res:lottie_door.json'

UI_SCREEN_WAIT_FOR_DOOR_OPEN = {
    'title':'Please open the door',
    'lottie': UI_LOTTIE_DOOR,
    **UI_COMMON_OPTIONS
}

DELAY_AFTER_DOOR_OPENED = 5.0