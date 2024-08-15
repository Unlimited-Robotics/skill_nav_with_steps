from .errors import *

MAX_RETRY_COUNTER_REQUEST_FOR_HELP = 1
ERR_APP_ABORTED = (1, 'FSM aborted by user')

from raya.enumerations import UI_THEME_TYPE
UI_COMMON_OPTIONS = {
    'theme': UI_THEME_TYPE.WHITE,
    'back_button_text': '',
}

UI_SCREEN_WAIT_FOR_HELP_SELECTOR = {
    'title':'Teleoperation in process',
    'max_items_shown': 0,
    'data': [
            {'id': 1, 'name': 'Continue'},
        ],
    **UI_COMMON_OPTIONS
}

TIME_TO_WAIT_AFTER_CONTINUE = 1.0
TIMEOUT_TELEOPERATOR = -1.0
