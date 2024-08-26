TYPE_NAME = 'teleoperation'

from raya.enumerations import UI_THEME_TYPE, UI_ANIMATION_TYPE

UI_COMMON_OPTIONS = {
    'theme': UI_THEME_TYPE.WHITE,
    'back_button_text': '',
}

UI_CALL_TO_ACTION_TELEOPERATION_DONE = {
    'title': 'Teleoperation in process...',
    'subtitle': 'Please wait until the teleoperation is done.',
    'button_text': 'Done ✅',
    **UI_COMMON_OPTIONS
}

UI_LOTTIE_DELIVERING_PACKAGE = 'res:lottie_package_walking.json'

UI_SCREEN_NAVIGATING = {
    'title':'Hello! I\'m Gary, your delivery robot',
    'lottie': UI_LOTTIE_DELIVERING_PACKAGE,
    **UI_COMMON_OPTIONS
}
